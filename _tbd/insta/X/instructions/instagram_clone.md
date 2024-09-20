## Part 5: The `InstagramClone` Class

### Objective
Create an `InstagramClone` class to manage users and posts.

### Instance Attributes:
- `_users`: A **protected** list of `User` objects representing all users registered in the system. This should be accessible by subclasses but not directly modifiable from outside.

### Instance Methods:

- **`__init__(self)`**: Initializes the application with an empty list of users.

- **`

register_user(self, username, email)`**: Registers a new user and adds them to the protected `_users` list.

- **`get_user(self, username)`**: Retrieves a `User` object by username.

- **`get_posts_by_tag(self, tag)`**: Retrieves all posts containing a specific tag.

### Static Methods:

- **`is_valid_email(email)`**: Validates an email address (basic validation to check format).
