import unittest
from user import User
from post import Post

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        self.other_user = User("otheruser", "other@example.com")

    def test_user_initialization(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.bio, "")

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

    def test_create_post(self):
        post = self.user.create_post("Test post content")
        self.assertIsInstance(post, Post)
        self.assertEqual(post.content, "Test post content")
        self.assertEqual(post.user, self.user)

    def test_like_post(self):
        post = self.other_user.create_post("Other user's post")
        self.assertTrue(self.user.like_post(post))
        self.assertFalse(self.user.like_post(post))  # Trying to like again

    def test_send_private_message(self):
        message = self.user.send_private_message(self.other_user, "Test message")
        self.assertEqual(message.sender, self.user)
        self.assertEqual(message.recipient, self.other_user)
        self.assertEqual(message.content, "Test message")

    def test_view_private_messages(self):
        self.user.send_private_message(self.other_user, "Test message 1")
        self.other_user.send_private_message(self.user, "Test message 2")
        messages = self.user.view_private_messages()
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].content, "Test message 2")

if __name__ == '__main__':
    unittest.main()
