import unittest
from post import Post
from user import User
from comment import Comment

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.post = Post("Test content", self.user, ["tag1", "tag2"])

    def test_init(self):
        self.assertEqual(self.post.content, "Test content")
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post._tags, ["tag1", "tag2"])
        self.assertEqual(self.post._likes, [])
        self.assertEqual(self.post._comments, [])

    def test_invalid_content(self):
        with self.assertRaises(ValueError):
            Post("a" * 2201, self.user)

    def test_add_remove_comment(self):
        self.post.add_comment(self.user, "Test comment")
        self.assertEqual(len(self.post._comments), 1)
        self.assertIsInstance(self.post._comments[0], Comment)
        self.post.remove_comment(self.post._comments[0])
        self.assertEqual(len(self.post._comments), 0)

    def test_content_property(self):
        self.post.content = "New content"
        self.assertEqual(self.post.content, "New content")
        with self.assertRaises(ValueError):
            self.post.content = "a" * 2201

    def test_add_remove_tag(self):
        self.post.add_tag("newtag")
        self.assertIn("newtag", self.post._tags)
        self.post.remove_tag("newtag")
        self.assertNotIn("newtag", self.post._tags)

    def test_invalid_tag(self):
        with self.assertRaises(ValueError):
            self.post.add_tag("a" * 31)

    def test_add_remove_like(self):
        new_user = User("newuser", "new@example.com")
        self.post.add_like(new_user)
        self.assertIn(new_user, self.post._likes)
        self.post.remove_like(new_user)
        self.assertNotIn(new_user, self.post._likes)

    def test_get_post_count(self):
        initial_count = Post.get_post_count()
        Post("New post", self.user)
        self.assertEqual(Post.get_post_count(), initial_count + 1)

    def test_is_valid_tag(self):
        self.assertTrue(Post.is_valid_tag("validtag"))
        self.assertFalse(Post.is_valid_tag("a" * 31))
        self.assertFalse(Post.is_valid_tag("invalid tag"))

if __name__ == '__main__':
    unittest.main()
