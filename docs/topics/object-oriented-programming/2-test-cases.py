import unittest
from datetime import datetime
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertIsInstance(self.user.join_date, datetime)

    def test_display_info(self):
        # Capture the printed output
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.user.display_info()
        sys.stdout = sys.__stdout__
        
        # Check if the output contains the expected information
        output = captured_output.getvalue()
        self.assertIn("Username: testuser", output)
        self.assertIn("Email: test@example.com", output)
        self.assertIn("Joined on:", output)

    def test_bio(self):
        self.user = User("testuser", "test@example.com", "This is a bio")
        self.assertEqual(self.user.bio, "This is a bio")

    def test_default_bio(self):
        self.assertEqual(self.user.bio, "")

if __name__ == '__main__':
    unittest.main()