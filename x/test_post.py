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
        self.assertEqual(post.tags, set())
        self.assertEqual(Post.post_count, 1)

    def test_init_with_tags(self):
        content = "Post with tags"
        tags = set(["tag1", "tag2"])
        post = Post(content, tags)
        self.assertEqual(post.tags, tags)

    def test_init_invalid(self):
        content = "a" * 2201
        with self.assertRaises(ValueError):
            Post(content)

    def test_init_valid_boundary(self):
        content = "a" * 2200  # Exactly 2200 characters
        post = Post(content)
        self.assertEqual(post.content, content)

    def test_content_property(self):
        content = "Test content"
        post = Post(content)
        self.assertEqual(post.content, content)

    def test_add_tag_valid(self):
        post = Post("Test post")
        post.add_tag("validtag")
        self.assertIn("validtag", post.tags)

    def test_add_tag_invalid(self):
        post = Post("Test post")
        with self.assertRaises(ValueError):
            post.add_tag("invalid tag with spaces")

    def test_remove_tag(self):
        post = Post("Test post", set(["tag1", "tag2"]))
        post.remove_tag("tag1")
        self.assertNotIn("tag1", post.tags)
        self.assertIn("tag2", post.tags)

    def test_remove_nonexistent_tag(self):
        post = Post("Test post", set(["tag1"]))
        post.remove_tag("tag2")  # Should not raise an error
        self.assertEqual(post.tags, set(["tag1"]))

    def test_remove_tag_multiple_times(self):
        post = Post("Test post", set(["tag1"]))
        post.remove_tag("tag2")  # Remove a tag that doesn't exist
        post.remove_tag("tag2")  # Remove it again, should still not raise any errors
        self.assertEqual(post.tags, set(["tag1"]))

    def test_get_post_count(self):
        Post("Post 1")
        Post("Post 2")
        self.assertEqual(Post.get_post_count(), 2)

    def test_is_valid_tag(self):
        self.assertTrue(Post.is_valid_tag("validtag"))
        self.assertFalse(Post.is_valid_tag("invalid tag"))
        self.assertFalse(Post.is_valid_tag("a" * 31))

    def test_is_valid_tag_boundary(self):
        self.assertTrue(Post.is_valid_tag("a" * 30))  # Exactly 30 characters

    def test_empty_content(self):
        with self.assertRaises(ValueError):
            Post("")  # Empty content should raise an error

    def test_content_too_short(self):
        with self.assertRaises(ValueError):
            Post("ab")  # Content with fewer than 3 characters

    def test_content_valid_min_length(self):
        content = "abc"  # Exactly 3 characters
        post = Post(content)
        self.assertEqual(post.content, content)

if __name__ == '__main__':
    unittest.main()
