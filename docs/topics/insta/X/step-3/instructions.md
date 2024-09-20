# `User` Class

## Instance Attributes:

- **`_followers`**: A **private** list of `User` objects representing the users who follow this user. This list can only be updated through specific methods like `follow()` and `unfollow()` to ensure the integrity of follower interactions.

- **`_following`**: A **private** list of `User` objects representing the users this user follows. Like `_followers`, this list is managed through dedicated methods.

- **_messages**: A private list of Message objects representing the messages received by this user. This list is managed through the receive_message() method to ensure proper message handling.


## Instance Methods:

- **`follow(self, user: 'User') -> None`**: Adds the specified `User` object to the current user's `_following` list, and adds the current user to the target user's `_followers` list. The method ensures that a user cannot follow the same person more than once.

- **`unfollow(self, user: 'User') -> None`**: Removes the specified `User` object from the current user's `_following` list, and removes the current user from the target user's `_followers` list.

- **`send_message(self, recipient: 'User', content: str) -> Message`**: Creates and sends a new `Message` object from the current user to the specified recipient. The method should:

  - Create a new `Message` object with the current user as the sender, the specified recipient, and the given content.
  - Call the `receive_message()` method on the recipient user to deliver the message.

- **`receive_message(self, message: 'Message') -> None`**: Receives a `Message` object and adds it to the user's private `_messages` list. This method should:

  - Verify that the recipient of the message is the current user.
  - Add the received message to the `_messages` list.
  - Perform any necessary operations to mark the message as received or trigger notifications (if implemented).


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

- **`receive_message(self, message: 'Message') -> None`**: Receives a message from another user and adds it to the `_messages` list.
