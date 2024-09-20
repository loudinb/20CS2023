class Analytics:
    total_likes = 0
    total_shares = 0
    active_users = set()

    @classmethod
    def update_likes(cls, count: int) -> None:
        cls.total_likes += count

    @classmethod
    def update_shares(cls, count: int) -> None:
        cls.total_shares += count

    @classmethod
    def add_active_user(cls, user_id: str) -> None:
        cls.active_users.add(user_id)

    @classmethod
    def remove_active_user(cls, user_id: str) -> None:
        cls.active_users.discard(user_id)

    @staticmethod
    def calculate_engagement_rate(total_interactions: int, total_users: int) -> float:
        return (total_interactions / total_users * 100) if total_users else 0

    @staticmethod
    def identify_trending_posts(posts: list, threshold: int) -> list:
        return [post for post in posts if post.likes_count > threshold]

    @classmethod
    def generate_report(cls) -> str:
        engagement_rate = cls.calculate_engagement_rate(cls.total_likes + cls.total_shares, len(cls.active_users))
        return f"""
        Total Likes: {cls.total_likes}
        Total Shares: {cls.total_shares}
        Active Users: {len(cls.active_users)}
        Current Engagement Rate: {engagement_rate:.2f}%"""