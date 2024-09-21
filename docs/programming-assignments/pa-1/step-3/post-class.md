# `Post` Class

Update the `Post` class in `post.py` to include the following additional attributes and methods:

## Additional Instance Attributes:

- **`_comments`**: A **protected** list of `Comment` objects representing the comments on the post. Comments are managed using the `add_comment()` and `remove_comment()` methods. Subclasses may access this attribute if needed.

## Additional Instance Methods:

1. **`add_comment(self, user, content)`**: 
   - Create a new `Comment` object with the given `user` as the author and the provided `content`.
   - Add the newly created `Comment` object to the `_comments` list.

2. **`remove_comment(self, comment)`**: 
   - Remove the specified `Comment` object from the `_comments` list, if it exists.
   - If the comment doesn't exist in the list, handle this case appropriately (e.g., raise an exception or simply return).
