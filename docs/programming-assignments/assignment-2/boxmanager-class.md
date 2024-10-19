# `BoxManager` Class

The `BoxManager` class manages multiple boxes in the Adaptive Review System (ARS). It handles the organization and movement of cards between different boxes based on the user's performance.

Follow the specifications provided below to create a `BoxManager` class in the `ars/boxmanager.py` file.

## Imports

Ensure you have the following imports at the beginning of your file:

```python
from typing import List, Dict
from ars.box import Box
from ars.card import Card
from datetime import timedelta
import uuid
```

## Attributes

| Name             | Kind     | Access Level | Type                  | Description                                    |
|------------------|----------|--------------|----------------------|------------------------------------------------|
| `_boxes`         | Instance | Protected    | `List[Box]`          | List of boxes managed by BoxManager            |
| `_card_location` | Instance | Protected    | `Dict[uuid.UUID, int]`| Dictionary mapping card IDs to box indices    |

## Methods

| Name         | Kind     | Return Type | Parameters                 | Description                                           |
|--------------|----------|-------------|----------------------------|-------------------------------------------------------|
| `__init__`   | Instance | None        | None                       | Initialize a new BoxManager instance                  |
| `move_card`  | Instance | None        | `card: Card, correct: bool`| Moves a card based on whether it was answered correctly |
| `get_next_card` | Instance | `Card`   | None                       | Determines and returns the next card to present       |

### Implementation Details

**`__init__(self) -> None`**
- Initialize a new BoxManager instance.
- Create five boxes with the following names and priority intervals:
  1. "Missed Questions" with interval of 60 seconds
  2. "Unasked Questions" with maximum interval (use `timedelta.max`)
  3. "Correctly Answered Once" with interval of 360 seconds
  4. "Correctly Answered Twice" with interval of 600 seconds
  5. "Known Questions" with maximum interval (use `timedelta.max`)
- Store these boxes in `self._boxes`.
- Initialize `self._card_location` as an empty dictionary.

**`move_card(self, card: Card, correct: bool) -> None`**
- Get the current box index of the card from `self._card_location`.
- If the card is not in any box (current_box is None):
  - Set `new_box` to 1 (Unasked Questions)
- If the answer was correct:
  - If the card was in box 0 (Missed Questions), move it to box 2 (Correctly Answered Once)
  - Otherwise, move it to the next box, but not beyond the last box
- If the answer was incorrect:
  - Move the card to box 0 (Missed Questions)
- Remove the card from its current box (if it exists in one)
- Add the card to the new box
- Update `self._card_location` with the new box index for the card

**`get_next_card(self) -> Card`**
- Iterate through all boxes except the last one (Known Questions):
  - Call `get_next_priority_card()` on each box
  - If a card is returned, return that card
- If no card is found in any box, return None

## Example Usage

Here's an example of how to use the BoxManager class:

```python
from ars.boxmanager import BoxManager
from ars.card import Card
from ars.qtype.shortanswer import ShortAnswer

# Create a BoxManager
manager = BoxManager()

# Create some cards
question1 = ShortAnswer("What is the capital of France?", "Paris")
card1 = Card(question1)

question2 = ShortAnswer("What is the largest planet in our solar system?", "Jupiter")
card2 = Card(question2)

# Move cards into the system
manager.move_card(card1, False)  # This will put card1 in the "Missed Questions" box
manager.move_card(card2, False)  # This will put card2 in the "Unasked Questions" box

# Get the next card to ask
next_card = manager.get_next_card()
if next_card:
    print(f"Next question: {next_card.ask()}")

# Simulate answering the question correctly
manager.move_card(next_card, True)

# Get the next card again
next_card = manager.get_next_card()
if next_card:
    print(f"Next question: {next_card.ask()}")
```
