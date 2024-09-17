from datetime import datetime
from comment import Comment
from tag import Tag

class Post:
    post_id_counter = 0

    def __init__(self, user, content):
        Post.post_id_counter += 1
        self._id = Post.post_id_counter
        self._user = user
        self._content = content
        self._timestamp = datetime.now()
        self._likes = 0
        self._comments = []
        self._tags = []

    @property
    def id(self):
        return self._id

    @property
    def user(self):
        return self._user

    @property
    def content(self):
        return self._content

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def likes_count(self):
        return self._likes

    @property
    def comments(self):
        return self._comments

    @property
    def tags(self):
        return self._tags

    def _like(self):
        self._likes += 1

    def _unlike(self):
        if self._likes > 0:
            self._likes -= 1

    def toggle_like(self):
        if self._likes > 0:
            self._unlike()
            return False
        else:
            self._like()
            return True

    def add_comment(self, user, content):
        comment = Comment(user, self, content)
        self._comments.append(comment)
        return comment

    def add_tag(self, tag_name):
        tag = Tag.get_or_create(tag_name)
        if tag not in self._tags:
            self._tags.append(tag)
        return tag

    @classmethod
    def get_post_count(cls):
        return cls.post_id_counter

    @staticmethod
    def is_valid_content(content):
        return 0 < len(content) <= 500

    @classmethod
    def create_shared_post(cls, original_post, user, additional_content=""):
        shared_content = f"Shared post from {original_post.user.username}: {original_post.content}\n\n{additional_content}"
        return cls(user, shared_content)

    def display(self):
        print(f"Post ID: {self._id}")
        print(f"Content: {self._content}")
        print(f"Posted by: {self._user.username}")
        print(f"Posted on: {self._timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Likes: {self._likes}")
        print(f"Number of comments: {len(self._comments)}")
        if self._tags:
            print("Tags:", ", ".join(tag.name for tag in self._tags))
        if self._comments:
            print("Comments:")
            for comment in self._comments:
                comment.display()
