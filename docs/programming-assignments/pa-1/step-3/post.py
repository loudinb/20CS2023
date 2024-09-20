from datetime import datetime
from comment import Comment  # Assuming Comment is defined elsewhere

class Post:
    post_count = 0

    def __init__(self, content, author, tags=None):
        if len(content) > 2200:
            raise ValueError("Content must be 2200 characters or less.")
        self.__content = content
        self.timestamp = datetime.now()
        self._tags = tags or []
        self.author = author  # Add the author attribute
        self._likes = []
        self._comments = []  # Initialize _comments list
        Post.post_count += 1

    def add_comment(self, user, content):
        comment = Comment(user, content)
        self._comments.append(comment)

    def remove_comment(self, comment):
        if comment in self._comments:
            self._comments.remove(comment)

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        if len(value) > 2200:
            raise ValueError("Content must be 2200 characters or less.")
        self.__content = value

    def add_tag(self, tag):
        if not self.is_valid_tag(tag):
            raise ValueError("Invalid tag")
        self._tags.append(tag)

    def remove_tag(self, tag):
        if tag in self._tags:
            self._tags.remove(tag)

    def add_like(self, user):
        if user not in self._likes:
            self._likes.append(user)

    def remove_like(self, user):
        if user in self._likes:
            self._likes.remove(user)

    @classmethod
    def get_post_count(cls):
        return cls.post_count

    @staticmethod
    def is_valid_tag(tag):
        return len(tag) <= 30 and tag.isalnum()