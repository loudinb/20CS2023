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
   - Check for periods and underscores separately from alphanumeric characters.
   - Return `False` otherwise.
   - Implementation hint: `return 3 <= len(username) <= 30 and username.replace(".", "").replace("_", "").isalnum()`

2. **`@staticmethod is_valid_email(email: str) -> bool`**: 
   - Validate the email address format using a regular expression.
   - Use the following regex pattern: `r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'`
   - Return `True` if the email matches the pattern.
   - Return `False` otherwise.
   - Implementation hint: 
     ```python
     import re
     pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
     return re.match(pattern, email) is not None
     ```

Remember to import the `re` module at the top of the file:
```python
import re
```

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

## Testing

### Interactive Testing

To interactively test the implemented classes, you can use Python's interactive shell. Here are some steps to follow:

1. Open a terminal and navigate to the directory containing your Python files.
2. Start the Python interactive shell by typing `python` or `python3` (depending on your system).
3. Import the classes you want to test. For example:
   ```python
   from user import User
   from post import Post
   from comment import Comment
   from message import Message
   ```
4. Create instances of the classes and test their methods. For example:
   ```python
   # Test User class
   user = User("testuser", "test@example.com")
   print(user.username)  # Should print: testuser
   user.bio = "This is a test bio"
   print(user.bio)  # Should print: This is a test bio
   print(User.get_user_count())  # Should print: 1

   # Test Post class
   post = Post("This is a test post", ["test", "example"])
   print(post.content)  # Should print: This is a test post
   post.add_tag("newt ag")
   print(post._tags)  # Should print: ['test', 'example', 'newtag']
   print(Post.get_post_count())  # Should print: 1

   # Test Comment class
   comment = Comment("This is a test comment")
   print(comment.content)  # Should print: This is a test comment
   print(comment.timestamp)  # Should print the current date and time

   # Test Message class
   message = Message("This is a test message")
   print(message.content)  # Should print: This is a test message
   print(message.timestamp)  # Should print the current date and time
   ```
5. Try to trigger validation errors by providing invalid inputs:
   ```python
   User("a", "invalid")  # Should raise ValueError
   Post("a" * 2201)  # Should raise ValueError
   ```

### Running Unit Tests

To run the unit tests for our Instagram-like app classes, download the following test files:

- [test_user.py](./test_user.py)
- [test_post.py](./test_post.py)
- [test_comment.py](./test_comment.py)
- [test_message.py](./test_message.py)

Follow these steps to run the tests:

1. Ensure that all your implementation files (`user.py`, `post.py`, `comment.py`, `message.py`) and their corresponding test files (`test_user.py`, `test_post.py`, `test_comment.py`, `test_message.py`) are in the same directory.

2. Open a terminal or command prompt and navigate to the directory containing these files.

3. To run all tests at once, use the following command:
   ```
   python -m unittest discover
   ```
   This command will discover and run all test files in the current directory that start with `test_`.

4. To run tests for a specific module, use one of the following commands:
   ```
   python -m unittest test_user.py
   python -m unittest test_post.py
   python -m unittest test_comment.py
   python -m unittest test_message.py
   ```

5. The test results will be displayed in the terminal. You'll see information about which tests passed and which (if any) failed.

6. If all tests pass, you should see output similar to this:
   ```
   ......................
   ----------------------------------------------------------------------
   Ran 22 tests in 0.002s

   OK
   ```
   The exact number of tests may vary depending on how many test cases are in each test file.

7. If any tests fail, you'll see detailed information about which tests failed and why. Use this information to debug and fix any issues in your implementation.
