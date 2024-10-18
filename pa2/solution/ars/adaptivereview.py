"""Core module for running the Adaptive Review System (ARS) session."""

from typing import List, Dict, Type
from ars.boxmanager import BoxManager
from ars.qtype.shortanswer import ShortAnswer
from ars.card import Card
from ars.qtype.question import Question
from ars.qtype.shortanswer import ShortAnswer
from ars.qtype.truefalse import TrueFalse

class AdaptiveReview:
    """Main controller for running an adaptive review session."""

    question_type_map: Dict[str, Type[Question]] = {
        "shortanswer": ShortAnswer,
        "truefalse": TrueFalse
        # Add more mappings as you implement more question types
    }


    def __init__(self, question_data: List[dict]) -> None:
        """Initializes the Adaptive Review System."""
        self.box_manager = BoxManager()
        self._initialize_cards(question_data)

    def _initialize_cards(self, question_data: List[dict]) -> None:
        """Initializes cards and places them in the Unasked Questions box."""
        for q in question_data:
            # Determine the question type from the data
            question_type = q.get("type")

            # Use the question_type_map to get the corresponding class
            question_class = self.question_type_map.get(question_type)

            if not question_class:
                print(f"Unknown question type: {question_type}. Skipping this question.")
                continue

            # Initialize the question using the appropriate class
            if question_type == "shortanswer":
                question = question_class(
                    question=q["question"],
                    correct_answer=q["correct_answer"],
                    case_sensitive=q.get("case_sensitive", False)
                )
            elif question_type == "truefalse":
                question = question_class(
                    question=q["question"],
                    correct_answer=q["correct_answer"],
                    explanation=q.get("explanation", "")
                )
            else:
                print(f"Unsupported question type: {question_type}. Skipping this question.")
                continue

            # Create a card for the initialized question and add to the Unasked Questions box
            card = Card(question)
            self.box_manager.add_card_to_box(1, card)  # Box 1: Unasked Questions


    def start(self) -> None:
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
