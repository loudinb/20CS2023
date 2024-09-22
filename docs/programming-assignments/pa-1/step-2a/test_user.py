import unittest
from datetime import datetime
from user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        """Set up basic users for testing"""
        self.user1 = User(username="valid_user", email="user@example.com")
        self.user2 = User(username="another_user", email="another@example.com")
    
    def test_valid_user_creation(self):
        """Test user creation with valid inputs"""
        self.assertEqual(self.user1.username, "valid_user")
        self.assertEqual(self.user1.email, "user@example.com")
        self.assertEqual(self.user1.bio, "")
        self.assertTrue(isinstance(self.user1.joined_on, datetime))
        self.assertEqual(len(self.user1.posts), 0)
        self.assertEqual(len(self.user1.following), 0)
        self.assertEqual(len(self.user1.followers), 0)

    def test_invalid_username(self):
        """Test creation with invalid usernames"""
        with self.assertRaises(ValueError):
            User(username="x", email="test@example.com")  # too short
        with self.assertRaises(ValueError):
            User(username="a"*31, email="test@example.com")  # too long
        with self.assertRaises(ValueError):
            User(username="invalid@", email="test@example.com")  # invalid character
    
    def test_invalid_email(self):
        """Test creation with invalid emails"""
        with self.assertRaises(ValueError):
            User(username="validuser", email="invalid-email")  # no domain
        with self.assertRaises(ValueError):
            User(username="validuser", email="invalid@com")  # incomplete domain
    
    def test_bio_setter(self):
        """Test bio setter with valid and invalid bios"""
        self.user1.bio = "This is a valid bio."
        self.assertEqual(self.user1.bio, "This is a valid bio.")
        
        # Bio with exactly 150 characters
        valid_bio = "x" * 150
        self.user1.bio = valid_bio
        self.assertEqual(self.user1.bio, valid_bio)
        
        # Bio too long
        with self.assertRaises(ValueError):
            self.user1.bio = "x" * 151
    
    def test_follow_unfollow(self):
        """Test following and unfollowing another user"""
        self.user1.follow(self.user2)
        self.assertIn(self.user2, self.user1.following)
        self.assertIn(self.user1, self.user2.followers)

        self.user1.unfollow(self.user2)
        self.assertNotIn(self.user2, self.user1.following)
        self.assertNotIn(self.user1, self.user2.followers)
    
    def test_follow_edge_cases(self):
        """Test following and unfollowing edge cases"""
        # Following the same user multiple times
        self.user1.follow(self.user2)
        self.user1.follow(self.user2)  # Should not duplicate
        self.assertEqual(len(self.user1.following), 1)

        # Unfollowing without being followed
        self.user1.unfollow(self.user2)  # Should not raise an error
    
    def test_is_valid_username(self):
        """Test static method for valid usernames"""
        self.assertTrue(User.is_valid_username("valid_name"))
        self.assertFalse(User.is_valid_username("x"))  # too short
        self.assertFalse(User.is_valid_username("a"*31))  # too long
        self.assertFalse(User.is_valid_username("invalid@"))  # invalid char
    
    def test_is_valid_email(self):
        """Test static method for valid emails"""
        self.assertTrue(User.is_valid_email("valid@example.com"))
        self.assertFalse(User.is_valid_email("invalid-email"))
        self.assertFalse(User.is_valid_email("invalid@com"))
    
    def test_user_count(self):
        """Test that user count increments correctly"""
        initial_count = User.get_user_count()
        User(username="newuser", email="new@example.com")
        self.assertEqual(User.get_user_count(), initial_count + 1)

if __name__ == "__main__":
    unittest.main()
