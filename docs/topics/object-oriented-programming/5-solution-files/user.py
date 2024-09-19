import re
from private_message import PrivateMessage

class User:
    total_users = 0

    def __init__(self, username, email):
        if not User.is_valid_username(username):
            raise ValueError("Invalid username")
        self._username = username
        self._email = email
        self._posts = []
        self._received_messages = []
        User.total_users += 1

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if self._validate_email(value):
            self._email = value
        else:
            raise ValueError("Invalid email format")

    @staticmethod
    def is_valid_username(username):
        return username.isalnum() and 3 <= len(username) <= 20

    @staticmethod
    def _validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @classmethod
    def get_user_count(cls):
        return cls.total_users

    @classmethod
    def create_anonymous_user(cls):
        anonymous_username = f"anon_{cls.total_users + 1}"
        return cls(anonymous_username, f"{anonymous_username}@example.com")

    def create_post(self, content):
        from post import Post
        new_post = Post(self, content)
        self._posts.append(new_post)
        return new_post

    def send_private_message(self, recipient, content):
        message = PrivateMessage(self, recipient, content)
        recipient._received_messages.append(message)
        return message

    def view_private_messages(self):
        return self._received_messages
