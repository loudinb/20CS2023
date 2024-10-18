"""Module for the Card class, which wraps a quiz question and tracks its timestamp."""

from ars.qtype.question import Question
from datetime import datetime

class Card:
    """A wrapper for a quiz question.
    
    Attributes:
        question (Question): The quiz question associated with the card.
        last_asked (datetime): The timestamp when the question was last asked.
    """

    def __init__(self, question: Question) -> None:
        """Initializes a card with the given quiz question.

        Args:
            question (Question): The question to be wrapped in the card.
        """
        pass

    def ask(self) -> str:
        """Returns the question text to be presented to the user and updates the last asked timestamp."""
        pass

    def check_answer(self, answer: str) -> bool:
        """Checks if the provided answer is correct.

        Args:
            answer (str): The answer provided by the user.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        pass

    def reset(self) -> None:
        """Resets the last asked time."""
        pass

    def __repr__(self) -> str:
        """Returns a string representation of the Card object."""
        pass
