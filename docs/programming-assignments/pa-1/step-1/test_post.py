import unittest
from datetime import datetime
from post import Post

class TestPost(unittest.TestCase):

    def setUp(self):
        # Reset post count before each test
        Post.post_count = 0

    def test_valid_post_creation(self):
        # Test creating a valid post with content and no tags
        post = Post("This is a valid post")
        self.assertEqual(post.content, "This is a valid post")
        self.assertEqual(post.tags, set())  # No tags initially
        self.assertTrue(isinstance(post.timestamp, datetime))  # Timestamp check
        self.assertEqual(Post.get_post_count(), 1)  # Post count incremented

    def test_post_content_minimum_boundary(self):
        # Test valid post content at the minimum boundary (3 characters)
        post = Post("abc")
        self.assertEqual(post.content, "abc")

    def test_post_content_maximum_boundary(self):
        # Test valid post content at the maximum boundary (2200 characters)
        content = "a" * 2200
        post = Post(content)
        self.assertEqual(post.content, content)

    def test_invalid_post_content_too_short(self):
        # Test invalid post content (less than 3 characters)
        with self.assertRaises(ValueError):
            Post("ab")  # 2 characters

    def test_invalid_post_content_too_long(self):
        # Test invalid post content (more than 2200 characters)
        content = "a" * 2201
        with self.assertRaises(ValueError):
            Post(content)

    def test_add_valid_tag(self):
        # Test adding valid tags to a post
        post = Post("Test post")
        post.add_tag("python")
        self.assertIn("python", post.tags)

    def test_add_invalid_tag(self):
        # Test adding an invalid tag (non-alphanumeric)
        post = Post("Test post")
        with self.assertRaises(ValueError):
            post.add_tag("!invalid@tag")  # Contains non-alphanumeric characters

    def test_add_tag_max_length_boundary(self):
        # Test adding a valid tag with exactly 30 characters
        tag = "a" * 30
        post = Post("Test post")
        post.add_tag(tag)
        self.assertIn(tag, post.tags)

    def test_add_tag_exceeding_length(self):
        # Test adding a tag that exceeds 30 characters
        tag = "a" * 31
        post = Post("Test post")
        with self.assertRaises(ValueError):
            post.add_tag(tag)

    def test_remove_existing_tag(self):
        # Test removing an existing tag
        post = Post("Test post", tags=["python"])
        post.remove_tag("python")
        self.assertNotIn("python", post.tags)

    def test_remove_non_existent_tag(self):
        # Test removing a tag that doesn't exist (should not raise an error)
        post = Post("Test post", tags=["python"])
        post.remove_tag("java")  # Tag does not exist
        self.assertNotIn("java", post.tags)

    def test_post_count_increments(self):
        # Test that post count increments as expected
        Post("First post")
        Post("Second post")
        self.assertEqual(Post.get_post_count(), 2)

    def test_liked_by_initially_empty(self):
        # Test that the liked_by list is empty upon initialization
        post = Post("This is a post")
        self.assertEqual(post.liked_by, [])

    def test_is_valid_tag(self):
        # Test static method for valid tag cases
        self.assertTrue(Post.is_valid_tag("python"))
        self.assertFalse(Post.is_valid_tag("invalid!"))  # Contains non-alphanumeric characters
        self.assertFalse(Post.is_valid_tag("a" * 31))  # Exceeds 30 characters

    def test_is_valid_content(self):
        # Test static method for content validation
        self.assertTrue(Post.is_valid_content("Valid content"))
        self.assertFalse(Post.is_valid_content("ab"))  # Too short
        self.assertFalse(Post.is_valid_content("a" * 2201))  # Exceeds the limit

if __name__ == "__main__":
    unittest.main()
