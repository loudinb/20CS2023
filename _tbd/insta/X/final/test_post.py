import unittest
from post import Post
from user import User

class TestPost(unittest.TestCase):

    def setUp(self):
        self.user1 = User("user1", "user1@example.com")
        self.post = Post("This is a test post.", self.user1, ["test", "post"])

    def test_post_initialization(self):
        self.assertEqual(self.post.content, "This is a test post.")
        self.assertEqual(self.post.author, self.user1)
        self.assertIn("test", self.post._tags)

    def test_content_setter(self):
        self.post.content = "Updated content"
        self.assertEqual(self.post.content, "Updated content")
        with self.assertRaises(ValueError):
            self.post.content = "x" * 2201  # Exceeding 2200 characters

    def test_tag_addition_removal(self):
        self.post.add_tag("newtag")
        self.assertIn("newtag", self.post._tags)
        self.post.remove_tag("newtag")
        self.assertNotIn("newtag", self.post._tags)

    def test_likes_functionality(self):
        self.post.add_like(self.user1)
        self.assertIn(self.user1, self.post._likes)
        self.post.remove_like(self.user1)
        self.assertNotIn(self.user1, self.post._likes)

if __name__ == "__main__":
    unittest.main()
