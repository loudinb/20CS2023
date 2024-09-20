import unittest
from user import User
from post import Post

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.post = Post("Test content", self.user, ["tag1", "tag2"])

    def test_add_remove_comment(self):
        comment = self.post.add_comment(self.user, "Test comment")
        self.assertIn(comment, self.post.comments)
        
        removed = self.post.remove_comment(comment)
        self.assertTrue(removed)
        self.assertNotIn(comment, self.post.comments)

    def test_add_remove_like(self):
        self.post.add_like(self.user)
        self.assertIn(self.user, self.post.likes)

        self.post.remove_like(self.user)
        self.assertNotIn(self.user, self.post.likes)

    def test_add_remove_tag(self):
        self.post.add_tag("tag3")
        self.assertIn("tag3", self.post.tags)
        
        removed = self.post.remove_tag("tag3")
        self.assertTrue(removed)
        self.assertNotIn("tag3", self.post.tags)

    def test_content_property(self):
        self.post.content = "Updated content"
        self.assertEqual(self.post.content, "Updated content")
        with self.assertRaises(ValueError):
            self.post.content = "a" * (Post.CAPTION_LIMIT + 1)

    def test_post_count(self):
        initial_count = Post.get_post_count()
        Post("New post", self.user)
        self.assertEqual(Post.get_post_count(), initial_count + 1)

    def test_is_valid_tag(self):
        self.assertTrue(Post.is_valid_tag("validtag123"))
        self.assertFalse(Post.is_valid_tag("invalid tag"))
        self.assertFalse(Post.is_valid_tag("a" * 31))  # too long

if __name__ == '__main__':
    unittest.main()
