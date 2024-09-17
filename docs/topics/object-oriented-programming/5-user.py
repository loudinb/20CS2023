from datetime import datetime
import re

class User:
    user_count = 0
    min_username_length = 3
    max_bio_length = 150

    def __init__(self, username, email, bio=""):
        if len(username) < User.min_username_length:
            raise ValueError(f"Username must be at least {User.min_username_length} characters long")
        self._username = username
        self._email = email
        self._bio = User.truncate_bio(bio)
        self._join_date = datetime.now()
        self._posts = []
        self._followers = []
        User.user_count += 1

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if User.is_valid_email(value):
            self._email = value
        else:
            raise ValueError("Invalid email format")

    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self, value):
        self._bio = User.truncate_bio(value)

    @classmethod
    def display_user_count(cls):
        print(f"Total number of users: {cls.user_count}")

    @classmethod
    def create_from_string(cls, user_string):
        username, email, bio = user_string.split(',')
        return cls(username, email, bio)

    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @classmethod
    def set_max_bio_length(cls, length):
        cls.max_bio_length = length

    @staticmethod
    def truncate_bio(bio):
        return bio[:User.max_bio_length]

    def create_post(self, content):
        post = {
            "content": content,
            "timestamp": datetime.now(),
            "likes": 0
        }
        self._posts.append(post)
        print(f"Post created: {content}")

    def like_post(self, post_index):
        if 0 <= post_index < len(self._posts):
            self._posts[post_index]['likes'] += 1
            print(f"Post {post_index + 1} liked!")
        else:
            raise IndexError("Invalid post index")

    def display_info(self):
        print(f"Username: {self._username}")
        print(f"Email: {self._email}")
        print(f"Bio: {self._bio}")
        print(f"Joined on: {self._join_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Number of posts: {len(self._posts)}")
        print(f"Followers: {len(self._followers)}")
        print(f"Total users: {User.user_count}")

    def display_posts(self):
        if not self._posts:
            print("No posts yet.")
        else:
            for i, post in enumerate(self._posts, 1):
                print(f"\nPost {i}:")
                print(f"Content: {post['content']}")
                print(f"Posted on: {post['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Likes: {post['likes']}")

    def follow(self, other_user):
        if other_user not in self._followers:
            self._followers.append(other_user)
            print(f"{self._username} is now following {other_user.username}")
        else:
            print(f"{self._username} is already following {other_user.username}")

    @property
    def follower_count(self):
        return len(self._followers)
