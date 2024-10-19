# `Question` Abstract Base Class

The `Question` abstract base class represents the foundation for all quiz questions in the Adaptive Review System (ARS). It defines the basic structure and interface that all specific question types must implement.

Follow the specifications provided below to create a `Question` abstract base class in the `ars/qtype/question.py` file.

## Class Definition

Create an abstract base class named `Question` that inherits from `ABC` (Abstract Base Class).

```python
from abc import ABC, abstractmethod

class Question(ABC):
    """Abstract base class for quiz items."""
    # Implementation details will go here
```

## Abstract Methods

| Name                      | Kind     | Return Type | Parameters     | Description                                           |
|---------------------------|----------|-------------|----------------|-------------------------------------------------------|
| `ask`                     | Abstract | `str`       | None           | Returns the question as a string                      |
| `check_answer`            | Abstract | `bool`      | `answer: str`  | Checks if the provided answer is correct              |
| `incorrect_answer_feedback` | Abstract | `str`     | None           | Returns feedback for an incorrect answer              |

### Implementation Details

**`ask(self) -> str`**
- Implement this method as an abstract method using the `@abstractmethod` decorator.
- This method should be implemented by subclasses to return the question text as a string.

```python
@abstractmethod
def ask(self) -> str:
    """Returns the question as a string."""
    pass
```

**`check_answer(self, answer: str) -> bool`**
- Implement this method as an abstract method using the `@abstractmethod` decorator.
- This method should be implemented by subclasses to check if the provided answer is correct.
- It should take a string `answer` as a parameter and return a boolean indicating whether the answer is correct.

```python
@abstractmethod
def check_answer(self, answer: str) -> bool:
    """Checks if the provided answer is correct.

    Args:
        answer: The answer to validate.

    Returns:
        True if the answer is correct, False otherwise.
    """
    pass
```

**`incorrect_answer_feedback(self) -> str`**
- Implement this method as an abstract method using the `@abstractmethod` decorator.
- This method should be implemented by subclasses to provide feedback when an incorrect answer is given.
- It should return a string containing the feedback message.

```python
@abstractmethod
def incorrect_answer_feedback(self) -> str:
    """Returns a response to display when the user provides an incorrect answer."""
    pass
```

## Additional Method

| Name     | Kind     | Return Type | Parameters | Description                                           |
|----------|----------|-------------|------------|-------------------------------------------------------|
| `__repr__` | Instance | `str`       | None       | Returns a string representation of the Question object |

### Implementation Details

**`__repr__(self) -> str`**
- Implement this method to return a string representation of the Question object.
- This method should be implemented in the base class and can be overridden by subclasses if needed.

```python
@abstractmethod
def __repr__(self) -> str:
    """Returns a string representation of the Question object."""
    pass
```