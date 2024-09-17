from datetime import datetime
import re
from post import Post
from private_message import PrivateMessage

class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email
        self._join_date = datetime.now()
        self._posts = []
        self._liked_posts = set()
        self._received_messages = []
        self._bio = ""

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

    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self, value):
        if len(value) <= 150:
            self._bio = value
        else:
            raise ValueError("Bio must be 150 characters or less")

    def _validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def create_post(self, content):
        new_post = Post(self, content)
        self._posts.append(new_post)
        return new_post

    def like_post(self, post):
        if post not in self._liked_posts:
            self._liked_posts.add(post)
            post.toggle_like()
            return True
        return False

    def comment_on_post(self, post, content):
        return post.add_comment(self, content)

    def display_info(self):
        print(f"Username: {self._username}")
        print(f"Email: {self._email}")
        print(f"Bio: {self._bio}")
        print(f"Joined on: {self._join_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Number of posts: {len(self._posts)}")
        print(f"Number of liked posts: {len(self._liked_posts)}")

    def get_activity_feed(self):
        activities = []
        for post in self._posts:
            activities.append(("Post created", post.timestamp, post.content))
        for post in self._liked_posts:
            activities.append(("Post liked", post.timestamp, post.content))
        for post in self._posts:
            for comment in post.comments:
                if comment.user == self:
                    activities.append(("Comment made", comment.timestamp, comment.content))
        return sorted(activities, key=lambda x: x[1], reverse=True)

    def send_private_message(self, recipient, content):
        message = PrivateMessage(self, recipient, content)
        recipient._received_messages.append(message)
        return message

    def view_private_messages(self):
        return self._received_messages
