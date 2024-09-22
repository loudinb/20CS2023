import re
from datetime import datetime
from post import Post
from comment import Comment

class User:

    user_count = 0

    def __init__(self, username, email):
        if not self.is_valid_username(username):
            raise ValueError("Invalid username.")
        
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")

        self._username = username
        self._email = email
        self._bio = ""
        self._joined_on = datetime.now()
        self._posts = []
        self._liked_posts = []
        self._comments = []
        self._liked_comments = []
        self.following = []
        self.followers = []
        
        User.user_count += 1

    @property
    def posts(self):
        return self._posts

    @property
    def username(self):
        return self._username
    
    @property
    def email(self):
        return self._email

    @property
    def bio(self):
        return self._bio
    
    @bio.setter
    def bio(self, new_bio):
        if len(new_bio) > 150:
            raise ValueError("Bio must be 150 characters or less.")
        self._bio = new_bio

    @property
    def joined_on(self):
        return self._joined_on

    def follow(self, user):
        if user is not self and user not in self.following:
            self.following.append(user)
            user.followers.append(self)

    def unfollow(self, user):
        if user in self.following:
            self.following.remove(user)
            user.followers.remove(self)

    @staticmethod
    def is_valid_username(username):
        if not 3 <= len(username) <= 30:
            return False

        for char in username:
            if not (char.isalnum() or char in ['.', '_']):
                return False

        return True

    @staticmethod
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None
    
    @classmethod
    def get_user_count(cls):
        return cls.user_count
    
    def create_post(self, content, tags=None):
        post = Post(self, content, tags)
        self._posts.append(post)

    def delete_post(self, post):
        if post in self._posts:
            self._posts.remove(post)
            Post.post_count -= 1

    def like_post(self, post):
        if post not in self._posts and post not in self._liked_posts:
            self._liked_posts.append(post)
            post.like(self)

    def unlike_post(self, post):
        if post in self._liked_posts:
            self._liked_posts.remove(post)
            post.unlike(self)

    def comment_on_post(self, post, content, tags=None):
        comment = post.add_comment(self, content, tags)
        self._comments.append(comment)

    def delete_comment_on_post(self, post, comment):
        if comment in self._comments:
            post.delete_comment(comment)
            self._comments.remove(comment)

    def like_comment(self, comment):
        if comment not in self._comments and comment not in self._liked_comments:
            self._liked_comments.append(comment)
            comment.like(self)

    def unlike_comment(self, comment):
        if comment in self._liked_comments:
            self._liked_comments.remove(comment)
            comment.unlike(self)

