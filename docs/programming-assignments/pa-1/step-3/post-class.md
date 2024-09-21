# `Post` Class

Update the `Post` class in `post.py` to include the following additional attributes and methods:

## Additional Instance Attributes:

| Name        | Kind      | Access Level | Type            | Description                                                                |
|-------------|-----------|--------------|-----------------|----------------------------------------------------------------------------|
| `_comments` | Instance  | Protected (#)| `list[Comment]` | A protected list of `Comment` objects representing comments on the post. Managed using the `add_comment()` and `remove_comment()` methods. |

## Additional Instance Methods:

### **`add_comment(self, user, content)`**:
- Create a new `Comment` object with the specified `user` as the author and the given `content`.
- Add the newly created `Comment` object to the `_comments` list.

### **`remove_comment(self, comment)`**:
- Remove the specified `Comment` object from the `_comments` list, if it exists.
- If the comment doesn't exist in the list, handle the case appropriately (e.g., raise an exception or simply return).
