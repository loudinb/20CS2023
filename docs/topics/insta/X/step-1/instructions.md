# `User` Class

Create a `user.py` file and define a `User` class that represents a user in the social media application. The class should have the following attributes and methods:

## Instance Attributes:

- **`username`**: A **public** string representing the user's unique username. This attribute is directly accessible, and its validation is handled by the `is_valid_username` static method. 

- **`_email`**: A **protected** string representing the user's email address. The email can be accessed or validated through methods if needed but is protected to prevent external modifications.

- **`_bio`**: A **protected** string representing the user's biography, limited to 150 characters. Access and modification of the biography are managed through the `bio` property, and the setter enforces the length limit.

## Instance Methods:

- **`__init__(self, username: str, email: str)`**: Initializes the `User` object with a `username` and an `email`. The `username` and `email` are validated using the `is_valid_username` and `is_valid_email` static methods. The `bio` is initialized to an empty string, and lists for posts, followers, and following are initialized as empty lists. This method also increments the `user_count` class attribute.  Raise a `ValueError` if the username or email is invalid.

- **`@property bio(self) -> str`**: A property method for accessing the user's biography. The getter returns the `_bio` value, and the setter ensures that the bio is no longer than 150 characters. If the limit is exceeded, a `ValueError` is raised.

- **`@classmethod get_user_count(cls) -> int`**: Returns the current number of users in the system by accessing the `user_count` class attribute.

## Class Attributes:

- **`user_count`**: A **class attribute** that tracks the total number of users. It is incremented by 1 each time a new `User` object is created.

## Static Methods:

- **`is_valid_username(username: str) -> bool`**: A static method that validates the `username`. The username must be between 3 and 30 characters long and can contain letters, numbers, periods, and underscores. Returns `True` if valid, otherwise `False`.

- **`is_valid_email(email: str) -> bool`**: A static method that validates the format of an email address using a regular expression (regex). It checks that the email contains an "@" symbol, a valid domain, and follows common email format rules. Returns `True` if valid, otherwise `False`.

# `Post` Class

Create a `post.py` file and define a `Post` class that represents a post in the social media application. The class should have the following attributes and methods:

## Instance Attributes:

- **`__content`**: A **private** string representing the post’s content, limited to 2200 characters. The content should only be modified through the `content` property, ensuring strict validation.
  - **Why private**: Post content must be validated and controlled within the class, preventing external or subclass access. This ensures that the length constraint is always enforced.

- **`timestamp`**: A **public** `datetime` object recording when the post was created. The timestamp is set upon initialization and should not be modified afterward.

- **`_tags`**: A **protected** list of strings representing the tags in the post. This attribute is modifiable through specific methods such as `add_tag()` and `remove_tag()`. Subclasses can also access and modify this attribute if necessary.

## Instance Methods:

- **`__init__(self, content: str, tags: Optional[List[str]] = None)`**: Initializes the `Post` object with the required `content` (string) and optional list of `tags`. It also records the `timestamp` when the post is created. Validation of content length is performed within the constructor using the setter.

- **`@property content(self) -> str`**: This **property** manages access to the private `__content` attribute. The getter returns the post content. The setter ensures the content does not exceed 2200 characters. A `ValueError` is raised if the content exceeds this limit.
  - **Why private**: This ensures that all modifications to post content are validated through the property setter, which enforces the length constraint.

- **`add_tag(self, tag: str) -> None`**: Adds a tag to the `_tags` list. The `tag` must be validated using the `is_valid_tag()` static method before being added.

- **`remove_tag(self, tag: str) -> None`**: Removes a tag from the `_tags` list if it exists.

## Class Attributes:

- **`post_count`**: A **class attribute** that tracks the total number of posts in the system. This attribute is incremented in the `__init__` method each time a new `Post` object is created.

## Class Methods:

- **`@classmethod get_post_count(cls) -> int`**: A **class method** that returns the current total number of posts in the system by accessing the `post_count` class attribute.

## Static Methods:

- **`@staticmethod is_valid_tag(tag: str) -> bool`**: A **static method** that checks whether a tag is valid. A valid tag must be alphanumeric and no more than 30 characters long. Returns `True` if valid, otherwise `False`.


# `Comment` Class

Create a `comment.py` file and define a `Comment` class that represents a comment on a post in the social media application. The class should have the following attributes and methods:

## Instance Attributes:

- **`__content`**: A **private** string representing the comment’s content, limited to 2200 characters. The content should only be modified through the `content` property, ensuring strict validation.
  - **Why private**: Comment content must be validated and controlled within the class, preventing direct access or modification. This ensures that the length constraint is always enforced.

- **`timestamp`**: A **public** `datetime` object representing when the comment was made. This attribute is initialized at the time the comment is created and should not be modified afterward.

## Instance Methods:

- **`__init__(self, content: str)`**: Initializes the `Comment` object with the required `content`. It also records the `timestamp` when the comment is created. Validation of content length is performed within the constructor using the setter.

- **`@property content(self) -> str`**: This **property** manages access to the private `__content` attribute. The getter returns the comment content. The setter ensures the content does not exceed 2200 characters. A `ValueError` is raised if the content exceeds this limit.
  - **Why private**: This ensures that all modifications to comment content are validated through the property setter, which enforces the length constraint.


# `Message` Class

Create a `message.py` file and define a `Message` class that represents a direct message between users in the social media application. The class should have the following attributes and methods:

## Instance Attributes:

- **`__content`**: A **private** string representing the message’s content, limited to 2000 characters. The content should only be modified through the `content` property, ensuring strict validation.
  - **Why private**: Message content is sensitive and must be validated and controlled within the class, preventing direct access or modification. This ensures that the length constraint is always enforced.

- **`timestamp`**: A **public** `datetime` object representing the time when the message was sent. This attribute is initialized at the time of message creation and should not be modified afterward.

## Instance Methods:

- **`__init__(self, content: str)`**: Initializes the `Message` object with the required `content`. It also records the `timestamp` when the message is created. The content length is validated within the constructor using the setter.

- **`@property content(self) -> str`**: This **property** manages access to the private `__content` attribute. The getter returns the message content. The setter ensures the content does not exceed 2000 characters. A `ValueError` is raised if the content exceeds this limit.
  - **Why private**: This ensures that all modifications to message content are validated through the property setter, which enforces the length constraint.