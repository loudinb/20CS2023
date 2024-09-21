# `User` Class

Update the `User` class in `user.py` to include the following additional attributes and methods:

## Additional Instance Attributes:

| Name        | Kind      | Access Level | Type           | Description                                                                 |
|-------------|-----------|--------------|----------------|-----------------------------------------------------------------------------|
| `_messages` | Instance  | Private (#)  | `list[Message]`| A private list of `Message` objects representing the messages received by this user. This list is managed through the `receive_message()` method. |

## Additional Instance Methods:

### **`send_message(self, recipient, content)`**:
- Create a new `Message` object with the current user as the sender, the specified recipient, and the given content.
- Call the `receive_message()` method on the recipient user to deliver the message.
- Return the created `Message` object.

### **`receive_message(self, message)`**:
- Verify that the recipient of the message is the current user.
- Add the received message to the `_messages` list.
- Implement any necessary operations to mark the message as received or trigger notifications (if applicable).

## Updated Instance Methods:

### **`follow(self, user)`**:
- Ensure that a user cannot follow the same person more than once.
- Add appropriate checks before adding to the `_following` and `_followers` lists.

### **`unfollow(self, user)`**:
- Add appropriate checks to ensure the user is in the `_following` list before removing.

