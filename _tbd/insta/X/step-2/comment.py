from user import User  # Assuming User is defined elsewhere

class Comment:
    def __init__(self, author: User, content: str):
        # Initialization code from Section 1 remains unchanged
        self.author: User = author  # Add the author attribute
