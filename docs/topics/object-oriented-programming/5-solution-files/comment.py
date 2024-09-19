from datetime import datetime

class Comment:
    total_comments = 0

    def __init__(self, user, post, content):
        self._user = user
        self._post = post
        self._content = Comment.format_content(content)
        self._timestamp = datetime.now()
        self._likes = 0
        Comment.total_comments += 1

    @property
    def timestamp(self):
        return self._timestamp

    @staticmethod
    def format_content(content):
        return ' '.join(content.split()).capitalize()

    def _increment_likes(self):
        self._likes += 1

    def like(self):
        self._increment_likes()

    @classmethod
    def get_average_comments_per_post(cls):
        from post import Post
        if Post.total_posts == 0:
            return 0
        return cls.total_comments / Post.total_posts
