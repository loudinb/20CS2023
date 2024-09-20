from comment import Comment

class Post:
    def add_comment(self, user: 'User', content: str) -> None:
        comment = Comment(user, content)
        # Assume _comments is a list of comments initialized elsewhere
        self._comments.append(comment)

    def remove_comment(self, comment: Comment) -> None:
        if comment in self._comments:
            self._comments.remove(comment)
