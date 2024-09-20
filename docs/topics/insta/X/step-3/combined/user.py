from typing import List, Optional
import re
from post import Post
from comment import Comment

class User:
    user_count: int = 0

    def __init__(self, username: str, email: str):
        if not self.is_valid_username(username):
            raise ValueError("Invalid username.")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")
        
        self.username: str = username  # Public attribute
        self._email: str = email  # Protected email attribute
        self._bio: str = ""  # Protected bio, initialized to an empty string
        self._followers: List[User] = []
        self._following: List[User] = []
        self._posts: List[Post] = []
        
        User.user_count += 1

    def create_post(self, content: str, tags: Optional[List[str]] = None) -> None:
        post = Post(content, self, tags)
        self._posts.append(post)

    def delete_post(self, post: Post) -> None:
        if post in self._posts:
            self._posts.remove(post)

    def like_post(self, post: Post) -> None:
        post.add_like(self)

    def unlike_post(self, post: Post) -> None:
        post.remove_like(self)

    def comment_on_post(self, post: Post, content: str) -> None:
        post.add_comment(self, content)

    
    def follow(self, user: 'User') -> None:
        if user not in self._following:
            self._following.append(user)
            user._followers.append(self)

    def unfollow(self, user: 'User') -> None:
        if user in self._following:
            self._following.remove(user)
            user._followers.remove(self)

    @property
    def bio(self) -> str:
        return self._bio

    @bio.setter
    def bio(self, value: str) -> None:
        if len(value) > 150:
            raise ValueError("Bio must be 150 characters or less.")
        self._bio = value

    @classmethod
    def get_user_count(cls) -> int:
        return cls.user_count

    @staticmethod
    def is_valid_username(username: str) -> bool:
        return 3 <= len(username) <= 30 and username.replace(".", "").replace("_", "").isalnum()

    @staticmethod
    def is_valid_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None
