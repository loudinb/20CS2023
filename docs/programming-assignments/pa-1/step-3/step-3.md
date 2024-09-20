# Step 3: Final Enhancements

In this step, we will make final enhancements to our Instagram-like application by adding more functionality to the existing classes. We will focus on refining the `User` and `Post` classes to support additional features.

## `User` Class

Update the `User` class in `user.py` to include the following additional attributes and methods:

### Additional Instance Attributes:

- **`_messages`**: A **private** list of `Message` objects representing the messages received by this user. This list is managed through the `receive_message()` method to ensure proper message handling.

### Additional Instance Methods:

1. **`send_message(self, recipient: 'User', content: str) -> Message`**: 
   - Create a new `Message` object with the current user as the sender, the specified recipient, and the given content.
   - Call the `receive_message()` method on the recipient user to deliver the message.
   - Return the created `Message` object.

2. **`receive_message(self, message: 'Message') -> None`**: 
   - Verify that the recipient of the message is the current user.
   - Add the received message to the `_messages` list.
   - Implement any necessary operations to mark the message as received or trigger notifications (if implemented).

### Updated Instance Methods:

1. **`follow(self, user: 'User') -> None`**: 
   - Ensure that a user cannot follow the same person more than once.
   - Add appropriate checks before adding to the `_following` and `_followers` lists.

2. **`unfollow(self, user: 'User') -> None`**: 
   - Add appropriate checks to ensure the user is in the `_following` list before removing.

## `Post` Class

Update the `Post` class in `post.py` to include the following additional attributes and methods:

### Additional Instance Attributes:

- **`_comments`**: A **protected** list of `Comment` objects representing the comments on the post. Comments are managed using the `add_comment()` and `remove_comment()` methods. Subclasses may access this attribute if needed.

### Additional Instance Methods:

1. **`add_comment(self, user: 'User', content: str) -> None`**: 
   - Create a new `Comment` object with the given `user` as the author and the provided `content`.
   - Add the newly created `Comment` object to the `_comments` list.

2. **`remove_comment(self, comment: 'Comment') -> None`**: 
   - Remove the specified `Comment` object from the `_comments` list, if it exists.
   - If the comment doesn't exist in the list, handle this case appropriately (e.g., raise an exception or simply return).


## Testing

### Interactive Testing

To interactively test the new features implemented in the `User` and `Post` classes, you can use Python's interactive shell. Follow these steps:

1. Open a terminal and navigate to the directory containing your Python files.
2. Start the Python interactive shell by typing `python` or `python3` (depending on your system).
3. Import the updated classes:
   ```python
   from user import User
   from post import Post
   from message import Message
   from comment import Comment
   ```
4. Create instances of the classes and test the new methods:
   ```python
   # Test User class enhancements
   user1 = User("user1", "user1@example.com")
   user2 = User("user2", "user2@example.com")
   
   # Test follow and unfollow
   user1.follow(user2)
   print(user1._following)  # Should contain user2
   print(user2._followers)  # Should contain user1
   user1.unfollow(user2)
   print(user1._following)  # Should be empty
   print(user2._followers)  # Should be empty
   
   # Test send_message and receive_message
   message = user1.send_message(user2, "Hello, user2!")
   print(message.content)  # Should print: Hello, user2!
   print(user2._messages)  # Should contain the message
   
   # Test Post class enhancements
   post = Post("This is a test post", ["test"])
   
   # Test add_comment
   post.add_comment(user1, "Great post!")
   print(post._comments)  # Should contain the comment
   
   # Test remove_comment
   comment_to_remove = post._comments[0]
   post.remove_comment(comment_to_remove)
   print(post._comments)  # Should be empty
   ```
5. Try to trigger edge cases and potential errors:
   ```python
   # Attempt to follow the same user twice
   user1.follow(user2)
   user1.follow(user2)  # Should not add user2 again
   
   # Attempt to unfollow a user not being followed
   user1.unfollow(user2)
   user1.unfollow(user2)  # Should handle this case gracefully
   
   # Attempt to remove a non-existent comment
   non_existent_comment = Comment("This comment doesn't exist")
   post.remove_comment(non_existent_comment)  # Should handle this case gracefully
   ```

### Running Unit Tests

To run the unit tests for our Instagram-like app classes, download the following test files:

- [test_user.py](./test_user.py)
- [test_post.py](./test_post.py)
- [test_comment.py](./test_comment.py)
- [test_message.py](./test_message.py)

Follow these steps to run the tests:

1. Ensure that your implementation files (`user.py`, `post.py`) and their corresponding test files (`test_user.py`, `test_post.py`) are in the same directory and have been updated to include tests for the new features.

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
