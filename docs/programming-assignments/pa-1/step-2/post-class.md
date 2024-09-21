# `Post` Class

Update the `Post` class in `post.py` to include the following methods and attributes:

## Additional Instance Attributes:

- **`author`**: A **public** `User` object representing the user who created the post.
- **`_likes`**: A **protected** list of `User` objects representing users who have liked the post. Initialize as an empty list in the constructor.

## Additional Instance Methods:

1. **`add_like(self, user)`**: 
   - Check if the user is not already in the `_likes` list.
   - If not, append the user to the `_likes` list.

2. **`remove_like(self, user)`**: 
   - Check if the user is in the `_likes` list.
   - If so, remove the user from the `_likes` list.
