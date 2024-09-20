# Exercise 1

## Create `User` Class

The `User` class represents a user in the application, managing user information, posts, followers, and other user interactions.  Create a `user.py` file and implement the `User` class based on the following specifications:

### Instance Attributes:

- **`username`**: A **public** string representing the user's unique username. This should be accessible outside the class, as usernames are generally public. Validation of the username is done through the `is_valid_username` static method.
  
- **`_email`**: A **protected** string representing the user's email address. Direct access to the email is restricted to protect user privacy, but it may be accessed through a method if needed. The email is validated using the `is_valid_email` static method.
  
- **`_bio`**: A **protected** string representing the user's biography (limited to 150 characters). This attribute is modifiable through the `bio` property and its setter method, which ensures that the bio does not exceed 150 characters. Direct access to `_bio` is discouraged.

- **`_posts`**: A **private** list of `Post` objects (representing posts created by the user). This list should only be manipulated through specific methods like `create_post` and `delete_post`, preventing direct external access.
  
- **`_followers`**: A **private** list of `User` objects representing users who follow this user. This list can only be updated through methods like `follow()` or `unfollow()`, preventing external modification.

- **`_following`**: A **private** list of `User` objects representing users that this user follows. It is controlled through methods like `follow()` or `unfollow()`, similar to `_followers`.

### Instance Methods:

- **`__init__(self, username, email)`**: Initializes a `User` object with a username and email. The username and email are validated by the `is_valid_username` and `is_valid_email` static methods, respectively. It also initializes the `_bio`, `_posts`, `_followers`, and `_following` attributes with default values. The `user_count` class attribute is incremented by 1 whenever a new user is created.

  - `_bio`: Initialized to an empty string.
  - `_posts`, `_followers`, and `_following`: Initialized as empty lists.

- **`@property bio(self)`**: Provides controlled access to the user's biography. The getter method retrieves the current biography, and the setter method ensures that the biography is no longer than 150 characters. Raises a `ValueError` if the bio exceeds the character limit.
  
- **`create_post(self, content, tags=None)`**: Allows the user to create a post. The post is then added to the protected `_posts` list. Parameters include `content` (the post text) and `tags` (optional list of tags).

- **`delete_post(self, post)`**: Removes a specified post from the user's `_posts` list.

- **`follow(self, user)`**: Adds the specified `User` object to this user's `_following` list and updates the target user's `_followers` list. Before adding, the method checks that the user isn't already being followed.

- **`unfollow(self, user)`**: Removes the specified `User` object from this user's `_following` list and updates the target user's `_followers` list.

- **`like_post(self, post)`**: Allows the user to like a post, adding the user to the post's `likes` list.

- **`unlike_post(self, post)`**: Removes the user's like from the post.

- **`comment_on_post(self, post, content)`**: Allows the user to comment on a specified post. The `content` argument is the text of the comment.

- **`send_message(self, recipient, content)`**: Sends a message from this user to another `User`. The recipient is a `User` object, and `content` is the message text.

### Class Attributes:

- **`user_count`**: A **class attribute** that tracks the total number of users in the system. It is incremented by 1 each time a new `User` object is created.

### Class Methods:

- **`get_user_count(cls)`**: A **class method** that returns the current number of `User` instances in the system, i.e., the value of `user_count`.

### Static Methods:

- **`is_valid_username(username)`**: A **static method** that checks if a username is valid. The username must be between 3 and 30 characters long, and can only contain letters, numbers, periods, or underscores. Returns `True` if valid, otherwise `False`.

- **`is_valid_email(email)`**: A **static method** that validates the format of an email address using a regular expression (regex). It ensures that the email contains an "@" symbol, has a valid domain, and follows common email format rules. Returns `True` if valid, otherwise `False`.

    ```python
    import re

    email_address = "bearcat@uc.edu"
    regex_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(regex_pattern, email_address):
        return True
    else:
        return False
    ```



### Implementation Comments

- **Encapsulation**: Sensitive or mutable attributes like `_email`, `_bio`, `_posts`, `_followers`, and `_following` are protected or private to prevent direct external access and modification. Instead, they are managed through appropriate methods to maintain control over the user's data.
  
- **Validation**: Username and email attributes are validated upon initialization of the user to ensure proper formatting and uniqueness constraints.
  
- **Privacy**: The `_email` attribute is protected to avoid exposing sensitive information like the user's email address. Access to it can be restricted or controlled based on further design choices, such as creating a getter method.
  
- **Mutability of Lists**: The lists `_posts`, `_followers`, and `_following` are encapsulated to avoid direct modifications. Users can only modify these attributes through provided methods like `create_post`, `follow`, and `unfollow`, ensuring better control over user actions and relationships.
