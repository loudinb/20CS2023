"""Module for managing boxes in the Adaptive Review System."""

from datetime import timedelta
from typing import List, Dict, Optional
from .box import Box
from .qtype.question import Question

class BoxManager:
    """Manages multiple boxes in the Adaptive Review System."""

    def __init__(self):
        """Initialize the BoxManager with predefined boxes."""
        self._boxes: List[Box] = [
            Box("Missed Questions", timedelta(seconds=60)),
            Box("Unasked Questions", timedelta(seconds=0)),
            Box("Correctly Answered Once", timedelta(seconds=180)),
            Box("Correctly Answered Twice", timedelta(seconds=360)),
            Box("Known Questions", timedelta.max)
        ]
        self._question_location: Dict[str, int] = {}

    def add_new_question(self, question: Question) -> None:
        """
        Add a new question to the Unasked Questions box.
  
        Args:
            question (Question): The question to add.
        """
        self._boxes[1].add_question(question)
        self._question_location[str(question.id)] = 1

    def move_question(self, question: Question, answered_correctly: bool) -> None:
        """
        Move a question based on whether it was answered correctly.
  
        Args:
            question (Question): The question to move.
            answered_correctly (bool): True if the question was answered correctly, False otherwise.
        """
        current_box = self._question_location.get(str(question.id))

        if answered_correctly:
            if current_box == 0:
                new_box = 2
            else:
                new_box = min(current_box + 1, len(self._boxes) - 1)
        else:
            new_box = 0

        self._boxes[current_box].remove_question(question)
        self._boxes[new_box].add_question(question)
        self._question_location[str(question.id)] = new_box

    def get_next_question(self) -> Optional[Question]:
        """
        Determine and return the next question to present.
  
        Returns:
            Optional[Question]: The next question to present, or None if no question is available.
        """
        for box in self._boxes[:-1]:
            next_question = box.get_next_priority_question()
            if next_question:
                return next_question
        
        return None