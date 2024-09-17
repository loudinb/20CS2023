from datetime import datetime
from post import Post

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.join_date = datetime.now()
        self.posts = []

    def create_post(self, content):
        new_post = Post(self, content)
        self.posts.append(new_post)
        print(f"Post created: {content}")

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Joined on: {self.join_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Number of posts: {len(self.posts)}")