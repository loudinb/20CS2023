import unittest
from user import User

class TestUser(unittest.TestCase):
    def test_is_valid_username(self):
        self.assertTrue(User.is_valid_username("john_doe"))
        self.assertFalse(User.is_valid_username("jo"))  # Too short
        self.assertFalse(User.is_valid_username("john@doe"))  # Invalid character

    def test_generate_random_username(self):
        username = User.generate_random_username()
        self.assertTrue(username.startswith("user_"))
        self.assertEqual(len(username), 13)  # "user_" + 8 random characters

    def test_format_user_info(self):
        info = User.format_user_info("john_doe", "john@example.com")
        self.assertEqual(info, "User: john_doe (Email: john@example.com)")

    def test_user_creation_with_invalid_username(self):
        with self.assertRaises(ValueError):
            User("jo", "john@example.com")

    def test_user_creation_with_invalid_email(self):
        with self.assertRaises(ValueError):
            User("john_doe", "invalid_email")

if __name__ == '__main__':
    unittest.main()
