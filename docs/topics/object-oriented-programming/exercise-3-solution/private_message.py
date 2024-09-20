from datetime import datetime

class PrivateMessage:
    _total_messages = 0

    def __init__(self, sender, recipient, content):
        self._sender = sender
        self._recipient = recipient
        self._content = content
        self._timestamp = datetime.now()
        PrivateMessage._total_messages += 1

    @property
    def sender(self):
        return self._sender

    @property
    def recipient(self):
        return self._recipient

    @property
    def content(self):
        return self._content

    @property
    def timestamp(self):
        return self._timestamp

    @staticmethod
    def get_total_message_count():
        return PrivateMessage._total_messages

    def display_message(self, user):
        if user == self._sender or user == self._recipient:
            print(f"From: {self._sender.username}")
            print(f"To: {self._recipient.username}")
            print(f"Sent on: {self._timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Content: {self._content}")
        else:
            print("You don't have permission to view this message.")
