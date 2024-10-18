import uuid
from datetime import datetime
from ars.qtype.question import Question

class Card:
    """A wrapper for a quiz question.
    
    Attributes:
        id (uuid.UUID): A unique identifier for the card.
        question (Question): The quiz question associated with the card.
        last_asked (datetime): The timestamp when the question was last asked.
    """

    def __init__(self, question: Question) -> None:
        """Initializes a card with the given quiz question and a unique identifier.

        Args:
            question (Question): The question to be wrapped in the card.
        """
        self.id = uuid.uuid4()
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
        return f"Card(id={self.id}, question={repr(self.question)}, last_asked={self.last_asked})"

    def __eq__(self, other):
        """Defines equality based on the card's unique id."""
        if isinstance(other, Card):
            return self.id == other.id
        return False

    def __hash__(self):
        """Defines a hash value based on the card's unique id."""
        return hash(self.id)