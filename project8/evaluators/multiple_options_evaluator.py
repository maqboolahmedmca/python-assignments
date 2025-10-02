from typing import Any, List
from evaluators.evaluator import Evaluator
from model.base_question import BaseQuestion

class MultipleOptionsEvaluator(Evaluator):
    """Evaluator for multiple-option questions."""

    def __init__(self, mode: str = "penalty"):
        """
        mode can be:
          - "strict"   → all correct & no wrong = 100, else 0
          - "partial"  → partial credit, wrong answers ignored
          - "penalty"  → partial credit with penalty for wrong answers
        """
        self.mode = mode

    def evaluate_answer(self, question: BaseQuestion, answers: List[Any]) -> int:
        if not hasattr(question, "correct_answer"):
            raise ValueError("Question does not have correct_answer field")

        correct_answers = set(question.correct_answer)
        given_answers = set(answers)

        if not correct_answers:
            return 0

        total_correct = len(correct_answers)
        correct_matches = len(correct_answers & given_answers)
        wrong_matches = len(given_answers - correct_answers)

        if self.mode == "strict":
            return 100 if (correct_matches == total_correct and wrong_matches == 0) else 0

        elif self.mode == "partial":
            return int((correct_matches / total_correct) * 100)

        elif self.mode == "penalty":
            score_pct = ((correct_matches - wrong_matches) / total_correct) * 100
            return max(0, int(score_pct))

        else:
            raise ValueError(f"Unknown mode: {self.mode}")
        
    # def evaluate_answer(self, question: BaseQuestion, answers: List[Any]) -> int:
    #     if not hasattr(question, "correct_answer"):
    #         raise ValueError("Question does not have correct_answer field")

    #     correct_answers = set(question.correct_answer)   # expected
    #     given_answers = set(answers)                    # student input

    #     if not correct_answers:
    #         return 0

    #     # Correct choices matched
    #     correct_matches = len(correct_answers & given_answers)

    #     # Wrong choices penalize
    #     wrong_matches = len(given_answers - correct_answers)

    #     print("correct_matches: " + str(correct_matches) + " wrong_matches: " + str(wrong_matches))
    #     # Score calculation (simple version: correctness ratio)
    #     total_correct = len(correct_answers)
    #     score_pct = max(0, (correct_matches - wrong_matches) / total_correct * 100)

    #     flag = score_pct == 100
    #     return flag, score_pct

    