import unittest
from user import User
from post import Post

class TestUser(unittest.TestCase):
    def setUp(self):
        User.total_users = 0  # Reset total_users before each test
        self.user = User("testuser", "test@example.com")

    def test_user_initialization(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.bio, "")
        self.assertEqual(User.get_user_count(), 1)

    def test_invalid_username(self):
        with self.assertRaises(ValueError):
            User("ab", "invalid@example.com")  # Too short
        with self.assertRaises(ValueError):
            User("user@name", "invalid@example.com")  # Contains invalid character

    def test_create_anonymous_user(self):
        anon_user = User.create_anonymous_user()
        self.assertTrue(anon_user.username.startswith("anonymous_"))
        self.assertTrue(anon_user.email.endswith("@example.com"))
        self.assertEqual(User.get_user_count(), 2)

    def test_email_setter(self):
        self.user.email = "newemail@example.com"
        self.assertEqual(self.user.email, "newemail@example.com")
        with self.assertRaises(ValueError):
            self.user.email = "invalid_email"

    def test_bio_setter(self):
        self.user.bio = "This is a test bio"
        self.assertEqual(self.user.bio, "This is a test bio")
        with self.assertRaises(ValueError):
            self.user.bio = "x" * 151

    def test_get_user_count(self):
        User("user2", "user2@example.com")
        User("user3", "user3@example.com")
        self.assertEqual(User.get_user_count(), 3)

    def test_is_valid_username(self):
        self.assertTrue(User.is_valid_username("validuser123"))
        self.assertFalse(User.is_valid_username("ab"))
        self.assertFalse(User.is_valid_username("invalid@user"))

    def test_create_post(self):
        post = self.user.create_post("Test post content")
        self.assertIsInstance(post, Post)
        self.assertEqual(post.content, "Test post content")
        self.assertEqual(post.user, self.user)

    def test_like_post(self):
        other_user = User("otheruser", "other@example.com")
        post = other_user.create_post("Other user's post")
        self.assertTrue(self.user.like_post(post))
        self.assertFalse(self.user.like_post(post))  # Trying to like again

if __name__ == '__main__':
    unittest.main()
