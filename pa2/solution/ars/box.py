from datetime import datetime, timedelta
from typing import List, Optional
from ars.card import Card

class Box:
    """Represents a box that holds a set of cards for adaptive review."""

    def __init__(self, name: str, priority_interval: timedelta) -> None:
        """Initializes a box with a name and priority interval."""
        self.name = name
        self._cards: List[Card] = []
        self.priority_interval = priority_interval

    def add_card(self, card: Card) -> None:
        """Adds a card to the box."""
        if card not in self._cards:
            self._cards.append(card)

    def remove_card(self, card: Card) -> None:
        """Removes a card from the box."""
        if card in self._cards:
            self._cards.remove(card)

    def get_next_priority_card(self) -> Optional[Card]:
        """Returns the next priority card if available, or None."""
        now = datetime.now()
        for card in self._cards:
            if card.last_asked is None or (now - card.last_asked) >= self.priority_interval:
                return card
        return None

    def __len__(self) -> int:
        """Returns the number of cards in the box."""
        return len(self._cards)

    def __repr__(self) -> str:
        """Returns a string representation of the Box object."""
        return f"Box(name='{self.name}', cards_count={len(self._cards)})"