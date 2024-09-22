# `Comment` Class

The `Comment` class represents a comment in an Instagram-like application. It includes attributes for comment content, tags, and timestamp, as well as methods for managing comment data.

Follow the specifications provided below to create a `Comment` class in the `comment.py` file.

## Attributes

| Name         | Kind     | Access Level | Type       | Description                                    |
|--------------|----------|--------------|------------|------------------------------------------------|
| `comment_count` | Class    | Public       | `int`           | Class attribute tracking total number of comments |
| `_content`   | Instance | Protected      | `str`      | Comment content (3-2200 characters)            |
| `_timestamp`  | Instance | Protected       | `datetime` | Date and time when the comment was created     |
| `_tags`      | Instance | Protected      | `set`      | Set of tags associated with the comment        |
| `_liked_by`     | Instance | Protected      | `list[User]`    | List of users who have liked the comment          |

## Methods

| Name                 | Kind     | Return Type | Parameters     | Description                                           |
|----------------------|----------|-------------|----------------|-------------------------------------------------------|
| `__init__`           | Instance | None        | `content: str` | Initialize a new Comment instance                     |
| `content`            | Property | `str`       | None           | Get the comment's content                             |
| `tags`               | Property | `set`       | None           | Get the comment's set of tags                         |
| `add_tag`            | Instance | None        | `tag: str`     | Add a valid tag to the comment                        |
| `remove_tag`         | Instance | None        | `tag: str`     | Remove a tag from the comment's set of tags           |
| `timestamp`          | Property | `datetime`  | None                                 | Get the message's timestamp                           |
| `get_comment_count`     | Class    | `int`       | None                        | Return the total number of Comments instances created     |
| `is_valid_tag`       | Static   | `bool`      | `tag: str`                  | Check if a tag is valid                               |
| `is_valid_content`   | Static   | `bool`      | `content: str`              | Check if post content is valid                        |


### Implementation Details

**`__init__(self, content, tags=None)`**
- The `__init__` method initializes a new instance of the `Comment` class. The `content` parameter is required, and `tags` is optional.
- Validate the `content` using the `is_valid_content` method. If the `content` is invalid, raise a `ValueError` with the message "Invalid comment content.".
- Set the `_content` attribute to the `content` parameter.
- Initialize `_tags` as an empty set.
- If `tags` are provided, validate each tag using the `is_valid_tag` method. If any tag is invalid, raise a `ValueError` with the message "Invalid tag.". Otherwise, add each valid tag to the `_tags` attribute.
- Set the `_timestamp` attribute to the current date and time using `datetime.now()`.
- Initialize `_liked_by` as an empty lists.
- Increment the `comment_count` class attribute by 1 to keep track of the number of `Comment` instances created.

**`content(self)`**
- Implement the getter method for `_content`, which returns the value of the `_content` attribute. This provides read-only access to the post's content.

**`timestamp(self)`**
- Implement the getter method for `_timestamp`, which returns the value of the `_timestamp` attribute. This provides read-only access to the message's creation time.

**`tags(self)`**
- Implement the getter method for `_tags`, which returns the value of the `_tags` attribute. This provides read-only access to the post's set of tags.

**`add_tag(self, tag)`**
- Validate the `tag` using the `is_valid_tag` method.
- If the tag is valid, add it to the `_tags` set. If invalid, raise a `ValueError` with the message "Invalid tag.".

**`remove_tag(self, tag)`**
- Remove the specified `tag` from `_tags` if it exists. If the tag is not in the set, do nothing.
- Use the `discard` method of the set for this operation.

**`get_comment_count(cls)`**
- Implement this method as a class method that returns the current value of the `comment_count` class attribute.
- This method provides a way to retrieve the total number of `Comment` instances that have been created.

**`is_valid_tag(tag)`**
- Implement this method as a static method to validate the `tag`.
- Return `True` if the `tag` is alphanumeric and no more than 30 characters long.
- Return `False` if the `tag` exceeds 30 characters or contains non-alphanumeric characters.

**`is_valid_content(content)`**
- Implement this method as a static method to validate the `content`.
- Return `True` if the length of `content` is between 3 and 2200 characters (inclusive).
- Return `False` if the `content` is shorter than 3 characters or longer than 2200 characters.