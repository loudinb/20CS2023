from datetime import datetime

class Message:
    def __init__(self, sender, content):
        if len(content) > 2200:
            raise ValueError("Message content must be 2000 characters or less.")
        
        self._content = content
        self.timestamp = datetime.now()
        self._sender = sender

    @property
    def content(self):
        return self._content
    
    @property
    def sender(self):
        return self._sender
    

    
