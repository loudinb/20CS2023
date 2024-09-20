from datetime import datetime

class Message:
    def __init__(self, sender, recipient, content):
        if len(content) > 2000:
            raise ValueError("Message content must be 2000 characters or less.")
        self.__content = content
        self.timestamp = datetime.now()
        self.sender = sender  # Add sender attribute
        self.recipient = recipient  # Add recipient attribute

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        if len(value) > 2000:
            raise ValueError("Message content must be 2000 characters or less.")
        self.__content = value
