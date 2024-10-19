# `TrueFalse` Class

The `TrueFalse` class represents a true/false question in the Adaptive Review System (ARS). It inherits from the `Question` abstract base class and implements the specific behavior for true/false questions.

Follow the specifications provided below to create a `TrueFalse` class in the `ars/qtype/truefalse.py` file. Remember to import the `Question` abstract base class and inherit from it:

```python
from ars.qtype.question import Question

class TrueFalse(Question):
    # Implementation will go here
```

Ensure that all abstract methods from the `Question` class are implemented in the `TrueFalse` class.

## Attributes

| Name               | Kind     | Access Level | Type   | Description                                    |
|--------------------|----------|--------------|--------|------------------------------------------------|
| `_question`        | Instance | Protected    | `str`  | The text of the true/false question            |
| `_correct_answer`  | Instance | Protected    | `bool` | The correct answer (True or False)             |
| `_explanation`     | Instance | Protected    | `str`  | Additional explanation for the correct answer  |

## Methods

| Name                      | Kind     | Return Type | Parameters                                          | Description                                           |
|---------------------------|----------|-------------|-----------------------------------------------------|-------------------------------------------------------|
| `__init__`                | Instance | None        | `question: str, correct_answer: bool, explanation: str = ""` | Initialize a new TrueFalse instance                   |
| `ask`                     | Instance | `str`       | None                                                | Returns the question text                             |
| `check_answer`            | Instance | `bool`      | `answer: str`                                       | Checks if the provided answer is correct              |
| `incorrect_answer_feedback` | Instance | `str`     | None                                                | Returns feedback for an incorrect answer              |
| `__repr__`                | Instance | `str`       | None                                                | Returns a string representation of the TrueFalse object |

### Implementation Details

**`__init__(self, question: str, correct_answer: bool, explanation: str = "")`**
- Initialize a new TrueFalse question instance.
- Set `self._question` to the provided `question` parameter.
- Set `self._correct_answer` to the provided `correct_answer` parameter.
- Set `self._explanation` to the provided `explanation` parameter (default is an empty string).
- Raise a `ValueError` with the message "The correct_answer must be a boolean (True or False)." if `correct_answer` is not a boolean.

**`ask(self) -> str`**
- Implement this method to return the question text.
- The returned string should be in the format: "{self._question} (True/False)"

**`check_answer(self, answer: str) -> bool`**
- Implement this method to check if the provided answer is correct.
- Convert the input `answer` to lowercase and strip any leading/trailing whitespace.
- Return `True` if the normalized answer matches the correct answer:
  - If `answer` is "true" or "t", it should match `self._correct_answer == True`
  - If `answer` is "false" or "f", it should match `self._correct_answer == False`
- Return `False` for any other input.

**`incorrect_answer_feedback(self) -> str`**
- Implement this method to provide feedback when an incorrect answer is given.
- Return a string in the format: "Incorrect. {self._explanation}" if an explanation is provided.
- If no explanation is provided, return "Incorrect. The correct answer is {correct_answer}.", where `correct_answer` is "True" or "False" based on `self._correct_answer`.

**`__repr__(self) -> str`**
- Implement this method to return a string representation of the TrueFalse object.
- The returned string should be in the format: "TrueFalse(question='{self._question}', correct_answer={self._correct_answer})"

## Example Usage

Here's an example of how to create and use a TrueFalse question:

```python
from ars.qtype.truefalse import TrueFalse

# Create a TrueFalse question
question = TrueFalse("The Earth is flat.", False, "The Earth is actually an oblate spheroid.")

# Ask the question
print(question.ask())

# Check an answer
user_answer = input("Your answer (True/False): ")
if question.check_answer(user_answer):
    print("Correct!")
else:
    print(question.incorrect_answer_feedback())

# Print the question object
print(repr(question))
```