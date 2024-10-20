# `BoxManager` Class

The `BoxManager` class manages multiple boxes in the Adaptive Review System. It handles the organization and movement of questions between different boxes based on the user's performance.

Follow the specifications provided below to create a `BoxManager` class in the `boxmanager.py` file. The module-level docstring should be:

```python
"""Module for managing boxes in the Adaptive Review System."""
```

## Attributes

| Name                | Kind     | Access Level | Type                   | Description                                    |
|---------------------|----------|--------------|------------------------|------------------------------------------------|
| `_boxes`            | Instance | Protected    | `List[Box]`            | List of boxes managed by the BoxManager        |
| `_question_location`| Instance | Protected    | `Dict[str, int]`       | Dictionary mapping question IDs (as strings) to box indices |

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
  """Initialize a new BoxManager instance.

  Creates predefined boxes with specific priority intervals:
      - "Missed Questions": 60 seconds
      - "Unasked Questions": 0 seconds (no delay)
      - "Correctly Answered Once": 180 seconds
      - "Correctly Answered Twice": 360 seconds
      - "Known Questions": timedelta.max
  """
  ```
- Create the following boxes and add them to the `_boxes` list:
  1. "Missed Questions" with a priority interval of 60 seconds
  2. "Unasked Questions" with a maximum priority interval of 0 seconds (no delay)
  3. "Correctly Answered Once" with a priority interval of 180 seconds
  4. "Correctly Answered Twice" with a priority interval of 360 seconds
  5. "Known Questions" with a `timedelta.max` priority interval
- Initialize the `_question_location` dictionary as an empty dictionary, using string representations of the question IDs as keys.

**`add_new_question(self, question)`**
- Implement this method to add a new question to the Unasked Questions box (index 1).
- Add a docstring to describe the method.
  ```python
  """Add a new question to the Unasked Questions box.
  
  Args:
      question (Question): The question to add.
  
  The question's ID is stored as a string key in the `_question_location` dictionary.
  """
  ```
- Add the question to the second box in `_boxes` (index 1).
- Update the `_question_location` dictionary with `str(question.id)` as the key and the box index (1) as the value.

**`move_question(self, question, answered_correctly)`**
- Implement this method to move a question based on whether it was answered correctly.
- Add a docstring to describe the method.
  ```python
  """Move a question based on whether it was answered correctly.
  
  Args:
      question (Question): The question to move.
      answered_correctly (bool): True if the question was answered correctly, False otherwise.
  
  Moves the question to a new box based on the current box and the correctness of the answer.
  Updates `_question_location` with the new index and logs the box counts.
  """
  ```
- Get the current box index from `_question_location` using `str(question.id)`.
- Set a variable named `new_box` to determine the next box:
  - If answered correctly:
    - If the current box is 0 (Missed Questions), set the new box to 2 (Correctly Answered Once)
    - Otherwise, move to the next box (minimum of current box + 1 and the last box index)
  - If answered incorrectly, move to box 0 (Missed Questions)
- Remove the question from the current box.
- Add the question to the new box.
- Update `_question_location` with the new index.
- Call `_log_box_counts()`.

**`get_next_question(self) -> Optional[Question]`**
- Implement this method to determine and return the next question to present.
- Add a docstring to describe the method.
  ```python
  """Determine and return the next question to present.
  
  Returns:
      Optional[Question]: The next question to present, or None if no question is available.
  
  Iterates through all boxes except the "Known Questions" box to find the next priority question.
  """
  ```
- Iterate through all boxes except the last one (Known Questions):
  - Call `get_next_priority_question()` on each box.
  - If a question is returned, return that question.
- If no question is found in any box, return None.

**`_log_box_counts(self)`**
- Implement this method to log the number of questions in each box.
- Add a docstring to describe the method.
  ```python
  """Log the number of questions in each box by name and count.

  Useful for tracking the distribution of questions across the system.
  """
  ```
- Log the name and question count for each box to monitor the distribution of questions across the system.

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
