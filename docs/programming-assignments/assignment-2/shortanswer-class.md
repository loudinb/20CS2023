# `ShortAnswer` Class

The `ShortAnswer` class represents a short answer question in the Adaptive Review System. It inherits from the `Question` base class and implements specific behavior for short answer questions.

Follow the specifications provided below to create a `ShortAnswer` class in the `shortanswer.py` file within the `qtype` directory. Use the following for the module-level docstring:

```python
"""Module for the ShortAnswer quiz item class in the Adaptive Review System."""
```

## Attributes

| Name             | Kind     | Access Level | Type  | Description                                   |
|------------------|----------|--------------|-------|-----------------------------------------------|
| `_case_sensitive`| Instance | Protected    | `bool`| Flag to determine if answer is case sensitive |

Note: This class also inherits all attributes from the `Question` base class.

## Methods

| Name                 | Kind     | Return Type | Parameters                                        | Description                                           |
|----------------------|----------|-------------|---------------------------------------------------|-------------------------------------------------------|
| `__init__`           | Instance | None        | `question: str, answer: str, case_sensitive: bool = False` | Initialize a new ShortAnswer instance |
| `ask`                | Instance | `str`       | None                                              | Return the short answer question (inherited from `Question`)|
| `check_answer`       | Instance | `bool`      | `answer: str`                                     | Check if the provided answer is correct               |
| `incorrect_feedback` | Instance | `str`       | None                                              | Return feedback for an incorrect answer               |
| `_normalize`         | Instance | `str`       | `text: str`                                       | Normalize the text for comparison                     |

### Implementation Details

**`class ShortAnswer(Question)`**
- Define the `ShortAnswer` class that inherits from the `Question` base class.
- The class docstring should be:
  ```python
  """A quiz item representing a short answer question."""
  ```

**`__init__(self, question, answer, case_sensitive = False)`**
- Implement the constructor method to initialize a new `ShortAnswer` instance.
- The docstring should be:
  ```python
  """Initialize a short answer quiz item.

    Args:
        question (str): The question prompt.
        answer (str): The correct answer.
        case_sensitive (bool, optional): Whether the answer comparison should be case-sensitive. 
                                         Defaults to False.
  """
  ```
- Call the superclass `__init__` method with `question` and `answer` parameters.
- Set the `_case_sensitive` attribute to the `case_sensitive` parameter.

**`_normalize(self, text)`**
- Implement this private method to normalize the text for comparison.
- The docstring should be:
  ```python
  """Normalize the text for comparison.

  Args:
      text (str): The text to normalize.

  Returns:
      str: The normalized text.
  """
  ```
- Strip leading and trailing whitespace from the input `text`.
- If `_case_sensitive` is `False`, convert the text to lowercase.
- Remove all punctuation from the text using the following regular expression.
  ```python
  text = re.sub(r'[^\w\s]', '', text)
  ```
- Return the normalized text.

**`check_answer(self, answer)`**
- Implement this method to check if the provided answer is correct.
- The docstring should be:
  ```python
  """Check if the provided answer is correct.

  Args:
      answer (str): The provided answer.

  Returns:
      bool: True if the provided answer is correct, False otherwise.
  """
  ```
- Use the `_normalize` method to normalize both the provided answer and the correct answer.
- Return `True` if the normalized provided answer matches the normalized correct answer, `False` otherwise.

**`incorrect_feedback(self)`**
- Implement this method to return feedback for an incorrect answer.
- Add a docstring to describe the method.
  ```python
  """Return feedback for an incorrect answer.

  Returns:
      str: Feedback message for an incorrect answer.
  """
  ```
- Return a string that includes "Incorrect. The correct answer is: " followed by the correct answer as it was originally provided.

### Testing the `ShortAnswer` Class

To test the `ShortAnswer` class, you can create an instance of the class, ask the question, check the answer, and provide feedback based on the correctness of the answer. Here's an example of how to use the `ShortAnswer` class:

```python
from ars.qtype.shortanswer import ShortAnswer

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
