from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseQuestion(ABC):
    """Abstract class for Questions"""

    def __init__(self, id: int, text: str, marks: int, correct_answer: Any, chapter_id: int = None) -> None:
        super().__init__()
        self.id = id
        self.text = text
        self.marks = marks
        self.correct_answer = correct_answer
        self.chapter_id = chapter_id

    def get_text(self) -> str:
        return self.text

    def get_marks(self) -> int:
        return self.marks

    def get_correct_answer(self) -> Any:
        return self.correct_answer
        
    # @abstractmethod
    # def evaluate(self, answer: Any) -> int:
    #     """ Evaluate & return the score in percentage """
    #     self.evaluator.evaluate_answer(self, answer)

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict for DB insertion."""
        pass

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} type={self.type} text='{self.text}' marks={self.marks}>"
