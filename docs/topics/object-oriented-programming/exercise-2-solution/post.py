from datetime import datetime
from comment import Comment

class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = datetime.now()
        self.likes = 0
        self.comments = []

    def like(self):
        self.likes += 1

    def add_comment(self, user, content):
        comment = Comment(user, self, content)
        self.comments.append(comment)
        return comment

    def display(self):
        print(f"Content: {self.content}")
        print(f"Posted by: {self.user.username}")
        print(f"Posted on: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Likes: {self.likes}")
        print(f"Number of comments: {len(self.comments)}")
        if self.comments:
            print("Comments:")
            for comment in self.comments:
                comment.display()