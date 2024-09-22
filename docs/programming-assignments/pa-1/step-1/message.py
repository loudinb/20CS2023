from datetime import datetime

class Message:

    message_count = 0

    def __init__(self, content, sender, recipient):
        if not self.is_valid_content(content):
            raise ValueError("Invalid message content.")
        
        self._content = content
        self._timestamp = datetime.now()
        self._sender = sender
        self._recipient = recipient

        Message.message_count += 1

    @property
    def content(self):
        return self._content
    
    @property
    def sender(self):
        return self._sender
    
    @property
    def recipient(self):
        return self._recipient
    
    @property
    def timestamp(self):
        return self._timestamp
    
    @classmethod
    def get_message_count(cls):
        return cls.message_count
    
    @staticmethod
    def is_valid_content(content):
        return 1 <= len(content) <= 2200