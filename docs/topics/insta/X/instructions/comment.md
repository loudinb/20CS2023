## `Comment` Class Documentation

### Section 1: Core `Comment` Implementation (No Dependencies)

This section includes the components of the `Comment` class that can be implemented without relying on other classes (`User`).

#### Instance Attributes:

- **`__content`**: A **private** string representing the comment’s content, limited to 2200 characters. The content should only be modified through the `content` property, ensuring strict validation.
  - **Why private**: Comment content must be validated and controlled within the class, preventing direct access or modification. This ensures that the length constraint is always enforced.

- **`timestamp`**: A **public** `datetime` object representing when the comment was made. This attribute is initialized at the time the comment is created and should not be modified afterward.

#### Instance Methods:

- **`__init__(self, content: str)`**: Initializes the `Comment` object with the required `content`. It also records the `timestamp` when the comment is created. Validation of content length is performed within the constructor using the setter.

- **`@property content(self) -> str`**: This **property** manages access to the private `__content` attribute. The getter returns the comment content. The setter ensures the content does not exceed 2200 characters. A `ValueError` is raised if the content exceeds this limit.
  - **Why private**: This ensures that all modifications to comment content are validated through the property setter, which enforces the length constraint.

---

### Section 2: Implementation Details Involving `User`

This section includes the components of the `Comment` class that require the `User` class for proper implementation. The `User` class is expected to be available for these attributes and methods.

#### Instance Attributes:

- **`author`**: A **public** `User` object representing the user who made the comment. Since comments are associated with the author, this attribute can be accessible externally.

#### Instance Methods:

- **`__init__(self, author: 'User', content: str)`**: Initializes the `Comment` object with the `author` (a `User` object) and `content`. The constructor validates the content length using the setter, and also initializes the `timestamp`.

---

### Section 3: Full Class Overview

This section contains the full class implementation, combining everything from the above sections.

#### Full Class

```python
from typing import Optional
from datetime import datetime
from user import User  # Assuming User is defined elsewhere

class Comment:
    def __init__(self, author: 'User', content: str):
        if len(content) > 2200:
            raise ValueError("Comment content must be 2200 characters or less.")
        
        self.author: User = author  # Public attribute representing the author of the comment
        self.__content: str = content  # Private attribute for comment content
        self.timestamp: datetime = datetime.now()  # Timestamp on comment creation

    # Property to get and set the comment content
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        if len(value) > 2200:
            raise ValueError("Comment content must be 2200 characters or less.")
        self.__content = value
```
