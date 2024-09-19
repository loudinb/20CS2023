import unittest
from analytics import Analytics
from post import Post
from user import User

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        Analytics.total_likes = 0
        Analytics.total_shares = 0
        Analytics.active_users = set()

    def test_update_likes(self):
        Analytics.update_likes(5)
        self.assertEqual(Analytics.total_likes, 5)

    def test_update_shares(self):
        Analytics.update_shares(3)
        self.assertEqual(Analytics.total_shares, 3)

    def test_add_active_user(self):
        Analytics.add_active_user("user1")
        self.assertIn("user1", Analytics.active_users)

    def test_remove_active_user(self):
        Analytics.add_active_user("user1")
        Analytics.remove_active_user("user1")
        self.assertNotIn("user1", Analytics.active_users)

    def test_calculate_engagement_rate(self):
        rate = Analytics.calculate_engagement_rate(50, 1000)
        self.assertEqual(rate, 5.0)

    def test_identify_trending_posts(self):
        user = User("testuser", "test@example.com")
        post1 = Post(user, "Trending post")
        post2 = Post(user, "Not trending")
        for _ in range(10):
            post1.toggle_like(User("user1", "user1@example.com"))
        trending = Analytics.identify_trending_posts([post1, post2], 5)
        self.assertEqual(len(trending), 1)
        self.assertEqual(trending[0], post1)

    def test_generate_report(self):
        Analytics.update_likes(100)
        Analytics.update_shares(50)
        Analytics.add_active_user("user1")
        Analytics.add_active_user("user2")
        report = Analytics.generate_report()
        self.assertIn("Total Likes: 100", report)
        self.assertIn("Total Shares: 50", report)
        self.assertIn("Active Users: 2", report)
        self.assertIn("Current Engagement Rate:", report)

if __name__ == '__main__':
    unittest.main()
