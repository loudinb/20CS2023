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
        content = "a" * 2201  # Now, only > 2200 characters is invalid
        with self.assertRaises(ValueError):
            Comment(content)

    def test_init_valid_boundary(self):
        content = "a" * 2200  # Exactly 2200 characters is now valid
        comment = Comment(content)
        self.assertEqual(comment.content, content)

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
            comment.content = "a" * 2201  # Now, only > 2200 characters is invalid

    def test_add_tag_valid(self):
        comment = Comment("Test comment")
        comment.add_tag("validtag")
        self.assertIn("validtag", comment.tags)

    def test_add_tag_valid_boundary(self):
        comment = Comment("Test comment")
        tag = "a" * 30  # Exactly 30 characters is valid
        comment.add_tag(tag)
        self.assertIn(tag, comment.tags)

    def test_add_tag_invalid(self):
        comment = Comment("Test comment")
        with self.assertRaises(ValueError):
            comment.add_tag("invalid tag!")  # Contains spaces and non-alphanumeric characters

    def test_add_tag_too_long(self):
        comment = Comment("Test comment")
        with self.assertRaises(ValueError):
            comment.add_tag("a" * 31)  # Exceeds 30 characters

    def test_remove_tag(self):
        comment = Comment("Test comment")
        comment.add_tag("tag1")
        comment.add_tag("tag2")
        comment.remove_tag("tag1")
        self.assertNotIn("tag1", comment.tags)
        self.assertIn("tag2", comment.tags)

    def test_remove_nonexistent_tag(self):
        comment = Comment("Test comment")
        comment.add_tag("tag1")
        comment.remove_tag("nonexistent")  # Should not raise an error
        self.assertIn("tag1", comment.tags)

if __name__ == '__main__':
    unittest.main()
