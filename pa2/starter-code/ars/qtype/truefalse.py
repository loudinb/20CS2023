"""Module for the TrueFalse quiz item class, which checks answers based on a true/false response."""

from .question import Question

class TrueFalse(Question):
    """A quiz item representing a true/false question.
    
    Attributes:
        question (str): The question text that expects a true/false response.
        correct_answer (bool): The correct answer, either True or False.
        explanation (str): Additional information to explain why the correct answer is False.
    """

    def __init__(self, question: str, correct_answer: bool, explanation: str = "") -> None:
        """Initializes a true/false quiz item.
        
        Args:
            question (str): The question to be displayed.
            correct_answer (bool): The correct answer, either True or False.
            explanation (str): Additional information if the correct answer is False.
        """
        pass

    def ask(self) -> str:
        """Returns the true/false question."""
        pass

    def check_answer(self, answer: str) -> bool:
        """Checks if the provided answer matches the correct answer.
        
        Args:
            answer (str): The answer provided by the user.
        
        Returns:
            bool: True if the answer matches the correct answer, False otherwise.
        """
        pass

    def get_feedback(self) -> str:
        """Returns feedback based on the correct answer and explanation."""
        pass

    def __repr__(self) -> str:
        """Returns a string representation of the TrueFalse object."""
        pass
