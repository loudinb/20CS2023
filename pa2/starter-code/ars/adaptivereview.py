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
        pass

    def _initialize_cards(self, question_data: List[dict]) -> None:
        """Initializes cards and places them in the Unasked Questions box."""
        pass


    def start(self) -> None:
        """Runs the interactive adaptive review session."""
        pass
