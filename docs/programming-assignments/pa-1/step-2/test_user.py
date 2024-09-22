import unittest
from user import User
from post import Post

class TestUser(unittest.TestCase):

    def setUp(self):
        User.user_count = 0

    def test_init_valid(self):
        user = User("validuser", "valid@email.com")
        self.assertEqual(user.username, "validuser")
        self.assertEqual(user._email, "valid@email.com")

    def test_init_invalid_username(self):
        with self.assertRaises(ValueError):
            User("in", "test@email.com")  # Too short

    def test_init_invalid_email(self):
        with self.assertRaises(ValueError):
            User("validuser", "invalid-email")

    def test_bio_property(self):
        user = User("testuser", "test@email.com")
        self.assertEqual(user.bio, "")
    
    def test_bio_setter_valid(self):
        user = User("testuser", "test@email.com")
        user.bio = "This is a valid bio"
        self.assertEqual(user.bio, "This is a valid bio")

    def test_bio_setter_invalid(self):
        user = User("testuser", "test@email.com")
        with self.assertRaises(ValueError):
            user.bio = "a" * 151  # Too long
    
    def test_bio_setter_edge_case(self):
        user = User("testuser", "test@email.com")
        bio_text = "a" * 150  # Exactly 150 characters
        user.bio = bio_text
        self.assertEqual(user.bio, bio_text)  # Should accept 150 characters without error

    def test_get_user_count(self):
        User("user1", "user1@email.com")
        User("user2", "user2@email.com")
        self.assertEqual(User.get_user_count(), 2)

    def test_is_valid_username(self):
        self.assertTrue(User.is_valid_username("valid_user"))
        self.assertTrue(User.is_valid_username("valid.user"))
        self.assertFalse(User.is_valid_username("in"))  # Too short
        self.assertFalse(User.is_valid_username("invalid username"))  # Contains space
        self.assertFalse(User.is_valid_username("a" * 31))  # Too long
        self.assertTrue(User.is_valid_username("abc"))  # Exactly 3 characters
        self.assertTrue(User.is_valid_username("a" * 30))  # Exactly 30 characters

    def test_is_valid_email(self):
        self.assertTrue(User.is_valid_email("valid@email.com"))
        self.assertTrue(User.is_valid_email("valid.user+tag@email.co.uk"))
        self.assertFalse(User.is_valid_email("invalid-email"))
        self.assertFalse(User.is_valid_email("invalid@email"))

    def test_create_post(self):
        user = User("testuser", "test@email.com")
        user.create_post("This is a post", tags=["test", "post"])
        # self.assertEqual(len(user._posts), 1)
        # self.assertEqual(user._posts[0].content, "This is a post")

    # def test_delete_post(self):
    #     user = User("testuser", "test@email.com")
    #     post = Post("To be deleted")
    #     user.create_post(post.content)
    #     user.delete_post(user._posts[0])
    #     self.assertEqual(len(user._posts), 0)

    # def test_delete_nonexistent_post(self):
    #     post = Post("Nonexistent post")
    #     self.user.delete_post(post)  # Should not raise an error
    #     self.assertEqual(len(self.user._posts), 0)

    # def test_like_post(self):
    #     post = Post("Some post")
    #     self.user.like_post(post)
    #     self.assertIn(self.user, post.likes)  # Assuming Post has a 'likes' attribute

    # def test_unlike_post(self):
    #     post = Post("Some post")
    #     self.user.like_post(post)
    #     self.user.unlike_post(post)
    #     self.assertNotIn(self.user, post.likes)

    # # Missing test cases for follow/unfollow functionalities

    # def test_follow_user(self):
    #     user2 = User("user2", "user2@email.com")
    #     self.user.follow(user2)
    #     self.assertIn(user2, self.user._following)
    #     self.assertIn(self.user, user2._followers)

    # def test_unfollow_user(self):
    #     user2 = User("user2", "user2@email.com")
    #     self.user.follow(user2)
    #     self.user.unfollow(user2)
    #     self.assertNotIn(user2, self.user._following)
    #     self.assertNotIn(self.user, user2._followers)

if __name__ == '__main__':
    unittest.main()
