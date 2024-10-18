import unittest
from pa2.solution.src.question_box import QuestionBox

class TestQuestionBox(unittest.TestCase):
    """Test cases for the QuestionBox class."""

    def setUp(self):
        """Set up a QuestionBox instance for testing."""
        self.box = QuestionBox(index=1)

    def test_initialization(self):
        """Test that a QuestionBox initializes with the correct index and no items."""
        self.assertEqual(self.box.index, 1)
        self.assertEqual(len(self.box), 0)

    def test_add_item(self):
        """Test adding an item to the QuestionBox."""
        self.box.add("What is the capital of France?")
        self.assertEqual(len(self.box), 1)
        self.assertIn("What is the capital of France?", self.box.items)

    def test_remove_item(self):
        """Test removing an item from the QuestionBox."""
        self.box.add("What is the capital of France?")
        self.box.remove("What is the capital of France?")
        self.assertEqual(len(self.box), 0)
        self.assertNotIn("What is the capital of France?", self.box.items)

    def test_len_method(self):
        """Test the __len__ method for counting items."""
        self.box.add("What is the capital of France?")
        self.box.add("Name the largest ocean.")
        self.assertEqual(len(self.box), 2)

    def test_repr_method(self):
        """Test the __repr__ method for a valid string representation."""
        self.box.add("What is the capital of France?")
        repr_string = repr(self.box)
        self.assertEqual(repr_string, "QuestionBox(index=1, items_count=1)")

    def test_remove_nonexistent_item(self):
        """Test removing an item that does not exist in the QuestionBox."""
        self.box.add("What is the capital of France?")
        with self.assertRaises(ValueError):
            self.box.remove("What is the largest continent?")

if __name__ == '__main__':
    unittest.main()
