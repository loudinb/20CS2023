from typing import List
import re

class User:
    user_count: int = 0

    def __init__(self, username: str, email: str):
        if not self.is_valid_username(username):
            raise ValueError("Invalid username.")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")
        
        self.username: str = username  # Public attribute
        self._email: str = email  # Protected email attribute
        self._bio: str = ""  # Protected bio, initialized to an empty string
        
        User.user_count += 1

    @property
    def bio(self) -> str:
        return self._bio

    @bio.setter
    def bio(self, value: str) -> None:
        if len(value) > 150:
            raise ValueError("Bio must be 150 characters or less.")
        self._bio = value

    @classmethod
    def get_user_count(cls) -> int:
        return cls.user_count

    @staticmethod
    def is_valid_username(username: str) -> bool:
        return 3 <= len(username) <= 30 and username.replace(".", "").replace("_", "").isalnum()

    @staticmethod
    def is_valid_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None
