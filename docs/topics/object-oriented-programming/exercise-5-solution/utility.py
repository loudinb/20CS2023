import re
import random
import string
from datetime import datetime

class Utility:
    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def generate_random_string(length):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def format_timestamp(timestamp):
        return timestamp.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def truncate_string(s, length):
        return s[:length] + '...' if len(s) > length else s

    @staticmethod
    def get_current_timestamp():
        return datetime.now()
