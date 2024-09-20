import unittest
from user import User
from private_message import PrivateMessage

class TestPrivateMessage(unittest.TestCase):
    def setUp(self):
        self.sender = User("sender", "sender@example.com")
        self.recipient = User("recipient", "recipient@example.com")
        self.message = PrivateMessage(self.sender, self.recipient, "Test message content")

    def test_private_message_initialization(self):
        self.assertEqual(self.message.sender, self.sender)
        self.assertEqual(self.message.recipient, self.recipient)
        self.assertEqual(self.message.content, "Test message content")

    def test_get_total_message_count(self):
        initial_count = PrivateMessage.get_total_message_count()
        PrivateMessage(self.sender, self.recipient, "Another message")
        self.assertEqual(PrivateMessage.get_total_message_count(), initial_count+1)