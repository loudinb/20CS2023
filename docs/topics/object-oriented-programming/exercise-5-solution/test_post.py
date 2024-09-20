import unittest
from post import Post
from user import User

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")

    def test_is_valid_content(self):
        self.assertTrue(Post.is_valid_content("Valid content"))
        self.assertFalse(Post.is_valid_content(""))  # Empty content
        self.assertFalse(Post.is_valid_content("a" * 281))  # Too long

    def test_extract_hashtags(self):
        content = "I love #python and #coding"
        hashtags = Post.extract_hashtags(content)
        self.assertEqual(hashtags, ["python", "coding"])

    def test_format_post(self):
        long_content = "This is a very long post content that should be truncated"
        formatted = Post.format_post(long_content)
        self.assertTrue(len(formatted) <= 53)  # 50 chars + 3 for ellipsis
        self.assertTrue(formatted.endswith("..."))

    def test_post_creation_with_invalid_content(self):
        with self.assertRaises(ValueError):
            Post(self.user, "")

if __name__ == '__main__':
    unittest.main()
