
import unittest
from user import User
from post import Post

class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User("testuser", "test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")

    def test_invalid_username(self):
        with self.assertRaises(ValueError):
            User("a", "test@example.com")  # Too short
        with self.assertRaises(ValueError):
            User("a" * 21, "test@example.com")  # Too long
        with self.assertRaises(ValueError):
            User("invalid@user", "test@example.com")  # Contains invalid character

    def test_change_email(self):
        user = User("testuser", "test@example.com")
        user.email = "newemail@example.com"
        self.assertEqual(user.email, "newemail@example.com")
        with self.assertRaises(ValueError):
            user.email = "invalid_email"

    def test_create_post(self):
        user = User("testuser", "test@example.com")
        post = user.create_post("Test post content")
        self.assertIsInstance(post, Post)
        self.assertEqual(post._user, user)
        self.assertEqual(post._content, "Test post content")

    def test_get_user_count(self):
        initial_count = User.get_user_count()
        User("user1", "user1@example.com")
        User("user2", "user2@example.com")
        self.assertEqual(User.get_user_count(), initial_count + 2)

    def test_create_anonymous_user(self):
        anon_user = User.create_anonymous_user()
        self.assertTrue(anon_user.username.startswith("anon"))
        self.assertTrue(anon_user.email.endswith("@example.com"))

    def test_send_private_message(self):
        sender = User("sender", "sender@example.com")
        recipient = User("recipient", "recipient@example.com")
        message = sender.send_private_message(recipient, "Hello!")
        self.assertEqual(message.sender, sender)
        self.assertEqual(message.recipient, recipient)
        self.assertEqual(message.content, "Hello!")
        self.assertIn(message, recipient.view_private_messages())

if __name__ == '__main__':
    unittest.main()
