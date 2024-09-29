from likeablecontent import LikeableContent
from typing import List

class Comment(LikeableContent):
    """
    Represents a Comment on a post in the InstaMimic system.
    """
    
    comment_count = 0

    def __init__(self, author: 'User', content: str, tags: List[str] = None):
        super().__init__(author, content, tags)
        Comment.comment_count += 1

    @staticmethod
    def is_valid_content(content: str) -> bool:
        return len(content) > 0
