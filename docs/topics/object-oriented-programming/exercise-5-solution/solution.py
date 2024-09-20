import re
from utility import Utility

class User:
    def __init__(self, username, email):
        if not User.is_valid_username(username):
            raise ValueError("Invalid username")
        if not Utility.is_valid_email(email):
            raise ValueError("Invalid email")
        self._username = username
        self._email = email

    @staticmethod
    def is_valid_username(username):
        return username.isalnum() and 3 <= len(username) <= 20

    @staticmethod
    def generate_random_username():
        return f"user_{Utility.generate_random_string(8)}"

    @staticmethod
    def format_user_info(username, email):
        return f"User: {username} (Email: {email})"

    # ... (other methods remain the same)
