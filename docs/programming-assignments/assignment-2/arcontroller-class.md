# `ARController` Class

The `ARController` class serves as the main controller for running an adaptive review session in the Adaptive Review System. It manages the interaction between the user, questions, and the BoxManager.

Follow the specifications provided below to create an `ARController` class in the `arcontroller.py` file.

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

**`__init__(self, question_data: List[dict]) -> None`**
- Initialize the `ARController` instance with the given `question_data`.
- Create a new `BoxManager` instance and assign it to `_box_manager`.
- Call `_initialize_questions` with the `question_data`.

**`_initialize_questions(self, question_data: List[dict]) -> None`**
- Implement this private method to initialize questions and add them to the BoxManager.
- Iterate through the `question_data` list:
  - For each question dictionary, get the `type` key.
  - Based on the question type, create either a `ShortAnswer` or `TrueFalse` question:
    - For "shortanswer" type:
      - Create a `ShortAnswer` instance with `question`, `correct_answer`, and `case_sensitive` (default to False if not provided) from the dictionary.
    - For "truefalse" type:
      - Create a `TrueFalse` instance with `question`, `correct_answer`, and `explanation` (default to empty string if not provided) from the dictionary.
  - If the question type is not supported, print a message and continue to the next question.
  - Add the created question to the BoxManager using `add_new_question`.
  - Handle any `KeyError` exceptions that might occur due to missing required fields, print an error message, and skip the question.

**`start(self) -> None`**
- Implement this method to run the interactive adaptive review session.
- Print a welcome message and instructions for quitting the session.
- Enter a loop that continues until all questions have been reviewed:
  - Get the next question from the BoxManager using `get_next_question`.
  - If there are no more questions, print a completion message and break the loop.
  - Print the question using the `ask` method.
  - Get the user's answer as input.
  - If the user enters 'q', break the loop to quit the session.
  - Check if the answer is correct using the question's `check_answer` method.
  - Print "Correct!" if the answer is correct, otherwise print the `incorrect_feedback`.
  - Move the question in the BoxManager based on whether it was answered correctly.
- Print a thank you message when the session ends.

Remember to import the necessary modules at the beginning of your file:

```python
from typing import List
from .boxmanager import BoxManager
from .qtype.shortanswer import ShortAnswer
from .qtype.truefalse import TrueFalse
```

Here's an example of how to use the `ARController` class:

```python
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

This example demonstrates creating an ARController with sample question data and starting the adaptive review session. The session will continue until the user quits or all questions have been reviewed.