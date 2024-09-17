import unittest
from user import User
from post import Post
from tag import Tag

class TestTag(unittest.TestCase):
    def setUp(self):
        Tag.all_tags = {}  # Reset all_tags before each test
        self.user = User("testuser", "test@example.com")

    def test_get_or_create(self):
        tag1 = Tag.get_or_create("testtag")
        tag2 = Tag.get_or_create("testtag")
        self.assertEqual(tag1, tag2)
        self.assertEqual(len(Tag.all_tags), 1)

    def test_add_post(self):
        tag = Tag.get_or_create("testtag")
        post = Post(self.user, "Test post with #testtag")
        tag.add_post(post)
        self.assertEqual(len(tag.posts), 1)
        self.assertEqual(tag.posts[0], post)

    def test_get_trending_tags(self):
        tag1 = Tag.get_or_create("popular")
        tag2 = Tag.get_or_create("lessPopular")
        tag3 = Tag.get_or_create("leastPopular")

        for _ in range(5):
            tag1.add_post(Post(self.user, f"Post with #popular"))
        for _ in range(3):
            tag2.add_post(Post(self.user, f"Post with #lessPopular"))
        tag3.add_post(Post(self.user, "Post with #leastPopular"))

        trending_tags = Tag.get_trending_tags(limit=2)
        self.assertEqual(len(trending_tags), 2)
        self.assertEqual(trending_tags[0].name, "popular")
        self.assertEqual(trending_tags[1].name, "lesspopular")

    def test_get_all_tags(self):
        Tag.get_or_create("tag1")
        Tag.get_or_create("tag2")
        Tag.get_or_create("tag3")
        all_tags = Tag.get_all_tags()
        self.assertEqual(len(all_tags), 3)
        self.assertTrue(all(isinstance(tag, Tag) for tag in all_tags))

if __name__ == '__main__':
    unittest.main()
