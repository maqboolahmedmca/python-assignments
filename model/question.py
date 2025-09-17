from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Question:
    id: Optional[int]
    chapter_id: int
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    answer: str
