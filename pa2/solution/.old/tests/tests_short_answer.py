import unittest
from short_answer import ShortAnswer
from question import Question

class TestShortAnswer(unittest.TestCase):
    def setUp(self):
        self.question_case_sensitive = ShortAnswer(
            "What is the capital of France?", 
            "Paris", 
            case_sensitive=True
        )
        self.question_case_insensitive = ShortAnswer(
            "What is the largest planet in our solar system?", 
            "Jupiter", 
            case_sensitive=False
        )

    def test_initialization(self):
        self.assertEqual(self.question_case_sensitive.question, "What is the capital of France?")
        self.assertEqual(self.question_case_sensitive.correct_answer, "Paris")
        self.assertTrue(self.question_case_sensitive.case_sensitive)

        self.assertEqual(self.question_case_insensitive.question, "What is the largest planet in our solar system?")
        self.assertEqual(self.question_case_insensitive.correct_answer, "Jupiter")
        self.assertFalse(self.question_case_insensitive.case_sensitive)

    def test_get_question(self):
        self.assertEqual(self.question_case_sensitive.get_question(), "What is the capital of France?")
        self.assertEqual(self.question_case_insensitive.get_question(), "What is the largest planet in our solar system?")

    def test_check_answer_case_sensitive(self):
        self.assertTrue(self.question_case_sensitive.check_answer("Paris"))
        self.assertFalse(self.question_case_sensitive.check_answer("paris"))
        self.assertFalse(self.question_case_sensitive.check_answer("PARIS"))
        self.assertFalse(self.question_case_sensitive.check_answer("London"))

    def test_check_answer_case_insensitive(self):
        self.assertTrue(self.question_case_insensitive.check_answer("Jupiter"))
        self.assertTrue(self.question_case_insensitive.check_answer("jupiter"))
        self.assertTrue(self.question_case_insensitive.check_answer("JUPITER"))
        self.assertFalse(self.question_case_insensitive.check_answer("Saturn"))

    def test_check_answer_whitespace(self):
        self.assertTrue(self.question_case_sensitive.check_answer("Paris "))
        self.assertTrue(self.question_case_sensitive.check_answer(" Paris"))
        self.assertTrue(self.question_case_sensitive.check_answer(" Paris "))

    def test_check_answer_empty(self):
        self.assertFalse(self.question_case_sensitive.check_answer(""))
        self.assertFalse(self.question_case_insensitive.check_answer(""))

    def test_repr(self):
        expected_repr = "ShortAnswer(question='What is the capital of France?', correct_answer='Paris', case_sensitive=True)"
        self.assertEqual(repr(self.question_case_sensitive), expected_repr)

    def test_inheritance(self):
        self.assertIsInstance(self.question_case_sensitive, ShortAnswer)
        self.assertIsInstance(self.question_case_sensitive, Question)

if __name__ == '__main__':
    unittest.main()