# `Message` Class

The `Message` class represents a private message in an Instagram-like application. It includes attributes for message content, timestamp, sender, and recipient, as well as methods for managing message data.

Follow the specifications provided below to create a `Message` class in the `message.py` file.

## Attributes

| Name         | Kind     | Access Level | Type       | Description                                    |
|--------------|----------|--------------|------------|------------------------------------------------|
| `_content`   | Instance | Private      | `str`      | Message content (max 2200 characters)          |
| `_timestamp` | Instance | Private      | `datetime` | Date and time when the message was created     |
| `_sender`    | Instance | Private      | `User`     | User object representing the message sender    |
| `_recipient` | Instance | Private      | `User`     | User object representing the message recipient |
| `message_count` | Class | Public       | `int`      | Class attribute tracking total number of messages |

## Methods

| Name                 | Kind     | Return Type | Parameters                           | Description                                           |
|----------------------|----------|-------------|--------------------------------------|-------------------------------------------------------|
| `__init__`           | Instance | None        | `content: str, sender: User, recipient: User` | Initialize a new Message instance                     |
| `content`            | Property | `str`       | None                                 | Get the message's content                             |
| `sender`             | Property | `User`      | None                                 | Get the message's sender                              |
| `recipient`          | Property | `User`      | None                                 | Get the message's recipient                           |
| `timestamp`          | Property | `datetime`  | None                                 | Get the message's timestamp                           |
| `get_message_count`  | Class    | `int`       | None                                 | Return the total number of Message instances created  |
| `is_valid_content`   | Static   | `bool`      | `content: str`                       | Check if message content is valid                     |

### Implementation Details

**`__init__(self, content: str, sender: User, recipient: User)`**
- The `__init__` method initializes a new instance of the `Message` class. The `content`, `sender`, and `recipient` parameters are required.
- Validate the `content` using the `is_valid_content` method. If the `content` is invalid, raise a `ValueError` with the message "Invalid message content.".
- Set the `_content` attribute to the `content` parameter.
- Set the `_sender` attribute to the `sender` parameter.
- Set the `_recipient` attribute to the `recipient` parameter.
- Set the `_timestamp` attribute to the current date and time using `datetime.now()`.
- Increment the `message_count` class attribute by 1 to keep track of the number of `Message` instances created.

**`content(self)`**
- Implement the getter method for `_content`, which returns the value of the `_content` attribute. This provides read-only access to the message's content.

**`sender(self)`**
- Implement the getter method for `_sender`, which returns the value of the `_sender` attribute. This provides read-only access to the message's sender.

**`recipient(self)`**
- Implement the getter method for `_recipient`, which returns the value of the `_recipient` attribute. This provides read-only access to the message's recipient.

**`timestamp(self)`**
- Implement the getter method for `_timestamp`, which returns the value of the `_timestamp` attribute. This provides read-only access to the message's creation time.

**`get_message_count(cls)`**
- Implement this method as a class method that returns the current value of the `message_count` class attribute.
- This method provides a way to retrieve the total number of `Message` instances that have been created.

**`is_valid_content(content)`**
- Implement this method as a static method to validate the `content`.
- Return `True` if the length of `content` is between 1 and 2200 characters (inclusive).
- Return `False` if the `content` is empty or longer than 2200 characters.

These improved instructions provide a more comprehensive and consistent approach to implementing the `Message` class, aligning it with the style used for other classes in the application.