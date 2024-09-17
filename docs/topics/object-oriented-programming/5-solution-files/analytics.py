from user import User
from post import Post
from comment import Comment

class Analytics:
    total_likes = 0
    total_shares = 0
    active_users = set()

    @classmethod
    def update_likes(cls, count):
        cls.total_likes += count

    @classmethod
    def update_shares(cls, count):
        cls.total_shares += count

    @classmethod
    def add_active_user(cls, user):
        cls.active_users.add(user)

    @staticmethod
    def calculate_engagement_rate(post):
        total_interactions = post.likes_count + len(post.comments)
        return total_interactions / len(User.get_user_count()) if User.get_user_count() > 0 else 0

    @classmethod
    def identify_trending_posts(cls, posts, threshold=0.1):
        return [post for post in posts if cls.calculate_engagement_rate(post) > threshold]

    @classmethod
    def generate_summary_report(cls):
        report = f"Total Users: {User.get_user_count()}\n"
        report += f"Total Posts: {Post.get_post_count()}\n"
        report += f"Total Comments: {Comment.get_total_comments()}\n"
        report += f"Total Likes: {cls.total_likes}\n"
        report += f"Total Shares: {cls.total_shares}\n"
        report += f"Active Users: {len(cls.active_users)}\n"
        report += f"Average Comments per Post: {Comment.get_average_comments_per_post():.2f}"
        return report
