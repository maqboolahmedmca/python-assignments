from typing import Any
from evaluators.evaluator import Evaluator
from model.base_question import BaseQuestion


class SingleOptionEvaluator(Evaluator):
    """
    Evaluate Single|TrueFalse
    """

    def __init__(self):
        super().__init__()

    def evaluate_answer(self, question: BaseQuestion, answer: str) -> int:
        """ Evaluate & return the score in percentage """
        print(f"correct_answer: {question.correct_answer} given_answer: {answer}")
        if (question.correct_answer == answer):
            return 100
        else:
            return 0

    

    