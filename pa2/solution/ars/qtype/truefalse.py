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
        if not isinstance(correct_answer, bool):
            raise ValueError("The correct_answer must be a boolean (True or False).")

        self.question = question
        self.correct_answer = correct_answer
        self.explanation = explanation

    def ask(self) -> str:
        """Returns the true/false question."""
        return f"{self.question} (True/False)"

    def check_answer(self, answer: str) -> bool:
        """Checks if the provided answer matches the correct answer.
        
        Args:
            answer (str): The answer provided by the user.
        
        Returns:
            bool: True if the answer matches the correct answer, False otherwise.
        """
        normalized_answer = answer.strip().lower()
        if normalized_answer in ["true", "t"]:
            user_answer = True
        elif normalized_answer in ["false", "f"]:
            user_answer = False
        else:
            raise ValueError("Answer must be 'True' or 'False'.")

        return user_answer == self.correct_answer

    def get_feedback(self) -> str:
        """Returns feedback based on the correct answer and explanation."""
        if self.correct_answer:
            return "The correct answer is True."
        else:
            return f"The correct answer is False. {self.explanation}"

    def __repr__(self) -> str:
        """Returns a string representation of the TrueFalse object."""
        return f"TrueFalse(question='{self.question}', correct_answer={self.correct_answer})"
