import unittest
from datetime import datetime
from comment import Comment

class TestComment(unittest.TestCase):
    def test_init_valid(self):
        content = "This is a valid comment"
        comment = Comment(content)
        self.assertEqual(comment.content, content)
        self.assertIsInstance(comment.timestamp, datetime)

    def test_init_invalid(self):
        content = "a" * 2201
        with self.assertRaises(ValueError):
            Comment(content)

    def test_content_property(self):
        content = "Test content"
        comment = Comment(content)
        self.assertEqual(comment.content, content)

    def test_content_setter_valid(self):
        comment = Comment("Initial content")
        new_content = "Updated content"
        comment.content = new_content
        self.assertEqual(comment.content, new_content)

    def test_content_setter_invalid(self):
        comment = Comment("Initial content")
        with self.assertRaises(ValueError):
            comment.content = "a" * 2201

if __name__ == '__main__':
    unittest.main()
