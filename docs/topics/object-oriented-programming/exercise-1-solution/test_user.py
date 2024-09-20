import unittest
from datetime import datetime
from user import User
from post import Post

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")

    def test_user_initialization(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertIsInstance(self.user.join_date, datetime)
        self.assertEqual(len(self.user.posts), 0)

    def test_create_post(self):
        self.user.create_post("Test post content")
        self.assertEqual(len(self.user.posts), 1)
        self.assertIsInstance(self.user.posts[0], Post)
        self.assertEqual(self.user.posts[0].content, "Test post content")
        self.assertEqual(self.user.posts[0].user, self.user)

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

if __name__ == '__main__':
    unittest.main()