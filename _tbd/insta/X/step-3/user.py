from post import Post
from comment import Comment

class User:
    def __init__(self, username: str, email: str):
        # Initialization code from Sections 1 and 2 remains unchanged
        self._posts: List[Post] = []

    def create_post(self, content: str, tags: Optional[List[str]] = None) -> None:
        post = Post(content, self, tags)
        self._posts.append(post)

    def delete_post(self, post: Post) -> None:
        if post in self._posts:
            self._posts.remove(post)

    def like_post(self, post: Post) -> None:
        post.add_like(self)

    def unlike_post(self, post: Post) -> None:
        post.remove_like(self)

    def comment_on_post(self, post: Post, content: str) -> None:
        post.add_comment(self, content)
