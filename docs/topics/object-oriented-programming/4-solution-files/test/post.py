import unittest
from user import User
from post import Post

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.post = Post(self.user, "Test post content")

    def test_post_initialization(self):
        self.assertEqual(self.post.user, self.user)
        self.assertEqual(self.post.content, "Test post content")
        self.assertEqual(self.post.likes_count, 0)
        self.assertEqual(len(self.post.comments), 0)

    def test_toggle_like(self):
        self.assertTrue(self.post.toggle_like())
        self.assertEqual(self.post.likes_count, 1)
        self.assertFalse(self.post.toggle_like())
        self.assertEqual(self.post.likes_count, 0)

    def test_add_comment(self):
        commenter = User("commenter", "commenter@example.com")
        comment = self.post.add_comment(commenter, "Test comment")
        self.assertEqual(len(self.post.comments), 1)
        self.assertEqual(comment.user, commenter)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.content, "Test comment")

    def test_display(self):
        import io
        import sys
        commenter = User("commenter", "commenter@example.com")
        self.post.add_comment(commenter, "Test comment")
        self.post.toggle_like()
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.post.display()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Content: Test post content", output)
        self.assertIn("Posted by: testuser", output)
        self.assertIn("Likes: 1", output)
        self.assertIn("Number of comments: 1", output)
        self.assertIn("Comment by commenter: Test comment", output)

if __name__ == '__main__':
    unittest.main()
