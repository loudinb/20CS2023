from post import Post
from message import Message
from comment import Comment

class User:
    # Class attribute to track total number of users
    user_count = 0

    def __init__(self, username, email):
        # Validate the username and email using static methods
        if not self.is_valid_username(username):
            raise ValueError("Invalid username.")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")
        
        self.username = username
        self._email = email  # Protected email attribute
        self._bio = ""       # Protected bio, initialized to an empty string
        self._posts = []     # Protected list to hold user's posts
        self._followers = [] # Protected list to hold followers
        self._following = [] # Protected list to hold following users

        # Increment the class attribute user_count each time a new user is created
        User.user_count += 1

    # Property to get and set the bio attribute
    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self, value):
        if len(value) <= 150:
            self._bio = value
        else:
            raise ValueError("Bio must be 150 characters or less.")

    # Create a new post for the user
    def create_post(self, content, tags=None):
        post = Post(content, tags)
        self._posts.append(post)

    # Delete a post from the user's posts
    def delete_post(self, post):
        if post in self._posts:
            self._posts.remove(post)

    # Follow another user
    def follow(self, user):
        if user not in self._following:
            self._following.append(user)
            user._followers.append(self)

    # Unfollow another user
    def unfollow(self, user):
        if user in self._following:
            self._following.remove(user)
            user._followers.remove(self)

    # Like a post
    def like_post(self, post):
        post.add_like(self)

    # Unlike a post
    def unlike_post(self, post):
        post.remove_like(self)

    # Comment on a post
    def comment_on_post(self, post, content):
        post.add_comment(self, content)

    # Send a message to another user
    def send_message(self, recipient, content):
        message = Message(self, recipient, content)
        recipient.receive_message(message)

    # Class method to get the total number of users
    @classmethod
    def get_user_count(cls):
        return cls.user_count

    # Static method to validate usernames
    @staticmethod
    def is_valid_username(username):
        if 3 <= len(username) <= 30 and username.replace(".", "").replace("_", "").isalnum():
            return True
        return False

    # Static method to validate email addresses using a basic regex
    @staticmethod
    def is_valid_email(email):
        import re
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None
