import unittest
from user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("testuser", "test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")

    def test_invalid_username(self):
        with self.assertRaises(ValueError):
            User("a", "test@example.com")  # Too short
        with self.assertRaises(ValueError):
            User("user@name", "test@example.com")  # Contains non-alphanumeric

    def test_invalid_email(self):
        user = User("testuser", "test@example.com")
        with self.assertRaises(ValueError):
            user.email = "invalid_email"

    def test_user_count(self):
        initial_count = User.get_user_count()
        User("user1", "user1@example.com")
        User("user2", "user2@example.com")
        self.assertEqual(User.get_user_count(), initial_count + 2)

    def test_anonymous_user(self):
        anon_user = User.create_anonymous_user()
        self.assertTrue(anon_user.username.startswith("anon_"))
        self.assertTrue(anon_user.email.endswith("@example.com"))

if __name__ == '__main__':
    unittest.main()
