# test_truefalse.py

import unittest
from ars.qtype.truefalse import TrueFalse

class TestTrueFalse(unittest.TestCase):

    def test_correct_answer_true(self):
        question = TrueFalse("Python is a programming language.", True)
        self.assertTrue(question.check_answer("true"))

    def test_correct_answer_false(self):
        question = TrueFalse("Python is named after a snake.", False)
        self.assertTrue(question.check_answer("false"))

    def test_incorrect_answer_true(self):
        question = TrueFalse("Python is a programming language.", True)
        self.assertFalse(question.check_answer("false"))

    def test_incorrect_answer_false(self):
        question = TrueFalse("Python is named after a snake.", False)
        self.assertFalse(question.check_answer("true"))

    def test_ask(self):
        question = TrueFalse("Python is a programming language.", True)
        self.assertEqual(question.ask(), "Python is a programming language. (True/False)")

if __name__ == "__main__":
    unittest.main()
