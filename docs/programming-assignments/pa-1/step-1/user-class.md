# `User` Class


::::{grid}
:gutter: 2

:::{grid-item}
:columns: 8
The `User` class represents a user in the Instagram-like application. Each user has a unique username, email address, and a biography.


The class diagram shown provides an overview of the class structure.  Create a `user.py` file and implement the `User` class following the specifications provided below.

Below you will find the detailed specifications for the `User` class, including the attributes and methods that need to be implemented.
:::
:::{grid-item}
:columns: 4
```{mermaid}
classDiagram
    class User {
        +static int user_count
        +str username
        #str _email
        #str _bio
        +__init__(username, email)
        +get_user_count()
        +bio(value)
        +is_valid_username(username)
        +is_valid_email(email)
        
    }
```
:::

::::


## Attributes

The `User` class must have the following attributes:

| Name               | Kind          | Access Level  | Type    | Description                          |
|--------------------|---------------|---------------|---------|--------------------------------------|
| `username`         | Instance      | Public (+)    | `str`   | The user's username.                 |
| `_email`           | Instance      | Protected (#) | `str`   | The user's email, intended for internal use. |
| `_bio`             | Instance      | Protected (#) | `str`   | The user's biography, internal use.  |
| `user_count`       | Class         | Public (+)    | `int`   | Tracks the total number of users.    |




## Methods

The `User` class must have the following methods:


| Name                | Kind          | Return Type   | Parameters                          | Description                                |
|---------------------|---------------|--------------|-------------------------------------|--------------------------------------------|
| `__init__`          | Instance      | `None`         | `self`, `username`, `email`         | Initializes a new user object with username and email. |
| `bio`               | Property      | `None`         | `self`                              | Gets the user's bio.                       |
| `bio`               | Property      | `None`         | `self`, `value`                     | Sets the user's bio.                       |
| `get_user_count`    | Class         | `int`          | `cls`                               | Returns the total number of users.         |
| `is_valid_username` | Static        | `bool`         | `username`                          | Checks if the given username is valid.     |
| `is_valid_email`    | Static        | `bool`         | `email`                             | Checks if the given email is valid.        |



### Implementation Details

**`__init__(self, username, email)`**
- The `__init__` method is the constructor for the `User` class. The `username` and `email` parameters are required. 
- The `__init__` method should validate that `username` and `email` are valid before initializing the attributes. If either the `username` or `email` is invalid, raise a `ValueError` with an appropriate message. If both are valid, initialize the `username` and `_email` attributes with the provided values.
- The `_bio` attribute should be initialized to an empty string.
- Increment the `user_count` class attribute by 1.

**`bio(self)`**
- Implement the getter that returns the value of `_bio`.

**`bio(self, value)`**
- Implement the setter which accepts a string `value`. If the `value` is longer than 150 characters, raise a `ValueError`. Otherwise, set `_bio` to the new `value`.


**`get_user_count(cls)`**
- Return the current value of the `user_count` class attribute.


**`is_valid_username(username)`**
- Return `True` if the `username` is 3-30 characters long and contains only letters, numbers, periods, and underscores.
- Return `False` otherwise.


**`is_valid_email(email)`**
- Return `True` if the `email` is in a valid format, i.e., it contains a username, the `@` symbol, a domain name, and a top-level domain (e.g., `.com`, `.org`, `.net`). Use the following regex pattern: `r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'`
- Return `False` otherwise.


## Testing

### Interactive Testing

To interactively test the implemented classes, you can use Python's interactive shell. Here are some steps to follow:

1. Open a terminal and navigate to the directory containing your Python files.
2. Start the Python interactive shell by typing `python` or `python3` (depending on your system).
3. Import the classes you want to test. For example:
   ```python
   from user import User
   ```
4. Create instances of the classes and test their methods. For example:
   ```python
   # Test User class
   user = User("testuser", "test@example.com")
   print(user.username)  # Should print: testuser
   user.bio = "This is a test bio"
   print(user.bio)  # Should print: This is a test bio
   print(User.get_user_count())  # Should print: 1

5. Try to trigger validation errors by providing invalid inputs:
   ```python
   User("a", "invalid")  # Should raise ValueError
   ```

### Running Unit Tests

To run the unit tests for our Instagram-like app classes, download the following test files:

- [test_user.py](./test_user.py)

Follow these steps to run the tests:

1. Ensure that all your implementation files (`user.py`) and their corresponding test files (`test_user.py`) are in the same directory.

2. Open a terminal or command prompt and navigate to the directory containing these files.

3. To run all tests at once, use the following command:
   ```
   python -m unittest discover
   ```
   This command will discover and run all test files in the current directory that start with `test_`.

4. To run tests for a specific module, use one of the following commands:
   ```
   python -m unittest test_user.py
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
