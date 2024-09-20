import unittest
from comment import Comment
from user import User
from post import Post

class TestComment(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.post = Post(self.user, "Test post")

    def test_create_comment(self):
        comment = Comment(self.user, self.post, "Test comment")
        self.assertEqual(comment._user, self.user)
        self.assertEqual(comment._post, self.post)
        self.assertEqual(comment._content, "Test comment")

    def test_format_content(self):
        formatted = Comment.format_content("  this   is   a   test   ")
        self.assertEqual(formatted, "This is a test")

    def test_like_comment(self):
        comment = Comment(self.user, self.post, "Test comment")
        initial_likes = comment._likes
        comment.like()
        self.assertEqual(comment._likes, initial_likes + 1)

    def test_get_average_comments_per_post(self):
        Comment(self.user, self.post, "Comment 1")
        Comment(self.user, self.post, "Comment 2")
        average = Comment.get_average_comments_per_post()
        self.assertEqual(average, 1.0)

if __name__ == '__main__':
    unittest.main()
