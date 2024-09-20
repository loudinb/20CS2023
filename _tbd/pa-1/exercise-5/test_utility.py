import unittest
from utility import Utility
from datetime import datetime

class TestUtility(unittest.TestCase):
    def test_is_valid_email(self):
        self.assertTrue(Utility.is_valid_email("user@example.com"))
        self.assertFalse(Utility.is_valid_email("invalid_email"))

    def test_generate_random_string(self):
        random_string = Utility.generate_random_string(10)
        self.assertEqual(len(random_string), 10)
        self.assertTrue(random_string.isalnum())

    def test_format_timestamp(self):
        timestamp = datetime(2023, 1, 1, 12, 0, 0)
        formatted = Utility.format_timestamp(timestamp)
        self.assertEqual(formatted, "2023-01-01 12:00:00")

    def test_truncate_string(self):
        long_string = "This is a long string"
        truncated = Utility.truncate_string(long_string, 10)
        self.assertEqual(truncated, "This is a ...")

    def test_get_current_timestamp(self):
        timestamp = Utility.get_current_timestamp()
        self.assertIsInstance(timestamp, datetime)
        self.assertTrue((datetime.now() - timestamp).total_seconds() < 1)

if __name__ == '__main__':
    unittest.main()
