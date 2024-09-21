# `Comment` Class

Update the `Comment` class in `comment.py` to include the following methods and attributes:

## Additional Instance Attributes:

| Name     | Kind      | Access Level | Type         | Description                                                                |
|----------|-----------|--------------|--------------|----------------------------------------------------------------------------|
| `author` | Instance  | Public (+)   | `User`       | The `User` object representing the author who made the comment.             |

## Updated Instance Methods:

### **`__init__(self, author, content)`**:
- Initialize the `author` attribute with the given `User` object.
- Set the `content` using the existing setter method, ensuring it adheres to the content length validation.
- Initialize the `timestamp` attribute as in the original implementation (i.e., set it to the current date and time).

