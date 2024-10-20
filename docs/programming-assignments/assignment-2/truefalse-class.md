# `TrueFalse` Class

The `TrueFalse` class represents a true/false question in the Adaptive Review System. It inherits from the `Question` base class and implements specific behavior for true/false questions.

Follow the specifications provided below to create a `TrueFalse` class in the `truefalse.py` file within the `qtype` directory.  The module level docstring should be:

```python
"""Module for the TrueFalse quiz item class in the Adaptive Review System."""
```

## Attributes

| Name          | Kind     | Access Level | Type     | Description                                    |
|---------------|----------|--------------|----------|------------------------------------------------|
| `_explanation`| Instance | Protected    | `str`    | Additional information explaining the answer   |

Note: This class also inherits all attributes from the `Question` base class.

## Methods

| Name                 | Kind     | Return Type | Parameters                                        | Description                                           |
|----------------------|----------|-------------|---------------------------------------------------|-------------------------------------------------------|
| `__init__`           | Instance | None        | `question: str, answer: bool, explanation: str = ""` | Initialize a new TrueFalse instance |
| `ask`                | Instance | `str`       | None                                              | Return the true/false question                        |
| `check_answer`       | Instance | `bool`      | `answer: str`                                     | Check if the provided answer is correct               |
| `incorrect_feedback` | Instance | `str`       | None                                              | Return feedback for an incorrect answer               |

### Implementation Details

**`class TrueFalse(Question)`**
- Define the `TrueFalse` class that inherits from the `Question` class.
- Add a docstring to describe the class.
  ```python
  """Class for a True/False quiz item."""
  ```

**`__init__(self, question, answer, explanation = "")`**
- Implement the `__init__` method to initialize a new `TrueFalse` instance.
- Add a docstring to describe the method.
  ```python
  """Initialize a true/false quiz item.
        
    Args:
        question (str): The question to be displayed.
        answer (bool): The correct answer, either True or False.
        explanation (str, optional): Additional information to explain the correct answer.

    Raises:
        ValueError: If the answer is not a boolean.
  """ 
  ```
- Call the superclass `__init__` method with `question` and `answer` parameters.
- Validate that the `answer` is a boolean. If not, raise a `ValueError` with the message "The answer must be a boolean (True or False)."
- Set the `_explanation` attribute to the `explanation` parameter.

**`ask(self) -> str`**
- Override the `ask` method from the base class.
- Add a docstring to describe the method.
  ```python
  """Return the true/false question text."""
  ```
- Call the superclass `ask` method to update the `_last_asked` timestamp.
- Return the question text appended with " (True/False)".

**`check_answer(self, answer: str) -> bool`**
- Implement this method to check if the provided answer is correct.
- Add a docstring to describe the method.
  ```python
  """Check if the provided answer is correct.
        
    Args:
        answer (str): The user's answer to the question.
        
    Returns:
        bool: True if the answer is correct, False otherwise.
        
    Raises:
        ValueError: If the answer is not 'True' or 'False'.
    """
    ```
- Normalize the input `answer` by stripping whitespace and converting to lowercase.
- Convert the normalized answer to a boolean:
  - If the normalized answer is "true" or "t", set `user_answer` to `True`.
  - If the normalized answer is "false" or "f", set `user_answer` to `False`.
  - For any other input, raise a `ValueError` with the message "Answer must be 'True' or 'False'."
- Return `True` if `user_answer` matches the `_answer` attribute, `False` otherwise.

**`incorrect_feedback(self) -> str`**
- Implement this method to return feedback for an incorrect answer.
- Add a docstring to describe the method.
  ```python
  """Return feedback for an incorrect answer.

  Returns:
      str: Feedback message for an incorrect answer, including the explanation if provided.
  """
  ```
- Return a string that includes "Incorrect." followed by the explanation, only if `_explanation` is not an empty string.

### Testing the `TrueFalse` Class

To test the `TrueFalse` class, you can create an instance of the class, ask the question, check the answer, and provide feedback based on the correctness of the answer. Here's an example:

```python
from ars.qtype.truefalse import TrueFalse

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