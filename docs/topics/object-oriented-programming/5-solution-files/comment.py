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
    def user(self):
        return self._user

    @property
    def post(self):
        return self._post

    @property
    def content(self):
        return self._content

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def likes(self):
        return self._likes

    def _increment_likes(self):
        self._likes += 1

    def like(self):
        self._increment_likes()

    def display(self):
        print(f"Comment by {self._user.username}: {self._content}")
        print(f"Posted on: {self._timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Likes: {self._likes}")

    @classmethod
    def get_total_comments(cls):
        return cls.total_comments

    @classmethod
    def get_average_comments_per_post(cls):
        from post import Post
        total_posts = Post.get_post_count()
        if total_posts == 0:
            return 0
        return cls.total_comments / total_posts

    @staticmethod
    def format_content(content):
        return content.strip().capitalize()
