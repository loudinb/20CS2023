import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")

    def test_protected_attributes(self):
        self.assertTrue(hasattr(self.user, '_username'))
        self.assertTrue(hasattr(self.user, '_email'))
        self.assertTrue(hasattr(self.user, '_bio'))
        self.assertTrue(hasattr(self.user, '_join_date'))
        self.assertTrue(hasattr(self.user, '_posts'))

    def test_username_property(self):
        self.assertEqual(self.user.username, "testuser")
        with self.assertRaises(AttributeError):
            self.user.username = "newuser"

    def test_email_property(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.user.email = "new@example.com"
        self.assertEqual(self.user.email, "new@example.com")
        with self.assertRaises(ValueError):
            self.user.email = "invalid_email"

    def test_bio_property(self):
        self.assertEqual(self.user.bio, "")
        self.user.bio = "New bio"
        self.assertEqual(self.user.bio, "New bio")
        with self.assertRaises(ValueError):
            self.user.bio = "a" * 151

    def test_create_post(self):
        self.user.create_post("Test content")
        self.assertEqual(len(self.user._posts), 1)
        self.assertEqual(self.user._posts[0]["content"], "Test content")
        self.assertEqual(self.user._posts[0]["likes"], 0)

    def test_like_post(self):
        self.user.create_post("Test post")
        self.user.like_post(0)
        self.assertEqual(self.user._posts[0]["likes"], 1)
        with self.assertRaises(IndexError):
            self.user.like_post(1)

    def test_follow(self):
        other_user = User("other", "other@example.com")
        self.user.follow(other_user)
        self.assertIn(other_user, self.user._followers)

    def test_follower_count_property(self):
        other_user1 = User("other1", "other1@example.com")
        other_user2 = User("other2", "other2@example.com")
        self.user.follow(other_user1)
        self.user.follow(other_user2)
        self.assertEqual(self.user.follower_count, 2)

    def test_display_info(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.user.display_info()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("Username: testuser", output)
        self.assertIn("Email: test@example.com", output)
        self.assertIn("Joined on:", output)
        self.assertIn("Number of posts: 0", output)
        self.assertIn("Followers: 0", output)

if __name__ == '__main__':
    unittest.main()