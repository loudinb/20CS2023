"""Unit tests for the Box class."""

import unittest
from datetime import timedelta, datetime
from ars.box import Box
from ars.qtype.question import Question

class MockQuestion(Question):
    """A mock Question class for testing purposes."""
    def check_answer(self, answer):
        return True
    def incorrect_feedback(self):
        return "Incorrect"

class TestBox(unittest.TestCase):
    """Test cases for the Box class."""

    def setUp(self):
        """Set up test fixtures."""
        self.box_name = "Test Box"
        self.priority_interval = timedelta(minutes=5)
        self.box = Box(self.box_name, self.priority_interval)
        self.question1 = MockQuestion("Question 1?", "Answer 1")
        self.question2 = MockQuestion("Question 2?", "Answer 2")

    def test_initialization(self):
        """Test the initialization of a Box instance."""
        self.assertEqual(self.box.name, self.box_name)
        self.assertEqual(self.box.priority_interval, self.priority_interval)
        self.assertEqual(len(self.box), 0)

    def test_add_question(self):
        """Test adding questions to the box."""
        self.box.add_question(self.question1)
        self.assertEqual(len(self.box), 1)
        
        # Adding the same question again should not increase the count
        self.box.add_question(self.question1)
        self.assertEqual(len(self.box), 1)

        self.box.add_question(self.question2)
        self.assertEqual(len(self.box), 2)

    def test_remove_question(self):
        """Test removing questions from the box."""
        self.box.add_question(self.question1)
        self.box.add_question(self.question2)
        
        self.box.remove_question(self.question1)
        self.assertEqual(len(self.box), 1)

        # Removing a question not in the box should not raise an error
        self.box.remove_question(self.question1)
        self.assertEqual(len(self.box), 1)

        self.box.remove_question(self.question2)
        self.assertEqual(len(self.box), 0)

    def test_get_next_priority_question(self):
        """Test getting the next priority question."""
        self.box.add_question(self.question1)
        self.box.add_question(self.question2)

        # Set last_asked time for question1 to be older than the priority interval
        self.question1._last_asked = datetime.now() - self.priority_interval - timedelta(seconds=1)
        
        # Set last_asked time for question2 to be newer than the priority interval
        self.question2._last_asked = datetime.now()

        next_question = self.box.get_next_priority_question()
        self.assertEqual(next_question, self.question1)

        # If no questions are due, should return None
        self.question1._last_asked = datetime.now()
        self.assertIsNone(self.box.get_next_priority_question())

    def test_len(self):
        """Test the __len__ method."""
        self.assertEqual(len(self.box), 0)
        self.box.add_question(self.question1)
        self.assertEqual(len(self.box), 1)
        self.box.add_question(self.question2)
        self.assertEqual(len(self.box), 2)

    def test_str(self):
        """Test the __str__ method."""
        expected_str = f"Box(name='{self.box_name}', questions_count=0)"
        self.assertEqual(str(self.box), expected_str)

        self.box.add_question(self.question1)
        expected_str = f"Box(name='{self.box_name}', questions_count=1)"
        self.assertEqual(str(self.box), expected_str)

if __name__ == '__main__':
    unittest.main()