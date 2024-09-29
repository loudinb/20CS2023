from likeablecontent import LikeableContent
from typing import List

class Post(LikeableContent):
    """
    Represents a Post made by a user in the InstaMimic system.
    """
    
    post_count = 0

    def __init__(self, author: 'User', content: str, tags: List[str] = None):
        super().__init__(author, content, tags)
        self._comments = []
        Post.post_count += 1

    @property
    def comments(self) -> List['Comment']:
        return self._comments

    @staticmethod
    def is_valid_content(content: str) -> bool:
        return len(content) > 0

    def add_comment(self, comment: 'Comment'):
        self._comments.append(comment)
