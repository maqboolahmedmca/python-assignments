from dataclasses import dataclass, field, asdict
from typing import List, Optional
from model.chapter import Chapter

@dataclass
class Subject:
    id: Optional[int]
    name: str
    chapters: List["Chapter"] = field(default_factory=list)

    def add_chapter(self, chapter: "Chapter") -> None:
        self.chapters.append(chapter)


