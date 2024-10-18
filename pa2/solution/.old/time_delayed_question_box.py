import time
from pa2.solution.src.question_box import QuestionBox

class TimeDelayedQuestionBox(QuestionBox):
    """A question box with a time delay before items become eligible for reattempt.

    Attributes:
        reattempt_delay: The delay time (in seconds) before an item can be retried.
        items: A list of tuples, where each tuple contains an item and the timestamp when it was added.
    """

    def __init__(self, delay = 90):
        """Initializes the TimeDelayedQuestionBox with a specified delay.

        Args:
            delay: The time delay in seconds before an item becomes eligible for reattempt. Defaults to 90 seconds.
        """
        super().__init__(0)  # Always set index to 0
        self.reattempt_delay = delay
        self.items = []  # Store (item, timestamp) tuples

    def add(self, item):
        """Adds an item to the question box with the current timestamp.

        Args:
            item: The item to be added.
        """
        self.items.append((item, time.time()))

    def remove(self, item):
        """Removes an item from the question box.

        Args:
            item: The item to be removed.
        """
        self.items = [entry for entry in self.items if entry[0] != item]

    def get_eligible(self):
        """Retrieves a list of items that are eligible for reattempt based on the delay.

        Returns:
            A list of items that have been in the box for at least the reattempt delay.
        """
        current_time = time.time()
        return [item for item, timestamp in self.items if current_time - timestamp >= self.reattempt_delay]

    def __repr__(self):
        """Returns a string representation of the TimeDelayedQuestionBox.

        Returns:
            A string representing the TimeDelayedQuestionBox object.
        """
        return (f"{self.__class__.__name__}(index=0, reattempt_delay={self.reattempt_delay}, "
                f"items_count={len(self.items)})")
