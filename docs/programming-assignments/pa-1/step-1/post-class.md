# `Post` Class



::::{grid}
:gutter: 2

:::{grid-item}
:columns: 8
The `Post` class represents a post in the Instagram-like application. Each post has content, tags, and a timestamp.

The class diagram shown provides an overview of the class structure.  Create a `post.py` file and implement the `Post` class following the specifications below, including the attributes and methods that need to be implemented.
:::
:::{grid-item}
:columns: 4
```{mermaid}
classDiagram
    class Post {
         +str __content
         +datetime timestamp
         #List[str] _tags
         +static int post_count
         +__init__(content, tags)
         +content()
         +add_tag(tag)
         +remove_tag(tag)
         +get_post_count()
         +is_valid_tag(tag)
    }
```
:::

::::

## Attributes


The `Post` class must have the following attributes:

| Name               | Kind          | Access Level  | Type                          | Description                                         |
|--------------------|---------------|---------------|-------------------------------|-----------------------------------------------------|
| `__content`        | Instance      | Private       | `str`                         | The content of the post, with a max length of 2200 characters. |
| `timestamp`        | Instance      | Public (+)    | `datetime`                    | The timestamp when the post is created, set to the current date and time. |
| `_tags`            | Instance      | Protected (#) | `List[str]`                   | A list of tags associated with the post.             |
| `post_count`       | Class         | Public (+)    | `int`                         | Tracks the total number of posts created.            |


## Methods

The `Post` class must have the following methods:


| Name                | Kind          | Return Type   | Parameters                          | Description                                |
|---------------------|---------------|--------------|-------------------------------------|--------------------------------------------|
| `__init__`          | Instance      | `None`        | `self`, `content`, `tags=None`      | Initializes a new post with content, tags, and a timestamp. Increments `post_count`. |
| `content`           | Property      | `str`         | `self`                              | Gets the post content. Validates content length on setting. |
| `add_tag`           | Instance      | `None`        | `self`, `tag`                       | Adds a valid tag to the `_tags` list. Raises `ValueError` if invalid. |
| `remove_tag`        | Instance      | `None`        | `self`, `tag`                       | Removes the specified tag from the `_tags` list if it exists. |
| `get_post_count`    | Class         | `int`         | `cls`                               | Returns the total number of posts created. |
| `is_valid_tag`      | Static        | `bool`        | `tag`                               | Returns `True` if the tag is alphanumeric and <= 30 characters. |


### Implementation Details

**`__init__(self, content, tags)`**:
- The `__init__` method initializes a new post object with the provided content and tags (if any).
- The `__init__` method should set the `__content` attribute using the `content` property setter (which will validate the length). If `tags` are provided, validate 


initialize the `_tags` attribute using ; otherwise, initialize it with an empty list.
- Set `timestamp` to the current date and time using `datetime.now()`.
- Increment the `post_count` class attribute by 1.


**`add_tag(self, tag)`**: 
- Validate the tag using `is_valid_tag` static method.
- If valid, add the tag to `_tags`. If invalid, raise a `ValueError`.

**`remove_tag(self, tag)`**: 
   - Remove the specified tag from `_tags` if it exists. Do nothing if the tag is not in the list.

**`content(self)`**:
   - Implement a getter that returns the `__content` value.
   - Implement a setter that accepts a string value. If the new content is longer than 2200 characters, raise a `ValueError`. Otherwise, set `__content` to the new value.

**`get_post_count(cls)`**: 
   - Return the current value of `post_count`.

**`is_valid_tag(tag) -> bool`**: 
   - Return `True` if the tag is alphanumeric and no more than 30 characters long.
   - Return `False` otherwise.
