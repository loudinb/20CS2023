from user import User  # Assuming User is defined elsewhere

class Message:
    def __init__(self, sender: User, recipient: User, content: str):
        # Initialization code from Section 1 remains unchanged
        self.sender: User = sender  # Add sender attribute
        self.recipient: User = recipient  # Add recipient attribute
