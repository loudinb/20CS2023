`### Section 3: Implementation Details Involving `User` (for Social Interaction)

This section covers attributes and methods that require the `User` class to implement social interactions like following and messaging.


---

### Section 4: Full Class Overview

This section contains the full class implementation, combining everything from the above sections.

#### Full Class

```python
from typing import List, Optional
from post import Post  # Assuming Post is defined elsewhere
from message import Message  # Assuming Message is defined elsewhere

class User:
    # Class attribute to track the total number of users
    user_count: int = 0

    def __init__(self, username: str, email: str):
        if not self.is_valid_username(username):
            raise ValueError("Invalid username.")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")
        
        self.username: str = username  # Public attribute
        self._email: str = email  # Protected email attribute
        self._bio: str = ""  # Protected bio, initialized to an empty string
        self._posts: List[Post] = []  # Private list of posts
        self._followers: List[User] = []  # Private list of followers
        self._following: List[User] = []  # Private list of following users
        
        User.user_count += 1

    # Property to get and set bio
    @property
    def bio(self) -> str:
        return self._bio

    @bio.setter
    def bio(self, value: str) -> None:
        if len(value) > 150:
            raise ValueError("Bio must be 150 characters or less.")
        self._bio = value

    # Create a post
    def create_post(self, content: str, tags: Optional[List[str]] = None) -> None:
        post = Post(content, tags)
        self._posts.append(post)

    # Delete a post
    def delete_post(self, post: Post) -> None:
        if post in self._posts:
            self._posts.remove(post)

    # Follow a user
    def follow(self, user: 'User') -> None:
        if user not in self._following:
            self._following.append(user)
            user._followers.append(self)

    # Unfollow a user
    def unfollow(self, user: 'User') -> None:
        if user in self._following:
            self._following.remove(user)
            user._followers.remove(self)

    # Like a post
    def like_post(self, post: Post) -> None:
        post.add_like(self)

    # Unlike a post
    def unlike_post(self, post: Post) -> None:
        post.remove_like(self)

    # Comment on a post
    def comment_on_post(self, post: Post, content: str) -> None:
        post.add_comment(self, content)

    # Send a message to another user
    def send_message(self, recipient: 'User', content: str) -> None:
        message = Message(self, recipient, content)
        recipient.receive_message(message)

    # Class method to get total user count
    @classmethod
    def get_user_count(cls) -> int:
        return cls.user_count

    # Static method to validate username
    @staticmethod
    def is_valid_username(username: str) -> bool:
        return 3 <= len(username) <= 30 and username.replace(".", "").replace("_", "").isalnum()

    # Static method to validate email address
    @staticmethod
    def is_valid_email(email: str) -> bool:
        import re
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None
```