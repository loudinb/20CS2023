import re
from datetime import datetime
from post import Post
from comment import Comment
from message import Message

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
        self._posts = []
        self._followers = []
        self._following = []
        self._messages = []  # New attribute for received messages
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

    def create_post(self, content, tags=None):
        """Create a new post and add it to the user's list of posts."""
        new_post = Post(content, tags)
        self._posts.append(new_post)

    def delete_post(self, post):
        """Delete a post if it exists in the user's list of posts."""
        if post in self._posts:
            self._posts.remove(post)

    def like_post(self, post):
        """Like a post by calling the add_like method on the post."""
        post.add_like(self)

    def unlike_post(self, post):
        """Unlike a post by calling the remove_like method on the post."""
        post.remove_like(self)

    def comment_on_post(self, post, content):
        """Comment on a post by creating a new comment and adding it to the post."""
        new_comment = Comment(self, content)
        post.add_comment(new_comment)

    def follow(self, user):
        """Follow another user and add them to the following list."""
        if user not in self._following:  # Enhanced to prevent duplicate follows
            self._following.append(user)
            user._followers.append(self)

    def unfollow(self, user):
        """Unfollow a user by removing them from the following list."""
        if user in self._following:  # Enhanced to prevent unnecessary unfollows
            self._following.remove(user)
            user._followers.remove(self)

    def send_message(self, recipient, content):
        """Send a message to a recipient and deliver it using the receive_message method."""
        new_message = Message(self, recipient, content)
        recipient.receive_message(new_message)
        return new_message

    def receive_message(self, message):
        """Receive a message and add it to the user's message list."""
        if message.recipient == self:
            self._messages.append(message)