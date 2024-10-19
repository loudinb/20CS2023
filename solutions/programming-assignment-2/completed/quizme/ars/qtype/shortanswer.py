"""Module for the ShortAnswer quiz item class, which checks answers based on user input."""

from .question import Question
import re

class ShortAnswer(Question):
    """A quiz item representing a short answer question."""

    def __init__(self, question, answer, case_sensitive=False):
        """Initialize a short answer quiz item.

        Args:
            question (str): The question prompt.
            answer (str): The correct answer.
            case_sensitive (bool): Whether the answer comparison should be case-sensitive.
        """
        super().__init__(question, answer)
        self._case_sensitive = case_sensitive

    
    def _normalize(self, text: str) -> str:
        """Normalize the text for comparison.

        Args:
            text (str): The text to normalize.

        Returns:
            str: The normalized text.
        """
        text = text.strip()
        if not self._case_sensitive:
            text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text
    
    def check_answer(self, answer):
        """Check if the provided answer is correct.

        Args:
            answer (str): The provided answer.

        Returns:
            bool: True if the provided answer is correct, False otherwise.
        """
        return self._normalize(answer) == self._normalize(self._answer)
    
    def incorrect_feedback(self):
        """Return feedback for an incorrect answer.

        Returns:
            str: Feedback message for an incorrect answer.
        """
        return f"Incorrect. The correct answer is: {self._answer}"