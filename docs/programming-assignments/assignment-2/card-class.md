# `Card` Class

The `Card` class represents a wrapper for a quiz question in the Adaptive Review System (ARS). It encapsulates a question along with metadata such as a unique identifier and the last time the question was asked.

Follow the specifications provided below to create a `Card` class in the `ars/card.py` file.

## Imports

Ensure you have the following imports at the beginning of your file:

```python
import uuid
from datetime import datetime
from ars.qtype.question import Question
```

## Attributes

| Name         | Kind     | Access Level | Type       | Description                                    |
|--------------|----------|--------------|------------|------------------------------------------------|
| `id`         | Instance | Public       | `uuid.UUID`| A unique identifier for the card               |
| `question`   | Instance | Public       | `Question` | The quiz question associated with the card     |
| `last_asked` | Instance | Public       | `datetime` | The timestamp when the question was last asked |

## Methods

| Name           | Kind     | Return Type | Parameters        | Description                                           |
|----------------|----------|-------------|-------------------|-------------------------------------------------------|
| `__init__`     | Instance | None        | `question: Question` | Initialize a new Card instance                     |
| `ask`          | Instance | `str`       | None              | Returns the question text and updates last_asked      |
| `check_answer` | Instance | `bool`      | `answer: str`     | Checks if the provided answer is correct              |
| `reset`        | Instance | None        | None              | Resets the last_asked time                            |
| `__repr__`     | Instance | `str`       | None              | Returns a string representation of the Card object    |
| `__eq__`       | Instance | `bool`      | `other`           | Defines equality based on the card's unique id        |
| `__hash__`     | Instance | `int`       | None              | Defines a hash value based on the card's unique id    |

### Implementation Details

**`__init__(self, question: Question) -> None`**
- Initialize a new Card instance.
- Set `self.id` to a new UUID using `uuid.uuid4()`.
- Set `self.question` to the provided `question` parameter.
- Set `self.last_asked` to `None`.

**`ask(self) -> str`**
- Update `self.last_asked` to the current time using `datetime.now()`.
- Return the result of calling `self.question.ask()`.

**`check_answer(self, answer: str) -> bool`**
- Return the result of calling `self.question.check_answer(answer)`.

**`reset(self) -> None`**
- Set `self.last_asked` to `None`.

**`__repr__(self) -> str`**
- Return a string representation of the Card object in the format:
  `f"Card(id={self.id}, question={repr(self.question)}, last_asked={self.last_asked})"`

**`__eq__(self, other)`**
- Return `True` if `other` is an instance of `Card` and its `id` is equal to `self.id`.
- Return `False` otherwise.

**`__hash__(self)`**
- Return the hash value of `self.id`.

## Example Usage

Here's an example of how to create and use a Card:

```python
from ars.card import Card
from ars.qtype.shortanswer import ShortAnswer

# Create a question
question = ShortAnswer("What is the capital of France?", "Paris")

# Create a Card with the question
card = Card(question)

# Ask the question
print(card.ask())

# Check an answer
user_answer = input("Your answer: ")
if card.check_answer(user_answer):
    print("Correct!")
else:
    print("Incorrect.")

# Print the card object
print(repr(card))

# Reset the card
card.reset()
```