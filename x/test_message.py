import unittest
from datetime import datetime
from message import Message

class TestMessage(unittest.TestCase):
    def test_init_valid(self):
        content = "This is a valid message"
        message = Message(content)
        self.assertEqual(message.content, content)
        self.assertIsInstance(message.timestamp, datetime)

    def test_init_invalid(self):
        content = "a" * 2201  # Exceeds 2200 characters
        with self.assertRaises(ValueError):
            Message(content)

    def test_init_valid_boundary(self):
        content = "a" * 2200  # Exactly 2200 characters
        message = Message(content)
        self.assertEqual(message.content, content)

    def test_content_property(self):
        content = "Test content"
        message = Message(content)
        self.assertEqual(message.content, content)

    def test_timestamp(self):
        message = Message("This is a valid message")
        self.assertIsInstance(message.timestamp, datetime)

    def test_empty_message(self):
        content = ""
        message = Message(content)
        self.assertEqual(message.content, content)  # Empty content should be valid

if __name__ == '__main__':
    unittest.main()