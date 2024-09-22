import unittest
from datetime import datetime
from comment import Comment

class TestComment(unittest.TestCase):

    def setUp(self):
        # This runs before each test to reset the comment count
        Comment.comment_count = 0

    def test_valid_comment_creation(self):
        # Test a valid comment with content and no tags
        comment = Comment("This is a valid comment")
        self.assertEqual(comment.content, "This is a valid comment")
        self.assertEqual(comment.tags, set())  # Empty tags set
        self.assertTrue(isinstance(comment.timestamp, datetime))  # Timestamp check
        self.assertEqual(Comment.get_comment_count(), 1)

    def test_comment_content_minimum_boundary(self):
        # Test valid comment content at the minimum length boundary (3 characters)
        comment = Comment("abc")
        self.assertEqual(comment.content, "abc")
    
    def test_comment_content_maximum_boundary(self):
        # Test valid comment content at the maximum length boundary (2200 characters)
        content = "a" * 2200
        comment = Comment(content)
        self.assertEqual(comment.content, content)

    def test_invalid_comment_content_too_short(self):
        # Test invalid comment content (less than 3 characters)
        with self.assertRaises(ValueError):
            Comment("ab")  # 2 characters

    def test_invalid_comment_content_too_long(self):
        # Test invalid comment content (more than 2200 characters)
        content = "a" * 2201
        with self.assertRaises(ValueError):
            Comment(content)

    def test_add_valid_tag(self):
        # Test adding valid tags to a comment
        comment = Comment("Test comment")
        comment.add_tag("python")
        self.assertIn("python", comment.tags)

    def test_add_invalid_tag(self):
        # Test adding an invalid tag (non-alphanumeric)
        comment = Comment("Test comment")
        with self.assertRaises(ValueError):
            comment.add_tag("!invalid@tag")  # Contains non-alphanumeric characters

    def test_add_tag_max_length_boundary(self):
        # Test adding a valid tag at the boundary (30 characters)
        tag = "a" * 30
        comment = Comment("Test comment")
        comment.add_tag(tag)
        self.assertIn(tag, comment.tags)

    def test_add_tag_exceeding_length(self):
        # Test adding a tag exceeding the 30-character limit
        tag = "a" * 31
        comment = Comment("Test comment")
        with self.assertRaises(ValueError):
            comment.add_tag(tag)

    def test_remove_existing_tag(self):
        # Test removing an existing tag
        comment = Comment("Test comment", tags=["python"])
        comment.remove_tag("python")
        self.assertNotIn("python", comment.tags)
    
    def test_remove_non_existent_tag(self):
        # Test removing a tag that doesn't exist (should not raise an error)
        comment = Comment("Test comment", tags=["python"])
        comment.remove_tag("java")  # Tag does not exist
        self.assertNotIn("java", comment.tags)

    def test_comment_count_increments(self):
        # Test that comment count increments as expected
        Comment("First comment")
        Comment("Second comment")
        self.assertEqual(Comment.get_comment_count(), 2)

    def test_liked_by_initially_empty(self):
        # Test that the liked_by list is empty upon initialization
        comment = Comment("This is a comment")
        self.assertEqual(comment._liked_by, [])

    def test_is_valid_tag(self):
        # Test static method for valid tag cases
        self.assertTrue(Comment.is_valid_tag("python"))
        self.assertFalse(Comment.is_valid_tag("invalid!"))  # Contains non-alphanumeric characters
        self.assertFalse(Comment.is_valid_tag("a" * 31))  # Exceeds 30 characters

    def test_is_valid_content(self):
        # Test static method for content validation
        self.assertTrue(Comment.is_valid_content("Valid content"))
        self.assertFalse(Comment.is_valid_content("ab"))  # Too short
        self.assertFalse(Comment.is_valid_content("a" * 2201))  # Exceeds the limit

if __name__ == "__main__":
    unittest.main()
