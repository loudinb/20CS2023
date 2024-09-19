import unittest
from user import User
from post import Post
from comment import Comment

class TestComment(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.post = Post(self.user, "Test post content")

    def test_comment_creation(self):
        comment = Comment(self.user, self.post, "Test comment")
        self.assertEqual(comment._content, "Test comment")
        self.assertEqual(comment._user, self.user)
        self.assertEqual(comment._post, self.post)

    def test_content_formatting(self):
        comment = Comment(self.user, self.post, "  test   comment  ")
        self.assertEqual(comment._content, "Test comment")

    def test_like_comment(self):
        comment = Comment(self.user, self.post, "Test comment")
        initial_likes = comment._likes
        comment.like()
        self.assertEqual(comment._likes, initial_likes + 1)

    def test_average_comments_per_post(self):
        initial_average = Comment.get_average_comments_per_post()
        Comment(self.user, self.post, "Comment 1")
        Comment(self.user, self.post, "Comment 2")
        new_average = Comment.get_average_comments_per_post()
        self.assertGreater(new_average, initial_average)

if __name__ == '__main__':
    unittest.main()
