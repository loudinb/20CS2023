from datetime import datetime
from comment import Comment

class Post:
    post_count = 0
    CAPTION_LIMIT = 2200

    def __init__(self, content, author, tags=None):
        self.content = content
        self.author = author
        self.timestamp = datetime.now()
        self.tags = tags or []
        self.likes = []
        self.comments = []
        Post.post_count += 1

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if len(value) <= self.CAPTION_LIMIT:
            self._content = value
        else:
            raise ValueError(f"Caption must be {self.CAPTION_LIMIT} characters or less")

    def add_comment(self, user, content):
        new_comment = Comment(user, content)
        self.comments.append(new_comment)
        return new_comment

    def remove_comment(self, comment):
        if comment in self.comments:
            self.comments.remove(comment)
            return True
        return False

    def add_like(self, user):
        if user not in self.likes:
            self.likes.append(user)

    def remove_like(self, user):
        if user in self.likes:
            self.likes.remove(user)

    def add_tag(self, tag):
        if tag not in self.tags and Post.is_valid_tag(tag):
            self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
            return True
        return False

    @classmethod
    def get_post_count(cls):
        return cls.post_count

    @staticmethod
    def is_valid_tag(tag):
        return tag.isalnum() and len(tag) <= 30
