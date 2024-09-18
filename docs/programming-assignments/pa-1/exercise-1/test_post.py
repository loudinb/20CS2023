import unittest
from datetime import datetime
from user import User
from post import Post

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.post = Post(self.user, "Test post content")

    def test_post_initialization(self):
        self.assertEqual(self.post.user, self.user)
        self.assertEqual(self.post.content, "Test post content")
        self.assertIsInstance(self.post.timestamp, datetime)
        self.assertEqual(self.post.likes, 0)

    def test_display(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.post.display()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Content: Test post content", output)
        self.assertIn("Posted by: testuser", output)
        self.assertIn("Posted on:", output)
        self.assertIn("Likes: 0", output)

if __name__ == '__main__':
    unittest.main()