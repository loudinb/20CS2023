"""Module for the ShortAnswer quiz item class, which checks answers based on user input."""

from .question import Question
import re

class ShortAnswer(Question):
    """A quiz item representing a short answer question.
    
    Attributes:
        question: The question text with a short answer response.
        correct_answer: The correct answer string.
        case_sensitive: Boolean indicating if the answer checking should be case-sensitive.
    """

    def __init__(self, question: str, correct_answer: str, case_sensitive: bool = False) -> None:
        """Initializes a short answer quiz item.

        Args:
            question: The question to be displayed.
            correct_answer: The correct answer to the question.
            case_sensitive: If True, the answer comparison will be case-sensitive.
        """
        pass

    def ask(self) -> str:
        """Returns the short answer question."""
        pass

    def check_answer(self, answer: str) -> bool:
        """Checks if the provided answer matches the correct answer.

        Args:
            answer: The answer provided by the user.

        Returns:
            True if the answer is correct, False otherwise.
        """
        pass

    def __repr__(self) -> str:
        """Returns a string representation of the ShortAnswer object."""
        pass
