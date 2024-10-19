"""Module for the ShortAnswer quiz item class, which checks answers based on user input."""

from .question import Question
import re

class ShortAnswer(Question):
    """A quiz item representing a short answer question.
    
    Attributes:
        question: The question text with a short answer response.
        answer: The correct answer string.
        case_sensitive: Boolean indicating if the answer checking should be case-sensitive.
    """


    def __init__(self, question: str, answer: str, case_sensitive_answer: bool = False) -> None:
        """Initializes a short answer quiz item.

        Args:
            question: The question to be displayed.
            correct_answer: The correct answer to the question.
            case_sensitive: If True, the answer comparison will be case-sensitive.
        """
        self._question = question
        self._answer = answer
        self._case_sensitive_answer = case_sensitive_answer


    def ask(self) -> str:
        """Returns the short answer question."""
        return self._question
    

    def check_answer(self, answer: str) -> bool:
        """Checks if the provided answer matches the correct answer.

        Args:
            answer: The answer provided by the user.

        Returns:
            True if the answer is correct, False otherwise.
        """
        def normalize(text: str) -> str:
            # Remove leading/trailing spaces, lower case if needed, and strip punctuation.
            text = text.strip()
            if not self._case_sensitive_answer:
                text = text.lower()
            return re.sub(r'[^\w\s]', '', text)  # Removes punctuation

        return normalize(answer) == normalize(self._answer)


    def get_incorrect_answer_feedback(self) -> str:
        """Returns a response to display when the user provides an incorrect answer."""
        return f"Incorrect. The correct answer is: {self._answer}"    


    def __repr__(self) -> str:
        """Returns a string representation of the ShortAnswer object."""
        return (f"ShortAnswer(question='{self._question}', "
                f"answer='{self._answer}', "
                f"case_sensitive_answer={self._case_sensitive_answer})")
