from datetime import datetime

class Comment:

    comment_count = 0

    def __init__(self, author, content, tags=None):
        if not self.is_valid_content(content):
            raise ValueError("Invalid comment content.")
        self._author = author
        self._content = content
        self._tags = set()
        if tags:
            for tag in tags:
                if not self.is_valid_tag(tag):
                    raise ValueError("Invalid tag.")
                self._tags.add(tag)
        self._created_on = datetime.now()
        self._liked_by = []

        Comment.comment_count += 1

    @property
    def content(self):
        return self._content
    
    @property
    def created_on(self):
        return self._created_on
    
    @property
    def tags(self):
        return self._tags
    
    def add_tag(self, tag):
        if not self.is_valid_tag(tag):
            raise ValueError("Invalid tag.")
        self._tags.add(tag)

    def remove_tag(self, tag):
        if tag in self._tags:
            self._tags.discard(tag)

    @staticmethod
    def is_valid_content(content):
        if len(content) < 3 or len(content) > 2200:
            return False
        return True
    
    @staticmethod
    def is_valid_tag(tag):
        if len(tag) <= 30 and tag.isalnum():
            return True
        return False
    
    @staticmethod
    def get_comment_count():
        return Comment.comment_count