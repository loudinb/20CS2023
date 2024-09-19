import unittest
from post import Post
from user import User
from tag import Tag

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
        Tag.all_tags.clear()

    def test_create_post(self):
        post = Post(self.user, "This is a #test post")
        self.assertEqual(post._user, self.user)
        self.assertEqual(post._content, "This is a #test post")
        self.assertEqual(len(post.tags), 1)
        self.assertEqual(post.tags[0].name, "test")

    def test_invalid_content(self):
        with self.assertRaises(ValueError):
            Post(self.user, "")
        with self.assertRaises(ValueError):
            Post(self.user, "a" * 281)

    def test_toggle_like(self):
        post = Post(self.user, "Test post")
        liker = User("liker", "liker@example.com")
        post.toggle_like(liker)
        self.assertEqual(post.likes_count, 1)
        post.toggle_like(liker)
        self.assertEqual(post.likes_count, 0)

    def test_create_shared_post(self):
        original_post = Post(self.user, "Original post")
        sharer = User("sharer", "sharer@example.com")
        shared_post = Post.create_shared_post(sharer, original_post)
        self.assertEqual(shared_post._user, sharer)
        self.assertTrue(shared_post._content.startswith("Shared: Original post"))

    def test_add_tag(self):
        post = Post(self.user, "Post without tags")
        post.add_tag("newtag")
        self.assertEqual(len(post.tags), 1)
        self.assertEqual(post.tags[0].name, "newtag")

    def test_extract_tags(self):
        post = Post(self.user, "Post with #multiple #tags")
        self.assertEqual(len(post.tags), 2)
        self.assertEqual(post.tags[0].name, "multiple")
        self.assertEqual(post.tags[1].name, "tags")

if __name__ == '__main__':
    unittest.main()
