from datetime import datetime
from tag import Tag

class Post:
    post_id_counter = 0
    total_posts = 0

    def __init__(self, user, content):
        if not Post.is_valid_content(content):
            raise ValueError("Invalid post content")
        self._user = user
        self._content = content
        self._timestamp = datetime.now()
        self._likes = set()
        self._comments = []
        self._tags = self._extract_tags(content)
        Post.post_id_counter += 1
        self._id = Post.post_id_counter
        Post.total_posts += 1

    @property
    def likes_count(self):
        return len(self._likes)

    @staticmethod
    def is_valid_content(content):
        return 0 < len(content) <= 280

    def _like_post(self, user):
        self._likes.add(user)

    def _unlike_post(self, user):
        self._likes.discard(user)

    def toggle_like(self, user):
        if user in self._likes:
            self._unlike_post(user)
        else:
            self._like_post(user)

    @classmethod
    def get_post_count(cls):
        return cls.total_posts

    @classmethod
    def create_shared_post(cls, user, original_post):
        content = f"Shared: {original_post._content[:50]}..."
        return cls(user, content)

    def _extract_tags(self, content):
        words = content.split()
        return [Tag.get_or_create_tag(word[1:]) for word in words if word.startswith('#')]
