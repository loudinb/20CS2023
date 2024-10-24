import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        User.user_count = 0
        self.user1 = User("user1", "user1@example.com")
        self.user2 = User("user2", "user2@example.com")

    def test_user_initialization(self):
        self.assertEqual(self.user1.username, "user1")
        self.assertEqual(self.user1._email, "user1@example.com")
        self.assertEqual(self.user1.bio, "")
        self.assertEqual(User.get_user_count(), 2)

    def test_bio_setter(self):
        self.user1.bio = "Hello, I am user1!"
        self.assertEqual(self.user1.bio, "Hello, I am user1!")
        with self.assertRaises(ValueError):
            self.user1.bio = "x" * 151  # Exceeding 150 characters

    def test_following_functionality(self):
        self.user1.follow(self.user2)
        self.assertIn(self.user2, self.user1._following)
        self.assertIn(self.user1, self.user2._followers)
        self.user1.unfollow(self.user2)
        self.assertNotIn(self.user2, self.user1._following)
        self.assertNotIn(self.user1, self.user2._followers)

    def test_post_creation_and_deletion(self):
        self.user1.create_post("My first post!")
        self.assertEqual(len(self.user1._posts), 1)
        post = self.user1._posts[0]
        self.user1.delete_post(post)
        self.assertEqual(len(self.user1._posts), 0)

if __name__ == "__main__":
    unittest.main()
