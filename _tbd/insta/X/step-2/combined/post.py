from typing import List, Optional
from datetime import datetime
from user import User  # Assuming User is defined elsewhere

class Post:
    post_count: int = 0

    def __init__(self, content: str, author: User, tags: Optional[List[str]] = None):
        if len(content) > 2200:
            raise ValueError("Content must be 2200 characters or less.")
        
        self.__content: str = content
        self.timestamp: datetime = datetime.now()
        self._tags: List[str] = tags or []
        self.author: User = author  # Add the author attribute
        self._likes: List[User] = []
        
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

    def add_like(self, user: User) -> None:
        if user not in self._likes:
            self._likes.append(user)

    def remove_like(self, user: User) -> None:
        if user in self._likes:
            self._likes.remove(user)

    @classmethod
    def get_post_count(cls) -> int:
        return cls.post_count

    @staticmethod
    def is_valid_tag(tag: str) -> bool:
        return len(tag) <= 30 and tag.isalnum()
