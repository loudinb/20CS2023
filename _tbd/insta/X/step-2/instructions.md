# `User` Class

Update the `User` class to include the following methods and attributes:

## Instance Attributes:

- **`_posts`**: A **private** list of `Post` objects representing the posts created by the user. This list can only be manipulated through specific methods like `create_post` and `delete_post` to maintain control over the posts.

## Instance Methods:

- **`create_post(self, content: str, tags: Optional[List[str]] = None) -> None`**: Allows the user to create a post. The post content is provided as a string, and an optional list of tags may also be provided. The post is added to the `_posts` list.

- **`delete_post(self, post: 'Post') -> None`**: Removes a specified post from the `_posts` list.

- **`like_post(self, post: 'Post') -> None`**: Adds the user to the `Post` object's likes list. This method assumes that the `Post` class provides an appropriate method to handle likes.

- **`unlike_post(self, post: 'Post') -> None`**: Removes the user from the `Post` object's likes list.

- **`comment_on_post(self, post: 'Post', content: str) -> None**: Adds a comment to the post. The post and comment content are provided as arguments.


# `Post` Class

Update the `Post` class to include the following methods and attributes:

## Instance Attributes:

- **`author`**: A **public** `User` object representing the user who created the post. Since authorship of posts is generally public information, this attribute can be accessible to external code.

- **`_likes`**: A **protected** list of `User` objects representing users who have liked the post. Likes are managed through the `add_like()` and `remove_like()` methods. Subclasses may access this attribute directly but should still use the methods for modification.

## Instance Methods:

- **`add_like(self, user: 'User') -> None`**: Adds a `User` object to the `_likes` list, representing the user liking the post. The method ensures that the user has not already liked the post.

- **`remove_like(self, user: 'User') -> None`**: Removes a `User` object from the `_likes` list, representing the user unliking the post.


# `Comment` Class

Update the `Comment` class to include the following methods and attributes:

## Instance Attributes:

- **`author`**: A **public** `User` object representing the user who made the comment. Since comments are associated with the author, this attribute can be accessible externally.

## Instance Methods:

- **`__init__(self, author: 'User', content: str)`**: Initializes the `Comment` object with the `author` (a `User` object) and `content`. The constructor validates the content length using the setter, and also initializes the `timestamp`.


# `Message` Class

Update the `Message` class to include the following methods and attributes:

## Instance Attributes:

- **`sender`**: A **public** `User` object representing the user who sent the message. Since messages are associated with the sender in a public context (e.g., messaging systems), this attribute can be accessible externally.

- **`recipient`**: A **public** `User` object representing the user who is the recipient of the message. Similar to the sender, this attribute is public as it represents the user receiving the message.

## Instance Methods:

- **`__init__(self, sender: 'User', recipient: 'User', content: str)`**: Initializes the `Message` object with the `sender` (a `User` object), `recipient` (a `User` object), and `content`. The constructor validates the content length using the setter, and also initializes the `timestamp`.