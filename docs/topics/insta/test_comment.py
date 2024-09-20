import unittest
from user import User
from comment import Comment

class TestComment(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.comment = Comment(self.user, "Test comment")

    def test_comment_creation(self):
        self.assertEqual(self.comment.author, self.user)
        self.assertEqual(self.comment.content, "Test comment")
        self.assertIsNotNone(self.comment.timestamp)

    def test_content_property(self):
        self.comment.content = "Updated comment"
        self.assertEqual(self.comment.content, "Updated comment")
        with self.assertRaises(ValueError):
            self.comment.content = "a" * (Comment.COMMENT_LIMIT + 1)

    def test_is_valid_content(self):
        self.assertTrue(Comment.is_valid_content("Valid comment"))
        self.assertFalse(Comment.is_valid_content(""))  # empty comment
        self.assertFalse(Comment.is_valid_content("a" * (Comment.COMMENT_LIMIT + 1)))  # too long

if __name__ == '__main__':
    unittest.main()
