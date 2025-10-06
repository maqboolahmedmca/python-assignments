from typing import Any
from model.base_question import BaseQuestion
from model.objective_question import ObjectiveQuestion
from model.single_option_question import SingleOptionQuestion
from model.multiple_options_question import MultipleOptionsQuestion
from project8.evaluators.single_option_evaluator import SingleOptionEvaluator
from project8.evaluators.multiple_options_evaluator import MultipleOptionsEvaluator
from services.questionnaire_regex_parser import QuestionnaireRegexParser
from dao.questionnaire_dao import QuestionnaireDao
from model.subject import Subject
import json

TXT_FILE_PATH = "../content/chemistry_questions.txt"
SINGLE_OPTION_EVALUATOR=SingleOptionEvaluator()
MULTIPLE_OPTIONS_EVALUATOR=MultipleOptionsEvaluator("strict")

class QuestionaireManager:
    def __init__(self):
        self.parser = QuestionnaireRegexParser()
        self.dao = QuestionnaireDao()

    def extract_file_text(self):
        """Extract text from a txt file."""
        try:
            with open(TXT_FILE_PATH, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError as e:
            print(e)

    def parse_question_paper(self, text):
        subject = self.parser.parse_question_paper(text)
        if (subject is None):
            raise ValueError("Failed to parse questions from the text")
        return subject
    
    def evaluate(self, question: BaseQuestion, answer: Any) -> float:
        """Delegates evaluation to the evaluator, then applies marks."""
        evaluator = self.get_evaluator(question.type)
        percentage = evaluator.evaluate_answer(question, answer)
        return int((percentage / 100.0) * question.marks)
    
    def get_evaluator(self, type: str):
        if (type == 'single'):
            return SINGLE_OPTION_EVALUATOR
        elif (type == 'multiple'):
            return MULTIPLE_OPTIONS_EVALUATOR
        else:
            ValueError("Not implemented")
    
    def is_json(self, value):
        if isinstance(value, (list, dict)):  
            return True
        if isinstance(value, str):
            try:
                json.loads(value)  
            except json.JSONDecodeError:
                return False
                
    def store_questions_to_db(self, type_questions: list[ObjectiveQuestion]):
        total_stored = 0
        total_questions = len(type_questions)
        existing_questions = 0
        for tq in type_questions:
            question_text = tq.text
            existing_question = self.dao.get_type_question_by_text(question_text)

            if (existing_question):
                print(f"Question already exists in DB: {question_text}")
                existing_questions += 1
                continue    
            
            self.dao.insert_type_question(tq)
            total_stored += 1
        print(f"Total Questions Processed: {total_questions}")
        print(f"Total New Questions Stored: {total_stored}")
        print(f"Total Existing Questions Skipped: {existing_questions}")
    
    def trial_test(self, type_questions: list[BaseQuestion]=None):
        total_score = 0
        for tq in type_questions:

            print(f"\nQ: {tq.text}")
            print(f"A) {tq.options[0]}")
            print(f"B) {tq.options[1]}")
            print(f"C) {tq.options[2]}")
            print(f"D) {tq.options[3]}")
            # print(f"{tq.correct_answer}")
            answer = input("Your answer (A/B/C/D): ").strip().upper()

            if "," in answer:
                answer = answer.split(",")

            score = self.evaluate(tq, answer)
            if score > 0:
                total_score += score
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is {tq.correct_answer}.")
            
            choice = input("Press Enter to continue or type 'q' to quit: ")
            if choice.strip().lower() == "q":
                break

        print(f"\nYour total score: {total_score}/{len(type_questions)}")
    
    def list_type_questions(self):
        type_questions = manager.dao.list_type_questions()
        print(f"Total Questions found in DB: {len(type_questions)}")
        for tq in type_questions:
            print(f"Class: {type(tq).__name__} Q{tq.id}: {tq.text}")
            print(f"  Options: {tq.options}")
            print(f"  Correct Answer: {tq.correct_answer}")
            print(f"  Marks: {tq.marks}")
        return type_questions

manager = QuestionaireManager()
txt = manager.extract_file_text()
subject = manager.parse_question_paper(txt)
type_questions = []
for chapter in subject.chapters:
    print(f"  Chapter {chapter.id}: {chapter.name}")
    for question in chapter.questions:
        answer = question.answer
        if (answer == "True" or answer == "False"):
            options = ["True", "False"]
            type_question = SingleOptionQuestion(question.id, question.text, options, answer, 1)
        elif (manager.is_json(answer)):
            if (len(answer) == 1):
                options = [question.option_a, question.option_b, question.option_c, question.option_d]
                type_question = SingleOptionQuestion(question.id, question.text, options, answer[0], 1)
            elif (len(answer) > 1):
                options = [question.option_a, question.option_b, question.option_c, question.option_d]
                type_question = MultipleOptionsQuestion(question.id, question.text, options, answer, 2)
        else:
            print(f"Unknown answer format: {answer}")
            raise ValueError("Cannot determine question type")
        
        if (type_question):
            type_questions.append(type_question)

# Store all the type_questions in to DB:
manager.store_questions_to_db(type_questions)

# List all the type_questions from DB:
type_questions = manager.list_type_questions()

# Trial Test
manager.trial_test(type_questions=type_questions)
