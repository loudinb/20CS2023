"""Module for the TrueFalse quiz item class, which checks answers based on a true/false response."""

from typing import Optional
from .question import Question


class TrueFalse(Question):
    """A quiz item representing a true/false question."""

    def __init__(self, question: str, answer: bool, explanation: Optional[str] = None) -> None:
        """Initialize a true/false quiz item.
        
        Args:
            question: The question to be displayed.
            answer: The correct answer, either True or False.
            explanation: Additional information to explain the correct answer.

        Raises:
            ValueError: If the answer is not a boolean.
        """
        super().__init__(question, answer)
        if not isinstance(answer, bool):
            raise ValueError("The answer must be a boolean (True or False).")
        self._explanation = explanation or ""

    def ask(self) -> str:
        """Return the true/false question."""
        super().ask()
        return f"{self._question} (True/False)"

    def check_answer(self, answer: str) -> bool:
        """Check if the provided answer matches the correct answer."""
        normalized_answer = answer.strip().lower()
        if normalized_answer in ("true", "t"):
            user_answer = True
        elif normalized_answer in ("false", "f"):
            user_answer = False
        else:
            raise ValueError("Answer must be 'True' or 'False'.")

        return user_answer == self._answer

    def incorrect_feedback(self) -> str:
        """Return feedback for an incorrect answer."""
        return f"Incorrect. {self._explanation}"