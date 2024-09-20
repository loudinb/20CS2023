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
