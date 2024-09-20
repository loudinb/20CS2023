# `User` Class

## Instance Attributes:

- **`_followers`**: A **private** list of `User` objects representing the users who follow this user. This list can only be updated through specific methods like `follow()` and `unfollow()` to ensure the integrity of follower interactions.

- **`_following`**: A **private** list of `User` objects representing the users this user follows. Like `_followers`, this list is managed through dedicated methods.

## Instance Methods:

- **`follow(self, user: 'User') -> None`**: Adds the specified `User` object to the current user's `_following` list, and adds the current user to the target user's `_followers` list. The method ensures that a user cannot follow the same person more than once.

- **`unfollow(self, user: 'User') -> None`**: Removes the specified `User` object from the current user's `_following` list, and removes the current user from the target user's `_followers` list.

- **`send_message(self, recipient: 'User', content: str) -> None`**: Sends a message from the current user to another `User`. This assumes that the `Message` class is available and is used to create a message object.



# `Post` Class


## Instance Attributes:

- **`_comments`**: A **protected** list of `Comment` objects representing the comments on the post. Comments are managed using the `add_comment()` and `remove_comment()` methods. Subclasses may access this attribute if needed.

## Instance Methods:

- **`add_comment(self, user: 'User', content: str) -> None`**: Adds a `Comment` to the protected `_comments` list. The `user` argument specifies the author of the comment, and `content` is the comment text. The `Comment` object is created and added to the list.

- **`remove_comment(self, comment: 'Comment') -> None`**: Removes a specific `Comment` object from the `_comments` list, if it exists.


# `Comment` Class

No changes are required for the `Comment` class in this step.

# `Message` Class

Update the `Message` class to include the following methods and attributes:

## Instance Methods:

- **`send_message(self, recipient: 'User', content: str) -> None`**: Initializes the `Message` object with `recipient`, and `content`. The message is then sent from the sender to the recipient. The method should handle the creation of the `Message` object and any necessary operations to send the message.