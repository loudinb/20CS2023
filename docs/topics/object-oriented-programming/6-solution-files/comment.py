from utility import Utility

class Comment:
    def __init__(self, user, post, content):
        if not Comment.is_valid_content(content):
            raise ValueError("Invalid comment content")
        self._user = user
        self._post = post
        self._content = Comment.format_content(content)
        self._timestamp = Utility.get_current_timestamp()

    @staticmethod
    def format_content(content):
        return ' '.join(content.split()).capitalize()

    @staticmethod
    def is_valid_content(content):
        return 0 < len(content) <= 200

    @staticmethod
    def generate_comment_preview(content, length=30):
        return Utility.truncate_string(content, length)

    def display(self):
        return f"{self._user.username} commented: {self._content} ({Utility.format_timestamp(self._timestamp)})"

    # ... (other methods remain the same)
