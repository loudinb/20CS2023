from typing import List, Optional
from datetime import datetime

class Post:
    post_count: int = 0

    def __init__(self, content: str, tags: Optional[List[str]] = None):
        if len(content) > 2200:
            raise ValueError("Content must be 2200 characters or less.")
        
        self.__content: str = content
        self.timestamp: datetime = datetime.now()
        self._tags: List[str] = tags or []
        
        Post.post_count += 1

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        if len(value) > 2200:
            raise ValueError("Content must be 2200 characters or less.")
        self.__content = value

    def add_tag(self, tag: str) -> None:
        if not self.is_valid_tag(tag):
            raise ValueError("Invalid tag")
        self._tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        if tag in self._tags:
            self._tags.remove(tag)

    @classmethod
    def get_post_count(cls) -> int:
        return cls.post_count

    @staticmethod
    def is_valid_tag(tag: str) -> bool:
        return len(tag) <= 30 and tag.isalnum()
