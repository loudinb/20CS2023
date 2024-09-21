# Testing

## Interactive Testing

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

## Running Unit Tests

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
