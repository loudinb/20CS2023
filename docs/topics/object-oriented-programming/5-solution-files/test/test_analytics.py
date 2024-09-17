import unittest
from user import User
from post import Post
from comment import Comment
from analytics import Analytics

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        Analytics.total_likes = 0
        Analytics.total_shares = 0
        Analytics.active_users = set()
        User.total_users = 0
        Post.post_id_counter = 0
        Comment.total_comments = 0

        self.user1 = User("user1", "user1@example.com")
        self.user2 = User("user2", "user2@example.com")
        self.post1 = Post(self.user1, "Test post 1")
        self.post2 = Post(self.user2, "Test post 2")

    def test_update_likes(self):
        Analytics.update_likes(5)
        self.assertEqual(Analytics.total_likes, 5)

    def test_update_shares(self):
        Analytics.update_shares(3)
        self.assertEqual(Analytics.total_shares, 3)

    def test_add_active_user(self):
        Analytics.add_active_user(self.user1)
        Analytics.add_active_user(self.user2)
        self.assertEqual(len(Analytics.active_users), 2)

    def test_calculate_engagement_rate(self):
        self.post1.toggle_like()
        self.post1.add_comment(self.user2, "Test comment")
        engagement_rate = Analytics.calculate_engagement_rate(self.post1)
        self.assertEqual(engagement_rate, 1.0)  # (1 like + 1 comment) / 2 users = 1.0

    def test_identify_trending_posts(self):
        self.post1.toggle_like()
        self.post1.add_comment(self.user2, "Test comment")
        trending_posts = Analytics.identify_trending_posts([self.post1, self.post2], threshold=0.5)
        self.assertEqual(len(trending_posts), 1)
        self.assertEqual(trending_posts[0], self.post1)

    def test_generate_summary_report(self):
        self.post1.toggle_like()
        self.post1.add_comment(self.user2, "Test comment")
        Analytics.update_likes(1)
        Analytics.update_shares(1)
        Analytics.add_active_user(self.user1)
        report = Analytics.generate_summary_report()
        self.assertIn("Total Users: 2", report)
        self.assertIn("Total Posts: 2", report)
        self.assertIn("Total Comments: 1", report)
        self.assertIn("Total Likes: 1", report)
        self.assertIn("Total Shares: 1", report)
        self.assertIn("Active Users: 1", report)
        self.assertIn("Average Comments per Post: 0.50", report)

if __name__ == '__main__':
    unittest.main()
