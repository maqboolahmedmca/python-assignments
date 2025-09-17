from services.PdfTextExtractor import PdfExtractor
from services.questionnaire_regex_parser import QuestionnaireRegexParser
from dao.questionnaire_dao import QuestionnaireDao
from model.subject import Subject

class QuestionaireManager:
    def __init__(self):
        self.parser = QuestionnaireRegexParser()
        self.dao = QuestionnaireDao()

    def extract_pdf_text(self):
        try:
            extractor = PdfExtractor()
            extractor.load_pdf()
            return extractor.extract_text_from_all_pages()

        except FileNotFoundError as e:
            print(e)

        except Exception as e:
            print(f"An error occurred: {e}")

    def parse_question_paper(self, text):
        subject = self.parser.parse_question_paper(text)
        if (subject is None):
            raise ValueError("Failed to parse questions from the text")
        return subject
    
    def store_questions_to_db(self, subject: Subject):
        subject = self.dao.store_subject(subject)
        for chapter in subject.chapters:
            chapter.subject_id = subject.id
            self.dao.store_chapter(chapter)
            if (chapter.questions):
                for question in chapter.questions:
                    question.chapter_id = chapter.id
                    self.dao.store_question(question)
        
manager = QuestionaireManager()
text = manager.extract_pdf_text()
subject = manager.parse_question_paper(text)
manager.store_questions_to_db(subject)



