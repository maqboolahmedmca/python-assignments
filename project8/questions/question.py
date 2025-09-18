from abc import ABC, abstractmethod

from project8.evaluators import evaluator
from project8.evaluators.evaluator import Evaluator

class Question(ABC):
    """Abstract class for Questions"""

    def __init__(self, text: str, marks: int, evaluator: Evaluator) -> None:
        super().__init__()
        self.text = text
        self.marks = marks
        self.evaluator = evaluator

    def get_text(self) -> str:
        return self.text

    def get_marks(self) -> int:
        return self.marks

    @abstractmethod
    def evaluate(self, answer: str) -> int:
        """ Evaluate & return the score in percentage """
        self.evaluator.check_answer(self, answer)