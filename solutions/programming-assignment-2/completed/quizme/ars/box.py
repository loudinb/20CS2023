"""Module for the Box class in the Adaptive Review System."""
from datetime import datetime

class Box:
    """Represents a box that holds a set of questions for adaptive review."""

    def __init__(self, name, priority_interval):
        """Initialize a new Box instance.

        Args:
            name (str): The name of the box.
            priority_interval (timedelta): The time interval for prioritizing questions.
        """
        self._name: str = name
        self._questions = []
        self._priority_interval = priority_interval

    @property
    def name(self):
        """Returns the name of the box."""
        return self._name
    
    @property
    def priority_interval(self):
        """Returns the priority interval of the box."""
        return self._priority_interval
    
    def add_question(self, question):
        """Add a question to the box.

        Args:
            question (Question): The question to be added.
        """
        if question not in self._questions:
            self._questions.append(question)

    def remove_question(self, question):
        """Remove a question from the box.

        Args:
            question (Question): The question to be removed.
        """
        if question in self._questions:
            self._questions.remove(question)

    def get_next_priority_question(self):
        """Return the next priority question if available."""
        now = datetime.now()
        sorted_questions = sorted(self._questions, key=lambda question: question.last_asked)
        for question in sorted_questions:
            if (now - question.last_asked) >= self._priority_interval:
                return question
        return None
    

    def __len__(self):
        """Return the number of questions in the box."""
        return len(self._questions)
    

    def __str__(self):
        """Return a string representation of the Box object."""
        return f"Box(name='{self._name}', questions_count={len(self._questions)})"
