from datetime import datetime

class Post:
    
    post_count = 0

    def __init__(self, author, content, tags=None):
        if not self.is_valid_content(content):
            raise ValueError("Content exceeds 2200 characters.")
        
        self._tags = set()
        if tags is not None:
            for tag in tags:
                if not self.is_valid_tag(tag):
                    raise ValueError("Invalid tag.")
                self._tags.add(tag)

        self._content = content
        self.timestamp = datetime.now()
        self.author = author  # New attribute for author
        self._likes = []  # New attribute for likes
        self._comments = []  # New attribute for comments

        Post.post_count += 1

    @property
    def content(self):
        return self._content
    
    @property
    def tags(self):
        return self._tags
    
    def add_tag(self, tag):
        if not self.is_valid_tag(tag):
            raise ValueError("Invalid tag.")
        self._tags.add(tag)

    def remove_tag(self, tag):
        self._tags.discard(tag)
    
    def add_like(self, user):
        """Add a like from a user if they haven't already liked the post."""
        if user not in self._likes:
            self._likes.append(user)
    
    def remove_like(self, user):
        """Remove a like from a user if they have liked the post."""
        if user in self._likes:
            self._likes.remove(user)
    
    def add_comment(self, user, content):
        """Add a comment to the post."""
        from comment import Comment
        new_comment = Comment(user, content)
        self._comments.append(new_comment)
    
    def remove_comment(self, comment):
        """Remove a comment from the post."""
        if comment in self._comments:
            self._comments.remove(comment)

    @staticmethod
    def is_valid_tag(tag):
        return len(tag) <= 30 and tag.isalnum()

    @staticmethod
    def is_valid_content(content):
        return 3 <= len(content) <= 2200
    
    @classmethod
    def get_post_count(cls):
        return cls.post_count