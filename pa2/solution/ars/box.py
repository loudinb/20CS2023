"""Module for the Box class in the Adaptive Review System."""

from datetime import datetime, timedelta
from typing import List, Optional
from .qtype.question import Question

class Box:
    """Represents a box that holds a set of questions for adaptive review."""

    def __init__(self, name: str, priority_interval: timedelta) -> None:
        """Initialize a box with a name and priority interval."""
        self._name: str = name
        self._questions: List[Question] = []
        self._priority_interval: timedelta = priority_interval


    @property
    def name(self) -> str:
        """Returns the name of the box."""
        return self._name

    @property
    def priority_interval(self) -> timedelta:
        """Returns the priority interval of the box."""
        return self._priority_interval
    
    
    def add_question(self, question: Question) -> None:
        """Add a question to the box."""
        if question not in self._questions:
            self._questions.append(question)

    def remove_question(self, question: Question) -> None:
        """Remove a question from the box."""
        if question in self._questions:
            self._questions.remove(question)

    def get_next_priority_question(self) -> Optional[Question]:
        """Return the next priority question if available."""
        now = datetime.now()
        for question in self._questions:
            if question.last_asked is None or (now - question.last_asked) >= self._priority_interval:
                return question
        return None

    def __len__(self) -> int:
        """Return the number of questions in the box."""
        return len(self._questions)

    def __repr__(self) -> str:
        """Return a string representation of the Box object."""
        return f"Box(name='{self._name}', questions_count={len(self._questions)})"