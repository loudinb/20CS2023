# `User` Class

Update the `User` class in `user.py` to include the following additional attributes and methods:

## Additional Instance Attributes:

- **`_messages`**: A **private** list of `Message` objects representing the messages received by this user. This list is managed through the `receive_message()` method to ensure proper message handling.

## Additional Instance Methods:

1. **`send_message(self, recipient, content)`**: 
   - Create a new `Message` object with the current user as the sender, the specified recipient, and the given content.
   - Call the `receive_message()` method on the recipient user to deliver the message.
   - Return the created `Message` object.

2. **`receive_message(self, message)`**: 
   - Verify that the recipient of the message is the current user.
   - Add the received message to the `_messages` list.
   - Implement any necessary operations to mark the message as received or trigger notifications (if implemented).

## Updated Instance Methods:

1. **`follow(self, user)`**: 
   - Ensure that a user cannot follow the same person more than once.
   - Add appropriate checks before adding to the `_following` and `_followers` lists.

2. **`unfollow(self, user)`**: 
   - Add appropriate checks to ensure the user is in the `_following` list before removing.
