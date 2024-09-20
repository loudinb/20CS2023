## Part 4: The `Message` Class

## `Message` Class Documentation

### Section 1: Core `Message` Implementation (No Dependencies)

This section includes the components of the `Message` class that can be implemented without relying on other classes (`User`).

#### Instance Attributes:

- **`__content`**: A **private** string representing the message’s content, limited to 2000 characters. The content should only be modified through the `content` property, ensuring strict validation.
  - **Why private**: Message content is sensitive and must be validated and controlled within the class, preventing direct access or modification. This ensures that the length constraint is always enforced.

- **`timestamp`**: A **public** `datetime` object representing the time when the message was sent. This attribute is initialized at the time of message creation and should not be modified afterward.

#### Instance Methods:

- **`__init__(self, content: str)`**: Initializes the `Message` object with the required `content`. It also records the `timestamp` when the message is created. The content length is validated within the constructor using the setter.

- **`@property content(self) -> str`**: This **property** manages access to the private `__content` attribute. The getter returns the message content. The setter ensures the content does not exceed 2000 characters. A `ValueError` is raised if the content exceeds this limit.
  - **Why private**: This ensures that all modifications to message content are validated through the property setter, which enforces the length constraint.

---

### Section 2: Implementation Details Involving `User`

This section includes the components of the `Message` class that require the `User` class for proper implementation. The `User` class is expected to be available for these attributes and methods.

#### Instance Attributes:

- **`sender`**: A **public** `User` object representing the user who sent the message. Since messages are associated with the sender in a public context (e.g., messaging systems), this attribute can be accessible externally.

- **`recipient`**: A **public** `User` object representing the user who is the recipient of the message. Similar to the sender, this attribute is public as it represents the user receiving the message.

#### Instance Methods:

- **`__init__(self, sender: 'User', recipient: 'User', content: str)`**: Initializes the `Message` object with the `sender` (a `User` object), `recipient` (a `User` object), and `content`. The constructor validates the content length using the setter, and also initializes the `timestamp`.

---

### Section 3: Full Class Overview

This section contains the full class implementation, combining everything from the above sections.

#### Full Class

```python
from typing import Optional
from datetime import datetime
from user import User  # Assuming User is defined elsewhere

class Message:
    def __init__(self, sender: 'User', recipient: 'User', content: str):
        if len(content) > 2000:
            raise ValueError("Message content must be 2000 characters or less.")
        
        self.sender: User = sender  # Public attribute representing the sender
        self.recipient: User = recipient  # Public attribute representing the recipient
        self.__content: str = content  # Private attribute for message content
        self.timestamp: datetime = datetime.now()  # Timestamp on message creation

    # Property to get and set the message content
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        if len(value) > 2000:
            raise ValueError("Message content must be 2000 characters or less.")
        self.__content = value
```
