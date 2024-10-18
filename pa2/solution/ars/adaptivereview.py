"""Core module for running the Adaptive Review System (ARS) session."""

from typing import List
from ars.boxmanager import BoxManager
from ars.qtype.shortanswer import ShortAnswer
from ars.card import Card

class AdaptiveReview:
    """Main controller for running an adaptive review session."""

    def __init__(self, question_data: List[dict]) -> None:
        """Initializes the Adaptive Review System."""
        self.box_manager = BoxManager()
        self._initialize_cards(question_data)

    def _initialize_cards(self, question_data: List[dict]) -> None:
        """Initializes cards and places them in the Unasked Questions box."""
        for q in question_data:
            question = ShortAnswer(
                question=q["question"],
                correct_answer=q["correct_answer"],
                case_sensitive=q.get("case_sensitive", False)
            )
            card = Card(question)
            self.box_manager.add_card_to_box(1, card)

    def start_session(self) -> None:
        """Runs the interactive adaptive review session."""
        print("Welcome to the Adaptive Review Session!")
        while True:
            next_card = self.box_manager.get_next_card()

            if not next_card:
                print("All questions have been reviewed. Session complete!")
                break

            print(next_card.ask())
            user_answer = input("Your answer: ")

            if next_card.check_answer(user_answer):
                print("Correct!")
                self.box_manager.move_card_between_boxes(1, 2, next_card)
            else:
                print(f"Incorrect. The correct answer is: {next_card.question.correct_answer}")
                self.box_manager.move_card_between_boxes(1, 0, next_card)
