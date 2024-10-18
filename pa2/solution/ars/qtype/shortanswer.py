"""Module for the ShortAnswer quiz item class, which checks answers based on user input."""

from .question import Question
import re

class ShortAnswer(Question):
    """A quiz item representing a short answer question.
    
    Attributes:
        question: The question text with a short answer response.
        correct_answer: The correct answer string.
        case_sensitive: Boolean indicating if the answer checking should be case-sensitive.
    """

    def __init__(self, question: str, correct_answer: str, case_sensitive: bool = False) -> None:
        """Initializes a short answer quiz item.

        Args:
            question: The question to be displayed.
            correct_answer: The correct answer to the question.
            case_sensitive: If True, the answer comparison will be case-sensitive.
        """
        self.question = question
        self.correct_answer = correct_answer
        self.case_sensitive = case_sensitive

    def ask(self) -> str:
        """Returns the short answer question."""
        return self.question
    

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
            if not self.case_sensitive:
                text = text.lower()
            return re.sub(r'[^\w\s]', '', text)  # Removes punctuation

        return normalize(answer) == normalize(self.correct_answer)


    @property
    def incorrect_response(self) -> str:
        """Returns a response to display when the user provides an incorrect answer."""
        return f"Incorrect. The correct answer is: {self.correct_answer}"    


    def __repr__(self) -> str:
        """Returns a string representation of the ShortAnswer object."""
        truncated_question = (self.question[:30] + '...') if len(self.question) > 30 else self.question
        return (f"ShortAnswer(question='{truncated_question}', "
                f"correct_answer='{self.correct_answer}', "
                f"case_sensitive={self.case_sensitive})")
