"""This module defines the abstract base class for quiz questions.

The `Question` class provides the structure for creating quiz questions.
Each quiz question must implement methods to return a question and check
if an answer is correct.
"""

from abc import ABC, abstractmethod

class Question(ABC):
    """Abstract base class for quiz items."""

    def __init__(self, question: str, answer: str):
        self._question = question
        self._answer = answer

    @abstractmethod
    def ask(self) -> str:
        """Returns the question as a string."""
        pass

    @abstractmethod
    def check_answer(self, answer: str) -> bool:
        """Checks if the provided answer is correct.

        Args:
            answer: The answer to validate.

        Returns:
            True if the answer is correct, False otherwise.
        """
        pass

    @abstractmethod
    def get_incorrect_answer_feedback(self) -> str:
        """Returns a response to display when the user provides an incorrect answer."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Returns a string representation of the Question object."""
        pass