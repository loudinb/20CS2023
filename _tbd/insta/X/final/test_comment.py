import unittest
from comment import Comment
from user import User

class TestComment(unittest.TestCase):

    def setUp(self):
        self.user1 = User("user1", "user1@example.com")
        self.comment = Comment(self.user1, "This is a comment.")

    def test_comment_initialization(self):
        self.assertEqual(self.comment.content, "This is a comment.")
        self.assertEqual(self.comment.author, self.user1)

    def test_content_setter(self):
        self.comment.content = "Updated comment"
        self.assertEqual(self.comment.content, "Updated comment")
        with self.assertRaises(ValueError):
            self.comment.content = "x" * 2201  # Exceeding 2200 characters

if __name__ == "__main__":
    unittest.main()
