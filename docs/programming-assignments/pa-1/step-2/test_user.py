import unittest
from datetime import datetime
from user import User
from post import Post
from comment import Comment

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user1 = User("user1", "user1@example.com")
        self.user2 = User("user2", "user2@example.com")

    def test_init(self):
        self.assertEqual(self.user1.username, "user1")
        self.assertEqual(self.user1._email, "user1@example.com")
        self.assertIsInstance(self.user1._joined_on, datetime)

    def test_invalid_username(self):
        with self.assertRaises(ValueError):
            User("u", "user3@example.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            User("user3", "invalid-email")

    def test_bio_setter(self):
        self.user1.bio = "This is a bio"
        self.assertEqual(self.user1.bio, "This is a bio")
        with self.assertRaises(ValueError):
            self.user1.bio = "a" * 151

    def test_create_post(self):
        self.user1.create_post("This is a post")
        self.assertEqual(len(self.user1._posts), 1)
        self.assertEqual(self.user1._posts[0]._content, "This is a post")

    def test_delete_post(self):
        post = Post("This is a post")
        self.user1.create_post("This is a post")
        self.user1.delete_post(post)
        self.assertEqual(len(self.user1._posts), 0)

    def test_like_post(self):
        post = Post("This is a post")
        self.user1.like_post(post)
        self.assertIn(self.user1, post._likes)

    def test_unlike_post(self):
        post = Post("This is a post")
        self.user1.like_post(post)
        self.user1.unlike_post(post)
        self.assertNotIn(self.user1, post._likes)

    def test_follow_unfollow(self):
        self.user1.follow(self.user2)
        self.assertIn(self.user2, self.user1._following)
        self.assertIn(self.user1, self.user2._followers)
        self.user1.unfollow(self.user2)
        self.assertNotIn(self.user2, self.user1._following)

if __name__ == '__main__':
    unittest.main()