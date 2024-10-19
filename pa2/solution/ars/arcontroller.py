"""Core module for running the Adaptive Review System (ARS) session."""
from typing import List
from ars.boxmanager import BoxManager
from ars.card import Card
from ars.qtype.shortanswer import ShortAnswer
from ars.qtype.truefalse import TrueFalse

class ARController:
    """Main controller for running an adaptive review session."""

    def __init__(self, question_data: List[dict]) -> None:
        """Initializes the Adaptive Review Controller."""
        self.box_manager = BoxManager()
        self._initialize_cards(question_data)

    def _initialize_cards(self, question_data: List[dict]) -> None:
        """Initializes cards and places them in the Unasked Questions box."""
        for q in question_data:
            question_type = q.get("type")

            try:
                if question_type == "shortanswer":
                    question = ShortAnswer(
                        question=q["question"],
                        answer=q["correct_answer"],
                        case_sensitive_answer=q.get("case_sensitive", False)
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

                card = Card(question)
                self.box_manager.move_card(card, correct=False)  # This will add the card to box 1 (Unasked Questions)
            except KeyError as e:
                print(f"Missing required field for question: {e}. Skipping this question.")

    def start(self) -> None:
            """Runs the interactive adaptive review session."""
            print("Welcome to the Adaptive Review Session!")
            print("Type 'q' at any time to quit the session.")
            
            while True:
                card = self.box_manager.get_next_card()
                if not card:
                    print("All questions have been reviewed. Session complete!")
                    break

                print("\n" + card.ask())
                user_answer = input("Your answer: ")
                
                if user_answer.lower() == 'q':
                    break

                answer_is_correct = card.check_answer(user_answer)

                if answer_is_correct:
                    print("Correct!")
                else:
                    print(card.question.get_incorrect_answer_feedback())

                self.box_manager.move_card(card, answer_is_correct)

            print("Thank you for using the Adaptive Review System!")