from datetime import datetime
from user import User  # Assuming User is defined elsewhere

class Message:
    def __init__(self, sender: User, recipient: User, content: str):
        if len(content) > 2000:
            raise ValueError("Message content must be 2000 characters or less.")
        
        self.__content: str = content
        self.timestamp: datetime = datetime.now()
        self.sender: User = sender  # Add sender attribute
        self.recipient: User = recipient  # Add recipient attribute

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        if len(value) > 2000:
            raise ValueError("Message content must be 2000 characters or less.")
        self.__content = value
