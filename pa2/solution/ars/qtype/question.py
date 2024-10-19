"""Module for the base Question class in the Adaptive Review System."""

from abc import ABC, abstractmethod
from datetime import datetime
import uuid
from typing import Any, Optional

class Question(ABC):
    """Abstract base class for quiz questions."""

    def __init__(self, question: str, answer: Any) -> None:
        """Initialize a Question.

        Args:
            question: The question text.
            answer: The correct answer.
        """
        self._id: uuid.UUID = uuid.uuid4()
        self._question: str = question
        self._answer: Any = answer
        self._last_asked: Optional[datetime] = None

    @property
    def id(self) -> uuid.UUID:
        """Returns the unique identifier for the question."""
        return self._id

    @property
    def last_asked(self) -> Optional[datetime]:
        """Returns the timestamp when the question was last asked."""
        return self._last_asked

    @abstractmethod
    def ask(self) -> str:
        """Return the question as a string."""
        self._last_asked = datetime.now()
        return self._question

    @abstractmethod
    def check_answer(self, answer: Any) -> bool:
        """Check if the provided answer is correct.

        Args:
            answer: The answer to validate.

        Returns:
            True if the answer is correct, False otherwise.
        """

    @abstractmethod
    def incorrect_feedback(self) -> str:
        """Return feedback for an incorrect answer."""

    def reset(self) -> None:
        """Resets the last asked time."""
        self._last_asked = None

    def __eq__(self, other: object) -> bool:
        """Defines equality based on the question's unique id."""
        if isinstance(other, Question):
            return self._id == other.id
        return False

    def __hash__(self) -> int:
        """Defines a hash value based on the question's unique id."""
        return hash(self._id)

    def __repr__(self) -> str:
        """Return a string representation of the Question object."""
        return f"{self.__class__.__name__}(id={self._id}, question='{self._question}', last_asked={self._last_asked})"