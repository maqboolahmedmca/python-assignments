import re
from model.subject import Subject
from model.chapter import Chapter
from model.question import Question  

# Subject Regex Pattern
subject_pattern = re.compile(r'^\s*(\w+)')

# Chapter Regex Pattern
chapter_pattern = re.compile(
    r'Chapter\s+(?P<chapter_id>\d+):\s*(?P<chapter_name>.*?)\n',
    re.IGNORECASE
)

# -----------------------------
# Question Regex Pattern
# -----------------------------
question_pattern = re.compile(r"""
    (?P<number>\d+)\.\s*                      # Question number
    (?P<q_text>.*?)\s*                        # Question text
    A\)\s*(?P<option_a>.*?)\s*                # Option A
    B\)\s*(?P<option_b>.*?)\s*                # Option B
    C\)\s*(?P<option_c>.*?)\s*                # Option C
    D\)\s*(?P<option_d>.*?)\s*                # Option D
    Answer:\s*(?P<answer>[A-D])               # Answer
""", re.DOTALL | re.VERBOSE)

class QuestionnaireRegexParser:

    def parse_question_paper(self, text: str) -> Subject:
        # -----------------------------
        # Extract subject
        # -----------------------------
        match = subject_pattern.match(text)
        subject_name = match.group(1) if match else "Unknown"
        subject = Subject(None, subject_name)

        # -----------------------------
        # Extract chapter positions
        # -----------------------------
        chapter_positions = [(m.start(), int(m.group("chapter_id")), m.group("chapter_name").strip()) 
                            for m in chapter_pattern.finditer(text)]

        # ------------------------------
        # Extract chapters and questions
        # Prepare the entities in structure (subject -> chapters -> questions)
        # ------------------------------
        question_id_counter = 1

        for i, (start_pos, chapter_id, chapter_name) in enumerate(chapter_positions):
            end_pos = chapter_positions[i+1][0] if i+1 < len(chapter_positions) else len(text)
            chapter_text = text[start_pos:end_pos]

            chapter_entity = Chapter(chapter_id, subject.id, chapter_name)
            
            for q_match in question_pattern.finditer(chapter_text):
                question_entity = Question(question_id_counter, chapter_id, q_match.group("q_text").strip(), q_match.group("option_a").strip(), 
                q_match.group("option_b").strip(), q_match.group("option_c").strip(), q_match.group("option_d").strip(), q_match.group("answer").strip())
                
                chapter_entity.questions.append(question_entity)
                question_id_counter += 1

            subject.chapters.append(chapter_entity)
        return subject

# -----------------------------
# Testing Purpose only
# -----------------------------
if __name__ == "__main__":
    with open("project5/output.txt", "r", encoding="utf-8") as f:
        text = f.read()

    parser = QuestionnaireRegexParser()
    subject = parser.parse_question_paper(text)
    print(subject.to_dict())  

    for chapter in subject.chapters:
        print(f"  Chapter {chapter.id}: {chapter.name}")
        for question in chapter.questions:
            print(f"    Q{question.id}: {question.text}")
            print(f"      A) {question.option_a}")
            print(f"      B) {question.option_b}")
            print(f"      C) {question.option_c}")
            print(f"      D) {question.option_d}")
            print(f"      Answer: {question.answer}")
