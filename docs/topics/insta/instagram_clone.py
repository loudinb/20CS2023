from user import User

class InstagramClone:
    def __init__(self):
        self.users = []

    def register_user(self, username, email):
        if User.is_valid_username(username) and self.is_valid_email(email):
            new_user = User(username, email)
            self.users.append(new_user)
            return new_user
        else:
            raise ValueError("Invalid username or email")

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def get_posts_by_tag(self, tag):
        tagged_posts = []
        for user in self.users:
            for post in user.posts:
                if tag in post.tags:
                    tagged_posts.append(post)
        return tagged_posts

    @staticmethod
    def is_valid_email(email):
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
