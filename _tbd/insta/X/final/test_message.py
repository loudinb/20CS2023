import unittest
from message import Message
from user import User

class TestMessage(unittest.TestCase):

    def setUp(self):
        self.user1 = User("user1", "user1@example.com")
        self.user2 = User("user2", "user2@example.com")
        self.message = Message(self.user1, self.user2, "Hello, user2!")

    def test_message_initialization(self):
        self.assertEqual(self.message.content, "Hello, user2!")
        self.assertEqual(self.message.sender, self.user1)
        self.assertEqual(self.message.recipient, self.user2)

    def test_content_setter(self):
        self.message.content = "Updated message content"
        self.assertEqual(self.message.content, "Updated message content")
        with self.assertRaises(ValueError):
            self.message.content = "x" * 2001  # Exceeding 2000 characters

if __name__ == "__main__":
    unittest.main()
