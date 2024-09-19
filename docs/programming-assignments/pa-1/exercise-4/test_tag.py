import unittest
from tag import Tag

class TestTag(unittest.TestCase):
    def test_tag_creation(self):
        tag = Tag.get_or_create_tag("python")
        self.assertEqual(tag.name, "python")
        self.assertEqual(tag.post_count, 0)

    def test_get_or_create_tag(self):
        tag1 = Tag.get_or_create_tag("python")
        tag2 = Tag.get_or_create_tag("python")
        self.assertIs(tag1, tag2)  # Should be the same object

    def test_increment_post_count(self):
        tag = Tag.get_or_create_tag("python")
        initial_count = tag.post_count
        tag.increment_post_count()
        self.assertEqual(tag.post_count, initial_count + 1)

    def test_get_trending_tags(self):
        Tag.all_tags.clear()  # Clear existing tags
        python_tag = Tag.get_or_create_tag("python")
        java_tag = Tag.get_or_create_tag("java")
        cpp_tag = Tag.get_or_create_tag("cpp")

        python_tag.increment_post_count()
        python_tag.increment_post_count()
        java_tag.increment_post_count()

        trending_tags = Tag.get_trending_tags(limit=2)
        self.assertEqual(