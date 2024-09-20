import unittest
from user import User
from message import Message

class TestMessage(unittest.TestCase):
    def setUp(self):
        self.sender = User("sender", "sender@example.com")
        self.recipient = User("recipient", "recipient@example.com")
        self.message = Message(self.sender, self.recipient, "Test message")

    def test_message_creation(self):
        self.assertEqual(self.message.sender, self.sender)
        self.assertEqual(self.message.recipient, self.recipient)
        self.assertEqual(self.message.content, "Test message")
        self.assertIsNotNone(self.message.timestamp)

    def test_content_property(self):
        self.message.content = "Updated message"
        self.assertEqual(self.message.content, "Updated message")
        with self.assertRaises(ValueError):
            self.message.content = "a" * (Message.MESSAGE_LIMIT + 1)

    def test_message_count(self):
        initial_count = Message.get_message_count()
        Message(self.sender, self.recipient, "New message")
        self.assertEqual(Message.get_message_count(), initial_count + 1)

    def test_is_valid_content(self):
        self.assertTrue(Message.is_valid_content("Valid message"))
        self.assertFalse(Message.is_valid_content(""))  # empty message
        self.assertFalse(Message.is_valid_content("a" * (Message.MESSAGE_LIMIT + 1)))  # too long

if __name__ == '__main__':
    unittest.main()
