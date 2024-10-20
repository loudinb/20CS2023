import unittest
from datetime import timedelta
from ars.boxmanager import BoxManager
from ars.qtype.truefalse import TrueFalse
from ars.qtype.shortanswer import ShortAnswer


class TestBoxManager(unittest.TestCase):
    def setUp(self):
        self.box_manager = BoxManager()
        self.true_false_question = TrueFalse("Is the sky blue?", True)
        self.short_answer_question = ShortAnswer("What is the capital of France?", "Paris")

    def test_initial_boxes_count(self):
        """Test that BoxManager initializes with five boxes."""
        self.assertEqual(len(self.box_manager._boxes), 5)

    def test_add_new_truefalse_question(self):
        """Test adding a new True/False question to the Unasked Questions box."""
        initial_count = len(self.box_manager._boxes[1]._questions)
        self.box_manager.add_new_question(self.true_false_question)
        self.assertEqual(len(self.box_manager._boxes[1]._questions), initial_count + 1)
        self.assertIn(self.true_false_question, self.box_manager._boxes[1]._questions)

    def test_add_new_shortanswer_question(self):
        """Test adding a new Short Answer question to the Unasked Questions box."""
        initial_count = len(self.box_manager._boxes[1]._questions)
        self.box_manager.add_new_question(self.short_answer_question)
        self.assertEqual(len(self.box_manager._boxes[1]._questions), initial_count + 1)
        self.assertIn(self.short_answer_question, self.box_manager._boxes[1]._questions)

    def test_question_location_update(self):
        """Test that adding a new question updates the question location map."""
        self.box_manager.add_new_question(self.short_answer_question)
        self.assertIn(self.short_answer_question.id, self.box_manager._question_location)
        self.assertEqual(self.box_manager._question_location[self.short_answer_question.id], 1)

    def test_move_question_to_next_box(self):
        """Test moving a question to the next box."""
        self.box_manager.add_new_question(self.short_answer_question)
        self.box_manager.move_question(self.short_answer_question.id, 2)
        current_location = self.box_manager._question_location[self.short_answer_question.id]
        self.assertEqual(current_location, 2)
        self.assertIn(self.short_answer_question, self.box_manager._boxes[2]._questions)

    def test_move_question_back(self):
        """Test moving a question back to the previous box."""
        self.box_manager.add_new_question(self.true_false_question)
        self.box_manager.move_question(self.true_false_question.id, 2)
        self.box_manager.move_question(self.true_false_question.id, 1)
        current_location = self.box_manager._question_location[self.true_false_question.id]
        self.assertEqual(current_location, 1)
        self.assertIn(self.true_false_question, self.box_manager._boxes[1]._questions)

    def test_remove_question(self):
        """Test removing a question from the boxes."""
        self.box_manager.add_new_question(self.short_answer_question)
        self.box_manager.remove_question(self.short_answer_question.id)
        self.assertNotIn(self.short_answer_question, self.box_manager._boxes[1]._questions)
        self.assertNotIn(self.short_answer_question.id, self.box_manager._question_location)

if __name__ == '__main__':
    unittest.main()
