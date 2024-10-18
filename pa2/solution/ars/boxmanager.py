"""Module for managing multiple boxes in the Adaptive Review System."""

from typing import List, Optional
from ars.box import Box
from ars.card import Card
from datetime import timedelta

class BoxManager:
    """Manages multiple boxes in the Adaptive Review System."""

    def __init__(self) -> None:
        """Initializes the BoxManager with predefined boxes."""
        self._boxes: List[Box] = [
            Box("Missed Questions", timedelta(seconds=60)),
            Box("Unasked Questions", timedelta.max),
            Box("Correctly Answered Once", timedelta(seconds=360)),
            Box("Known Questions", timedelta.max)
        ]

    def add_card_to_box(self, box_index: int, card: Card) -> None:
        """Adds a card to a specific box."""
        self._boxes[box_index].add_card(card)

    def move_card_between_boxes(self, from_box: int, to_box: int, card: Card) -> None:
        """Moves a card from one box to another."""
        self._boxes[from_box].move_card_to(self._boxes[to_box], card)

    def get_next_card(self) -> Optional[Card]:
        """Determines and returns the next card to present, prioritizing missed and unasked cards."""
        for box in self._boxes:
            next_card = box.get_next_priority_card()
            if next_card:
                return next_card
        return None

    def __repr__(self) -> str:
        """Returns a string representation of the BoxManager object."""
        return f"BoxManager({', '.join([repr(box) for box in self._boxes])})"
