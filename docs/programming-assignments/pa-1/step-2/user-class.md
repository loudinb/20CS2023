# `User` Class

Update the `User` class in `user.py` to include the following methods and attributes:


## Additional Instance Methods:

### **`create_post(self, content, tags=None)`**:
- Create a new `Post` object with the given content, this user as the author, and optional tags.
- Append the new post to the `_posts` list.

### **`delete_post(self, post)`**:
- Remove the specified post from the `_posts` list if it exists.
- Use the list's `remove()` method, and handle cases where the post might not be in the list (handle `ValueError` gracefully).

### **`like_post(self, post)`**:
- Call the `add_like()` method on the provided `Post` object, passing `self` (the user) as the argument.

### **`unlike_post(self, post)`**:
- Call the `remove_like()` method on the provided `Post` object, passing `self` (the user) as the argument.

### **`comment_on_post(self, post, content)`**:
- Create a new `Comment` object with `self` as the author and the given content.
- Add this comment to the specified post (assuming the `Post` class has a method for adding comments).


