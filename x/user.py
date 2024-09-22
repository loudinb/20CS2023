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
        self._sent_messages = []
        self._received_messages = []
        
        User.user_count += 1


    @property
    def posts(self):
        return self._posts
    
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
        post = Post(content, tags)
        self._posts.append(post)
    

    def delete_post(self, post):
        self._posts.remove(post)

    def like_post(self, post):
        post.add_like(self)

    def unlike_post(self, post):
        post.remove_like(self)

    def comment_on_post(self, post, content):
        comment = Comment(self, content)
        post.add_comment(comment)

    def follow_user(self, user):
        if user is self:
            raise ValueError("You cannot follow yourself.")
        if user not in self._following:
            self._following.append(user)
            user._followers.append(self)

    def unfollow_user(self, user):
        self._following.remove(user)
        user._followers.remove(self)

    def send_message(self, recipient, content):
        message = Message(self, content)
        recipient.receive_message(message)
        self._messages.append(message)

    def receive_message(self, sender, message):
        self._messages.append(message)

    @property
    def followers(self):
        return self._followers
    
    @property
    def following(self):
        return self._following
    
    @property
    def messages(self):
        return self._messages

