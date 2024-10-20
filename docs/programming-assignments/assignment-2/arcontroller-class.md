# `ARController` Class

The `ARController` class serves as the main controller for running an adaptive review session. It manages the interaction between the user, questions, and the BoxManager.

Follow the specifications provided below to create an `ARController` class in the `arcontroller.py` file. The module-level docstring should be:

```python
"""Core module for running the Adaptive Review System (ARS) session."""
```

## Attributes

| Name           | Kind     | Access Level | Type         | Description                                    |
|----------------|----------|--------------|--------------|------------------------------------------------|
| `_box_manager` | Instance | Protected    | `BoxManager` | The BoxManager instance used by the controller |

## Methods

| Name                    | Kind     | Return Type | Parameters                  | Description                                           |
|-------------------------|----------|-------------|---------------------------|-------------------------------------------------------|
| `__init__`              | Instance | None        | `question_data: List[dict]` | Initialize a new ARController instance                |
| `_initialize_questions` | Instance | None        | `question_data: List[dict]` | Initialize questions and add them to the BoxManager   |
| `start`                 | Instance | None        | None                        | Run the interactive adaptive review session           |

### Implementation Details

**`ARController` Class**
- Add the `ARController` class.
- Add a docstring with a brief description of the class.
  ```python
  """Main controller for running an adaptive review session."""
  ```

**`__init__(self, question_data)`**
- Initialize the `ARController` instance with the given `question_data`.
- Add a docstring with a brief description of the method.
  ```python
  """Initialize the Adaptive Review Controller.

  Args:
      question_data (List[Dict[str, Any]]): A list of dictionaries containing question data.
  """
  ```
- Create a new `BoxManager` instance and assign it to `_box_manager`.
- Call `_initialize_questions` with the `question_data`.

**`_initialize_questions(self, question_data)`**
- Implement this private method to initialize questions and add them to the BoxManager.
- Add a docstring with a brief description of the method.
  ```python
  """Initialize questions and place them in the Unasked Questions box.

  Args:
      question_data (List[Dict[str, Any]]): A list of dictionaries containing question data.
  """
  ```
- Iterate through the `question_data` list:
  - For each question dictionary, get the `type` key.
  - Use the `try-except` block to create either a `ShortAnswer` or `TrueFalse` question and add it to the BoxManager:
    - **Try Block:**
      - If `"shortanswer"` type, create a `ShortAnswer` instance with `question`, `correct_answer`, and `case_sensitive` (default to `False` if not provided).
      - If `"truefalse"` type, create a `TrueFalse` instance with `question`, `correct_answer`, and `explanation` (default to an empty string if not provided).
      - If the question type is not supported, print a message and `continue` to the next question.
      - Add the created `question` to the BoxManager using `add_new_question`.
    - **Except Block:**
      - Handle any `KeyError` exceptions that might occur due to missing required fields, print an error message, and skip the question.

**`start(self) -> None`**
- Implement this method to run the interactive adaptive review session.
- Add a docstring with a brief description of the method.
  ```python
  """Run the interactive adaptive review session."""
  ```
- Print a message and instructions for quitting the session.
  ```python
  print("Type 'q' at any time to quit the session.")
  ```
- Enter a loop that continues until all questions have been reviewed:
  - Get the next question from the BoxManager using `get_next_question`.
  - If there are no more questions, print "All questions have been reviewed. Session complete!" and `break` from the loop.
  - Print the question using the `ask` method.
  - Get the user's answer as input and assign it to a variable named `user_answer`.
  - If the user enters 'q', `break` the loop to quit the session.
  - Check if `user_answer` is correct using the question's `check_answer` method.
  - Print "Correct!" if the answer is correct; otherwise, print the `incorrect_feedback` as provided by the question.
  - Move the question in the BoxManager based on whether it was answered correctly.
- Print "Thank you, goodbye!" when the session ends.

### Testing the `ARController` Class

You can test the `ARController` using the following sample code:

```python
from ars.arcontroller import ARController

# Sample question data
question_data = [
    {
        "type": "shortanswer",
        "question": "What's the capital of France?",
        "correct_answer": "Paris"
    },
    {
        "type": "truefalse",
        "question": "The Earth is flat.",
        "correct_answer": False,
        "explanation": "The Earth is actually approximately spherical."
    }
]

# Create and start the Adaptive Review Controller
controller = ARController(question_data)
controller.start()
```