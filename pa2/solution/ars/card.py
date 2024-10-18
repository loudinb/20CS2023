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
        self.question = question
        self.last_asked = None

    def ask(self) -> str:
        """Returns the question text to be presented to the user and updates the last asked timestamp."""
        self.last_asked = datetime.now()
        return self.question.ask()

    def check_answer(self, answer: str) -> bool:
        """Checks if the provided answer is correct.

        Args:
            answer (str): The answer provided by the user.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        return self.question.check_answer(answer)

    def reset(self) -> None:
        """Resets the last asked time."""
        self.last_asked = None

    def __repr__(self) -> str:
        """Returns a string representation of the Card object."""
        return f"Card(question={repr(self.question)}, last_asked={self.last_asked})"
