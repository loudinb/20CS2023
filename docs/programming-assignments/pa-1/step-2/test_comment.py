import unittest
from datetime import datetime
from comment import Comment
from user import User

class TestComment(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.comment = Comment(self.user, "Test comment")

    def test_init(self):
        self.assertEqual(self.comment.content, "Test comment")
        self.assertIsInstance(self.comment.timestamp, datetime)
        self.assertEqual(self.comment.author, self.user)

    def test_content_too_long(self):
        with self.assertRaises(ValueError):
            Comment(self.user, "a" * 2201)

    def test_content_property(self):
        self.assertEqual(self.comment.content, "Test comment")

    def test_content_setter(self):
        self.comment.content = "New comment"
        self.assertEqual(self.comment.content, "New comment")

    def test_content_setter_too_long(self):
        with self.assertRaises(ValueError):
            self.comment.content = "a" * 2201

if __name__ == '__main__':
    unittest.main()
