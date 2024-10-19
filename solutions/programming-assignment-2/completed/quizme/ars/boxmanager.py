
from .box import Box
from datetime import timedelta

class BoxManager:
    """Manages multiple boxes in the Adaptive Review System."""

    def __init__(self):
        """Initializes the BoxManager with predefined boxes."""
        self._boxes = [
            Box("Missed Questions", timedelta(seconds=60)),
            Box("Unasked Questions", timedelta(seconds=0)),
            Box("Correctly Answered Once", timedelta(seconds=180)),
            Box("Correctly Answered Twice", timedelta(seconds=360)),
            Box("Known Questions", timedelta.max)
        ]
        self._question_location = {}

    
    def add_new_question(self, question):
        """Add a new question to the Unasked Questions box.
  
        Args:
            question (Question): The question to add.
        """
        self._boxes[1].add_question(question)
        self._question_location[question.id] = 1


    def move_question(self, question, answered_correctly):
        """Move a question based on whether it was answered correctly.
  
        Args:
            question (Question): The question to move.
            answered_correctly (bool): True if the question was answered correctly, False otherwise.
        """
        current_box = self._question_location.get(question.id)

        if answered_correctly:
            if current_box == 0:
                new_box = 2
            else:
                new_box = min(current_box + 1, len(self._boxes) - 1)
        else:
            new_box = 0

        self._boxes[current_box].remove_question(question)
        self._boxes[new_box].add_question(question)
        self._question_location[question.id] = new_box

    def get_next_question(self):
        """Determine and return the next question to present.
  
        Returns:
            Optional[Question]: The next question to present, or None if no question is available.
        """

        for box in self._boxes[:-1]:
            next_question = box.get_next_priority_question()
            if next_question:
                return next_question
        
        return None