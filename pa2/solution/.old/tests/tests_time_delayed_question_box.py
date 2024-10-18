import unittest
import time
from time_delayed_question_box import TimeDelayedQuestionBox

class TestTimeDelayedQuestionBox(unittest.TestCase):
    """Test cases for the TimeDelayedQuestionBox class."""

    def setUp(self):
        """Set up a TimeDelayedQuestionBox instance for testing."""
        self.box = TimeDelayedQuestionBox(delay=2)  # 2-second delay for testing

    def test_initialization(self):
        """Test that the TimeDelayedQuestionBox initializes with the correct delay and no items."""
        self.assertEqual(self.box.reattempt_delay, 2)
        self.assertEqual(len(self.box.items), 0)

    def test_add_item(self):
        """Test adding an item to the TimeDelayedQuestionBox."""
        self.box.add("What is the capital of France?")
        self.assertEqual(len(self.box.items), 1)
        self.assertEqual(self.box.items[0][0], "What is the capital of France?")

    def test_remove_item(self):
        """Test removing an item from the TimeDelayedQuestionBox."""
        self.box.add("What is the capital of France?")
        self.box.remove("What is the capital of France?")
        self.assertEqual(len(self.box.items), 0)

    def test_get_eligible_no_items(self):
        """Test that no items are eligible if the delay has not passed."""
        self.box.add("What is the capital of France?")
        self.assertEqual(self.box.get_eligible(), [])

    def test_get_eligible_with_delay(self):
        """Test that items become eligible after the delay period."""
        self.box.add("What is the capital of France?")
        time.sleep(2)  # Wait for the delay period to pass
        self.assertEqual(self.box.get_eligible(), ["What is the capital of France?"])

    def test_get_eligible_multiple_items(self):
        """Test eligibility with multiple items added at different times."""
        self.box.add("What is the capital of France?")
        time.sleep(1)
        self.box.add("Name the largest ocean.")
        time.sleep(1)
        eligible_items = self.box.get_eligible()
        self.assertIn("What is the capital of France?", eligible_items)
        self.assertNotIn("Name the largest ocean.", eligible_items)
        
        # Wait another second to ensure all items are eligible
        time.sleep(1)
        eligible_items = self.box.get_eligible()
        self.assertIn("Name the largest ocean.", eligible_items)

    def test_repr_method(self):
        """Test the __repr__ method for a valid string representation."""
        self.box.add("What is the capital of France?")
        repr_string = repr(self.box)
        self.assertTrue("TimeDelayedQuestionBox" in repr_string)
        self.assertTrue("reattempt_delay=2" in repr_string)
        self.assertTrue("items_count=1" in repr_string)

if __name__ == '__main__':
    unittest.main()
