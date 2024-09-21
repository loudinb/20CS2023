# `Message` Class

::::{grid}
:gutter: 2

::: {grid-item}
:columns: 8
The `Message` class represents a message in an Instagram-like application. Each message has content and a timestamp.

The class diagram below provides an overview of the class structure. Create a `message.py` file and implement the `Message` class according to the following specifications, including the attributes and methods that need to be implemented.
:::

::: {grid-item}
:columns: 4
```{mermaid}
classDiagram
    class Message {
         +str content
         +datetime timestamp
         +__init__(content)
         +content()
    }
```
:::

::::

## Attributes

The `Message` class must have the following attributes:

| Name         | Kind      | Access Level | Type         | Description                                                                |
|--------------|-----------|--------------|--------------|----------------------------------------------------------------------------|
| `_content`   | Instance  | Private      | `str`        | The content of the message, with a maximum length of 2200 characters.       |
| `timestamp`  | Instance  | Public (+)   | `datetime`   | The timestamp when the message is created, set to the current date and time.|

## Methods

The `Message` class must have the following methods:

| Name                | Kind          | Return Type   | Parameters         | Description                                                                 |
|---------------------|---------------|---------------|--------------------|-----------------------------------------------------------------------------|
| `__init__(self, content)` | Instance | `None`        | `content: str`     | Initializes the message with content and sets the timestamp. Validates content length. |
| `content(self)`      | Property      | `str`         | None               | Returns the content of the message.                                          |

### Implementation Details

**`__init__(self, content)`**:
- The `__init__` method is the constructor for the `Message` class.
- If `content` exceeds 2200 characters, raise a `ValueError`. Otherwise, set the `_content` attribute to the value of `content`.
- Set the `timestamp` attribute to the current date and time.

**`content(self)`**:
- Implement a getter method that returns the value of `_content`.
