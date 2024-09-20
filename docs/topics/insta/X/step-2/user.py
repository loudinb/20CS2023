from typing import List, Optional

class User:
    # Add new attributes for followers and following
    def __init__(self, username: str, email: str):
        # Initialization code from Section 1 remains unchanged
        self._followers: List[User] = []
        self._following: List[User] = []

    def follow(self, user: 'User') -> None:
        if user not in self._following:
            self._following.append(user)
            user._followers.append(self)

    def unfollow(self, user: 'User') -> None:
        if user in self._following:
            self._following.remove(user)
            user._followers.remove(self)
