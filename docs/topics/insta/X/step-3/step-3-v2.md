# Step 3: Final Enhancements

In this step, we will make final enhancements to our Instagram-like application by adding more functionality to the existing classes. We will focus on refining the `User` and `Post` classes to support additional features.

## `User` Class

Update the `User` class in `user.py` to include the following additional attributes and methods:

### Additional Instance Attributes:

- **`_messages`**: A **private** list of `Message` objects representing the messages received by this user. This list is managed through the `receive_message()` method to ensure proper message handling.

### Additional Instance Methods:

1. **`send_message(self, recipient: 'User', content: str) -> Message`**: 
   - Create a new `Message` object with the current user as the sender, the specified recipient, and the given content.
   - Call the `receive_message()` method on the recipient user to deliver the message.
   - Return the created `Message` object.

2. **`receive_message(self, message: 'Message') -> None`**: 
   - Verify that the recipient of the message is the current user.
   - Add the received message to the `_messages` list.
   - Implement any necessary operations to mark the message as received or trigger notifications (if implemented).

### Updated Instance Methods:

1. **`follow(self, user: 'User') -> None`**: 
   - Ensure that a user cannot follow the same person more than once.
   - Add appropriate checks before adding to the `_following` and `_followers` lists.

2. **`unfollow(self, user: 'User') -> None`**: 
   - Add appropriate checks to ensure the user is in the `_following` list before removing.

## `Post` Class

Update the `Post` class in `post.py` to include the following additional attributes and methods:

### Additional Instance Attributes:

- **`_comments`**: A **protected** list of `Comment` objects representing the comments on the post. Comments are managed using the `add_comment()` and `remove_comment()` methods. Subclasses may access this attribute if needed.

### Additional Instance Methods:

1. **`add_comment(self, user: 'User', content: str) -> None`**: 
   - Create a new `Comment` object with the given `user` as the author and the provided `content`.
   - Add the newly created `Comment` object to the `_comments` list.

2. **`remove_comment(self, comment: 'Comment') -> None`**: 
   - Remove the specified `Comment` object from the `_comments` list, if it exists.
   - If the comment doesn't exist in the list, handle this case appropriately (e.g., raise an exception or simply return).

Remember to import necessary types and classes at the top of each file:
- `from typing import List`
- `from user import User`  # Where necessary
- `from comment import Comment`  # Where necessary
- `from message import Message`  # Where necessary

Ensure to use type hints for all attributes and method parameters as shown in the examples above.

## Implementation Notes

1. When implementing these enhancements, ensure that you maintain proper encapsulation and data integrity.
2. Handle edge cases and potential errors, such as attempting to follow a user who is already being followed.
3. Consider implementing additional helper methods if needed to keep the code clean and maintainable.
4. Remember to update any existing methods that might be affected by these new attributes and methods.
5. Test your implementation thoroughly to ensure all features work as expected and interact correctly with each other.