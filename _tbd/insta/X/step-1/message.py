from datetime import datetime

class Message:
    def __init__(self, content: str):
        if len(content) > 2000:
            raise ValueError("Message content must be 2000 characters or less.")
        
        self.__content: str = content
        self.timestamp: datetime = datetime.now()

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        if len(value) > 2000:
            raise ValueError("Message content must be 2000 characters or less.")
        self.__content = value
