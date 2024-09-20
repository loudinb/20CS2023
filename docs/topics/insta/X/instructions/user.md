## `User` Class Documentation

### Section 1: Core `User` Implementation (No Dependencies)

This section includes the components of the `User` class that can be implemented without relying on other classes like `Post` and `Message`.

#### Instance Attributes:

- **`username`**: A **public** string representing the user's unique username. This attribute is directly accessible, and its validation is handled by the `is_valid_username` static method.

- **`_email`**: A **protected** string representing the user's email address. The email can be accessed or validated through methods if needed but is protected to prevent external modifications.

- **`_bio`**: A **protected** string representing the user's biography, limited to 150 characters. Access and modification of the biography are managed through the `bio` property, and the setter enforces the length limit.

#### Instance Methods:

- **`__init__(self, username: str, email: str)`**: Initializes the `User` object with a `username` and an `email`. The `username` and `email` are validated using the `is_valid_username` and `is_valid_email` static methods. The `bio` is initialized to an empty string, and lists for posts, followers, and following are initialized as empty lists. This method also increments the `user_count` class attribute.

- **`@property bio(self) -> str`**: A property method for accessing the user's biography. The getter returns the `_bio` value, and the setter ensures that the bio is no longer than 150 characters. If the limit is exceeded, a `ValueError` is raised.

- **`@classmethod get_user_count(cls) -> int`**: Returns the current number of users in the system by accessing the `user_count` class attribute.

#### Class Attributes:

- **`user_count`**: A **class attribute** that tracks the total number of users. It is incremented by 1 each time a new `User` object is created.

#### Static Methods:

- **`is_valid_username(username: str) -> bool`**: A static method that validates the `username`. The username must be between 3 and 30 characters long and can contain letters, numbers, periods, and underscores. Returns `True` if valid, otherwise `False`.

- **`is_valid_email(email: str) -> bool`**: A static method that validates the format of an email address using a regular expression (regex). It checks that the email contains an "@" symbol, a valid domain, and follows common email format rules. Returns `True` if valid, otherwise `False`.

---

### Section 2: Implementation Details Involving `Post`

This section includes methods and attributes that require the `Post` class for proper implementation. The `Post` class is expected to be available for these attributes and methods.

#### Instance Attributes:

- **`_posts`**: A **private** list of `Post` objects representing the posts created by the user. This list can only be manipulated through specific methods like `create_post` and `delete_post` to maintain control over the posts.

#### Instance Methods:

- **`create_post(self, content: str, tags: Optional[List[str]] = None) -> None`**: Allows the user to create a post. The post content is provided as a string, and an optional list of tags may also be provided. The post is added to the `_posts` list.

- **`delete_post(self, post: 'Post') -> None`**: Removes a specified post from the `_posts` list.

- **`like_post(self, post: 'Post') -> None`**: Adds the user to the `Post` object's likes list. This method assumes that the `Post` class provides an appropriate method to handle likes.

- **`unlike_post(self, post: 'Post') -> None`**: Removes the user from the `Post` object's likes list.

- **`comment_on_post(self, post: 'Post', content: str) -> None**: Adds a comment to the post. The post and comment content are provided as arguments.

---

### Section 3: Implementation Details Involving `User` (for Social Interaction)

This section covers attributes and methods that require the `User` class to implement social interactions like following and messaging.

#### Instance Attributes:

- **`_followers`**: A **private** list of `User` objects representing the users who follow this user. This list can only be updated through specific methods like `follow()` and `unfollow()` to ensure the integrity of follower interactions.

- **`_following`**: A **private** list of `User` objects representing the users this user follows. Like `_followers`, this list is managed through dedicated methods.

#### Instance Methods:

- **`follow(self, user: 'User') -> None`**: Adds the specified `User` object to the current user's `_following` list, and adds the current user to the target user's `_followers` list. The method ensures that a user cannot follow the same person more than once.

- **`unfollow(self, user: 'User') -> None`**: Removes the specified `User` object from the current user's `_following` list, and removes the current user from the target user's `_followers` list.

- **`send_message(self, recipient: 'User', content: str) -> None`**: Sends a message from the current user to another `User`. This assumes that the `Message` class is available and is used to create a message object.

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