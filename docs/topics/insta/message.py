from datetime import datetime

class Message:
    message_count = 0
    MESSAGE_LIMIT = 2000

    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = datetime.now()
        Message.message_count += 1

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if len(value) <= self.MESSAGE_LIMIT:
            self._content = value
        else:
            raise ValueError(f"Message must be {self.MESSAGE_LIMIT} characters or less")

    @classmethod
    def get_message_count(cls):
        return cls.message_count

    @staticmethod
    def is_valid_content(content):
        return 0 < len(content) <= Message.MESSAGE_LIMIT
