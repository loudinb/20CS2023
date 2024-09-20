# Exercise 3

## Encapsulation

In this exercise, you will refactor the existing classes to implement encapsulation and data hiding principles. You'll also create a new `PrivateMessage` class to practice these concepts further.

```{warning}
If there is any ambiguity in the requirements, make a reasonable assumption and proceed.  Then look at the provided unit tests to understand the expected behavior, and adjust your implementation accordingly.
```

## Step 1: Refactor the `User` Class

Update the `user.py` file:

1. Change all instance attributes to use a single underscore prefix (e.g., `self._username`).
2. Implement properties for `username` and `email` with appropriate getters and setters.
3. Create a `_validate_email` private method to check email format and use it within the email setter.
4. Update the `update_bio` method to use a property for `bio` with a setter that enforces the character limit.

## Step 2: Refactor the `Post` Class

Update the `post.py` file:

1. Change all instance attributes to use a single underscore prefix (e.g., `self._content`).
2. Implement a property for `likes_count` with a getter only.
3. Make the `like_post` and `unlike_post` methods protected by adding a single underscore prefix.
4. Create a public `toggle_like` method that calls the protected methods as appropriate.

## Step 3: Refactor the `Comment` Class

Update the `comment.py` file:

1. Change all instance attributes to use a single underscore prefix (e.g., `self._content`).
2. Implement a read-only property for `timestamp`.
3. Create a protected `_increment_likes` method and a public `like` method that calls it.

## Step 4: Create a `PrivateMessage` Class

Create a new file `private_message.py`:

1. Implement a `PrivateMessage` class with the following features:
   - Private attributes for sender, recipient, content, and timestamp.
   - A class attribute for keeping track of the total number of messages sent.
   - A static method to get the total message count.
   - Properties for accessing the private attributes (read-only for sender and recipient).
   - A method to display the message contents only if the provided user is either the sender or the recipient.

## Step 5: Update the `User` Class for Private Messages

In the `user.py` file:

1. Add a private attribute `_received_messages` initialized as an empty list.
2. Implement a method `send_private_message` that creates a new `PrivateMessage` and adds it to the recipient's `_received_messages`.
3. Create a method `view_private_messages` that returns a list of the user's received messages.

## Testing

### Interactive Testing

To test your refactored code interactively using a Python shell:

1. Open a terminal and navigate to your project directory.
2. Start the Python interactive shell by typing `python` or `python3`.
3. Import your classes:
   ```python
   from user import User
   from post import Post
   from comment import Comment
   from private_message import PrivateMessage
   ```
4. Create users and test the refactored methods:
   ```python
   user1 = User("johndoe", "john@example.com")
   user2 = User("janedoe", "jane@example.com")
   
   # Test properties
   print(user1.username)
   user1.email = "newemail@example.com"
   
   # Test protected methods
   post = user1.create_post("Hello, world!")
   post.toggle_like(user2)
   
   # Test private messages
   user1.send_private_message(user2, "Hi Jane!")
   print(user2.view_private_messages())
   ```
5. Verify that the output matches your expectations and that you cannot directly access private attributes.

### Running Unit Tests

Download the provided unit tests for the `User` and `Post` classes:

- [test_user.py](test_user.py)
- [test_post.py](test_post.py)
- [test_comment.py](test_comment.py)
- [test_private_message.py](test_private_message.py)

To run the provided unit tests:

1. Ensure you have a test files for each class: `test_user.py`, `test_post.py`, `test_comment.py`, and `test_private_message.py`.

2. Open a terminal and navigate to your project directory.

3. Run the tests for each class:
   ```
   python -m unittest test_user.py
   python -m unittest test_post.py
   python -m unittest test_comment.py
   python -m unittest test_private_message.py
   ```

4. To run all tests at once, use:
   ```
   python -m unittest discover
   ```

5. Review the test output. All tests should pass if your implementation is correct.

6. If any tests fail, review the error messages, go back to your implementation, and make the necessary corrections.
