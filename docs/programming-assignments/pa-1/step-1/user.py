import re
from datetime import datetime


class User:

    user_count = 0

    def __init__(self, username, email):
        if not self.is_valid_username(username):
            raise ValueError("Invalid username.")
        
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")

        self._username = username
        self._email = email
        self._bio = ""
        self._joined_on = datetime.now()
        self.posts = []
        self.following = []
        self.followers = []
        self.messages = []
        User.user_count += 1

    @property
    def username(self):
        return self._username
    
    @property
    def email(self):
        return self._email

    @property
    def bio(self):
        return self._bio
    
    @bio.setter
    def bio(self, new_bio):
        if len(new_bio) > 150:
            raise ValueError("Bio must be 150 characters or less.")
        self._bio = new_bio

    @property
    def joined_on(self):
        return self._joined_on

    def follow(self, user):
        if user not in self.following:
            self.following.append(user)
            user.followers.append(self)

    def unfollow(self, user):
        if user in self.following:
            self.following.remove(user)
            user.followers.remove(self)

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
