import unittest
from datetime import datetime
from user import User
from post import Post
from comment import Comment

class TestComment(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.post = Post(self.user, "Test post content")
        self.comment = Comment(self.user, self.post, "Test comment content")

    def test_comment_initialization(self):
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.content, "Test comment content")
        self.assertIsInstance(self.comment.timestamp, datetime)
        self.assertEqual(self.comment.likes, 0)

    def test_like(self):
        self.comment.like()
        self.assertEqual(self.comment.likes, 1)

    def test_display(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.comment.display()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Comment by testuser: Test comment content", output)
        self.assertIn("Posted on:", output)
        self.assertIn("Likes: 0", output)

if __name__ == '__main__':
    unittest.main()
