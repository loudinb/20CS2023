## `Post` Class Documentation

### Section 1: Core `Post` Implementation (No Dependencies)

This section includes the components of the `Post` class that can be implemented without relying on other classes (`User`, `Comment`).

#### Instance Attributes:

- **`__content`**: A **private** string representing the post’s content, limited to 2200 characters. The content should only be modified through the `content` property, ensuring strict validation.
  - **Why private**: Post content must be validated and controlled within the class, preventing external or subclass access. This ensures that the length constraint is always enforced.

- **`timestamp`**: A **public** `datetime` object recording when the post was created. The timestamp is set upon initialization and should not be modified afterward.

- **`_tags`**: A **protected** list of strings representing the tags in the post. This attribute is modifiable through specific methods such as `add_tag()` and `remove_tag()`. Subclasses can also access and modify this attribute if necessary.

#### Instance Methods:

- **`__init__(self, content: str, tags: Optional[List[str]] = None)`**: Initializes the `Post` object with the required `content` (string) and optional list of `tags`. It also records the `timestamp` when the post is created. Validation of content length is performed within the constructor using the setter.

- **`@property content(self) -> str`**: This **property** manages access to the private `__content` attribute. The getter returns the post content. The setter ensures the content does not exceed 2200 characters. A `ValueError` is raised if the content exceeds this limit.
  - **Why private**: This ensures that all modifications to post content are validated through the property setter, which enforces the length constraint.

- **`add_tag(self, tag: str) -> None`**: Adds a tag to the `_tags` list. The `tag` must be validated using the `is_valid_tag()` static method before being added.

- **`remove_tag(self, tag: str) -> None`**: Removes a tag from the `_tags` list if it exists.

#### Class Attributes:

- **`post_count`**: A **class attribute** that tracks the total number of posts in the system. This attribute is incremented in the `__init__` method each time a new `Post` object is created.

#### Class Methods:

- **`@classmethod get_post_count(cls) -> int`**: A **class method** that returns the current total number of posts in the system by accessing the `post_count` class attribute.

#### Static Methods:

- **`@staticmethod is_valid_tag(tag: str) -> bool`**: A **static method** that checks whether a tag is valid. A valid tag must be alphanumeric and no more than 30 characters long. Returns `True` if valid, otherwise `False`.

---

### Section 2: Implementation Details Involving `User`

This section includes methods that require the `User` class for proper implementation. The `User` class is expected to be available for these methods.

#### Instance Attributes:

- **`author`**: A **public** `User` object representing the user who created the post. Since authorship of posts is generally public information, this attribute can be accessible to external code.

- **`_likes`**: A **protected** list of `User` objects representing users who have liked the post. Likes are managed through the `add_like()` and `remove_like()` methods. Subclasses may access this attribute directly but should still use the methods for modification.

#### Instance Methods:

- **`add_like(self, user: 'User') -> None`**: Adds a `User` object to the `_likes` list, representing the user liking the post. The method ensures that the user has not already liked the post.

- **`remove_like(self, user: 'User') -> None`**: Removes a `User` object from the `_likes` list, representing the user unliking the post.

---

### Section 3: Implementation Details Involving `Comment`

This section covers methods that manage comments, requiring the `Comment` class for their implementation.

#### Instance Attributes:

- **`_comments`**: A **protected** list of `Comment` objects representing the comments on the post. Comments are managed using the `add_comment()` and `remove_comment()` methods. Subclasses may access this attribute if needed.

#### Instance Methods:

- **`add_comment(self, user: 'User', content: str) -> None`**: Adds a `Comment` to the protected `_comments` list. The `user` argument specifies the author of the comment, and `content` is the comment text. The `Comment` object is created and added to the list.

- **`remove_comment(self, comment: 'Comment') -> None`**: Removes a specific `Comment` object from the `_comments` list, if it exists.

---

### Section 4: Full Class Overview

This section contains the full class implementation, combining everything from the above sections.

#### Full Class

```python
from typing import List, Optional
from datetime import datetime
from user import User  # Assuming User is defined elsewhere
from comment import Comment  # Assuming Comment is defined elsewhere

class Post:
    # Class attribute to track total number of posts
    post_count: int = 0

    def __init__(self, content: str, author: 'User', tags: Optional[List[str]] = None):
        if len(content) > 2200:
            raise ValueError("Post content must be 2200 characters or less.")
        
        self.__content: str = content  # Private attribute
        self.author: User = author  # Public attribute
        self.timestamp: datetime = datetime.now()  # Timestamp on creation
        self._tags: List[str] = tags or []  # Protected list of tags
        self._likes: List[User] = []  # Protected list of likes
        self._comments: List[Comment] = []  # Protected list of comments

        Post.post_count += 1

    # Property to get and set the post content
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        if len(value) > 2200:
            raise ValueError("Post content must be 2200 characters or less.")
        self.__content = value

    # Add or remove tags
    def add_tag(self, tag: str) -> None:
        if not self.is_valid_tag(tag):
            raise ValueError("Invalid tag")
        self._tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        if tag in self._tags:
            self._tags.remove(tag)

    # Add or remove likes
    def add_like(self, user: 'User') -> None:
        if user not in self._likes:
            self._likes.append(user)

    def remove_like(self, user: 'User') -> None:
        if user in self._likes:
            self._likes.remove(user)

    # Add or remove comments
    def add_comment(self, user: 'User', content: str) -> None:
        comment = Comment(user, content)
        self._comments.append(comment)

    def remove_comment(self, comment: 'Comment') -> None:
        if comment in self._comments:
            self._comments.remove(comment)

    # Class method to get the total post count
    @classmethod
    def get_post_count(cls) -> int:
        return cls.post_count

    # Static method to validate a tag
    @staticmethod
    def is_valid_tag(tag: str) -> bool:
        return len(tag) <= 30 and tag.isalnum()
```