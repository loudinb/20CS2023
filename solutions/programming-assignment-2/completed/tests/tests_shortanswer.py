"""Unit tests for the ShortAnswer class."""

import unittest
from datetime import datetime
from ars.qtype.shortanswer import ShortAnswer

class TestShortAnswer(unittest.TestCase):
    """Test cases for the ShortAnswer class."""

    def setUp(self):
        """Set up test fixtures."""
        self.question_text = "What is the capital of France?"
        self.correct_answer = "Paris"
        self.sa_question = ShortAnswer(self.question_text, self.correct_answer)
        self.sa_question_case_sensitive = ShortAnswer(self.question_text, self.correct_answer, case_sensitive=True)

    def test_initialization(self):
        """Test the initialization of a ShortAnswer instance."""
        self.assertEqual(self.sa_question._question, self.question_text)
        self.assertEqual(self.sa_question._answer, self.correct_answer)
        self.assertFalse(self.sa_question._case_sensitive)
        self.assertTrue(self.sa_question_case_sensitive._case_sensitive)

    def test_ask_method(self):
        """Test the ask method."""
        self.assertEqual(self.sa_question.ask(), self.question_text)
        self.assertIsInstance(self.sa_question._last_asked, datetime)

    def test_check_answer_correct(self):
        """Test the check_answer method with correct answers."""
        self.assertTrue(self.sa_question.check_answer("Paris"))
        self.assertTrue(self.sa_question.check_answer("paris"))
        self.assertTrue(self.sa_question.check_answer(" Paris "))

    def test_check_answer_incorrect(self):
        """Test the check_answer method with incorrect answers."""
        self.assertFalse(self.sa_question.check_answer("London"))
        self.assertFalse(self.sa_question.check_answer(""))
        self.assertFalse(self.sa_question.check_answer("Par"))

    def test_check_answer_case_sensitive(self):
        """Test the check_answer method with case-sensitive flag."""
        self.assertTrue(self.sa_question_case_sensitive.check_answer("Paris"))
        self.assertFalse(self.sa_question_case_sensitive.check_answer("paris"))
        self.assertFalse(self.sa_question_case_sensitive.check_answer("PARIS"))

    def test_check_answer_punctuation(self):
        """Test the check_answer method with answers containing punctuation."""
        punctuated_sa = ShortAnswer("What's Sherlock's catchphrase?", "Elementary, my dear Watson!")
        self.assertTrue(punctuated_sa.check_answer("elementary my dear watson"))
        self.assertTrue(punctuated_sa.check_answer("Elementary, my dear Watson!"))
        self.assertFalse(punctuated_sa.check_answer("Elementary my dear Holmes"))

    def test_incorrect_feedback(self):
        """Test the incorrect_feedback method."""
        expected_feedback = f"Incorrect. The correct answer is: {self.correct_answer}"
        self.assertEqual(self.sa_question.incorrect_feedback(), expected_feedback)

    def test_equality(self):
        """Test the equality method."""
        # Same instance should be equal to itself
        self.assertEqual(self.sa_question, self.sa_question)

        # Two different instances should not be equal, even with the same content
        same_content_question = ShortAnswer(self.question_text, self.correct_answer)
        self.assertNotEqual(self.sa_question, same_content_question)

        # Different question should not be equal
        different_question = ShortAnswer("What is the capital of Spain?", "Madrid")
        self.assertNotEqual(self.sa_question, different_question)

        # Should not be equal to objects of different types
        self.assertNotEqual(self.sa_question, "Not a ShortAnswer object")

    def test_hash(self):
        """Test the hash method."""
        # Hash should be based on the UUID, so two different instances should have different hashes
        same_content_question = ShortAnswer(self.question_text, self.correct_answer)
        self.assertNotEqual(hash(self.sa_question), hash(same_content_question))

        # Same instance should always hash to the same value
        self.assertEqual(hash(self.sa_question), hash(self.sa_question))

if __name__ == '__main__':
    unittest.main()