from abc import ABC
from typing import Dict, Any, List
from model.base_question import BaseQuestion

class ObjectiveQuestion(BaseQuestion, ABC):
    """Abstract base for objective questions (with options)."""

    def __init__(self, id: int, type: str, text: str, options: List[str], correct_answer: Any,
                 marks: int):
        super().__init__(id, text, marks, correct_answer) #
        self.type = type
        self.options = options

    def get_options(self) -> List[str]:
        return self.options

    # def evaluate(self, answer) -> float:
    #     """Delegates evaluation to the evaluator, then applies marks."""
    #     percentage = self.evaluator.evaluate_answer(self, answer)
    #     return (percentage / 100.0) * self.marks
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "text": self.text,
            "marks": self.marks,
            "options": self.options,
            "correct_answer": self.correct_answer
        }
    
# Testing Only
row_base = (1, "single", "What is the capital of France?", 1)
row_obj = (1, ["Paris", "London", "Berlin"], "Paris")

# Create ObjectiveQuestion
singleQ = ObjectiveQuestion(
    id=row_base[0],
    type=row_base[1],
    text=row_base[2],
    marks=row_base[3],
    options=row_obj[1],
    correct_answer=row_obj[2],
)

print(singleQ)
print(singleQ.to_dict())
print("*" * 100)

row_base = (2, "truefalse", "Is it Blue?", 2)
row_obj = (2, ["True", "False"], "True")
trueFalseQ = ObjectiveQuestion(
    id=row_base[0],
    type=row_base[1],
    text=row_base[2],
    marks=row_base[3],
    options=row_obj[1],
    correct_answer=row_obj[2]
)

print(trueFalseQ)
print(trueFalseQ.to_dict())
print("*" * 100)