
import unittest
from tag import Tag

class TestTag(unittest.TestCase):
    def setUp(self):
        Tag.all_tags.clear()

    def test_get_or_create(self):
        tag1 = Tag.get_or_create("python")
        tag2 = Tag.get_or_create("python")
        self.assertIs(tag1, tag2)
        self.assertEqual(len(Tag.all_tags), 1)

    def test_increment_usage(self):
        tag = Tag.get_or_create("python")
        tag.increment_usage()
        self.assertEqual(tag.usage_count, 1)

    def test_get_trending_tags(self):
        tags = ["python", "java", "javascript", "csharp", "ruby", "go"]
        for tag_name in tags:
            tag = Tag.get_or_create(tag_name)
            for _ in range(tags.index(tag_name) + 1):
                tag.increment_usage()

        trending = Tag.get_trending_tags(3)
        self.assertEqual(len(trending), 3)
        self.assertEqual(trending[0].name, "go")
        self.assertEqual(trending[1].name, "ruby")
        self.assertEqual(trending[2].name, "csharp")

if __name__ == '__main__':
    unittest.main()
