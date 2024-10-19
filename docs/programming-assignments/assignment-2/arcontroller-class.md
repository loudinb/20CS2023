# `ARController` Class

The `ARController` class serves as the main controller for running an adaptive review session. It manages the overall flow of the quiz, including initializing questions, presenting them to the user, and processing answers.

Follow the specifications provided below to create an `ARController` class in the `ars/arcontroller.py` file.

## Imports

Ensure you have the following imports at the beginning of your file:

```python
from typing import List
from ars.boxmanager import BoxManager
from ars.card import Card
from ars.qtype.shortanswer import ShortAnswer
from ars.qtype.truefalse import TrueFalse
```

## Attributes

| Name           | Kind     | Access Level | Type         | Description                                    |
|----------------|----------|--------------|--------------|------------------------------------------------|
| `box_manager`  | Instance | Public       | `BoxManager` | The BoxManager instance for managing cards     |

## Methods

| Name                | Kind     | Return Type | Parameters                  | Description                                           |
|---------------------|----------|-------------|---------------------------|-------------------------------------------------------|
| `__init__`          | Instance | None        | `question_data: List[dict]` | Initialize a new ARController instance              |
| `_initialize_cards` | Instance | None        | `question_data: List[dict]` | Create cards from question data and add to BoxManager |
| `start`             | Instance | None        | None                      | Run the interactive adaptive review session           |

### Implementation Details

**`__init__(self, question_data: List[dict]) -> None`**
- Initialize a new ARController instance.
- Create a new BoxManager instance and assign it to `self.box_manager`.
- Call `self._initialize_cards(question_data)` to set up the initial cards.

**`_initialize_cards(self, question_data: List[dict]) -> None`**
- Iterate through the `question_data` list.
- For each question dictionary:
  - Check the `type` key to determine if it's a "shortanswer" or "truefalse" question.
  - Create the appropriate Question subclass instance (ShortAnswer or TrueFalse) with the provided data.
  - Create a new Card with this question.
  - Add the card to the BoxManager using `self.box_manager.move_card(card, correct=False)`.
- Handle potential KeyError exceptions if required fields are missing in the question data.
- Skip questions with unsupported types, printing a message to indicate this.

**`start(self) -> None`**
- Print a welcome message for the Adaptive Review Session.
- Enter a loop that continues until all questions have been reviewed or the user quits:
  - Get the next card from `self.box_manager.get_next_card()`.
  - If there are no more cards, print a completion message and break the loop.
  - Present the question to the user using `card.ask()`.
  - Get the user's answer as input.
  - If the user inputs 'q', break the loop to quit the session.
  - Check the answer using `card.check_answer(user_answer)`.
  - Print "Correct!" if the answer is right, otherwise print the incorrect answer feedback.
  - Move the card in the BoxManager based on whether the answer was correct.
- Print a thank you message when the session ends.

## Example Usage

Here's an example of how to use the ARController class:

```python
from ars.arcontroller import ARController

# Sample question data
questions = [
    {
        "type": "shortanswer",
        "question": "What is the capital of France?",
        "correct_answer": "Paris"
    },
    {
        "type": "truefalse",
        "question": "The Earth is flat.",
        "correct_answer": False,
        "explanation": "The Earth is actually an oblate spheroid."
    }
]

# Create an ARController instance
quiz = ARController(questions)

# Start the review session
quiz.start()
```
