from abc import ABC, abstractmethod
from typing import Any

from model.base_question import BaseQuestion

class Evaluator(ABC):
    """Abstract class for Questions"""

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def evaluate_answer(self, question: BaseQuestion, answer: Any) -> int:
        pass