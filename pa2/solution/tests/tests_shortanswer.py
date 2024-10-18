# test_shortanswer.py

import unittest
from ars.qtype.shortanswer import ShortAnswer

class TestShortAnswer(unittest.TestCase):

    def test_case_sensitive_correct(self):
        question = ShortAnswer("What is the capital of France?", "Paris", case_sensitive=True)
        self.assertTrue(question.check_answer("Paris"))

    def test_case_sensitive_incorrect(self):
        question = ShortAnswer("What is the capital of France?", "Paris", case_sensitive=True)
        self.assertFalse(question.check_answer("paris"))

    def test_case_insensitive_correct(self):
        question = ShortAnswer("What is the capital of France?", "Paris", case_sensitive=False)
        self.assertTrue(question.check_answer("paris"))

    def test_case_insensitive_incorrect(self):
        question = ShortAnswer("What is the capital of France?", "Paris", case_sensitive=False)
        self.assertFalse(question.check_answer("London"))

    def test_ask(self):
        question = ShortAnswer("What is the capital of France?", "Paris")
        self.assertEqual(question.ask(), "What is the capital of France?")

    def test_repr(self):
        question = ShortAnswer("What is the capital of France?", "Paris", case_sensitive=True)
        expected_repr = "ShortAnswer(question='What is the capital of France?', correct_answer='Paris', case_sensitive=True)"
        self.assertEqual(repr(question), expected_repr)

if __name__ == "__main__":
    unittest.main()
