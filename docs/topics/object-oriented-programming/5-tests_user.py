import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        User.user_count = 0  # Reset user count before each test

    def test_class_attributes(self):
        self.assertEqual(User.user_count, 0)
        self.assertEqual(User.min_username_length, 3)

    def test_user_count_increment(self):
        user1 = User("user1", "user1@example.com")
        self.assertEqual(User.user_count, 1)
        user2 = User("user2", "user2@example.com")
        self.assertEqual(User.user_count, 2)

    def test_username_length_validation(self):
        with self.assertRaises(ValueError):
            User("ab", "short@example.com")

    def test_display_user_count(self):
        User("user1", "user1@example.com")
        User("user2", "user2@example.com")
        
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        User.display_user_count()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("Total number of users: 2", output)

    def test_create_from_string(self):
        user = User.create_from_string("testuser,test@example.com,Test bio")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.bio, "Test bio")

    def test_is_valid_email(self):
        self.assertTrue(User.is_valid_email("test@example.com"))
        self.assertFalse(User.is_valid_email("invalid_email"))

    def test_display_info_with_user_count(self):
        user = User("testuser", "test@example.com")
        
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        user.display_info()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("Total users: 1", output)

    def test_set_max_bio_length(self):
        original_length = User.max_bio_length
        User.set_max_bio_length(100)
        self.assertEqual(User.max_bio_length, 100)
        User.set_max_bio_length(original_length)  # Reset to original value

    def test_bio_length_enforcement(self):
        User.set_max_bio_length(10)
        user = User("testuser", "test@example.com", "This bio is too long")
        self.assertEqual(len(user.bio), 10)
        User.set_max_bio_length(150)  # Reset to original value

    def test_truncate_bio(self):
        long_bio = "a" * 200
        truncated_bio = User.truncate_bio(long_bio)
        self.assertEqual(len(truncated_bio), User.max_bio_length)

if __name__ == '__main__':
    unittest.main()