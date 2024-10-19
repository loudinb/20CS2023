# `TrueFalse` Class

The `TrueFalse` class represents a true/false question in the Adaptive Review System. It inherits from the `Question` base class and implements specific behavior for true/false questions.

Follow the specifications provided below to create a `TrueFalse` class in the `truefalse.py` file within the `qtype` directory.

## Attributes

| Name          | Kind     | Access Level | Type     | Description                                    |
|---------------|----------|--------------|----------|------------------------------------------------|
| `_explanation`| Instance | Protected    | `str`    | Additional information explaining the answer   |

Note: This class also inherits all attributes from the `Question` base class.

## Methods

| Name                 | Kind     | Return Type | Parameters                                        | Description                                           |
|----------------------|----------|-------------|---------------------------------------------------|-------------------------------------------------------|
| `__init__`           | Instance | None        | `question: str, answer: bool, explanation: Optional[str] = None` | Initialize a new TrueFalse instance |
| `ask`                | Instance | `str`       | None                                              | Return the true/false question                        |
| `check_answer`       | Instance | `bool`      | `answer: str`                                     | Check if the provided answer is correct               |
| `incorrect_feedback` | Instance | `str`       | None                                              | Return feedback for an incorrect answer               |

### Implementation Details

**`__init__(self, question: str, answer: bool, explanation: Optional[str] = None) -> None`**
- Call the superclass `__init__` method with `question` and `answer` parameters.
- Validate that the `answer` is a boolean. If not, raise a `ValueError` with the message "The answer must be a boolean (True or False)."
- Set the `_explanation` attribute to the `explanation` parameter if provided, or an empty string if not.

**`ask(self) -> str`**
- Override the `ask` method from the base class.
- Call the superclass `ask` method to update the `_last_asked` timestamp.
- Return the question text appended with " (True/False)".

**`check_answer(self, answer: str) -> bool`**
- Implement this method to check if the provided answer is correct.
- Normalize the input `answer` by stripping whitespace and converting to lowercase.
- Convert the normalized answer to a boolean:
  - If the answer is "true" or "t", set `user_answer` to `True`.
  - If the answer is "false" or "f", set `user_answer` to `False`.
  - For any other input, raise a `ValueError` with the message "Answer must be 'True' or 'False'."
- Return `True` if `user_answer` matches the `_answer` attribute, `False` otherwise.

**`incorrect_feedback(self) -> str`**
- Implement this method to return feedback for an incorrect answer.
- Return a string that includes "Incorrect." followed by the explanation.

Remember to import the necessary modules at the beginning of your file:

```python
from typing import Optional
from .question import Question
```

Here's an example of how to use the `TrueFalse` class:

```python
tf_question = TrueFalse(
    question="Python is a statically typed language.",
    answer=False,
    explanation="Python is actually a dynamically typed language."
)

print(tf_question.ask())  # Outputs: Python is a statically typed language. (True/False)

user_input = input("Your answer (True/False): ")
if tf_question.check_answer(user_input):
    print("Correct!")
else:
    print(tf_question.incorrect_feedback())
```

This example demonstrates creating a TrueFalse question, asking it, checking the user's answer, and providing feedback.