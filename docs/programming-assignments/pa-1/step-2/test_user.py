import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")

    def test_init(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user._email, "test@example.com")
        self.assertEqual(self.user._bio, "")
        self.assertEqual(self.user._followers, [])
        self.assertEqual(self.user._following, [])

    def test_invalid_username(self):
        with self.assertRaises(ValueError):
            User("a", "test@example.com")
        with self.assertRaises(ValueError):
            User("a" * 31, "test@example.com")
        with self.assertRaises(ValueError):
            User("invalid@user", "test@example.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            User("validuser", "invalid_email")

    def test_follow(self):
        other_user = User("otheruser", "other@example.com")
        self.user.follow(other_user)
        self.assertIn(other_user, self.user._following)
        self.assertIn(self.user, other_user._followers)

    def test_unfollow(self):
        other_user = User("otheruser", "other@example.com")
        self.user.follow(other_user)
        self.user.unfollow(other_user)
        self.assertNotIn(other_user, self.user._following)
        self.assertNotIn(self.user, other_user._followers)

    def test_bio_property(self):
        self.user.bio = "Test bio"
        self.assertEqual(self.user.bio, "Test bio")

    def test_bio_setter_too_long(self):
        with self.assertRaises(ValueError):
            self.user.bio = "a" * 151

    def test_get_user_count(self):
        initial_count = User.get_user_count()
        User("newuser", "new@example.com")
        self.assertEqual(User.get_user_count(), initial_count + 1)

    def test_is_valid_username(self):
        self.assertTrue(User.is_valid_username("valid_user"))
        self.assertTrue(User.is_valid_username("valid.user"))
        self.assertFalse(User.is_valid_username("in"))
        self.assertFalse(User.is_valid_username("a" * 31))
        self.assertFalse(User.is_valid_username("invalid@user"))

    def test_is_valid_email(self):
        self.assertTrue(User.is_valid_email("test@example.com"))
        self.assertFalse(User.is_valid_email("invalid_email"))
        self.assertFalse(User.is_valid_email("test@example"))

if __name__ == '__main__':
    unittest.main()
