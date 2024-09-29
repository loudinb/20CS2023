from datetime import datetime
from typing import List

class LikeableContent:
    """
    Base class for content that can be liked (e.g., Post, Comment).
    Contains shared functionality for liking and unliking.
    """

    def __init__(self, author: 'User', content: str, tags: List[str] = None):
        self._author = author
        self._content = content
        self._created_at = datetime.now()
        self._tags = tags if tags else []
        self._liked_by = []

    @property
    def author(self) -> 'User':
        return self._author

    @property
    def content(self) -> str:
        return self._content

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def liked_by(self) -> List['User']:
        return self._liked_by

    @property
    def tags(self) -> List[str]:
        return self._tags

    def like(self, user: 'User'):
        if user not in self._liked_by:
            self._liked_by.append(user)

    def unlike(self, user: 'User'):
        if user in self._liked_by:
            self._liked_by.remove(user)
