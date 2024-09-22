import unittest
from datetime import datetime
from message import Message

class TestMessage(unittest.TestCase):

    def setUp(self):
        # Reset the message count before every test
        Message.message_count = 0

    def test_valid_message_creation(self):
        # Test creating a valid message
        message = Message("Hello!", "Alice", "Bob")
        self.assertEqual(message.content, "Hello!")
        self.assertEqual(message.sender, "Alice")
        self.assertEqual(message.recipient, "Bob")
        self.assertEqual(Message.get_message_count(), 1)
        self.assertTrue(isinstance(message.timestamp, datetime))

    def test_message_content_min_boundary(self):
        # Test message content at the minimum boundary (1 character)
        message = Message("a", "Alice", "Bob")
        self.assertEqual(message.content, "a")

    def test_message_content_max_boundary(self):
        # Test message content at the maximum boundary (2200 characters)
        content = "a" * 2200
        message = Message(content, "Alice", "Bob")
        self.assertEqual(message.content, content)

    def test_message_content_too_short(self):
        # Test that content shorter than 1 character raises a ValueError
        with self.assertRaises(ValueError):
            Message("", "Alice", "Bob")  # Empty content

    def test_message_content_too_long(self):
        # Test that content longer than 2200 characters raises a ValueError
        content = "a" * 2201
        with self.assertRaises(ValueError):
            Message(content, "Alice", "Bob")

    def test_message_sender(self):
        # Test that the sender is correctly set
        message = Message("Hi there!", "Alice", "Bob")
        self.assertEqual(message.sender, "Alice")

    def test_message_recipient(self):
        # Test that the recipient is correctly set
        message = Message("Hi there!", "Alice", "Bob")
        self.assertEqual(message.recipient, "Bob")

    def test_message_count_increment(self):
        # Test that message count increments correctly
        Message("First message", "Alice", "Bob")
        Message("Second message", "Charlie", "Dana")
        self.assertEqual(Message.get_message_count(), 2)

    def test_is_valid_content(self):
        # Test static method is_valid_content for various cases
        self.assertTrue(Message.is_valid_content("Valid content"))
        self.assertFalse(Message.is_valid_content(""))  # Too short
        self.assertFalse(Message.is_valid_content("a" * 2201))  # Too long

    def test_message_timestamp(self):
        # Test that the message's timestamp is close to the current time
        before = datetime.now()
        message = Message("Test message", "Alice", "Bob")
        after = datetime.now()
        self.assertTrue(before <= message.timestamp <= after)

if __name__ == "__main__":
    unittest.main()
