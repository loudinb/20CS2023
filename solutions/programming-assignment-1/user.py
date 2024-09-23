import re
from datetime import datetime

class User:

    user_count = 0

    def __init__(self, username, email):
        if not self.is_valid_username(username):
            raise ValueError("Invalid username.")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email.")
        
        self._username = username
        self._email = email
        self._bio = ""
        self._jonied_on = datetime.now()
        self._posts = []
        self._liked_posts = []
        self._comments = []
        self._liked_comments = []
        self.following = []
        self.followers = []

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
        return self._jonied_on
    
    @property
    def posts(self):
        return self._posts
    
    @staticmethod
    def is_valid_username(username):
        if len(username) < 3 or len(username) > 30:
            return False
        for char in username:
            if not char.isalnum() and char not in ['.', '_']:
                return False
        return True
    
    @staticmethod
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None
    
    @classmethod
    def get_user_count(cls):
        return cls.user_count
    