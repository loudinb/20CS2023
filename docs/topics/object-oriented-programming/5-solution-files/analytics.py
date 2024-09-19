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
        total_interactions = post.likes_count + len(post._comments)
        return total_interactions / len(Analytics.active_users) if Analytics.active_users else 0

    @classmethod
    def generate_summary_report(cls):
        return f"""
        Total Likes: {cls.total_likes}
        Total Shares: {cls.total_shares}
        Active Users: {len(cls.active_users)}
        """

    @staticmethod
    def identify_trending_posts(posts, threshold=0.5):
        return [post for post in posts if Analytics.calculate_engagement_rate(post) > threshold]
