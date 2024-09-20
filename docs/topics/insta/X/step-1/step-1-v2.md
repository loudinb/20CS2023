# Step 1: Implement Core Classes

This document provides instructions for implementing the core classes of our Instagram-like app: User, Post, Comment, and Message. Each class should be implemented in its own Python file.

## `User` Class

Create a `user.py` file and implement the `User` class as follows:

### Instance Attributes:

- **`username`**: A **public** string representing the user's unique username.
- **`_email`**: A **protected** string representing the user's email address.
- **`_bio`**: A **protected** string representing the user's biography, limited to 150 characters.

### Class Attributes:

- **`user_count`**: An integer that tracks the total number of users. Initialize it to 0.

### Instance Methods:

1. **`__init__(self, username: str, email: str)`**: 
   - Parameters: `username` (str), `email` (str)
   - Validate the `username` and `email` using the `is_valid_username` and `is_valid_email` static methods.
   - If either is invalid, raise a `ValueError` with an appropriate message.
   - Set the `username` and `_email` attributes.
   - Initialize `_bio` to an empty string.
   - Increment the `user_count` class attribute by 1.

2. **`@property bio(self) -> str`**: 
   - Implement a getter that returns the `_bio` value.
   - Implement a setter that accepts a string value. If the new bio is longer than 150 characters, raise a `ValueError`. Otherwise, set `_bio` to the new value.

### Class Methods:

1. **`@classmethod get_user_count(cls) -> int`**: 
   - Return the current value of `user_count`.

### Static Methods:

1. **`@staticmethod is_valid_username(username: str) -> bool`**: 
   - Validate the `username`.
   - Return `True` if the username is 3-30 characters long and contains only letters, numbers, periods, and underscores.
   - Return `False` otherwise.

2. **`@staticmethod is_valid_email(email: str) -> bool`**: 
   - Validate the email address format using a regular expression.
   - Return `True` if the email contains an "@" symbol, a valid domain, and follows common email format rules.
   - Return `False` otherwise.

## `Post` Class

Create a `post.py` file and implement the `Post` class as follows:

### Instance Attributes:

- **`__content`**: A **private** string for the post's content, limited to 2200 characters.
- **`timestamp`**: A **public** `datetime` object recording post creation time.
- **`_tags`**: A **protected** list of strings representing post tags.

### Class Attributes:

- **`post_count`**: An integer that tracks the total number of posts. Initialize it to 0.

### Instance Methods:

1. **`__init__(self, content: str, tags: Optional[List[str]] = None)`**: 
   - Parameters: `content` (str), `tags` (Optional[List[str]])
   - Set `__content` using the `content` property setter (which will validate the length).
   - Set `timestamp` to the current date and time using `datetime.now()`.
   - Initialize `_tags` with the provided tags or an empty list if None.
   - Increment the `post_count` class attribute by 1.

2. **`@property content(self) -> str`**: 
   - Implement a getter that returns the `__content` value.
   - Implement a setter that accepts a string value. If the new content is longer than 2200 characters, raise a `ValueError`. Otherwise, set `__content` to the new value.

3. **`add_tag(self, tag: str) -> None`**: 
   - Validate the tag using `is_valid_tag`.
   - If valid, add the tag to `_tags`. If invalid, raise a `ValueError`.

4. **`remove_tag(self, tag: str) -> None`**: 
   - Remove the specified tag from `_tags` if it exists. Do nothing if the tag is not in the list.

### Class Methods:

1. **`@classmethod get_post_count(cls) -> int`**: 
   - Return the current value of `post_count`.

### Static Methods:

1. **`@staticmethod is_valid_tag(tag: str) -> bool`**: 
   - Return `True` if the tag is alphanumeric and no more than 30 characters long.
   - Return `False` otherwise.

## `Comment` Class

Create a `comment.py` file and implement the `Comment` class as follows:

### Instance Attributes:

- **`__content`**: A **private** string for comment content, limited to 2200 characters.
- **`timestamp`**: A **public** `datetime` object for comment creation time.

### Instance Methods:

1. **`__init__(self, content: str)`**: 
   - Parameters: `content` (str)
   - Set `__content` using the `content` property setter (which will validate the length).
   - Set `timestamp` to the current date and time using `datetime.now()`.

2. **`@property content(self) -> str`**: 
   - Implement a getter that returns the `__content` value.
   - Implement a setter that accepts a string value. If the new content is longer than 2200 characters, raise a `ValueError`. Otherwise, set `__content` to the new value.

## `Message` Class

Create a `message.py` file and implement the `Message` class as follows:

### Instance Attributes:

- **`__content`**: A **private** string for message content, limited to 2000 characters.
- **`timestamp`**: A **public** `datetime` object for message creation time.

### Instance Methods:

1. **`__init__(self, content: str)`**: 
   - Parameters: `content` (str)
   - Set `__content` using the `content` property setter (which will validate the length).
   - Set `timestamp` to the current date and time using `datetime.now()`.

2. **`@property content(self) -> str`**: 
   - Implement a getter that returns the `__content` value.
   - Implement a setter that accepts a string value. If the new content is longer than 2000 characters, raise a `ValueError`. Otherwise, set `__content` to the new value.

Remember to import necessary types at the top of each file:
- `from typing import List, Optional`
- `from datetime import datetime`

Ensure to use type hints for all attributes and method parameters as shown in the examples above.