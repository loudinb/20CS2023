from datetime import datetime

class Comment:
    COMMENT_LIMIT = 2200

    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.timestamp = datetime.now()

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if len(value) <= self.COMMENT_LIMIT:
            self._content = value
        else:
            raise ValueError(f"Comment must be {self.COMMENT_LIMIT} characters or less")

    @staticmethod
    def is_valid_content(content):
        return 0 < len(content) <= Comment.COMMENT_LIMIT
