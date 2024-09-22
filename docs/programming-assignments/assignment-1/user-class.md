# `User` Class

The `User` class represents a user in an Instagram-like application. It includes attributes for user information, social connections, and content, as well as methods for user interactions.

Follow the specifications provided below to create a `User` class in the `user.py` file.

## Attributes

| Name               | Kind      | Access Level | Type                | Description                                    |
|--------------------|-----------|--------------|---------------------|------------------------------------------------|
| `user_count`       | Class     | Public       | `int`               | Class attribute tracking total number of users |
| `_username`        | Instance  | Protected      | `str`               | User's unique username                         |
| `_email`           | Instance  | Protected      | `str`               | User's email address                           |
| `_bio`             | Instance  | Protected      | `str`               | User's biography (max 150 characters)          |
| `_joined_on`       | Instance  | Protected      | `datetime`          | Date and time when the user joined             |
| `_posts`           | Instance  | Protected      | `list[Post]`        | List of user's posts                           |
| `_liked_posts`     | Instance  | Protected      | `list[Post]`        | List of posts liked by the user                |
| `_comments`        | Instance  | Protected      | `list[Comment]`     | List of comments made by the user              |
| `_liked_comments`  | Instance  | Protected      | `list[Comment]`     | List of comments liked by the user             |
| `following`        | Instance  | Public       | `list[User]`        | List of users this user is following           |
| `followers`        | Instance  | Public       | `list[User]`        | List of users following this user              |

## Methods

| Name                     | Kind     | Return Type | Parameters                   | Description                                                        |
|--------------------------|----------|-------------|------------------------------|--------------------------------------------------------------------|
| `__init__`               | Instance | None        | `username: str, email: str`  | Initialize a new User instance                                     |
| `username`               | Property | `str`       | None                         | Get the user's username                                            |
| `email`                  | Property | `str`       | None                         | Get the user's email address                                       |
| `bio`                    | Property | `str`       | None                         | Get the user's biography                                           |
| `bio` (setter)           | Property | None        | `new_bio: str`               | Set the user's biography (max 150 characters)                      |
| `joined_on`              | Property | `datetime`  | None                         | Get the date and time when the user joined                         |
| `posts`                  | Property | `list[Post]`| None                         | Get the list of user's posts                                       |
| `follow`                 | Instance | None        | `user: User`                 | Add a user to the following list and add self to their followers   |
| `unfollow`               | Instance | None        | `user: User`                 | Remove a user from the following list and remove self from their followers |
| `is_valid_username`      | Static   | `bool`      | `username: str`              | Check if a username is valid                                       |
| `is_valid_email`         | Static   | `bool`      | `email: str`                 | Check if an email is valid                                         |
| `get_user_count`         | Class    | `int`       | None                         | Return the total number of User instances created                  |
| `create_post`            | Instance | None        | `content: str, tags: list`   | Create a new post and add it to the user's posts                   |
| `delete_post`            | Instance | None        | `post: Post`                 | Delete a post from the user's posts                                |
| `like_post`              | Instance | None        | `post: Post`                 | Like a post and add it to the user's liked posts                   |
| `unlike_post`            | Instance | None        | `post: Post`                 | Unlike a post and remove it from the user's liked posts            |
| `comment_on_post`        | Instance | None        | `post: Post, content: str, tags: list` | Add a comment to a post                                   |
| `delete_comment_on_post` | Instance | None        | `post: Post, comment: Comment` | Delete a comment from a post                                     |
| `like_comment`           | Instance | None        | `comment: Comment`           | Like a comment and add it to the user's liked comments             |
| `unlike_comment`         | Instance | None        | `comment: Comment`           | Unlike a comment and remove it from the user's liked comments      |

### Implementation Details

**`__init__(self, username, email)`**
- The `__init__` method initializes a new instance of the `User` class. The `username` and `email` parameters are required.
- Validate the `username` using the `is_valid_username` method. If the `username` is invalid, raise a `ValueError` with the message "Invalid username.". 
- Validate the `email` using the `is_valid_email` method. If the `email` is invalid, raise a `ValueError` with the message "Invalid email address.".
- Set the `_username` attribute to the `username` parameter.
- Set the `_email` attribute to the `email` parameter.
- Set the `_bio` attribute to an empty string, as the user does not have a biography initially.
- Set the `_joined_on` attribute to the current date and time using `datetime.now()`, representing when the user was created.
- Initialize `_posts`, `_liked_posts`, `_comments`, `_liked_comments` as empty lists.
- Initialize `following` and `followers` as empty lists.
- Increment the `user_count` class attribute by 1 to keep track of the number of `User` instances created.

**`username(self)`**
- Implement the getter method for `_username`, which returns the value of the `_username` attribute. This provides read-only access to the user's username.

**`email(self)`**
- Implement the getter method for `_email`, which returns the value of the `_email` attribute. This provides read-only access to the user's email address.

**`bio(self)`**
- Implement the getter method for `_bio`, which returns the value of the `_bio` attribute. This provides access to the user's biography.

**`bio(self, new_bio)`**
- Implement the setter method for `_bio`. It accepts a string `new_bio` as the new biography. 
- If the `new_bio` exceeds 150 characters, raise a `ValueError` with the message "Bio must be 150 characters or less.". 
- If the length is valid, update the `_bio` attribute with the new `new_bio`.

**`joined_on(self)`**
- Implement the getter method for `_joined_on`, which returns the value of the `_joined_on` attribute. This provides read-only access to the user's join date and time.

**`posts(self)`**
- Implement the getter method for `_posts`, which returns the list of user's posts. This provides read-only access to the user's posts.

**`get_user_count(cls)`**
- Implement this method as a class method that returns the current value of the `user_count` class attribute.
- This method provides a way to retrieve the total number of `User` instances that have been created.

**`is_valid_username(username)`**
- Implement this method as a static method to validate the `username`.
- Return `False` if the `username` length is less than 3 or greater than 30 characters.
- Iterate through each character in the `username`:
  - If the character is not alphanumeric and not a period (`.`) or underscore (`_`), return `False`.
- If all checks pass, return `True`.

**`is_valid_email(email)`**
- Implement this method as a static method to validate the `email`.
- Use the regular expression pattern `r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"` to validate the `email` format.
- Use `re.match(pattern, email)` to check if the email matches the pattern.
- Return `True` if there's a match, `False` otherwise.

**`follow(self, user)`**:
- Check if the given user is not already in this user's `following` list and is not the user itself.
- If not, add the given user to this user's `following` list.
- Add this user to the given user's `followers` list.

**`unfollow(self, user)`**:
- Check if the given user is in this user's `following` list.
- If present, remove the given user from this user's `following` list.
- Remove this user from the given user's `followers` list.

**`create_post(self, content, tags=None)`**:
- Create a new `Post` instance with the given `content` and `tags`.
- Add the new post to the user's `_posts` list.

**`delete_post(self, post)`**:
- Check if the given `post` is in the user's `_posts` list.
- If present, remove the post from the `_posts` list.
- Decrement the `Post.post_count` class attribute.

**`like_post(self, post)`**:
- Check if the given `post` is not in the user's `_posts` and not in the `_liked_posts` list.
- If not, add the post to the user's `_liked_posts` list.
- Call the `like` method on the post, passing the user as an argument.

**`unlike_post(self, post)`**:
- Check if the given `post` is in the user's `_liked_posts` list.
- If present, remove the post from the `_liked_posts` list.
- Call the `unlike` method on the post, passing the user as an argument.

**`comment_on_post(self, post, content, tags=None)`**:
- Call the `add_comment` method on the given `post`, passing the user, `content`, and `tags` as arguments.
- Add the returned comment to the user's `_comments` list.

**`delete_comment_on_post(self, post, comment)`**:
- Check if the given `comment` is in the user's `_comments` list.
- If present, call the `delete_comment` method on the given `post`, passing the `comment` as an argument.
- Remove the comment from the user's `_comments` list.

**`like_comment(self, comment)`**:
- Check if the given `comment` is not in the user's `_comments` and not in the `_liked_comments` list.
- If not, add the comment to the user's `_liked_comments` list.
- Call the `like` method on the comment, passing the user as an argument.

**`unlike_comment(self, comment)`**:
- Check if the given `comment` is in the user's `_liked_comments` list.
- If present, remove the comment from the `_liked_comments` list.
- Call the `unlike` method on the comment, passing the user as an argument.