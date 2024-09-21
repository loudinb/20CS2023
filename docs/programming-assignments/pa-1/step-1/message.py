from datetime import datetime

class Message:
    def __init__(self, content):
        if len(content) > 2200:
            raise ValueError("Message content must be 2000 characters or less.")
        
        self._content = content
        self.timestamp = datetime.now()

    @property
    def content(self):
        return self._content
