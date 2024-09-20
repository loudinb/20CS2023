import unittest
from datetime import datetime
from message import Message
from user import User

class TestMessage(unittest.TestCase):
    def setUp(self):
        self.sender = User("sender", "sender@example.com")
        self.recipient = User("recipient", "recipient@example.com")
        self.message = Message(self.sender, self.recipient, "Test message")

    def test_init(self):
        self.assertEqual(self.message.content, "Test message")
        self.assertIsInstance(self.message.timestamp, datetime)
        self.assertEqual(self.message.sender, self.sender)
        self.assertEqual(self.message.recipient, self.recipient)

    def test_content_too_long(self):
        with self.assertRaises(ValueError):
            Message(self.sender, self.recipient, "a" * 2001)

    def test_content_property(self):
        self.assertEqual(self.message.content, "Test message")

    def test_content_setter(self):
        self.message.content = "New message"
        self.assertEqual(self.message.content, "New message")

    def test_content_setter_too_long(self):
        with self.assertRaises(ValueError):
            self.message.content = "a" * 2001

if __name__ == '__main__':
    unittest.main()
