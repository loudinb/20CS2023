# Exercise 1

## Classes and Objects Coding

In this exercise, you will create two classes for our Instagram-like app: `User` and `Post`. You'll define these classes in separate files to practice good code organization.

```{warning}
If there is any ambiguity in the requirements, make a reasonable assumption and proceed.  Then look at the provided unit tests to understand the expected behavior, and adjust your implementation accordingly.
```

### Step 1: Create `user.py` and `post.py` Files

1. Open your preferred text editor or IDE.
2. Create two new files and save them as `user.py` and `post.py` in your project directory.
3. At the top of both files, import the `datetime` class from the `datetime` module (`from datetime import datetime`).

### Step 2: Create the `User` Class

In your `user.py` file:

1. Import the `Post` class from `post.py`.
2. Create a `User` class with the following:
   - Define an `__init__` method that takes `username` and `email` as parameters.
   - Initialize instance attributes for `username`, `email`, and `join_date` (use `datetime.now()` for `join_date`).
   - Initialize an empty list called `posts` to store the user's posts.

### Step 3: Create the `Post` Class

In your `post.py` file:

1. Create a `Post` class with these requirements:
   - Define an `__init__` method that takes `user` and `content` as parameters.
   - Initialize instance attributes for `user`, `content`, `timestamp` (use `datetime.now()`), and `likes` (initialize to 0).

### Step 4: Add Methods to the `User` Class

In `user.py`, add the following methods to your `User` class:

1. `create_post(self, content)`: Creates a new `Post` instance and adds it to the user's `posts` list.
2. `display_info(self)`: Prints out the user's username, email, join date, and number of posts.

### Step 5: Add a Method to the `Post` Class

In `post.py`, add a `display(self)` method to your `Post` class that prints out the post's content, timestamp, and number of likes.


## Testing

### Interactive Testing

To test your code interactively using a Python shell:

1. Open a terminal and navigate to your project directory.
2. Start the Python interactive shell by typing `python` or `python3`.
3. Import your classes:
   ```python
   from user import User
   from post import Post
   ```
4. Create a user:
   ```python
   user1 = User("johndoe", "john@example.com")
   ```
5. Display user info:
   ```python
   user1.display_info()
   ```
6. Create a post:
   ```python
   user1.create_post("Hello, world!")
   ```
7. Access and display the post:
   ```python
   post = user1.posts[0]
   post.display()
   ```
8. Test other methods and interactions as needed.

### Running Unit Tests

Download the provided unit tests for the `User` and `Post` classes:

- [test_user.py](test_user.py)
- [test_post.py](test_post.py)

To run the provided unit tests:

1. Ensure you have a file named `test_user.py` for testing the `User` class and `test_post.py` for testing the `Post` class in your project directory.

2. Open a terminal and navigate to your project directory.

3. Run the tests for the `User` class:
   ```
   python -m unittest test_user.py
   ```

4. Run the tests for the `Post` class:
   ```
   python -m unittest test_post.py
   ```

5. Review the test output. All tests should pass if your implementation is correct.

6. If any tests fail, review the error messages, go back to your implementation, and make the necessary corrections.
