import unittest
from user import User
from post import Post
from comment import Comment

class TestComment(unittest.TestCase):
    def setUp(self):
        Comment.total_comments = 0  # Reset total_comments before each test
        self.user = User("testuser", "test@example.com")
        self.post = Post(self.user, "Test post content")
        self.comment = Comment(self.user, self.post, "Test comment content")

    def test_comment_initialization(self):
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.content, "Test comment content")
        self.assertEqual(self.comment.likes, 0)
        self.assertEqual(Comment.get_total_comments(), 1)

    def test_like(self):
        self.comment.like()
        self.assertEqual(self.comment.likes, 1)

    def test_get_total_comments(self):
        Comment(self.user, self.post, "Another comment")
        self.assertEqual(Comment.get_total_comments(), 2)

    def test_get_average_comments_per_post(self):
        Comment(self.user, self.post, "Second comment")
        Post(self.user, "Another post")  # Post without comments
        avg_comments = Comment.get_average_comments_per_post()
        self.assertEqual(avg_comments, 1.0)  # 2 comments / 2 posts = 1.0

    def test_format_content(self):
        formatted_content = Comment.format_content("  this is a test comment  ")
        self.assertEqual(formatted_content, "This is a test comment")

    def test_display(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.comment.display()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Comment by testuser: Test comment content", output)
        self.assertIn("Likes: 0", output)

if __name__ == '__main__':
    unittest.main()
