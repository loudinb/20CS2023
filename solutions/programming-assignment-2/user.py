from datetime import datetime
import re

class InvalidUsernameError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

class User:
    """
    Represents a user in the InstaMimic system.
    """

    user_count = 0

    def __init__(self, username: str, email: str):
        if not self.is_valid_username(username):
            raise InvalidUsernameError(f"Invalid username: {username}")
        if not self.is_valid_email(email):
            raise InvalidEmailError(f"Invalid email: {email}")
        
        self.__username = username
        self.__email = email
        self.__bio = ""
        self.__joined_on = datetime.now()
        self.__posts = []
        self.__liked_posts = []
        self.__comments = []
        self.__liked_comments = []
        self.following = []
        self.followers = []
        
        User.user_count += 1

    @property
    def username(self) -> str:
        return self.__username

    @property
    def email(self) -> str:
        return self.__email

    @property
    def bio(self) -> str:
        return self.__bio

    @bio.setter
    def bio(self, new_bio: str):
        if len(new_bio) > 150:
            raise ValueError("Bio must be 150 characters or less.")
        self.__bio = new_bio

    @property
    def joined_on(self) -> datetime:
        return self.__joined_on

    @property
    def posts(self) -> list:
        return self.__posts

    @staticmethod
    def is_valid_username(username: str) -> bool:
        return 3 <= len(username) <= 30 and all(char.isalnum() or char in ['.', '_'] for char in username)

    @staticmethod
    def is_valid_email(email: str) -> bool:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    @classmethod
    def get_user_count(cls) -> int:
        return cls.user_count
