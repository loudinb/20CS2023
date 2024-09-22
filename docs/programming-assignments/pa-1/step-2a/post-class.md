# `Post` Class

The `Post` class represents a post in an Instagram-like application. It includes attributes for post content, tags, timestamp, and social interactions, as well as methods for managing post data.

Follow the specifications provided below to create a `Post` class in the `post.py` file.

## Attributes

| Name         | Kind     | Access Level | Type            | Description                                    |
|--------------|----------|--------------|-----------------|------------------------------------------------|
| `post_count` | Class    | Public       | `int`           | Class attribute tracking total number of posts |
| `_content`   | Instance | Protected      | `str`           | Post content (3-2200 characters)               |
| `_timestamp`  | Instance | Protected     | `datetime`      | Date and time when the post was created        |
| `_tags`      | Instance | Protected      | `set`           | Set of tags associated with the post           |
| `_liked_by`     | Instance | Protected      | `list[User]`    | List of users who have liked the post          |
| `_comments`  | Instance | Protected      | `list[Comment]` | List of comments on the post                   |

## Methods

| Name                 | Kind     | Return Type | Parameters                  | Description                                           |
|----------------------|----------|-------------|-----------------------------|-------------------------------------------------------|
| `__init__`           | Instance | None        | `content: str, tags: set=None` | Initialize a new Post instance                        |
| `content`            | Property | `str`       | None                        | Get the post's content                                |
| `timestamp`          | Property | `datetime`  | None                                 | Get the message's timestamp                           |
| `tags`               | Property | `set`       | None                        | Get the post's set of tags                            |
| `liked_by`               | Property | `set`       | None                        | Get the set of users the post was liked by          |
| `add_tag`            | Instance | None        | `tag: str`                  | Add a valid tag to the post                           |
| `remove_tag`         | Instance | None        | `tag: str`                  | Remove a tag from the post's set of tags              |
| `get_post_count`     | Class    | `int`       | None                        | Return the total number of Post instances created     |
| `is_valid_tag`       | Static   | `bool`      | `tag: str`                  | Check if a tag is valid                               |
| `is_valid_content`   | Static   | `bool`      | `content: str`              | Check if post content is valid                        |

### Implementation Details

**`__init__(self, content, tags=None)`**
- The `__init__` method initializes a new instance of the `Post` class. The `content` parameter is required, and `tags` is optional.
- Validate the `content` using the `is_valid_content` method. If the `content` is invalid, raise a `ValueError` with the message "Invalid post content.".
- Set the `_content` attribute to the `content` parameter.
- Initialize `_tags` as an empty set.
- If `tags` are provided, validate each tag using the `is_valid_tag` method. If any tag is invalid, raise a `ValueError` with the message "Invalid tag.". Otherwise, add each valid tag to the `_tags` attribute.
- Set the `timestamp` attribute to the current date and time using `datetime.now()`.
- Initialize `_liked_by` and `_comments` as empty lists.
- Increment the `post_count` class attribute by 1 to keep track of the number of `Post` instances created.

**`content(self)`**
- Implement the getter method for `_content`, which returns the value of the `_content` attribute. This provides read-only access to the post's content.

**`timestamp(self)`**
- Implement the getter method for `_timestamp`, which returns the value of the `_timestamp` attribute. This provides read-only access to the message's creation time.

**`tags(self)`**
- Implement the getter method for `_tags`, which returns the value of the `_tags` attribute. This provides read-only access to the post's set of tags.

**`liked_by(self)`**
- Implement the getter method for `_liked_by`, which returns the value of the `_liked_by` attribute. This provides read-only access to the set of users who have liked the post.

**`add_tag(self, tag)`**
- Validate the `tag` using the `is_valid_tag` method.
- If the tag is valid, add it to the `_tags` set. If invalid, raise a `ValueError` with the message "Invalid tag.".

**`remove_tag(self, tag)`**
- Remove the specified `tag` from `_tags` if it exists. If the tag is not in the set, do nothing.
- Use the `discard` method of the set for this operation.

**`get_post_count(cls)`**
- Implement this method as a class method that returns the current value of the `post_count` class attribute.
- This method provides a way to retrieve the total number of `Post` instances that have been created.

**`is_valid_tag(tag)`**
- Implement this method as a static method to validate the `tag`.
- Return `True` if the `tag` is alphanumeric and no more than 30 characters long.
- Return `False` if the `tag` exceeds 30 characters or contains non-alphanumeric characters.

**`is_valid_content(content)`**
- Implement this method as a static method to validate the `content`.
- Return `True` if the length of `content` is between 3 and 2200 characters (inclusive).
- Return `False` if the `content` is shorter than 3 characters or longer than 2200 characters.