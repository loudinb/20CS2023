from typing import List, Dict
from ars.box import Box
from ars.card import Card
from datetime import timedelta
import uuid

class BoxManager:
    """Manages multiple boxes in the Adaptive Review System."""

    def __init__(self) -> None:
        """Initializes the BoxManager with predefined boxes."""
        self._boxes: List[Box] = [
            Box("Missed Questions", timedelta(seconds=60)),
            Box("Unasked Questions", timedelta.max),
            Box("Correctly Answered Once", timedelta(seconds=360)),
            Box("Correctly Answered Twice", timedelta(seconds=600)),
            Box("Known Questions", timedelta.max)
        ]
        self._card_location: Dict[uuid.UUID, int] = {}


    def move_card(self, card: Card, correct: bool) -> None:
        """
        Moves a card based on whether it was answered correctly.
        If the card is not in any box, it's added to box 1 (Unasked Questions).
        """
        current_box = self._card_location.get(card.id)
        
        if current_box is None:
            # Card is not in any box, add it to box 1 (Unasked Questions)
            new_box = 1
        elif correct:
            if current_box == 0:
                # If correct answer from box 0 (Missed Questions), move to box 2
                new_box = 2
            else:
                # Move to the next box, but not beyond the last box
                new_box = min(current_box + 1, len(self._boxes) - 1)
        else:
            # If incorrect, move to box 0 (Missed Questions)
            new_box = 0

        # Remove from current box if it exists
        if current_box is not None:
            self._boxes[current_box].remove_card(card)

        # Add to new box
        self._boxes[new_box].add_card(card)
        self._card_location[card.id] = new_box


    def get_next_card(self) -> Card:
        """Determines and returns the next card to present."""
        for box in self._boxes[:-1]:  # Exclude the last box (Known Questions)
            next_card = box.get_next_priority_card()
            if next_card:
                return next_card
        return None

