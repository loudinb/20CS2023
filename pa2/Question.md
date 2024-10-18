## Instructions for Implementing the `Question` Class

The `Question` class serves as an **abstract base class (ABC)** for all quiz items. It defines the basic structure and methods that any quiz item must implement. This allows for a flexible and consistent way to create various types of quiz questions (e.g., multiple-choice, true/false, fill-in-the-blank).

Follow the steps below to implement the `Question` class:

1. **Create Module:**

   Create a new Python file (e.g., `question.py`) to contain the `Question` class.

2. **Import Necessary Modules:**

   Begin by importing the `ABC` and `abstractmethod` from the `abc` module. This allows you to create an abstract base class that cannot be instantiated directly.

   ```python
   from abc import ABC, abstractmethod
   ```

3. **Define the `Question` Class:**

   Create the `Question` class by inheriting from `ABC`. This makes it an abstract base class.

   ```python
   class Question(ABC):
       """Abstract base class for quiz items."""
   ```

4. **Define `get_question` Abstract Method:**

   The `get_question` method should return the question text as a string.


5. **Define `check_answer` Abstract Method:**

   The `check_answer` method should take an answer as input and return a boolean indicating whether the answer is correct.


6. **Implement the `__repr__` Method:**

   Implement the `__repr__` method to provide a string representation of the `Question` object. This can be useful for debugging and testing.