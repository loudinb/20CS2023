from datetime import datetime
import re

class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email
        self._join_date = datetime.now()
        self._posts = []
        self._followers = []

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if self.__validate_email(value):
            self._email = value
        else:
            raise ValueError("Invalid email format")

    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self, value):
        if len(value) <= 150:
            self._bio = value
        else:
            raise ValueError("Bio must be 150 characters or less")

    def __validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

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
        print(f"Joined on: {self._join_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Number of posts: {len(self._posts)}")
        print(f"Followers: {len(self._followers)}")

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
