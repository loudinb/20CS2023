# `Box` Class

The `Box` class represents a container for questions in the Adaptive Review System. It manages a set of questions and provides methods for adding, removing, and retrieving questions based on priority.

Follow the specifications provided below to create a `Box` class in the `box.py` file. The module-level docstring should be:

```python
"""Module for the Box class in the Adaptive Review System."""
```

## Attributes

| Name                | Kind     | Access Level | Type             | Description                                    |
|---------------------|----------|--------------|------------------|------------------------------------------------|
| `_name`             | Instance | Protected    | `str`            | Name of the box                                |
| `_questions`        | Instance | Protected    | `List[Question]` | List of questions in the box                   |
| `_priority_interval`| Instance | Protected    | `timedelta`      | Time interval for prioritizing questions       |

## Methods

| Name                      | Kind     | Return Type        | Parameters           | Description                                           |
|---------------------------|----------|---------------------|----------------------|-------------------------------------------------------|
| `__init__`                | Instance | None                | `name: str, priority_interval: timedelta` | Initialize a new Box instance |
| `name`                    | Property | `str`               | None                 | Get the name of the box                               |
| `priority_interval`       | Property | `timedelta`         | None                 | Get the priority interval of the box                  |
| `add_question`            | Instance | None                | `question: Question` | Add a question to the box (if not already present)    |
| `remove_question`         | Instance | None                | `question: Question` | Remove a question from the box                        |
| `get_next_priority_question` | Instance | `Optional[Question]` | None              | Return the next priority question if available        |
| `__len__`                 | Instance | `int`               | None                 | Return the number of questions in the box             |
| `__str__`                 | Instance | `str`               | None                 | Return a string representation of the Box object      |

### Implementation Details

**`class Box`**
- Define the `Box` class.
- The class docstring should be:
  ```python
  """Represents a box that holds a set of questions for adaptive review."""
  ```

**`__init__(self, name, priority_interval)`**
- Implement the constructor method for the `Box` class.
- The docstring should be:
  ```python
  """Initialize a new Box instance.

  Args:
      name (str): The name of the box.
      priority_interval (timedelta): The time interval for prioritizing questions.
  """
  ```
- Set the `_name` attribute to the `name` parameter.
- Initialize the `_questions` attribute as an empty list.
- Set the `_priority_interval` attribute to the `priority_interval` parameter.

**`name(self)`**
- Implement this property to return the value of the `_name` attribute.
- The docstring should be:
  ```python
  """Returns the name of the box."""
  ```

**`priority_interval(self)`**
- Implement this property to return the value of the `_priority_interval` attribute.
- The docstring should be:
  ```python
  """Returns the priority interval of the box."""
  ```

**`add_question(self, question)`**
- Implement this method to add a question to the box.
- The docstring should be:
  ```python
  """Add a question to the box.

  Args:
      question (Question): The question to be added.
  """
  ```
- Check if the question is not already in `_questions` before adding it. Append it to the list only if not present.

**`remove_question(self, question: Question) -> None`**
- Implement this method to remove a question from the box.
- The docstring should be:
  ```python
  """Remove a question from the box.

  Args:
      question (Question): The question to be removed.
  """
  ```
- Check if the question is in `_questions` before removing it.
- If the question is in `_questions`, remove it from the list.

**`get_next_priority_question(self) -> Optional[Question]`**
- Implement this method to return the next priority question if available.
- The docstring should be:
  ```python
  """Return the next priority question if available.

  Returns:
      Optional[Question]: The next priority question or None if no priority question is available.
  """
  ```
- Create a variable named `sorted_questions` to store a sorted copy of the `_questions` list based on the `last_asked` attribute, so the oldest questions are at the beginning.  
- Create a variable named `now` to store the current time using `datetime.now()`.
- Iterate through the questions in `sorted_questions`:
  - If the time since it was last asked (e.g., `now - question.last_asked`) is greater than or equal to the `_priority_interval`, return that question.
- If no priority question is found, return `None`.

**`__len__(self)`**
- Implement this method to return the number of questions in the box.
- The docstring should be:
  ```python
  """Return the number of questions in the box."""
  ```
- Return the length of the `_questions` list.

**`__str__(self)`**
- Implement this method to return a string representation of the `Box` object.
- The docstring should be:
  ```python
  """Return a string representation of the Box object."""
  ```
- Return a string that includes the name of the box and the number of questions in the box.

### Testing the `Box` Class

To test the `Box` class, you can create an instance of the class, add some questions to it, and retrieve the next priority question. Here's an example of how to use the `Box` class:

```python
from datetime import timedelta
from time import sleep

from ars.box import Box
from ars.qtype.shortanswer import ShortAnswer

# Create a box
review_box = Box("Review Box", timedelta(seconds=30))

# Create some questions
q1 = ShortAnswer("What's the capital of France?", "Paris")

# Add questions to the box
review_box.add_question(q1)

print(review_box)  # Output: Box(name='Review Box', questions_count=1)

# Ask the question, which updates the last_asked property to the current time
print(q1.ask())  # Output: "What's the capital of France?"

# Get the next priority question
# Since the question was just asked, it won't be returned
next_question = review_box.get_next_priority_question()
if next_question:
    print(next_question.ask())
else:
    print("No priority question available")

sleep(31)  # Wait for the priority interval to pass

# Get the next priority question
# Since the question was asked more than 30 seconds ago, it will be returned
next_question = review_box.get_next_priority_question()
if next_question:
    print(next_question.ask())
```