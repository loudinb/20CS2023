import unittest
from datetime import datetime
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertIsInstance(self.user.join_date, datetime)
        self.assertEqual(self.user.posts, [])

    def test_display_info(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.user.display_info()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("Username: testuser", output)
        self.assertIn("Email: test@example.com", output)
        self.assertIn("Joined on:", output)
        self.assertIn("Number of posts: 0", output)

    def test_create_post(self):
        self.user.create_post("Test content")
        self.assertEqual(len(self.user.posts), 1)
        self.assertEqual(self.user.posts[0]["content"], "Test content")
        self.assertIsInstance(self.user.posts[0]["timestamp"], datetime)

    def test_display_posts(self):
        self.user.create_post("First post")
        self.user.create_post("Second post")

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.user.display_posts()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("First post", output)
        self.assertIn("Second post", output)
        self.assertIn("Posted on:", output)

    def test_like_post(self):
        self.user.create_post("Test post")
        self.user.like_post(0)
        self.assertEqual(self.user.posts[0]["likes"], 1)

    def test_display_posts_with_likes(self):
        self.user.create_post("Liked post")
        self.user.like_post(0)

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.user.display_posts()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("Liked post", output)
        self.assertIn("Likes: 1", output)

if __name__ == '__main__':
    unittest.main()