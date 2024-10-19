"""Module for managing multiple boxes in the Adaptive Review System."""

from typing import List, Dict, Optional
from datetime import timedelta
import uuid
from .box import Box
from .qtype.question import Question

class BoxManager:
    """Manages multiple boxes in the Adaptive Review System."""

    def __init__(self) -> None:
        """Initializes the BoxManager with predefined boxes."""
        self._boxes: List[Box] = [
            Box("Missed Questions", timedelta(seconds=60)),
            Box("Unasked Questions", timedelta.max),
            Box("Correctly Answered Once", timedelta(seconds=360)),
            Box("Correctly Answered Twice", timedelta(seconds=600)),
            Box("Known Questions", timedelta.max)
        ]
        self._question_location: Dict[uuid.UUID, int] = {}

    def add_new_question(self, question: Question) -> None:
        """Adds a new question to the Unasked Questions box."""
        self._boxes[1].add_question(question)
        self._question_location[question.id] = 1


    def move_question(self, question: Question, correct: bool) -> None:
        """Moves a question based on whether it was answered correctly."""
        current_box = self._question_location.get(question.id)

        if correct:
            if current_box == 0:
                new_box = 2
            else:
                new_box = min(current_box + 1, len(self._boxes) - 1)
        else:
            new_box = 0

        self._boxes[current_box].remove_question(question)
        self._boxes[new_box].add_question(question)
        self._question_location[question.id] = new_box

    def get_next_question(self) -> Optional[Question]:
        """Determines and returns the next question to present."""
        for box in self._boxes[:-1]:  # Exclude the last box (Known Questions)
            next_question = box.get_next_priority_question()
            if next_question:
                return next_question
        return None