import unittest
from user import User
from post import Post

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")

    def test_post_creation(self):
        post = Post(self.user, "Test content")
        self.assertEqual(post._content, "Test content")
        self.assertEqual(post._user, self.user)

    def test_invalid_content(self):
        with self.assertRaises(ValueError):
            Post(self.user, "")  # Empty content
        with self.assertRaises(ValueError):
            Post(self.user, "a" * 281)  # Content too long

    def test_like_post(self):
        post = Post(self.user, "Test content")
        another_user = User("another", "another@example.com")
        post.toggle_like(another_user)
        self.assertEqual(post.likes_count, 1)
        post.toggle_like(another_user)  # Unlike
        self.assertEqual(post.likes_count, 0)

    def test_post_count(self):
        initial_count = Post.get_post_count()
        Post(self.user, "Post 1")
        Post(self.user, "Post 2")
        self.assertEqual(Post.get_post_count(), initial_count + 2)

    def test_shared_post(self):
        original_post = Post(self.user, "Original content")
        shared_post = Post.create_shared_post(self.user, original_post)
        self.assertTrue(shared_post._content.startswith("Shared: "))

if __name__ == '__main__':
    unittest.main()
