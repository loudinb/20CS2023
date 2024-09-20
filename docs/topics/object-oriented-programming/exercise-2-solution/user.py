from datetime import datetime
from post import Post

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.join_date = datetime.now()
        self.posts = []
        self.liked_posts = set()

    def create_post(self, content):
        new_post = Post(self, content)
        self.posts.append(new_post)
        print(f"Post created: {content}")
        return new_post

    def like_post(self, post):
        if post not in self.liked_posts:
            self.liked_posts.add(post)
            post.like()
            print(f"{self.username} liked the post: {post.content[:20]}...")
        else:
            print(f"{self.username} has already liked this post.")

    def comment_on_post(self, post, content):
        comment = post.add_comment(self, content)
        print(f"{self.username} commented on the post: {content}")
        return comment

    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Joined on: {self.join_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Number of posts: {len(self.posts)}")
        print(f"Number of liked posts: {len(self.liked_posts)}")

    def get_activity_feed(self):
        activities = []
        for post in self.posts:
            activities.append(("Post created", post.timestamp, post.content))
        for post in self.liked_posts:
            activities.append(("Post liked", post.timestamp, post.content))
        for post in self.posts:
            for comment in post.comments:
                print(comment.content)
                if comment.user == self:
                    activities.append(("Comment made", comment.timestamp, comment.content))
        return sorted(activities, key=lambda x: x[1], reverse=True)