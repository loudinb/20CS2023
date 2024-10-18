## Instructions for Implementing the `QuestionBox` Class

Your task is to implement a Python class named `QuestionBox` that will be used to manage quiz questions. Follow the instructions below to create the `QuestionBox` class.

Follow the steps below:

1. **Create Module:**

   Create a new Python file (e.g., `question_box.py`) to contain the `QuestionBox` class.


2. **Define the `QuestionBox` Class:**
   
   Define the `QuestionBox` class. 

    ```python
    class QuestionBox:
        """A container for storing quiz questions with an index.

        Attributes:
           index: The index of the given box.
           items: A list of questions.
       """
   ```

2. **Implement the `__init__` Method:**
   
   The constructor method, `__init__`, should be designed to accept a single parameter, `index`, which serves as an identifier for the `QuestionBox`. This parameter should be an integer that uniquely identifies the specific box. The `index` attribute should be set to the value of the `index` parameter.  The `items` attribute should be initialized as an empty list.

   ```python
    def __init__(self, index):
        """Initializes a QuestionBox.

        Args:
            index (int): The identifier for the box.
            items (list): A list of items (questions) in the box.
        """
        
        pass
    ```
3. **Create the `add` Method:**
   
   Define a method named `add` that accepts a single argument, `item`. This method will append the provided `item` (a quiz question) to the `items` list.

   ```python
   def add(self, item):
       """Adds an item (question) to the box.

       Args:
           item (str): The question to add.
       """

       pass
   ```
4. **Create the `remove` Method:**
   
   Define a method named `remove` that accepts a single argument, `item`. This method will remove the specified `item` (a quiz question) from the `items` list. Assume that the `item` exists in the list.

   ```python
   def remove(self, item):
       """Removes an item (question) from the box.

       Args:
           item (str): The question to remove.
       """
   
       pass
   ```

5. **Implement the `__len__` Method:**
   
   Add a special method, `__len__`, which returns the number of items (questions) in the `QuestionBox`. This allows you to use the `len()` function on instances of `QuestionBox`.

   ```python
   def __len__(self):
       """Returns the number of items in the box.

       Returns:
           int: The number of items in the box.
       """

       pass
   ```

6. **Create the `__repr__` Method:**
   
   Implement the `__repr__` method to provide a string representation of the `QuestionBox`. This will make it easier to understand what the box contains when you print it.

   The method should return a string that includes the class name, the index of the box, and the count of items currently stored in the box.

   ```python
   def __repr__(self):
       """Returns a string representation of the QuestionBox.

       Returns:
           str: String showing the index and item count.
       """

       pass
   ```

7. **Test Your Implementation:**

    Test your implementation of the `QuestionBox` class by running the provided test cases. Ensure that the class functions as expected and passes all the tests.
    
    ```bash
    python -m unittest tests_question_boxes.py
    ```