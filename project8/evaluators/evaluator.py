from abc import ABC, abstractmethod

from project8.questions.question import Question

class Evaluator(ABC):
    """Abstract class for Questions"""

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def check_answer(self, question: Question, answer: str) -> int:
        """ Evaluate & return the score in percentage """
        print(question)
        print(answer)