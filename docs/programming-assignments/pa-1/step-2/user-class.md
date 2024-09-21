# `User` Class

Update the `User` class in `user.py` to include the following methods and attributes:

## Additional Instance Attributes:

- **`_posts`**: A **private** list of `Post` objects representing the posts created by the user. Initialize this as an empty list in the constructor.
- **`_followers`**: A **private** list of `User` objects representing users following this user. Initialize as an empty list in the constructor.
- **`_following`**: A **private** list of `User` objects representing users this user is following. Initialize as an empty list in the constructor.

## Additional Instance Methods:

1. **`create_post(self, content, tags)`**: 
   - Create a new `Post` object with the given content, this user as the author, and the optional tags.
   - Append the new post to the `_posts` list.

2. **`delete_post(self, post)`**: 
   - Remove the specified post from the `_posts` list if it exists.
   - Use list's `remove()` method, handling the case where the post might not be in the list.

3. **`like_post(self, post)`**: 
   - Call the `add_like()` method on the given post object, passing `self` as the argument.

4. **`unlike_post(self, post)`**: 
   - Call the `remove_like()` method on the given post object, passing `self` as the argument.

5. **`comment_on_post(self, post, content)`**: 
   - Create a new `Comment` object with `self` as the author and the given content.
   - Add this comment to the post (assuming the `Post` class has a method to add comments).

6. **`follow(self, user)`**: 
   - Add the given user to this user's `_following` list if not already present.
   - Add this user to the given user's `_followers` list.

7. **`unfollow(self, user)`**: 
   - Remove the given user from this user's `_following` list if present.
   - Remove this user from the given user's `_followers` list.

