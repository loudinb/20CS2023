"""Module for the TrueFalse quiz item class in the Adaptive Review System."""

from .question import Question

class TrueFalse(Question):
    """Class for a True/False quiz item."""

    def __init__(self, question: str, answer: bool, explanation: str = ""):
        """
        Initialize a True/False quiz item.

        Args:
            question (str): The question to be displayed.
            answer (bool): The correct answer, either True or False.
            explanation (str, optional): Additional information to explain the correct answer.
                                         Defaults to an empty string.

        Raises:
            ValueError: If the answer is not a boolean.
        """
        super().__init__(question, answer)
        if not isinstance(answer, bool):
            raise ValueError("The answer must be a boolean (True or False).")
        self._explanation = explanation

    def ask(self) -> str:
        """
        Return the true/false question.

        Returns:
            str: The question text appended with " (True/False)".
        """
        super().ask()
        return f"{self._question} (True/False)"
    
    def check_answer(self, answer: str) -> bool:
        """
        Check if the provided answer is correct.
        
        Args:
            answer (str): The user's answer to the question.
        
        Returns:
            bool: True if the answer is correct, False otherwise.
        
        Raises:
            ValueError: If the answer is not 'True' or 'False'.
        """
        normalized_answer = answer.strip().lower()
        if normalized_answer in ("true", "t"):
            user_answer = True
        elif normalized_answer in ("false", "f"):
            user_answer = False
        else:
            raise ValueError("Answer must be 'True' or 'False'.")

        return user_answer == self._answer
    
    def incorrect_feedback(self) -> str:
        """
        Return feedback for an incorrect answer.

        Returns:
            str: Feedback message for an incorrect answer, including the explanation if provided.
        """
        return f"Incorrect. {self._explanation}"