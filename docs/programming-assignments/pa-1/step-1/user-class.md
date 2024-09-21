# `User` Class

::::{grid}
:gutter: 2

::: {grid-item} 
:columns: 8 
The `User` class represents a user in an Instagram-like application. Each user has a unique username, email address, and a biography.

Follow the specifications provided below to create a `User` class in the `user.py` file.

:::

::: {grid-item}
:columns: 4

```{mermaid}
classDiagram
    class User {
        +static int user_count
        +str username
        #datetime _joined_on
        #str _email
        #str _bio
        +__init__(username, email)
        +get_user_count()
        +bio()
        +bio(value)
        +is_valid_username(username)
        +is_valid_email(email)
    }
```

:::

::::

## Attributes

The `User` class must have the following attributes:

| Name            | Kind          | Access Level   | Type        | Description                                     |
|-----------------|---------------|----------------|-------------|-------------------------------------------------|
| `username`      | Instance      | Public (+)     | `str`       | The user's username.                            |
| `_email`        | Instance      | Protected (#)  | `str`       | The user's email, for internal use only.        |
| `_bio`          | Instance      | Protected (#)  | `str`       | The user's biography, for internal use only.    |
| `_joined_on`    | Instance      | Protected (#)  | `datetime`  | The date and time when the user joined.         |
| `user_count`    | Class         | Public (+)     | `int`       | Tracks the total number of users.               |

## Methods

The `User` class must implement the following methods:

| Name                | Kind         | Return Type   | Parameters           | Description                                                                 |
|---------------------|--------------|---------------|----------------------|-----------------------------------------------------------------------------|
| `__init__(self, username, email)` | Instance | None          | `username: str`, `email: str`  | Initializes a new `User` object and increments the `user_count` attribute.  |
| `get_user_count()`   | Class        | `int`         | None                 | Returns the total number of users.                                          |
| `bio(self)`          | Property     | `str`         | None                 | Returns the user's biography.                                               |
| `bio(self, value)`   | Property Setter | None       | `value: str`         | Sets the biography with a length restriction of 150 characters or less.     |
| `is_valid_username(username)` | Static | `bool`       | `username: str`       | Returns `True` if the username is valid (3-30 characters, alphanumeric, `.` or `_` allowed). |
| `is_valid_email(email)`  | Static  | `bool`         | `email: str`          | Returns `True` if the email is valid, following a standard email format.    |



### Implementation Details

**`__init__(self, username, email)`**
- The `__init__` method initializes a new instance of the `User` class. The `username` and `email` parameters are required.
- Validate the `username` using the `is_valid_username` method. If the `username` is invalid, raise a `ValueError` with an appropriate error message. If valid, assign the `username` to the `username` attribute.
- Validate the `email` using the `is_valid_email` method. If the `email` is invalid, raise a `ValueError` with an appropriate error message. If valid, assign the `email` to the `_email` attribute.
- Set the `_bio` attribute to an empty string, as the user does not have a biography initially.
- Set the `_joined_on` attribute to the current date and time, representing when the user was created.
- Increment the `user_count` class attribute by 1 to keep track of the number of `User` instances created.

**`bio(self)`**
- Implement the getter method for `bio`, which should return the value of the `_bio` attribute. This provides access to the user's biography.

**`bio(self, value)`**
- Implement the setter method for `bio`. It accepts a string `value` as the new biography. 
- If the `value` exceeds 150 characters, raise a `ValueError` indicating that the biography must be 150 characters or fewer. 
- If the length is valid, update the `_bio` attribute with the new `value`.

**`get_user_count(cls)`**
- Implement this method as a class method that returns the current value of the `user_count` class attribute.
- This method provides a way to retrieve the total number of `User` instances that have been created.

**`is_valid_username(username)`**
- Implement this method as a static method to validate the `username`.
- Return `True` if the `username` meets the following criteria:
  - It is between 3 and 30 characters in length.
  - It contains only alphanumeric characters (letters and numbers), periods (`.`), and underscores (`_`).
- Return `False` if the `username` does not meet these criteria.

**`is_valid_email(email)`**
- Implement this method as a static method to validate the `email`.
- Return `True` if the `email` matches the following criteria:
  - The `email` follows a valid format, which includes a username, the `@` symbol, a domain name, and a top-level domain (e.g., `.com`, `.org`, `.net`).
  - Use the provided regular expression pattern to validate the `email` format: `r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'`.
- Return `False` if the `email` does not match the valid format.


## Testing

### Manual Testing

1. Open a terminal or command prompt.
2. Run Python by typing `python` or `python3` (depending on your system).
3. Import the `User` class:
   ```python
   from user import User
   ```
4. Create instances of the `User` class and test the methods:
   ```python
   user = User("testuser", "test@example.com")
   print(user.username)  # Expected output: testuser
   user.bio = "This is a test bio"
   print(user.bio)  # Expected output: This is a test bio
   print(User.get_user_count())  # Expected output: 1
   ```
5. Test invalid inputs to trigger validation errors:
   ```python
   User("a", "invalid-email")  # Expected: raises ValueError
   ```

### Running Unit Tests

To run unit tests for the `User` class, follow these steps:

1. Ensure that your `user.py` file and the corresponding test file (`test_user.py`) are in the same directory.
2. Open a terminal or command prompt and navigate to that directory.
3. To run all tests, use the following command:
   ```bash
   python -m unittest discover
   ```
   This command will discover and run all test files that start with `test_`.
4. To run tests for a specific module, use:
   ```bash
   python -m unittest test_user.py
   ```
5. The test results will appear in the terminal, indicating which tests passed or failed.

6. If all tests pass, you should see output like:
   ```bash
   ..........
   ----------------------------------------------------------------------
   Ran 10 tests in 0.002s
   OK
   ```

7. If any tests fail, the output will provide detailed information on what failed and why, helping you debug and fix the issues.