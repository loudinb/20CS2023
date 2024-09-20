# Exercise 2

## Instance Attributes and Methods

In this exercise, you will expand the Instagram-like app by adding a new `Comment` class and enhancing the existing `User` and `Post` classes with more instance attributes and methods.

```{warning}
If there is any ambiguity in the requirements, make a reasonable assumption and proceed.  Then look at the provided unit tests to understand the expected behavior, and adjust your implementation accordingly.
```

### Step 1: Create `comment.py` File

1. Open your preferred text editor or IDE.
2. Create a new file and save it as `comment.py` in your project directory.
3. At the top of the file, import the `datetime` class from the `datetime` module (`from datetime import datetime`).

### Step 2: Implement the `Comment` Class

In `comment.py`, create a `Comment` class with the following features:

1. An `__init__` method that takes `user`, `post`, and `content` as parameters.
2. Instance attributes for `user`, `post`, `content`, `timestamp` (use `datetime.now()`), and `likes` (initialize to 0).
3. A `like(self)` method that increments the likes count.
4. A `display(self)` method that prints the comment's content, author, timestamp, and likes.

### Step 3: Update the `Post` Class

In `post.py`, update the `Post` class:

1. Import the `Comment` class from `comment.py`.
2. Add a `comments` attribute to the `__init__` method, initialized as an empty list.
3. Implement an `add_comment(self, user, content)` method that creates a new `Comment` instance and adds it to the `comments` list.
4. A `like(self)` method that increments the likes count.
5. Update the `display(self)` method to show the number of comments and list all comments.

### Step 4: Enhance the `User` Class

In `user.py`, enhance the `User` class:

1. Add a `liked_posts` attribute to the `__init__` method, initialized as an empty set.
2. Implement a `like_post(self, post)` method that adds the post to `liked_posts` and calls the post's `like_post` method.
3. Add a `comment_on_post(self, post, content)` method that calls the post's `add_comment` method.
4. Implement a `get_activity_feed(self)` method that returns a list of the user's recent actions (posts created, posts liked, and comments made), sorted by timestamp.


## Testing

### Interactive Testing

To test your code interactively using a Python shell:

1. Open a terminal and navigate to your project directory.
2. Start the Python interactive shell by typing `python` or `python3`.
3. Import your classes:
   ```python
   from user import User
   from post import Post
   from comment import Comment
   ```
4. Create users, posts, and comments:
   ```python
   user1 = User("johndoe", "john@example.com")
   user2 = User("janedoe", "jane@example.com")
   post1 = user1.create_post("Hello, world!")
   user2.like_post(post1)
   user2.comment_on_post(post1, "Great post!")
   ```
5. Test various methods:
   ```python
   user1.display_info()
   post1.display()
   user2.get_activity_feed()
   ```
6. Verify that the output matches your expectations.

### Running Unit Tests

Download the provided unit tests for the `User` and `Post` classes:

- [test_user.py](test_user.py)
- [test_post.py](test_post.py)
- [test_comment.py](test_comment.py)

To run the provided unit tests:

1. Ensure you have files named `test_user.py`, `test_post.py`, and `test_comment.py` in your project directory.

2. Open a terminal and navigate to your project directory.

3. Run the tests for each class:
   ```
   python -m unittest test_user.py
   python -m unittest test_post.py
   python -m unittest test_comment.py
   ```

4. To run all tests at once, use:
   ```
   python -m unittest discover
   ```

5. Review the test output. All tests should pass if your implementation is correct.

6. If any tests fail, review the error messages, go back to your implementation, and make the necessary corrections.