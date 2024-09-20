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

- **`__init__(self, username: str, email: str)`**: 
  - Parameters: `username` (str), `email` (str)
  - Validates the `username` and `email` using the `is_valid_username` and `is_valid_email` static methods.
  - If either is invalid, raises a `ValueError` with an appropriate message.
  - Sets the `username` and `_email` attributes.
  - Initializes `_bio` to an empty string.
  - Increments the `user_count` class attribute by 1.

- **`@property bio(self) -> str`**: 
  - Getter: Returns the `_bio` value.
  - Setter: Accepts a string value. If the new bio is longer than 150 characters, raises a `ValueError`. Otherwise, sets `_bio` to the new value.

### Class Methods:

- **`@classmethod get_user_count(cls) -> int`**: 
  - Returns the current value of `user_count`.

### Static Methods:

- **`@staticmethod is_valid_username(username: str) -> bool`**: 
  - Validates the `username`.
  - Returns `True` if the username is 3-30 characters long and contains only letters, numbers, periods, and underscores.
  - Returns `False` otherwise.

- **`@staticmethod is_valid_email(email: str) -> bool`**: 
  - Validates the email address format using a regular expression.
  - Returns `True` if the email contains an "@" symbol, a valid domain, and follows common email format rules.
  - Returns `False` otherwise.

## `Post` Class

Create a `post.py` file and implement the `Post` class as follows:

### Instance Attributes:

- **`__content`**: A **private** string for the post's content, limited to 2200 characters.
- **`timestamp`**: A **public** `datetime` object recording post creation time.
- **`_tags`**: A **protected** list of strings representing post tags.

### Class Attributes:

- **`post_count`**: An integer that tracks the total number of posts. Initialize it to 0.

### Instance Methods:

- **`__init__(self, content: str, tags: Optional[List[str]] = None)`**: 
  - Parameters: `content` (str), `tags` (Optional[List[str]])
  - Sets `__content` using the `content` property setter (which will validate the length).
  - Sets `timestamp` to the current date and time using `datetime.now()`.
  - Initializes `_tags` with the provided tags or an empty list if None.
  - Increments the `post_count` class attribute by 1.

- **`@property content(self) -> str`**: 
  - Getter: Returns the `__content` value.
  - Setter: Accepts a string value. If the new content is longer than 2200 characters, raises a `ValueError`. Otherwise, sets `__content` to the new value.

- **`add_tag(self, tag: str) -> None`**: 
  - Validates the tag using `is_valid_tag`.
  - If valid, adds the tag to `_tags`. If invalid, raises a `ValueError`.

- **`remove_tag(self, tag: str) -> None`**: 
  - Removes the specified tag from `_tags` if it exists. Does nothing if the tag is not in the list.

### Class Methods:

- **`@classmethod get_post_count(cls) -> int`**: 
  - Returns the current value of `post_count`.

### Static Methods:

- **`@staticmethod is_valid_tag(tag: str) -> bool`**: 
  - Returns `True` if the tag is alphanumeric and no more than 30 characters long.
  - Returns `False` otherwise.

## `Comment` Class

Create a `comment.py` file and implement the `Comment` class as follows:

### Instance Attributes:

- **`__content`**: A **private** string for comment content, limited to 2200 characters.
- **`timestamp`**: A **public** `datetime` object for comment creation time.

### Instance Methods:

- **`__init__(self, content: str)`**: 
  - Parameters: `content` (str)
  - Sets `__content` using the `content` property setter (which will validate the length).
  - Sets `timestamp` to the current date and time using `datetime.now()`.

- **`@property content(self) -> str`**: 
  - Getter: Returns the `__content` value.
  - Setter: Accepts a string value. If the new content is longer than 2200 characters, raises a `ValueError`. Otherwise, sets `__content` to the new value.

## `Message` Class

Create a `message.py` file and implement the `Message` class as follows:

### Instance Attributes:

- **`__content`**: A **private** string for message content, limited to 2000 characters.
- **`timestamp`**: A **public** `datetime` object for message creation time.

### Instance Methods:

- **`__init__(self, content: str)`**: 
  - Parameters: `content` (str)
  - Sets `__content` using the `content` property setter (which will validate the length).
  - Sets `timestamp` to the current date and time using `datetime.now()`.

- **`@property content(self) -> str`**: 
  - Getter: Returns the `__content` value.
  - Setter: Accepts a string value. If the new content is longer than 2000 characters, raises a `ValueError`. Otherwise, sets `__content` to the new value.
