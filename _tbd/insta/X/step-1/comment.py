from datetime import datetime

class Comment:
    def __init__(self, content: str):
        if len(content) > 2200:
            raise ValueError("Content must be 2200 characters or less.")
        
        self.__content: str = content
        self.timestamp: datetime = datetime.now()

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        if len(value) > 2200:
            raise ValueError("Content must be 2200 characters or less.")
        self.__content = value
