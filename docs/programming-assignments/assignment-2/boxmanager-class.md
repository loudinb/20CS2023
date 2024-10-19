# `BoxManager` Class

The `BoxManager` class manages multiple boxes in the Adaptive Review System. It handles the organization and movement of questions between different boxes based on the user's performance.

Follow the specifications provided below to create a `BoxManager` class in the `boxmanager.py` file.

## Attributes

| Name                | Kind     | Access Level | Type                   | Description                                    |
|---------------------|----------|--------------|------------------------|------------------------------------------------|
| `_boxes`            | Instance | Protected    | `List[Box]`            | List of boxes managed by the BoxManager        |
| `_question_location`| Instance | Protected    | `Dict[uuid.UUID, int]` | Dictionary mapping question IDs to box indices |

## Methods

| Name                 | Kind     | Return Type        | Parameters                            | Description                                           |
|----------------------|----------|---------------------|-----------------------------------------|-------------------------------------------------------|
| `__init__`           | Instance | None                | None                                    | Initialize a new BoxManager instance                  |
| `add_new_question`   | Instance | None                | `question: Question`                    | Add a new question to the Unasked Questions box       |
| `move_question`      | Instance | None                | `question: Question, answered_correctly: bool` | Move a question based on whether it was answered correctly |
| `get_next_question`  | Instance | `Optional[Question]`| None                                    | Determine and return the next question to present     |
| `_log_box_counts`    | Instance | None                | None                                    | Log the number of questions in each box               |

### Implementation Details

**`BoxManager` Class**
- Implement the `BoxManager` class.
- Add a docstring to describe the class.
  ```python
  """Manages multiple boxes in the Adaptive Review System."""
  ```

**`__init__(self)`**
- Initialize the `BoxManager` instance with predefined boxes.
- Add a docstring to describe the method.
  ```python
  """Initialize a new BoxManager instance."""
  ```
- Create the following boxes and add them to the `_boxes` list:
  1. "Missed Questions" with a priority interval of 60 seconds
  2. "Unasked Questions" with a maximum priority interval of 0 seconds (no delay)
  3. "Correctly Answered Once" with a priority interval of 180 seconds
  4. "Correctly Answered Twice" with a priority interval of 360 seconds
  5. "Known Questions" with a maximum priority interval
- Initialize the `_question_location` dictionary as an empty dictionary.

**`add_new_question(self, question)`**
- Implement this method to add a new question to the Unasked Questions box (index 1).
- Add a docstring to describe the method.
  ```python
  """Add a new question to the Unasked Questions box.
  
  Args:
      question (Question): The question to add.
  """
  ```
- Add the question to the second box in `_boxes` (index 1).
- Update the `_question_location` dictionary with the question's ID and box index (1).

**`move_question(self, question, answered_correctly)`**
- Implement this method to move a question based on whether it was answered correctly.
- Add a docstring to describe the method.
  ```python
  """Move a question based on whether it was answered correctly.
  
  Args:
      question (Question): The question to move.
      answered_correctly (bool): True if the question was answered correctly, False otherwise.
  """
  ```
- Get the current box index from `_question_location` using the question's ID and assign it to a variable named `current_box`.
- Set a variable named `new_box` to the index of the box the question will be moved to based on the following rules:
  - If answered correctly:
    - If the current box is 0 (Missed Questions), set the new box 2 (Correctly Answered Once)
    - Otherwise, move to the next box (minimum of current box + 1 and the last box index)
  - If answered incorrectly, move to box 0 (Missed Questions)
- Remove the question from the current box.
- Add the question to the new box.
- Update the `_question_location` dictionary with the new box index.
- Call `_log_box_counts()` to log the updated box counts.

**`get_next_question(self) -> Optional[Question]`**
- Implement this method to determine and return the next question to present.
- Add a docstring to describe the method.
  ```python
  """Determine and return the next question to present.
  
  Returns:
      Optional[Question]: The next question to present, or None if no question is available.
  """
  ```
- Iterate through all boxes except the last one (Known Questions):
  - Call `get_next_priority_question()` on each box.
  - If a question is returned, return that question.
- If no question is found in any box, return None.


### Testing the `BoxManager` Class

The following example demonstrates how to use the `BoxManager` class to manage questions and move them between boxes based on the user's performance.

```python
from ars.qtype.shortanswer import ShortAnswer
from ars.boxmanager import BoxManager

# Create a BoxManager
box_manager = BoxManager()

# Create some questions
q1 = ShortAnswer("What's the capital of France?", "Paris")

# Add questions to the BoxManager
box_manager.add_new_question(q1)

# Get the next question
next_question = box_manager.get_next_question()
if next_question:
    print(next_question.ask())
    user_answer = input("Your answer: ")
    correct = next_question.check_answer(user_answer)
    if correct:
        print("Correct!")
    else:
        print(next_question.incorrect_feedback())
    box_manager.move_question(next_question, correct)
```
