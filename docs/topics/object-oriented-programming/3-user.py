from datetime import datetime

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.join_date = datetime.now()
        self.posts = []

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Joined on: {self.join_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Number of posts: {len(self.posts)}")

    def create_post(self, content):
        post = {
            "content": content,
            "timestamp": datetime.now(),
            "likes": 0
        }
        self.posts.append(post)
        print(f"Post created: {content}")

    def display_posts(self):
        if not self.posts:
            print("No posts yet.")
        else:
            for i, post in enumerate(self.posts, 1):
                print(f"\nPost {i}:")
                print(f"Content: {post['content']}")
                print(f"Posted on: {post['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Likes: {post['likes']}")

    def like_post(self, post_index):
        if 0 <= post_index < len(self.posts):
            self.posts[post_index]['likes'] += 1
            print(f"Post {post_index + 1} liked!")
        else:
            print("Invalid post index.")
