"""Unit tests for the TrueFalse class."""

import unittest
from datetime import datetime
from ars.qtype.truefalse import TrueFalse

class TestTrueFalse(unittest.TestCase):
    """Test cases for the TrueFalse class."""

    def setUp(self):
        """Set up test fixtures."""
        self.question_text = "Python is a compiled language."
        self.correct_answer = False
        self.explanation = "Python is an interpreted language, not a compiled one."
        self.tf_question = TrueFalse(self.question_text, self.correct_answer, self.explanation)

    def test_initialization(self):
        """Test the initialization of a TrueFalse instance."""
        self.assertEqual(self.tf_question._question, self.question_text)
        self.assertEqual(self.tf_question._answer, self.correct_answer)
        self.assertEqual(self.tf_question._explanation, self.explanation)

    def test_initialization_with_non_boolean_answer(self):
        """Test that initializing with a non-boolean answer raises a ValueError."""
        with self.assertRaises(ValueError):
            TrueFalse("Invalid question", "Not a boolean")

    def test_ask_method(self):
        """Test the ask method."""
        expected_question = f"{self.question_text} (True/False)"
        self.assertEqual(self.tf_question.ask(), expected_question)
        self.assertIsInstance(self.tf_question._last_asked, datetime)

    def test_check_answer_correct(self):
        """Test the check_answer method with correct answers."""
        self.assertTrue(self.tf_question.check_answer("False"))
        self.assertTrue(self.tf_question.check_answer("false"))
        self.assertTrue(self.tf_question.check_answer("F"))
        self.assertTrue(self.tf_question.check_answer("f"))

    def test_check_answer_incorrect(self):
        """Test the check_answer method with incorrect answers."""
        self.assertFalse(self.tf_question.check_answer("True"))
        self.assertFalse(self.tf_question.check_answer("true"))
        self.assertFalse(self.tf_question.check_answer("T"))
        self.assertFalse(self.tf_question.check_answer("t"))

    def test_check_answer_invalid(self):
        """Test the check_answer method with invalid inputs."""
        with self.assertRaises(ValueError):
            self.tf_question.check_answer("Not a boolean")

    def test_incorrect_feedback(self):
        """Test the incorrect_feedback method."""
        expected_feedback = f"Incorrect. {self.explanation}"
        self.assertEqual(self.tf_question.incorrect_feedback(), expected_feedback)

    def test_equality(self):
        """Test the equality method."""
        # Same instance should be equal to itself
        self.assertEqual(self.tf_question, self.tf_question)

        # Two different instances should not be equal, even with the same content
        same_content_question = TrueFalse(self.question_text, self.correct_answer, self.explanation)
        self.assertNotEqual(self.tf_question, same_content_question)

        # Different question should not be equal
        different_question = TrueFalse("Different question?", True, "Different explanation")
        self.assertNotEqual(self.tf_question, different_question)

        # Should not be equal to objects of different types
        self.assertNotEqual(self.tf_question, "Not a TrueFalse object")

    def test_hash(self):
        """Test the hash method."""
        # Hash should be based on the UUID, so two different instances should have different hashes
        same_content_question = TrueFalse(self.question_text, self.correct_answer, self.explanation)
        self.assertNotEqual(hash(self.tf_question), hash(same_content_question))

        # Same instance should always hash to the same value
        self.assertEqual(hash(self.tf_question), hash(self.tf_question))

if __name__ == '__main__':
    unittest.main()