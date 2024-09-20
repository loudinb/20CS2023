# `User` Class

#### Instance Attributes:

- **`username`**: A **public** string representing the user's unique username. This attribute is directly accessible, and its validation is handled by the `is_valid_username` static method.

- **`_email`**: A **protected** string representing the user's email address. The email can be accessed or validated through methods if needed but is protected to prevent external modifications.

- **`_bio`**: A **protected** string representing the user's biography, limited to 150 characters. Access and modification of the biography are managed through the `bio` property, and the setter enforces the length limit.

#### Instance Methods:

- **`__init__(self, username: str, email: str)`**: Initializes the `User` object with a `username` and an `email`. The `username` and `email` are validated using the `is_valid_username` and `is_valid_email` static methods. The `bio` is initialized to an empty string, and lists for posts, followers, and following are initialized as empty lists. This method also increments the `user_count` class attribute.

- **`@property bio(self) -> str`**: A property method for accessing the user's biography. The getter returns the `_bio` value, and the setter ensures that the bio is no longer than 150 characters. If the limit is exceeded, a `ValueError` is raised.

- **`@classmethod get_user_count(cls) -> int`**: Returns the current number of users in the system by accessing the `user_count` class attribute.

#### Class Attributes:

- **`user_count`**: A **class attribute** that tracks the total number of users. It is incremented by 1 each time a new `User` object is created.

#### Static Methods:

- **`is_valid_username(username: str) -> bool`**: A static method that validates the `username`. The username must be between 3 and 30 characters long and can contain letters, numbers, periods, and underscores. Returns `True` if valid, otherwise `False`.

- **`is_valid_email(email: str) -> bool`**: A static method that validates the format of an email address using a regular expression (regex). It checks that the email contains an "@" symbol, a valid domain, and follows common email format rules. Returns `True` if valid, otherwise `False`.
