# `Message` Class

Update the `Message` class in `message.py` to include the following methods and attributes:

## Additional Instance Attributes:

| Name       | Kind      | Access Level | Type         | Description                                                                |
|------------|-----------|--------------|--------------|----------------------------------------------------------------------------|
| `sender`   | Instance  | Public (+)   | `User`       | The `User` object representing the user who sent the message.               |
| `recipient`| Instance  | Public (+)   | `User`       | The `User` object representing the user who is the recipient of the message.|

## Updated Instance Methods:

### **`__init__(self, sender, recipient, content)`**:
- Initialize the `sender` and `recipient` attributes with the given `User` objects.
- Set the `content` using the existing setter method, ensuring it adheres to the content length validation.
- Initialize the `timestamp` attribute as in the original implementation (i.e., set it to the current date and time).

