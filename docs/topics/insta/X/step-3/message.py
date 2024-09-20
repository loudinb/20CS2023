class Message:
    # Assume User class is defined elsewhere with send_message functionality
    def send_message(self, recipient: 'User', content: str) -> None:
        message = Message(self, recipient, content)
        recipient.receive_message(message)
