# Step 2: Enhance Core Classes

In this step, we will enhance our Instagram-like application by adding more functionality to the existing classes. We will introduce new methods and attributes to the `User`, `Post`, `Comment`, and `Message` classes to support features like creating posts, liking posts, commenting on posts, following/unfollowing users, and sending messages.

## `User` Class

Update the `User` class in `user.py` to include the following methods and attributes:

### Additional Instance Attributes:

- **`_posts`**: A **private** list of `Post` objects representing the posts created by the user. Initialize this as an empty list in the constructor.
- **`_followers`**: A **private** list of `User` objects representing users following this user. Initialize as an empty list in the constructor.
- **`_following`**: A **private** list of `User` objects representing users this user is following. Initialize as an empty list in the constructor.

### Additional Instance Methods:

1. **`create_post(self, content: str, tags: Optional[List[str]] = None) -> None`**: 
   - Create a new `Post` object with the given content, this user as the author, and the optional tags.
   - Append the new post to the `_posts` list.

2. **`delete_post(self, post: 'Post') -> None`**: 
   - Remove the specified post from the `_posts` list if it exists.
   - Use list's `remove()` method, handling the case where the post might not be in the list.

3. **`like_post(self, post: 'Post') -> None`**: 
   - Call the `add_like()` method on the given post object, passing `self` as the argument.

4. **`unlike_post(self, post: 'Post') -> None`**: 
   - Call the `remove_like()` method on the given post object, passing `self` as the argument.

5. **`comment_on_post(self, post: 'Post', content: str) -> None`**: 
   - Create a new `Comment` object with `self` as the author and the given content.
   - Add this comment to the post (assuming the `Post` class has a method to add comments).

6. **`follow(self, user: 'User') -> None`**: 
   - Add the given user to this user's `_following` list if not already present.
   - Add this user to the given user's `_followers` list.

7. **`unfollow(self, user: 'User') -> None`**: 
   - Remove the given user from this user's `_following` list if present.
   - Remove this user from the given user's `_followers` list.

## `Post` Class

Update the `Post` class in `post.py` to include the following methods and attributes:

### Additional Instance Attributes:

- **`author`**: A **public** `User` object representing the user who created the post.
- **`_likes`**: A **protected** list of `User` objects representing users who have liked the post. Initialize as an empty list in the constructor.

### Additional Instance Methods:

1. **`add_like(self, user: 'User') -> None`**: 
   - Check if the user is not already in the `_likes` list.
   - If not, append the user to the `_likes` list.

2. **`remove_like(self, user: 'User') -> None`**: 
   - Check if the user is in the `_likes` list.
   - If so, remove the user from the `_likes` list.

## `Comment` Class

Update the `Comment` class in `comment.py` to include the following methods and attributes:

### Additional Instance Attributes:

- **`author`**: A **public** `User` object representing the user who made the comment.

### Updated Instance Methods:

1. **`__init__(self, author: 'User', content: str)`**: 
   - Initialize the `author` attribute with the given `User` object.
   - Set the `content` using the existing setter method.
   - Initialize the `timestamp` as in the original code.

## `Message` Class

Update the `Message` class in `message.py` to include the following methods and attributes:

### Additional Instance Attributes:

- **`sender`**: A **public** `User` object representing the user who sent the message.
- **`recipient`**: A **public** `User` object representing the user who is the recipient of the message.

### Updated Instance Methods:

1. **`__init__(self, sender: 'User', recipient: 'User', content: str)`**: 
   - Initialize the `sender` and `recipient` attributes with the given `User` objects.
   - Set the `content` using the existing setter method.
   - Initialize the `timestamp` as in the original code.

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