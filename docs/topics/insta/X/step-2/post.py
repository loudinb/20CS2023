from user import User  # Assuming User is defined elsewhere

class Post:
    def __init__(self, content: str, author: User, tags: Optional[List[str]] = None):
        # Initialization code from Section 1 remains unchanged
        self.author: User = author  # Add the author attribute
        self._likes: List[User] = []

    def add_like(self, user: User) -> None:
        if user not in self._likes:
            self._likes.append(user)

    def remove_like(self, user: User) -> None:
        if user in self._likes:
            self._likes.remove(user)
