import unittest
from user import User
from post import Post
from analytics import Analytics

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.post = Post(self.user, "Test post content")

    def test_update_likes(self):
        initial_likes = Analytics.total_likes
        Analytics.update_likes(5)
        self.assertEqual(Analytics.total_likes, initial_likes + 5)

    def test_update_shares(self):
        initial_shares = Analytics.total_shares
        Analytics.update_shares(3)
        self.assertEqual(Analytics.total_shares, initial_shares + 3)

    def test_add_active_user(self):
        initial_active_users = len(Analytics.active_users)
        Analytics.add_active_user(self.user)
        self.assertEqual(len(Analytics.active_users), initial_active_users + 1)

    def test_calculate_engagement_rate(self):
        Analytics.add_active_user(self.user)
        self.post.toggle_like(self.user)
        engagement_rate = Analytics.calculate_engagement_rate(self.post)
        self.assertGreater(engagement_rate, 0)

    def test_generate_summary_report(self):
        report = Analytics.generate_summary_report()
        self.assertIn("Total Likes:", report)
        self.assertIn("Total Shares:", report)
        self.assertIn("Active Users:", report)

    def test_identify_trending_posts(self):
        Analytics.add_active_user(self.user)
        self.post.toggle_like(self.user)
        trending_posts = Analytics.identify_trending_posts([self.post], threshold=0)
        self.assertIn(self.post, trending_posts)

if __name__ == '__main__':
    unittest.main()
