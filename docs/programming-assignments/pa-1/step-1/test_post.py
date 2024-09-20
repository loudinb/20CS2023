import unittest
from datetime import datetime
from post import Post

class TestPost(unittest.TestCase):
    def setUp(self):
        Post.post_count = 0

    def test_init_valid(self):
        content = "This is a valid post"
        post = Post(content)
        self.assertEqual(post.content, content)
        self.assertIsInstance(post.timestamp, datetime)
        self.assertEqual(post._tags, [])
        self.assertEqual(Post.post_count, 1)

    def test_init_with_tags(self):
        content = "Post with tags"
        tags = ["tag1", "tag2"]
        post = Post(content, tags)
        self.assertEqual(post._tags, tags)

    def test_init_invalid(self):
        content = "a" * 2201
        with self.assertRaises(ValueError):
            Post(content)

    def test_content_property(self):
        content = "Test content"
        post = Post(content)
        self.assertEqual(post.content, content)

    def test_content_setter_valid(self):
        post = Post("Initial content")
        new_content = "Updated content"
        post.content = new_content
        self.assertEqual(post.content, new_content)

    def test_content_setter_invalid(self):
        post = Post("Initial content")
        with self.assertRaises(ValueError):
            post.content = "a" * 2201

    def test_add_tag_valid(self):
        post = Post("Test post")
        post.add_tag("validtag")
        self.assertIn("validtag", post._tags)

    def test_add_tag_invalid(self):
        post = Post("Test post")
        with self.assertRaises(ValueError):
            post.add_tag("invalid tag with spaces")

    def test_remove_tag(self):
        post = Post("Test post", ["tag1", "tag2"])
        post.remove_tag("tag1")
        self.assertNotIn("tag1", post._tags)
        self.assertIn("tag2", post._tags)

    def test_remove_nonexistent_tag(self):
        post = Post("Test post", ["tag1"])
        post.remove_tag("tag2")  # Should not raise an error
        self.assertEqual(post._tags, ["tag1"])

    def test_get_post_count(self):
        Post("Post 1")
        Post("Post 2")
        self.assertEqual(Post.get_post_count(), 2)

    def test_is_valid_tag(self):
        self.assertTrue(Post.is_valid_tag("validtag"))
        self.assertFalse(Post.is_valid_tag("invalid tag"))
        self.assertFalse(Post.is_valid_tag("a" * 31))

if __name__ == '__main__':
    unittest.main()
