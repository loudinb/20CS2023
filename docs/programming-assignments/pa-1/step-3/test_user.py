import unittest
from user import User
from post import Post
from message import Message

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user1 = User("testuser1", "test1@example.com")
        self.user2 = User("testuser2", "test2@example.com")

    def test_init(self):
        self.assertEqual(self.user1.username, "testuser1")
        self.assertEqual(self.user1._email, "test1@example.com")
        self.assertEqual(self.user1._bio, "")
        self.assertEqual(self.user1._posts, [])
        self.assertEqual(self.user1._followers, [])
        self.assertEqual(self.user1._following, [])
        self.assertEqual(self.user1._messages, [])

    def test_invalid_username(self):
        with self.assertRaises(ValueError):
            User("a", "test@example.com")
        with self.assertRaises(ValueError):
            User("a" * 31, "test@example.com")
        with self.assertRaises(ValueError):
            User("invalid@user", "test@example.com")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            User("testuser", "invalid_email")

    def test_bio(self):
        self.user1.bio = "Test bio"
        self.assertEqual(self.user1.bio, "Test bio")
        with self.assertRaises(ValueError):
            self.user1.bio = "a" * 151

    def test_create_post(self):
        self.user1.create_post("Test post")
        self.assertEqual(len(self.user1._posts), 1)
        self.assertIsInstance(self.user1._posts[0], Post)

    def test_delete_post(self):
        post = Post("Test post", self.user1)
        self.user1._posts.append(post)
        self.user1.delete_post(post)
        self.assertEqual(len(self.user1._posts), 0)

    def test_follow_unfollow(self):
        self.user1.follow(self.user2)
        self.assertIn(self.user2, self.user1._following)
        self.assertIn(self.user1, self.user2._followers)
        self.user1.unfollow(self.user2)
        self.assertNotIn(self.user2, self.user1._following)
        self.assertNotIn(self.user1, self.user2._followers)

    def test_like_unlike_post(self):
        post = Post("Test post", self.user2)
        self.user1.like_post(post)
        self.assertIn(self.user1, post._likes)
        self.user1.unlike_post(post)
        self.assertNotIn(self.user1, post._likes)

    def test_comment_on_post(self):
        post = Post("Test post", self.user2)
        self.user1.comment_on_post(post, "Test comment")
        self.assertEqual(len(post._comments), 1)
        self.assertEqual(post._comments[0].content, "Test comment")

    def test_send_receive_message(self):
        self.user1.send_message(self.user2, "Test message")
        self.assertEqual(len(self.user2._messages), 1)
        self.assertEqual(self.user2._messages[0].content, "Test message")

    def test_get_user_count(self):
        initial_count = User.get_user_count()
        User("newuser", "new@example.com")
        self.assertEqual(User.get_user_count(), initial_count + 1)

    def test_is_valid_username(self):
        self.assertTrue(User.is_valid_username("valid_user"))
        self.assertFalse(User.is_valid_username("in"))
        self.assertFalse(User.is_valid_username("a" * 31))
        self.assertFalse(User.is_valid_username("invalid@user"))

    def test_is_valid_email(self):
        self.assertTrue(User.is_valid_email("test@example.com"))
        self.assertFalse(User.is_valid_email("invalid_email"))

if __name__ == '__main__':
    unittest.main()
