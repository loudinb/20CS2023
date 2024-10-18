## Instructions for Implementing the `TimeDelayedQuestionBox` Class

In this task, you will implement a class called `TimeDelayedQuestionBox`, which extends the `QuestionBox` class. This specialized version introduces a time-based mechanism that delays when items become eligible for reattempt, making it useful for adaptive learning scenarios. Follow the steps below to implement the class.  Follow the steps below:

1. **Create Module:**

   Create a new Python file (e.g., `time_delayed_question_box.py`) to contain the `TimeDelayedQuestionBox` class.

2. **Import Necessary Modules:**

   Start by importing the `time` module and the `QuestionBox` class. The `time` module will be used to manage timestamps, while `QuestionBox` provides the base functionality.

   ```python
   import time
   from question_box import QuestionBox
   ```

3. **Define the `TimeDelayedQuestionBox` Class:**
   
   Create a new class named `TimeDelayedQuestionBox` that inherits from `QuestionBox`. This will allow you to build on the existing features of `QuestionBox` and add the time-delay functionality.

   ```python
   class TimeDelayedQuestionBox(QuestionBox):
       """A question box with a time delay before items become eligible for reattempt.

       Attributes:
           reattempt_delay: The delay time (in seconds) before an item can be retried.
           items: A list of tuples, where each tuple contains an item and the timestamp when it was added.
       """
   ```

4. **Implement the `__init__` Method:**
   
   The constructor method should accept a single parameter, `delay`, which determines how long (in seconds) an item must wait before it is eligible for reattempt. Set a **default value of `90` seconds**. Inside the method, initialize:
   
   - `self.reattempt_delay` to store the provided `delay`.
   - `self.items` as an empty list, which will store tuples containing the item and its timestamp.
   - Call `super().__init__(0)` to ensure the base class initializes with an index of `0`.

   ```python
   def __init__(self, delay=90):
       """Initializes the TimeDelayedQuestionBox with a specified delay.

       Args:
           delay: The time delay in seconds before an item becomes eligible for reattempt. Defaults to 90 seconds.
       """

       pass
   ```

5. **Create the `add` Method:**
   
   Implement the `add` method to add an item to `self.items` along with the current timestamp. Use the `time.time()` function to record when the item was added.

   ```python
   def add(self, item):
       """Adds an item to the question box with the current timestamp.

       Args:
           item: The item to be added.
       """
       
       pass
   ```

6. **Create the `remove` Method:**
   
   Define the `remove` method to delete an item from `self.items`. Ensure that you remove the tuple containing the specified item, regardless of the timestamp.

   ```python
   def remove(self, item):
       """Removes an item from the question box.

       Args:
           item: The item to be removed.
       """
       
       pass
   ```

7. **Implement the `get_eligible` Method:**
   
   This method should return a list of items that are eligible for reattempt, meaning they have been in the box for at least `self.reattempt_delay` seconds. Use the current time and compare it to the stored timestamp for each item.

   ```python
   def get_eligible(self):
       """Retrieves a list of items that are eligible for reattempt based on the delay.

       Returns:
           A list of items that have been in the box for at least the reattempt delay.
       """
       
       pass
   ```

8. **Create the `__repr__` Method:**
   
   Define a `__repr__` method to return a string representation of the `TimeDelayedQuestionBox`. This will help in debugging and understanding the current state of the object.

   ```python
   def __repr__(self):
       """Returns a string representation of the TimeDelayedQuestionBox.

       Returns:
           A string representing the TimeDelayedQuestionBox object.
       """
       
       pass
   ```
