from datetime import datetime

class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = datetime.now()
        self.likes = 0

    def display(self):
        print(f"Content: {self.content}")
        print(f"Posted by: {self.user.username}")
        print(f"Posted on: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Likes: {self.likes}")