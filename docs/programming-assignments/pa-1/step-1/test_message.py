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
        content = "a" * 2001
        with self.assertRaises(ValueError):
            Message(content)

    def test_content_property(self):
        content = "Test content"
        message = Message(content)
        self.assertEqual(message.content, content)

    def test_content_setter_valid(self):
        message = Message("Initial content")
        new_content = "Updated content"
        message.content = new_content
        self.assertEqual(message.content, new_content)

    def test_content_setter_invalid(self):
        message = Message("Initial content")
        with self.assertRaises(ValueError):
            message.content = "a" * 2001

if __name__ == '__main__':
    unittest.main()
