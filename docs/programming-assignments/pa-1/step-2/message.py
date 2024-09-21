from datetime import datetime

class Message:
    def __init__(self, sender, recipient, content):
        if len(content) > 2200:
            raise ValueError("Message content must be 2200 characters or less.")
        
        self.sender = sender  # New attribute for sender
        self.recipient = recipient  # New attribute for recipient
        self._content = content
        self.timestamp = datetime.now()

    @property
    def content(self):
        return self._content
