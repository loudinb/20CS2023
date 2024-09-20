import unittest
from message import Message
from user import User

class TestMessage(unittest.TestCase):
    def setUp(self):
        self.sender = User("sender", "sender@example.com")
        self.recipient = User("recipient", "recipient@example.com")
        self.message = Message(self.sender, self.recipient, "Test message")

    def test_init(self):
        self.assertEqual(self.message.content, "Test message")
        self.assertEqual(self.message.sender, self.sender)
        self.assertEqual(self.message.recipient, self.recipient)

    def test_invalid_content(self):
        with self.assertRaises(ValueError):
            Message(self.sender, self.recipient, "a" * 2001)

    def test_content_property(self):
        self.message.content = "New content"
        self.assertEqual(self.message.content, "New content")
        with self.assertRaises(ValueError):
            self.message.content = "a" * 2001

if __name__ == '__main__':
    unittest.main()
