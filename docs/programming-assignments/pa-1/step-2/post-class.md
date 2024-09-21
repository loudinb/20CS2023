# `Post` Class

Update the `Post` class in `post.py` to include the following methods and attributes:

## Additional Instance Attributes:

| Name     | Kind      | Access Level | Type         | Description                                                                |
|----------|-----------|--------------|--------------|----------------------------------------------------------------------------|
| `author` | Instance  | Public (+)   | `User`       | The `User` object representing the author who created the post.             |
| `_likes` | Instance  | Protected (#)| `list[User]` | A protected list of `User` objects representing users who have liked the post. Initialize as an empty list in the constructor. |

## Additional Instance Methods:

### **`add_like(self, user)`**:
- Check if the user is not already in the `_likes` list.
- If the user is not in the list, append the user to `_likes`.

### **`remove_like(self, user)`**:
- Check if the user is in the `_likes` list.
- If the user is in the list, remove them from `_likes`.

