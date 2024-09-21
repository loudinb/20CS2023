from datetime import datetime


class Comment:

    def __init__(self, content):
        if len(content) > 2200:
            raise ValueError("Comment is too long")
        self._content = content
        self._tags = set()
        self.timestamp = datetime.now()

    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        if len(value) > 2200:
            raise ValueError("Comment is too long")
        self._content = value

    @property
    def tags(self):
        return self._tags
    
    def add_tag(self, tag):
        if len(tag) <= 30 and tag.isalnum():
            self._tags.add(tag)
        else:
            raise ValueError("Invalid tag.")
    
    def remove_tag(self, tag):
        self._tags.discard(tag)