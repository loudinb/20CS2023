import unittest
from comment import Comment
from user import User
from post import Post

class TestComment(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.post = Post(self.user, "Test post content")

    def test_format_content(self):
        formatted = Comment.format_content("  this is a comment  ")
        self.assertEqual(formatted, "This is a comment")

    def test_is_valid_content(self):
        self.assertTrue(Comment.is_valid_content("Valid comment"))
        self.assertFalse(Comment.is_valid_content(""))  # Empty comment
        self.assertFalse(Comment.is_valid_content("a" * 201))  # Too long

    def test_generate_comment_preview(self):
        long_comment = "This is a very long comment that should be previewed"
        preview = Comment.generate_comment_preview(long_comment, 20)
        self.assertEqual(len(preview), 23)  # 20 chars + 3 for ellipsis
        self.assertTrue(preview.endswith("..."))

    def test_comment_creation_with_invalid_content(self):
        with self.assertRaises(ValueError):
            Comment(self.user, self.post, "")

    def test_comment_display(self):
        comment = Comment(self.user, self.post, "Test comment")
        display = comment.display()
        self.assertIn("testuser commented: Test comment", display)
        self.assertIn("(", display)  # Check for timestamp

if __name__ == '__main__':
    unittest.main()
