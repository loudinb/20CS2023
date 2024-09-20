import unittest
from datetime import datetime
from post import Post
from user import User

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.post = Post("Test content", self.user, ["tag1", "tag2"])

    def test_init(self):
        self.assertEqual(self.post.content, "Test content")
        self.assertIsInstance(self.post.timestamp, datetime)
        self.assertEqual(self.post._tags, ["tag1", "tag2"])
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post._likes, [])

    def test_content_too_long(self):
        with self.assertRaises(ValueError):
            Post("a" * 2201, self.user)

    def test_content_property(self):
        self.assertEqual(self.post.content, "Test content")

    def test_content_setter(self):
        self.post.content = "New content"
        self.assertEqual(self.post.content, "New content")

    def test_content_setter_too_long(self):
        with self.assertRaises(ValueError):
            self.post.content = "a" * 2201

    def test_add_tag(self):
        self.post.add_tag("newtag")
        self.assertIn("newtag", self.post._tags)

    def test_add_invalid_tag(self):
        with self.assertRaises(ValueError):
            self.post.add_tag("invalid@tag")

    def test_remove_tag(self):
        self.post.remove_tag("tag1")
        self.assertNotIn("tag1", self.post._tags)

    def test_add_like(self):
        new_user = User("newuser", "new@example.com")
        self.post.add_like(new_user)
        self.assertIn(new_user, self.post._likes)

    def test_remove_like(self):
        new_user = User("newuser", "new@example.com")
        self.post.add_like(new_user)
        self.post.remove_like(new_user)
        self.assertNotIn(new_user, self.post._likes)

    def test_get_post_count(self):
        initial_count = Post.get_post_count()
        Post("New post", self.user)
        self.assertEqual(Post.get_post_count(), initial_count + 1)

    def test_is_valid_tag(self):
        self.assertTrue(Post.is_valid_tag("validtag"))
        self.assertFalse(Post.is_valid_tag("invalid tag"))
        self.assertFalse(Post.is_valid_tag("a" * 31))

if __name__ == '__main__':
    unittest.main()
