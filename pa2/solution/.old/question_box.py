
class QuestionBox:
    """A container for storing quiz questions with an index."""

    def __init__(self, index):
        """Initializes a QuestionBox.

        Args:
            index (int): The identifier for the box.
            items (list): A list of items (questions) in the box.
        """
        self.index = index
        self.items = []

    def add(self, item):
        """Adds an item (question) to the box.

        Args:
            item (str): The question to add.
        """
        self.items.append(item)

    def remove(self, item):
        """Removes an item (question) from the box.

        Args:
            item (str): The question to remove.
        """
        self.items.remove(item)

    def __len__(self):
        """Returns the number of items in the box.

        Returns:
            int: The number of items in the box.
        """
        return len(self.items)

    def __repr__(self):
        """Returns a string representation of the QuestionBox.

        Returns:
            str: String showing the index and item count.
        """
        return f"{self.__class__.__name__}(index={self.index}, items_count={len(self.items)})"

