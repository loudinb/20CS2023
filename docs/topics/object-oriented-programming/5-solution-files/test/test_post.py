import unittest
from user import User
from post import Post
from tag import Tag

class TestPost(unittest.TestCase):
    def setUp(self):
        Post.post_id_counter = 0  # Reset post_id_counter before each test
        self.user = User("testuser", "test@example.com")
        self.post = Post(self.user, "Test post content #testtag")

    def test_post_initialization(self):
        self.assertEqual(self.post.id, 1)
        self.assertEqual(self.post.user, self.user)
        self.assertEqual(self.post.content, "Test post content #testtag")
        self.assertEqual(self.post.likes_count, 0)
        self.assertEqual(len(self.post.comments), 0)
        self.assertEqual(len(self.post.tags), 0)

    def test_toggle_like(self):
        self.assertTrue(self.post.toggle_like())
        self.assertEqual(self.post.likes_count, 1)
        self.assertFalse(self.post.toggle_like())
        self.assertEqual(self.post.likes_count, 0)

    def test_add_comment(self):
        commenter = User("commenter", "commenter@example.com")
        comment = self.post.add_comment(commenter, "Test comment")
        self.assertEqual(len(self.post.comments), 1)
        self.assertEqual(comment.user, commenter)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.content, "Test comment")

    def test_add_tag(self):
        tag = self.post.add_tag("testtag")
        self.assertIsInstance(tag, Tag)
        self.assertEqual(len(self.post.tags), 1)
        self.assertEqual(tag.name, "testtag")

    def test_get_post_count(self):
        initial_count = Post.get_post_count()
        Post(self.user, "Another post")
        self.assertEqual(Post.get_post_count(), initial_count + 1)

    def test_is_valid_content(self):
        self.assertTrue(Post.is_valid_content("Valid content"))
        self.assertFalse(Post.is_valid_content(""))
        self.assertFalse(Post.is_valid_content("x" * 501))

    def test_create_shared_post(self):
        sharer = User("sharer", "sharer@example.com")
        shared_post = Post.create_shared_post(self.post, sharer, "Sharing this post")
        self.assertIn(self.post.content, shared_post.content)
        self.assertIn("Sharing this post", shared_post.content)
        self.assertEqual(shared_post.user, sharer)

if __name__ == '__main__':
    unittest.main()
