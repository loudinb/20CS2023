import re
from datetime import datetime

class User:

    user_count = 0

    def __init__(self, username, email):
        if not self.is_valid_username(username):
            raise ValueError("Invalid username.")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")
        self.username = username
        self._email = email
        self._bio = ""
        self._joined_on = datetime.now()
        User.user_count += 1

    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self, value):
        if len(value) > 150:
            raise ValueError("Bio must be 150 characters or less.")
        self._bio = value

    @staticmethod
    def is_valid_username(username):
        if not 3 <= len(username) <= 30:
            return False
        
        for char in username:
            if not (char.isalnum() or char in ['.', '_']):
                return False
        
        return True

    @staticmethod
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    @classmethod
    def get_user_count(cls):
        return cls.user_count