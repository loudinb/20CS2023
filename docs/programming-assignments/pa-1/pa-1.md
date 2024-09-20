# Assignment 1

```{warning}
I am currently updating this assignment to improve the instructions and provide more detailed guidance. There were too many complications that I felt distracted from understanding the core implementation of OOP in Python. Please wait for a few days as I make these updates. If you have any questions or need assistance, feel free to reach out to me.
```


**Instagram-like Application Using Object-Oriented Programming (OOP)**

In this assignment, you will implement an Instagram-like application using **Object-Oriented Programming (OOP)** principles in Python. The application will simulate basic social media functionalities, including user creation, following, posting, commenting, and messaging. The focus will be on two core OOP principles: **encapsulation** and **composition**.

## OOP Concepts in the Assignment

The assignment will require you to apply various OOP concepts to design and implement the Instagram-like application. Here are some key concepts that you will use:

### Instance Attributes and Methods

Instance attributes are specific to each object instance, and instance methods operate on those individual instances. Each object has its own copy of the instance attributes, and instance methods can modify those attributes.

```python
class User:
    def __init__(self, username: str, email: str):
        self.username = username  # Instance attribute
        self.email = email        # Instance attribute

    def create_post(self, content: str) -> None:  # Instance method
        # Create a post
        pass
```

### Class Attributes and Class Methods

Class attributes are shared among all instances of a class, meaning they maintain a single value across all objects. Class methods operate on the class itself and can modify class attributes but not instance attributes.

```python
class User:
    user_count = 0  # Class attribute shared among all instances

    @classmethod
    def get_user_count(cls) -> int:  # Class method
        return cls.user_count
```

### Static Methods

Static methods are independent of the class state and do not modify class or instance attributes. They are typically utility functions that logically belong to the class but do not need to access or modify class/instance data.

```python
class User:
    @staticmethod
    def is_valid_username(username: str) -> bool:  # Static method
        # Validate the username
        return len(username) > 2
```

### Properties

The `@property` decorator is used to define a method as a property, which allows access to an attribute through getter and setter methods. This provides control over how attributes are accessed and modified, enabling validation and constraints.

```python
class User:
    def __init__(self, username: str, email: str):
        self._bio = ""  # Protected attribute
        self.username = username
        self.email = email

    @property
    def bio(self) -> str:  # Property getter
        return self._bio

    @bio.setter
    def bio(self, value: str) -> None:  # Property setter
        if len(value) <= 150:
            self._bio = value
        else:
            raise ValueError("Bio cannot exceed 150 characters.")
```

### Data Encapsulation (Public, Protected, and Private Attributes)

Encapsulation controls how attributes are accessed and modified, allowing for restricted access when necessary:

- **Public attributes** (`attribute`): Accessible from anywhere, including outside the class. These are used for attributes that are safe for external access.
- **Protected attributes** (`_attribute`): Indicated by a single leading underscore, these are meant for internal use within the class and its subclasses. They can still be accessed externally, but this is discouraged by convention.
- **Private attributes** (`__attribute`): Indicated by a double leading underscore, these are restricted to the class itself. They cannot be accessed or modified directly from outside the class or its subclasses due to name-mangling, which ensures stronger encapsulation.

```python
class User:
    def __init__(self, username: str, email: str):
        self.username = username  # Public attribute: accessible from anywhere
        self._bio = ""  # Protected attribute: intended for internal use or subclasses
        self.__id = 123  # Private attribute: only accessible within this class
```

### Composition (Classes Containing Instances of Other Classes)

Composition is the practice of building complex objects by including instances of other classes as attributes. This allows you to model relationships where one object is "composed" of others.

In this example, the `Post` class contains a `User` object as the author of the post. Each post is associated with its author and content.

```python
class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.posts = []  # Composition: A user can have multiple posts

class Post:
    def __init__(self, content: str, author: User):
        self.content = content
        self.author = author  # Composition: The post has a user as its author
```

## Python Syntax in the Assignment

There are several Python features and syntax elements that you will use in this assignment to implement the Instagram-like application. We have not covered all of them in detail, so I will provide a brief overview of some key concepts:

### Regular Expressions

Regular expressions (regex) are powerful tools for pattern matching and string manipulation. They can be used to validate input, extract specific information, or perform complex text processing tasks.

For example, you can use regex to validate email addresses:

```python
import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None
```

### Date and Time Handling

Python's `datetime` module provides classes for working with dates and times. You can use these classes to handle timestamps, time differences, and date formatting.

```python
from datetime import datetime

current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
```

### Raising a ValueError

When validating input or enforcing constraints, you can raise a `ValueError` to indicate that the input is invalid. This allows you to handle errors and exceptions gracefully.

```python
def set_username(self, username: str) -> None:
    if len(username) > 3:
        self.username = username
    else:
        raise ValueError("Username must be at least 3 characters long.")
```
