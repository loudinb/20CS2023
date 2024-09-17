from datetime import datetime

class Comment:
    def __init__(self, user, post, content):
        self.user = user
        self.post = post
        self.content = content
        self.timestamp = datetime.now()
        self.likes = 0

    def like(self):
        self.likes += 1

    def display(self):
        print(f"Comment by {self.user.username}: {self.content}")
        print(f"Posted on: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Likes: {self.likes}")