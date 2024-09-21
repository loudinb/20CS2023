# `Message` Class

Update the `Message` class in `message.py` to include the following methods and attributes:

## Additional Instance Attributes:

- **`sender`**: A **public** `User` object representing the user who sent the message.
- **`recipient`**: A **public** `User` object representing the user who is the recipient of the message.

## Updated Instance Methods:

1. **`__init__(self, sender, recipient, content)`**: 
   - Initialize the `sender` and `recipient` attributes with the given `User` objects.
   - Set the `content` using the existing setter method.
   - Initialize the `timestamp` as in the original code.
