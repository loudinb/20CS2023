from datetime import datetime
from comment import Comment

class Post:
    def __init__(self, user, content):
        self._user = user
        self._content = content
        self._timestamp = datetime.now()
        self._likes = 0
        self._comments = []

    @property
    def user(self):
        return self._user

    @property
    def content(self):
        return self._content

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def likes_count(self):
        return self._likes

    @property
    def comments(self):
        return self._comments

    def _like(self):
        self._likes += 1

    def _unlike(self):
        if self._likes > 0:
            self._likes -= 1

    def toggle_like(self):
        if self._likes > 0:
            self._unlike()
            return False
        else:
            self._like()
            return True

    def add_comment(self, user, content):
        comment = Comment(user, self, content)
        self._comments.append(comment)
        return comment

    def display(self):
        print(f"Content: {self._content}")
        print(f"Posted by: {self._user.username}")
        print(f"Posted on: {self._timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Likes: {self._likes}")
        print(f"Number of comments: {len(self._comments)}")
        if self._comments:
            print("Comments:")
            for comment in self._comments:
                comment.display()
