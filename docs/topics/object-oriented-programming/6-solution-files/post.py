from utility import Utility

class Post:
    def __init__(self, user, content):
        if not Post.is_valid_content(content):
            raise ValueError("Invalid post content")
        self._user = user
        self._content = content
        self._hashtags = Post.extract_hashtags(content)

    @staticmethod
    def is_valid_content(content):
        return 0 < len(content) <= 280

    @staticmethod
    def extract_hashtags(content):
        return [word[1:] for word in content.split() if word.startswith('#')]

    @staticmethod
    def format_post(content):
        return Utility.truncate_string(content, 50)

    # ... (other methods remain the same)
