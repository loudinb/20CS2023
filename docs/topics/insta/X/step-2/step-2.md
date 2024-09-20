# Step 2

In this step, we will enhance our Instagram-like application by adding more functionality to the existing classes. We will introduce new methods and attributes to the `User`, `Post`, `Comment`, and `Message` classes to support features like creating posts, liking posts, commenting on posts, following/unfollowing users, and sending messages.

## `User` Class

Update the `User` class to include the following methods and attributes:

### Instance Attributes:

- **`_posts`**: A **private** list of `Post` objects representing the posts created by the user. Initialize this as an empty list in the constructor.
- **`_followers`**: A **private** list of `User` objects representing users following this user. Initialize as an empty list in the constructor.
- **`_following`**: A **private** list of `User` objects representing users this user is following. Initialize as an empty list in the constructor.

### Instance Methods:

- **`create_post(self, content: str, tags: Optional[List[str]] = None) -> None`**: 
  - Create a new `Post` object with the given content, this user as the author, and the optional tags.
  - Append the new post to the `_posts` list.

- **`delete_post(self, post: 'Post') -> None`**: 
  - Remove the specified post from the `_posts` list if it exists.
  - Use list's `remove()` method, handling the case where the post might not be in the list.

- **`like_post(self, post: 'Post') -> None`**: 
  - Call the `add_like()` method on the given post object, passing `self` as the argument.

- **`unlike_post(self, post: 'Post') -> None`**: 
  - Call the `remove_like()` method on the given post object, passing `self` as the argument.

- **`comment_on_post(self, post: 'Post', content: str) -> None**: 
  - Create a new `Comment` object with `self` as the author and the given content.
  - Add this comment to the post (assuming the `Post` class has a method to add comments).

- **`follow(self, user: 'User') -> None`**: 
  - Add the given user to this user's `_following` list if not already present.
  - Add this user to the given user's `_followers` list.

- **`unfollow(self, user: 'User') -> None`**: 
  - Remove the given user from this user's `_following` list if present.
  - Remove this user from the given user's `_followers` list.

## `Post` Class

Update the `Post` class to include the following methods and attributes:

### Instance Attributes:

- **`author`**: A **public** `User` object representing the user who created the post.
- **`_likes`**: A **protected** list of `User` objects representing users who have liked the post. Initialize as an empty list in the constructor.

### Instance Methods:

- **`add_like(self, user: 'User') -> None`**: 
  - Check if the user is not already in the `_likes` list.
  - If not, append the user to the `_likes` list.

- **`remove_like(self, user: 'User') -> None`**: 
  - Check if the user is in the `_likes` list.
  - If so, remove the user from the `_likes` list.

## `Comment` Class

Update the `Comment` class to include the following methods and attributes:

### Instance Attributes:

- **`author`**: A **public** `User` object representing the user who made the comment.

### Instance Methods:

- **`__init__(self, author: 'User', content: str)`**: 
  - Initialize the `author` attribute with the given `User` object.
  - Set the `content` using the existing setter method.
  - Initialize the `timestamp` as in the original code.

## `Message` Class

Update the `Message` class to include the following methods and attributes:

### Instance Attributes:

- **`sender`**: A **public** `User` object representing the user who sent the message.
- **`recipient`**: A **public** `User` object representing the user who is the recipient of the message.

### Instance Methods:

- **`__init__(self, sender: 'User', recipient: 'User', content: str)`**: 
  - Initialize the `sender` and `recipient` attributes with the given `User` objects.
  - Set the `content` using the existing setter method.
  - Initialize the `timestamp` as in the original code.

Remember to import necessary types and classes at the top of each file:
- `from typing import List, Optional`
- `from user import User`  # Where necessary
- `from post import Post`  # Where necessary

Ensure to use type hints for all attributes and method parameters as shown in the examples above.