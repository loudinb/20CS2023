"""Module for the ShortAnswer quiz item class, which checks answers based on user input."""

import re
from .question import Question

class ShortAnswer(Question):
    """A quiz item representing a short answer question."""

    def __init__(self, question: str, answer: str, case_sensitive: bool = False) -> None:
        """Initialize a short answer quiz item."""
        super().__init__(question, answer)
        self._case_sensitive = case_sensitive

    def ask(self) -> str:
        """Return the short answer question."""
        super().ask()
        return self._question

    def check_answer(self, answer: str) -> bool:
        """Check if the provided answer matches the correct answer."""
        return self._normalize(answer) == self._normalize(self._answer)

    def incorrect_feedback(self) -> str:
        """Return feedback for an incorrect answer."""
        return f"Incorrect. The correct answer is: {self._answer}"

    def _normalize(self, text: str) -> str:
        """Normalize the text for comparison."""
        text = text.strip()
        if not self._case_sensitive:
            text = text.lower()
        return re.sub(r'[^\w\s]', '', text)  # Removes punctuation