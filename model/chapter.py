from dataclasses import dataclass, field, asdict
from typing import List, Optional
from model.question import Question

@dataclass
class Chapter:
    id: Optional[int]
    subject_id: int
    name: str
    questions: List["Question"] = field(default_factory=list)
