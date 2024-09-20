import unittest
from datetime import datetime
from user import User
from post import Post

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.other_user = User("otheruser", "other@example.com")

    def test_user_initialization(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertIsInstance(self.user.join_date, datetime)
        self.assertEqual(len(self.user.posts), 0)
        self.assertEqual(len(self.user.liked_posts), 0)

    def test_create_post(self):
        post = self.user.create_post("Test post content")
        self.assertEqual(len(self.user.posts), 1)
        self.assertIsInstance(post, Post)
        self.assertEqual(post.content, "Test post content")
        self.assertEqual(post.user, self.user)

    def test_like_post(self):
        post = self.other_user.create_post("Other user's post")
        self.user.like_post(post)
        self.assertIn(post, self.user.liked_posts)
        self.assertEqual(post.likes, 1)

        # Test liking the same post again
        self.user.like_post(post)
        self.assertEqual(post.likes, 1)  # Likes should not increase

    def test_comment_on_post(self):
        post = self.other_user.create_post("Other user's post")
        comment = self.user.comment_on_post(post, "Test comment")
        self.assertIn(comment, post.comments)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.content, "Test comment")

    def test_display_info(self):
        import io
        import sys
        self.user.create_post("Test post")
        other_post = self.other_user.create_post("Other post")
        self.user.like_post(other_post)
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.user.display_info()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Username: testuser", output)
        self.assertIn("Email: test@example.com", output)
        self.assertIn("Joined on:", output)
        self.assertIn("Number of posts: 1", output)
        self.assertIn("Number of liked posts: 1", output)

    def test_get_activity_feed(self):
        self.user.create_post("Test post 1")
        other_post = self.other_user.create_post("Other user's post")
        self.user.like_post(other_post)
        self.user.comment_on_post(other_post, "Test comment")
        
        activity_feed = self.user.get_activity_feed()
        print(activity_feed)
        self.assertEqual(len(activity_feed), 2)
        print(activity_feed[1][0])
        self.assertIn("Post liked", activity_feed[0][0])
        self.assertIn("Post created", activity_feed[1][0])
        #self.assertIn("Comment made", activity_feed[0][0])

if __name__ == '__main__':
    unittest.main()
