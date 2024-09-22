
# `Post` Class

::::{grid}
:gutter: 2

::: {grid-item}
:columns: 8
The `Post` class represents a post in an Instagram-like application. Each post has content, tags, and a timestamp.

The class diagram below provides an overview of the class structure. Create a `post.py` file and implement the `Post` class according to the following specifications, including the attributes and methods that need to be implemented.
:::

::: {grid-item}
:columns: 4
```{mermaid}
classDiagram
    class Post {
         +str _content
         +datetime timestamp
         #set(str) _tags
         +static int post_count
         +__init__(content, tags=None)
         +content()
         +tags()
         +add_tag(tag)
         +remove_tag(tag)
         +is_valid_tag(tag)
         +is_valid_content(content)
         +get_post_count()
    }
```
:::

::::

## Attributes

The `Post` class must have the following attributes:

| Name         | Kind      | Access Level | Type         | Description                                                                |
|--------------|-----------|--------------|--------------|----------------------------------------------------------------------------|
| `_content`   | Instance  | Protected (#) | `str`        | The content of the post, which must be between 3 and 2200 characters long.  |
| `timestamp`  | Instance  | Public (+)    | `datetime`   | The timestamp when the post is created, set to the current date and time.   |
| `_tags`      | Instance  | Protected (#) | `set`        | A set of tags associated with the post.                                    |
| `post_count` | Class     | Public (+)    | `int`        | Tracks the total number of posts created.                                   |

## Methods

The `Post` class must have the following methods:

| Name                | Kind          | Return Type   | Parameters         | Description                                                                 |
|---------------------|---------------|---------------|--------------------|-----------------------------------------------------------------------------|
| `__init__(self, content, tags=None)` | Instance     | None          | `content: str`, `tags: set` (optional) | Initializes the post with content and optional tags, and validates them.     |
| `content(self)`      | Property      | `str`         | None               | Returns the post's content.                                                  |
| `tags(self)`         | Property      | `set`         | None               | Returns the post's set of tags.                                              |
| `add_tag(self, tag)` | Instance      | None          | `tag: str`         | Adds a valid tag to the post.                                                |
| `remove_tag(self, tag)` | Instance   | None          | `tag: str`         | Removes a tag from the post's set of tags. Does nothing if the tag is not present. |
| `get_post_count(cls)`| Class         | `int`         | None               | Returns the total number of posts created.                                   |
| `is_valid_tag(tag)`  | Static        | `bool`        | `tag: str`         | Returns `True` if the tag is alphanumeric and no more than 30 characters long. |
| `is_valid_content(content)` | Static  | `bool`        | `content: str`     | Returns `True` if the content is between 3 and 2200 characters long.         |

### Implementation Details

**`__init__(self, content, tags=None)`**:
- The `__init__` method is the constructor for the `Post` class. The `content` parameter is required, and `tags` is optional.
- Validate `content` using the `is_valid_content` static method. If the content is invalid, raise a `ValueError`. Otherwise, set the `_content` attribute.
- If `tags` is not provided, initialize `_tags` with an empty set.
- If `tags` are provided, validate each tag using the `is_valid_tag` static method. If any tag is invalid, raise a `ValueError`. Otherwise, add each valid tag to the `_tags` attribute.
- Set the `timestamp` attribute to the current date and time.
- Increment the `post_count` class attribute by 1 to keep track of the number of posts created.

**`content(self)`**:
- Implement a getter method that returns the `_content` value.

**`tags(self)`**:
- Implement a getter method that returns the `_tags` value.

**`get_post_count(cls)`**:
- Implement a class method that returns the current value of the `post_count` class attribute.

**`is_valid_content(content) -> bool`**:
- Implement a static method that returns `True` if the content is between 3 and 2200 characters long.
- Return `False` if the content is shorter than 3 characters or longer than 2200 characters.

**`is_valid_tag(tag) -> bool`**:
- Implement a static method that returns `True` if the tag is alphanumeric and no more than 30 characters long.
- Return `False` if the tag exceeds 30 characters or contains non-alphanumeric characters.

**`add_tag(self, tag)`**:
- Validate the tag using the `is_valid_tag` static method.
- If the tag is valid, add it to `_tags`. If invalid, raise a `ValueError`.

**`remove_tag(self, tag)`**:
- Remove the specified tag from `_tags` if it exists. If the tag is not in the set, do nothing.
- (Hint: The `discard` method of a set is appropriate for this operation, not `remove`, as it does not raise an error if the tag is absent.)
