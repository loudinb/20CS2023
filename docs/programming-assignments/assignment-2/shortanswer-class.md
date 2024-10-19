# `ShortAnswer` Class

The `ShortAnswer` class represents a short answer question in the Adaptive Review System. It inherits from the `Question` base class and implements specific behavior for short answer questions.

Follow the specifications provided below to create a `ShortAnswer` class in the `shortanswer.py` file within the `qtype` directory.

## Attributes

| Name             | Kind     | Access Level | Type  | Description                                   |
|------------------|----------|--------------|-------|-----------------------------------------------|
| `_case_sensitive`| Instance | Protected    | `bool`| Flag to determine if answer is case sensitive |

Note: This class also inherits all attributes from the `Question` base class.

## Methods

| Name                 | Kind     | Return Type | Parameters                                        | Description                                           |
|----------------------|----------|-------------|---------------------------------------------------|-------------------------------------------------------|
| `__init__`           | Instance | None        | `question: str, answer: str, case_sensitive: bool = False` | Initialize a new ShortAnswer instance |
| `ask`                | Instance | `str`       | None                                              | Return the short answer question                      |
| `check_answer`       | Instance | `bool`      | `answer: str`                                     | Check if the provided answer is correct               |
| `incorrect_feedback` | Instance | `str`       | None                                              | Return feedback for an incorrect answer               |
| `_normalize`         | Instance | `str`       | `text: str`                                       | Normalize the text for comparison                     |

### Implementation Details

**`__init__(self, question: str, answer: str, case_sensitive: bool = False) -> None`**
- Call the superclass `__init__` method with `question` and `answer` parameters.
- Set the `_case_sensitive` attribute to the `case_sensitive` parameter.

**`ask(self) -> str`**
- Override the `ask` method from the base class.
- Call the superclass `ask` method to update the `_last_asked` timestamp.
- Return the question text (the `_question` attribute).

**`check_answer(self, answer: str) -> bool`**
- Implement this method to check if the provided answer is correct.
- Use the `_normalize` method to normalize both the provided answer and the correct answer.
- Return `True` if the normalized provided answer matches the normalized correct answer, `False` otherwise.

**`incorrect_feedback(self) -> str`**
- Implement this method to return feedback for an incorrect answer.
- Return a string that includes "Incorrect. The correct answer is: " followed by the correct answer.

**`_normalize(self, text: str) -> str`**
- Implement this private method to normalize the text for comparison.
- Strip leading and trailing whitespace from the input `text`.
- If `_case_sensitive` is `False`, convert the text to lowercase.
- Remove all punctuation from the text using a regular expression.
- Return the normalized text.

Remember to import the necessary modules at the beginning of your file:

```python
import re
from .question import Question
```

Here's an example of how to use the `ShortAnswer` class:

```python
sa_question = ShortAnswer(
    question="What is the capital of France?",
    answer="Paris",
    case_sensitive=False
)

print(sa_question.ask())  # Outputs: What is the capital of France?

user_input = input("Your answer: ")
if sa_question.check_answer(user_input):
    print("Correct!")
else:
    print(sa_question.incorrect_feedback())
```

This example demonstrates creating a ShortAnswer question, asking it, checking the user's answer, and providing feedback. The answer checking is case-insensitive by default, so "paris" would be accepted as a correct answer.