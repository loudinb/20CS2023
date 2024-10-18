"""Module for the Box class, which manages a collection of cards in the Adaptive Review System."""

from datetime import datetime, timedelta
from typing import List, Optional
from ars.card import Card

class Box:
    """Represents a box that holds a set of cards for adaptive review."""
    
    def __init__(self, name: str, priority_interval: timedelta) -> None:
        """Initializes a box with a name and priority interval."""
        pass

    def add_card(self, card: Card) -> None:
        """Adds a card to the box."""
        pass

    def remove_card(self, card: Card) -> None:
        """Removes a card from the box."""
        pass

    def get_next_priority_card(self) -> Optional[Card]:
        """Returns the next priority card if available, or None."""
        pass

    def has_card(self, card: Card) -> bool:
        """Checks if the card is present in the box."""
        pass

    def move_card_to(self, destination: 'Box', card: Card) -> None:
        """Moves a card from this box to another box."""
        pass

    def __repr__(self) -> str:
        """Returns a string representation of the Box object."""
        pass
