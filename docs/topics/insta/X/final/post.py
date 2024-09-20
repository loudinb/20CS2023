from datetime import datetime
from comment import Comment  # Import here to avoid circular import

class Post:
    post_count = 0

    def __init__(self, content, author, tags=None):
        if len(content) > 2200:
            raise ValueError("Content must be 2200 characters or less.")

        self.__content = content
        self.author = author
        self.timestamp = datetime.now()
        self._tags = tags or []
        self._likes = []
        self._comments = []

        Post.post_count += 1

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        if len(value) > 2200:
            raise ValueError("Content must be 2200 characters or less.")
        self.__content = value

    def add_like(self, user):
        if user not in self._likes:
            self._likes.append(user)

    def remove_like(self, user):
        if user in self._likes:
            self._likes.remove(user)

    def add_tag(self, tag):
        if not self.is_valid_tag(tag):
            raise ValueError("Invalid tag")
        self._tags.append(tag)

    def remove_tag(self, tag):
        if tag in self._tags:
            self._tags.remove(tag)

    def add_comment(self, user, content):
        comment = Comment(user, content)
        self._comments.append(comment)

    def remove_comment(self, comment):
        if comment in self._comments:
            self._comments.remove(comment)

    @classmethod
    def get_post_count(cls):
        return cls.post_count

    @staticmethod
    def is_valid_tag(tag):
        return len(tag) <= 30 and tag.isalnum()
