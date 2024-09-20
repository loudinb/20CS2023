import re
from post import Post
from message import Message

class User:
    user_count = 0

    def __init__(self, username, email):
        if not self.is_valid_username(username):
            raise ValueError("Invalid username.")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")

        self.username = username  # Public attribute
        self._email = email  # Protected email attribute
        self._bio = ""  # Protected bio, initialized to an empty string
        self._posts = []  # Private list of posts
        self._followers = []  # Private list of followers
        self._following = []  # Private list of following users
        self._messages = []  # Private list to store received messages

        User.user_count += 1

    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self, value):
        if len(value) > 150:
            raise ValueError("Bio must be 150 characters or less.")
        self._bio = value

    def create_post(self, content, tags=None):
        post = Post(content, self, tags)
        self._posts.append(post)

    def delete_post(self, post):
        if post in self._posts:
            self._posts.remove(post)

    def follow(self, user):
        if user not in self._following and user != self:
            self._following.append(user)
            user._followers.append(self)

    def unfollow(self, user):
        if user in self._following:
            self._following.remove(user)
            user._followers.remove(self)

    def like_post(self, post):
        post.add_like(self)

    def unlike_post(self, post):
        post.remove_like(self)

    def comment_on_post(self, post, content):
        post.add_comment(self, content)


    def send_message(self, recipient, content):
        message = Message(self, recipient, content)
        recipient.receive_message(message)
    
    def receive_message(self, message):
        self._messages.append(message)

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    @staticmethod
    def is_valid_username(username):
        return 3 <= len(username) <= 30 and username.replace(".", "").replace("_", "").isalnum()

    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None