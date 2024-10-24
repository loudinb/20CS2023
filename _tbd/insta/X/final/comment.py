from datetime import datetime

class Comment:
    def __init__(self, author, content):
        if len(content) > 2200:
            raise ValueError("Content must be 2200 characters or less.")

        self.__content = content
        self.author = author
        self.timestamp = datetime.now()

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        if len(value) > 2200:
            raise ValueError("Content must be 2200 characters or less.")
        self.__content = value
