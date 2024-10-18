## Instructions for Implementing the `ShortAnswer` Class

In this task, you will implement the `ShortAnswer` class, which represents a short answer type of quiz question. This class should inherit from the `Question` abstract base class, ensuring that it adheres to the required structure of having methods to get the question and check the answer.

Follow the steps below to implement the `ShortAnswer` class:

1. **Create Module:**

   Create a new Python file (e.g., `short_answer.py`) to contain the `ShortAnswer` class.


2. **Import Necessary Modules:**
   
   Start by importing the `Question` class from your existing module. This will allow your `ShortAnswer` class to inherit from it.

   ```python
   from question import Question
   ```

2. **Define the `ShortAnswer` Class:**
   
    Define the `ShortAnswer` class, ensuring it inherits from `Question`. This will enforce the implementation of the `get_question` and `check_answer` methods.

    ```python
    class ShortAnswer(Question):
        """A quiz item representing a short answer question.
   
        Attributes:
           question: The question text with an expected short answer response.
           correct_answer: The correct answer string.
           case_sensitive: Boolean indicating if the answer checking should be case-sensitive.
        """
    ```

3. **Implement the `__init__` Method:**
   
    The constructor method, `__init__`, should be designed to **accept three parameters**: `question`, `correct_answer`, and `case_sensitive`.  The `case_sensitive` parameter should set a default value of `True`.  Each parameter will be used to **initialize the corresponding instance attributes**. 

4. **Implement the `get_question` Method:**
   
   This method should return the question string. Ensure that the method matches the return type specified in the abstract base class.


5. **Implement the `check_answer` Method:**

   This method should take an answer as input and return a boolean indicating whether the answer is correct.  It should account for whether the answer checking is case-sensitive. Use `strip()` to remove any leading or trailing spaces from the answers.


6. **Implement the `__repr__` Method:**
   
   This method should provide a string representation of the `ShortAnswer` object, making it easier to debug and test.

7. **Test Your Implementation:**

   Test your implementation of the `ShortAnswer` class by running the provided test cases. Ensure that the class functions as expected and passes all the tests.

   ```bash
   python -m unittest tests_short_answer.py
   ```