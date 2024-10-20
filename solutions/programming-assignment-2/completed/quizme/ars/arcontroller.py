"""Core module for running the Adaptive Review System (ARS) session."""

from typing import List, Dict, Any
from .boxmanager import BoxManager
from .qtype.shortanswer import ShortAnswer
from .qtype.truefalse import TrueFalse

class ARController:
    """Main controller for running an adaptive review session."""

    def __init__(self, question_data: List[Dict[str, Any]]):
        """
        Initialize the Adaptive Review Controller.

        Args:
            question_data (List[Dict[str, Any]]): A list of dictionaries containing question data.
        """
        self._box_manager = BoxManager()
        self._initialize_questions(question_data)

    def _initialize_questions(self, question_data: List[Dict[str, Any]]) -> None:
        """
        Initialize questions and place them in the Unasked Questions box.

        Args:
            question_data (List[Dict[str, Any]]): A list of dictionaries containing question data.
        """
        for q in question_data:
            question_type = q.get("type")

            try:
                if question_type == "shortanswer":
                    question = ShortAnswer(
                        question=q["question"],
                        answer=q["correct_answer"],
                        case_sensitive=q.get("case_sensitive", False)
                    )
                elif question_type == "truefalse":
                    question = TrueFalse(
                        question=q["question"],
                        answer=q["correct_answer"],
                        explanation=q.get("explanation", "")
                    )
                else:
                    print(f"Unsupported question type: {question_type}. Skipping this question.")
                    continue
                self._box_manager.add_new_question(question)
            except KeyError as e:
                print(f"Missing required field for question: {e}. Skipping this question.")

    def start(self) -> None:
        """Run the interactive adaptive review session."""
        print("Type 'q' at any time to quit the session.")
        
        while True:
            question = self._box_manager.get_next_question()
            if not question:
                print("All questions have been reviewed. Session complete!")
                break

            print(f"\n{question.ask()}")
            user_answer = input("Your answer: ")
            
            if user_answer.lower() == 'q':
                break

            try:
                answer_is_correct = question.check_answer(user_answer)

                if answer_is_correct:
                    print("Correct!")
                else:
                    print(question.incorrect_feedback())

                self._box_manager.move_question(question, answer_is_correct)
            except ValueError as e:
                print(f"Invalid input: {e}")

        print("Thank you, goodbye!")