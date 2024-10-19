# `Box` Class

The `Box` class represents a container for cards in the Adaptive Review System (ARS). It manages a set of cards and provides functionality for adding, removing, and retrieving cards based on priority intervals.

Follow the specifications provided below to create a `Box` class in the `ars/box.py` file.

## Imports

Ensure you have the following imports at the beginning of your file:

```python
from datetime import datetime, timedelta
from typing import List, Optional
from ars.card import Card
```

## Attributes

| Name                | Kind     | Access Level | Type            | Description                                    |
|---------------------|----------|--------------|-----------------|------------------------------------------------|
| `name`              | Instance | Public       | `str`           | The name of the box                            |
| `_cards`            | Instance | Protected    | `List[Card]`    | List of cards in the box                       |
| `priority_interval` | Instance | Public       | `timedelta`     | Time interval for prioritizing cards           |

## Methods

| Name                   | Kind     | Return Type    | Parameters     | Description                                           |
|------------------------|----------|----------------|----------------|-------------------------------------------------------|
| `__init__`             | Instance | None           | `name: str, priority_interval: timedelta` | Initialize a new Box instance |
| `add_card`             | Instance | None           | `card: Card`   | Adds a card to the box                                |
| `remove_card`          | Instance | None           | `card: Card`   | Removes a card from the box                           |
| `get_next_priority_card` | Instance | `Optional[Card]` | None       | Returns the next priority card if available, or None  |
| `__len__`              | Instance | `int`          | None           | Returns the number of cards in the box                |
| `__repr__`             | Instance | `str`          | None           | Returns a string representation of the Box object     |

### Implementation Details

**`__init__(self, name: str, priority_interval: timedelta) -> None`**
- Initialize a new Box instance.
- Set `self.name` to the provided `name` parameter.
- Initialize `self._cards` as an empty list.
- Set `self.priority_interval` to the provided `priority_interval` parameter.

**`add_card(self, card: Card) -> None`**
- If the `card` is not already in `self._cards`, append it to the list.

**`remove_card(self, card: Card) -> None`**
- If the `card` is in `self._cards`, remove it from the list.

**`get_next_priority_card(self) -> Optional[Card]`**
- Get the current time using `datetime.now()`.
- Iterate through `self._cards`:
  - If a card's `last_asked` is `None` or if the time since it was last asked is greater than or equal to `self.priority_interval`, return that card.
- If no priority card is found, return `None`.

**`__len__(self) -> int`**
- Return the length of `self._cards`.

**`__repr__(self) -> str`**
- Return a string representation of the Box object in the format:
  `f"Box(name='{self.name}', cards_count={len(self._cards)})"`

## Example Usage

Here's an example of how to create and use a Box:

```python
from ars.box import Box
from ars.card import Card
from ars.qtype.shortanswer import ShortAnswer
from datetime import timedelta

# Create a Box
box = Box("Review Box", timedelta(days=1))

# Create some cards and add them to the box
question1 = ShortAnswer("What is the capital of France?", "Paris")
card1 = Card(question1)
box.add_card(card1)

question2 = ShortAnswer("What is the largest planet in our solar system?", "Jupiter")
card2 = Card(question2)
box.add_card(card2)

# Get the next priority card
next_card = box.get_next_priority_card()
if next_card:
    print(f"Next question: {next_card.ask()}")

# Remove a card
box.remove_card(card1)

# Print the box information
print(repr(box))
print(f"Number of cards in the box: {len(box)}")
```
