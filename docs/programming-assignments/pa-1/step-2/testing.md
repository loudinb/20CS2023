
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
post = Post("This is a test post", user, ["test", "example"])
print(post.content)  # Should print: This is a test post
post.add_tag("newtag")
print(post._tags)  # Should print: ['test', 'example', 'newtag']
print(Post.get_post_count())  # Should print: 1

# Test Comment class
comment = Comment(user, "This is a test comment")
print(comment.content)  # Should print: This is a test comment
print(comment.timestamp)  # Should print the current date and time

# Test Message class
recipient = User("recipient", "recipient@example.com")
message = Message(user, recipient, "This is a test message")
print(message.content)  # Should print: This is a test message
print(message.timestamp)  # Should print the current date and time
```
5. Try to trigger validation errors by providing invalid inputs:
```python
User("a", "invalid")  # Should raise ValueError
Post("a" * 2201, user)  # Should raise ValueError
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