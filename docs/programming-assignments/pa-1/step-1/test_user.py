import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        User.user_count = 0

    def test_init_valid(self):
        user = User("validuser", "valid@email.com")
        self.assertEqual(user.username, "validuser")
        self.assertEqual(user._email, "valid@email.com")
        self.assertEqual(user.bio, "")
        self.assertEqual(User.user_count, 1)

    def test_init_invalid_username(self):
        with self.assertRaises(ValueError):
            User("in", "valid@email.com")  # Too short
        with self.assertRaises(ValueError):
            User("invalid username", "valid@email.com")  # Contains space

    def test_init_invalid_email(self):
        with self.assertRaises(ValueError):
            User("validuser", "invalid-email")

    def test_bio_property(self):
        user = User("testuser", "test@email.com")
        self.assertEqual(user.bio, "")

    def test_bio_setter_valid(self):
        user = User("testuser", "test@email.com")
        user.bio = "This is a valid bio"
        self.assertEqual(user.bio, "This is a valid bio")

    def test_bio_setter_invalid(self):
        user = User("testuser", "test@email.com")
        with self.assertRaises(ValueError):
            user.bio = "a" * 151  # Too long

    def test_get_user_count(self):
        User("user1", "user1@email.com")
        User("user2", "user2@email.com")
        self.assertEqual(User.get_user_count(), 2)

    def test_is_valid_username(self):
        self.assertTrue(User.is_valid_username("valid_user"))
        self.assertTrue(User.is_valid_username("valid.user"))
        self.assertFalse(User.is_valid_username("in"))  # Too short
        self.assertFalse(User.is_valid_username("invalid username"))  # Contains space
        self.assertFalse(User.is_valid_username("a" * 31))  # Too long

    def test_is_valid_email(self):
        self.assertTrue(User.is_valid_email("valid@email.com"))
        self.assertTrue(User.is_valid_email("valid.user+tag@email.co.uk"))
        self.assertFalse(User.is_valid_email("invalid-email"))
        self.assertFalse(User.is_valid_email("invalid@email"))

if __name__ == '__main__':
    unittest.main()
