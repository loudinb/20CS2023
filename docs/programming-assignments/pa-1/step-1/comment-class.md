# `Comment` Class

::::{grid}
:gutter: 2

::: {grid-item}
:columns: 8
The `Comment` class represents a comment in an Instagram-like application. Each comment has content, tags, and a timestamp.

The class diagram below provides an overview of the class structure. Create a `comment.py` file and implement the `Comment` class according to the following specifications, including the attributes and methods that need to be implemented.
:::

::: {grid-item}
:columns: 4
```{mermaid}
classDiagram
    class Comment {
         #str _content
         +datetime timestamp
         #set(str) _tags
         +__init__(content)
         +content()
         +tags()
         +add_tag(tag)
         +remove_tag(tag)
    }
```
:::

::::

## Attributes

The `Comment` class must have the following attributes:

| Name         | Kind      | Access Level | Type         | Description                                                                |
|--------------|-----------|--------------|--------------|----------------------------------------------------------------------------|
| `_content`   | Instance  | Protected (#) | `str`        | The content of the comment, which must be less than 2201 characters long.   |
| `timestamp`  | Instance  | Public (+)    | `datetime`   | The timestamp when the comment is created, set to the current date and time.|
| `_tags`      | Instance  | Protected (#) | `set`        | A set of tags associated with the comment.                                 |

## Methods

The `Comment` class must have the following methods:

| Name                | Kind          | Return Type   | Parameters         | Description                                                                 |
|---------------------|---------------|---------------|--------------------|-----------------------------------------------------------------------------|
| `__init__(self, content)` | Instance | `None`        | `content: str`     | Initializes the comment with content, validates content, and sets the timestamp. |
| `content(self)`      | Property      | `str`         | None               | Returns the comment's content.                                               |
| `content(self, value)` | Property Setter | `None`    | `value: str`       | Validates and sets the comment's content if it is valid. Raises `ValueError` if content exceeds 2200 characters. |
| `tags(self)`         | Property      | `set`         | None               | Returns the set of tags associated with the comment.                        |
| `add_tag(self, tag)` | Instance      | `None`        | `tag: str`         | Adds a valid tag to the comment's set of tags. Raises `ValueError` if the tag is invalid. |
| `remove_tag(self, tag)` | Instance   | `None`        | `tag: str`         | Removes a tag from the comment's set of tags if it exists. Does nothing if the tag is not present. |

### Implementation Details

**`__init__(self, content)`**:
- The `__init__` method is the constructor for the `Comment` class.
- If `content` is longer than 2200 characters, raise a `ValueError`. Otherwise, set the `_content` attribute to the value of `content`.
- Set the `timestamp` attribute to the current date and time.

**`content(self)`**:
- Implement a getter method that returns the value of `_content`.

**`content(self, value)`**:
- Implement a setter method that accepts a string `value`. If the `value` is longer than 2200 characters, raise a `ValueError`. Otherwise, set `_content` to the new `value`.

**`tags(self)`**:
- Implement a getter method that returns the value of `_tags`.

**`add_tag(self, tag)`**:
- Validate the tag. If the tag is valid (alphanumeric and no more than 30 characters), add it to the `_tags` attribute. If invalid, raise a `ValueError`.

**`remove_tag(self, tag)`**:
- Remove the specified tag from `_tags` if it exists. If the tag is not in the set, do nothing.
- (Hint: Use the `discard` method instead of `remove` to avoid errors when the tag is not found.)
