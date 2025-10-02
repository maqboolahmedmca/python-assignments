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
# question_pattern = re.compile(r"""
#     (?P<number>\d+)\.\s*                               # Question number
#     (?P<q_text>.*?(?=(?:A\)|Answer:)))                 # Question text (stop before A) or Answer:)
#     (?:                                                # Optional block of options
#         A\)\s*(?P<option_a>.*?)\s*
#         B\)\s*(?P<option_b>.*?)\s*
#         C\)\s*(?P<option_c>.*?)\s*
#         D\)\s*(?P<option_d>.*?)\s*
#     )?
#     Answer:\s*(?P<answer>.+?)(?=(?:\n\d+\.|\Z))         # Capture answer until next question or end
# """, re.DOTALL | re.VERBOSE)
question_pattern = re.compile(r"""
    (?P<number>\d+)\.\s*                               # Question number
    (?P<q_text>.*?(?=(?:A\)|Answer:)))                 # Question text
    (?:                                                # Optional block of options
        A\)\s*(?P<option_a>.*?)\s*
        B\)\s*(?P<option_b>.*?)\s*
        (?:C\)\s*(?P<option_c>.*?)\s*)?                # Optional C
        (?:D\)\s*(?P<option_d>.*?)\s*)?                # Optional D
    )?
    Answer:\s*(?P<answer>.+?)(?=(?:\n\d+\.|\Z))         # Capture answer until next question or end
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
                # Safe extraction (use None if missing)
                option_a = q_match.group("option_a").strip() if q_match.group("option_a") else None
                option_b = q_match.group("option_b").strip() if q_match.group("option_b") else None
                option_c = q_match.group("option_c").strip() if q_match.group("option_c") else None
                option_d = q_match.group("option_d").strip() if q_match.group("option_d") else None

                # Normalize answers into JSON array
                raw_answer = q_match.group("answer").strip() if q_match.group("answer") else ""
                print(f"Raw answer extracted: '{raw_answer}'")
                normalized_answer = self.normalize_answer(raw_answer)  
                json_answer = self.json_answer(normalized_answer)

                # Create Question entity
                question_entity = Question(
                    question_id_counter,
                    chapter_id,
                    q_match.group("q_text").strip(),
                    option_a,
                    option_b,
                    option_c,
                    option_d,
                    json_answer
                )

                chapter_entity.questions.append(question_entity)
                question_id_counter += 1

            subject.chapters.append(chapter_entity)

        return subject
    
    def normalize_answer(self, answer: str):
        answer = answer.strip()

        # Case 1: "A) Text, B) Text"
        matches = re.findall(r"([A-D])\)\s*([^,]+)", answer)
        if matches:
            return [f"{letter}) {text.strip()}" for letter, text in matches]

        # Case 2: True/False
        if answer.lower() in ("true", "false"):
            return [answer.capitalize()]

        # Case 3: "A, B, D"
        if "," in answer:
            return [a.strip() for a in answer.split(",")]

        # Case 4: Single choice like "A" or "D) Plasma"
        return [answer]


    def json_answer(self, answer):
        print("DEBUG answer:", answer, type(answer))
        json_answer = []
        for a in answer:
            if not isinstance(a, str):
                continue
            m = re.match(r'([A-D])\)', a)
            if m:
                json_answer.append(m.group(1))
            elif a in ("True", "False"):
                json_answer.append(a)  # keep True/False as-is
            else:
                json_answer.append(a)  # fallback
        return json_answer

# -----------------------------
# Testing Purpose only
# -----------------------------
if __name__ == "__main__":
    with open("content/chemistry_questions.txt", "r", encoding="utf-8") as f:
        text = f.read()

    print(text)
    parser = QuestionnaireRegexParser()
    subject = parser.parse_question_paper(text)
    if (subject is None):
        raise ValueError("Failed to parse questions from the text")
    
    #print(subject)  

    for chapter in subject.chapters:
        print(f"  Chapter {chapter.id}: {chapter.name}")
        for question in chapter.questions:
            print(f"    Q{question.id}: {question.text}")
            print(f"      A) {question.option_a}")
            print(f"      B) {question.option_b}")
            print(f"      C) {question.option_c}")
            print(f"      D) {question.option_d}")
            print(f"      Answer: {question.answer}")
