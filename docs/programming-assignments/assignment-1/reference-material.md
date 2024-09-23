# Reference Material

The following reference material provides syntax and examples for implementing the classes and various functionalities required for Assignment 1. You can refer to this material while working on the assignment.


(pa1-instance-attributes)=
## Instance Attributes 

Instance attributes are specific to each object instance, and instance methods operate on those individual instances. Each object has its own copy of the instance attributes, and instance methods can modify those attributes.

```python
class User:
    def __init__(self, username, email):
        self.username = username  # Instance attribute
        self.email = email        # Instance attribute
```

(pa1-instance-methods)=
## Instance Methods

Instance methods are functions that operate on individual instances of a class. They can access and modify both instance attributes and class attributes. They can access and modify instance attributes, perform operations specific to an object, and interact with other objects.

```python
class User:

    def create_post(self, content):  # Instance method
        # Create a post
        pass
```

(pa1-class-attributes)=
## Class Attributes 

Class attributes are shared among all instances of a class, meaning they maintain a single value across all objects. Class methods operate on the class itself and can modify class attributes but not instance attributes.

```python
class User:
    user_count = 0  # Class attribute shared among all instances

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1   # Accessing class attribute
```


(pa1-class-methods)=
## Class Methods

Class methods operate on the class itself and can modify class attributes but not instance attributes.  Class methods are defined using the `@classmethod` decorator and take the class itself as the first argument (`cls` by convention).

```python
class User:
    user_count = 0  # Class attribute shared among all instances

    @classmethod
    def get_user_count(cls) -> int:  # Class method
        return cls.user_count
```

(pa1-static-methods)=
## Static Methods

Static methods are independent of the class state and do not modify class or instance attributes. They are typically used for utility functions that belong logically to the class but do not require access to class or instance data. They are typically utility functions that logically belong to the class but do not need to access or modify class/instance data.  Static methods are defined using the `@staticmethod` decorator and do not take the class (e.g., `cls`) or instance (e.g., `self`) as the first argument.

```python
class User:
    @staticmethod
    def is_valid_username(username: str) -> bool:  # Static method
        # Validate the username
        return len(username) > 2
```

(pa1-properties)=
## Properties

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

(pa1-data-encapsulation)=
## Data Encapsulation (Public, Protected, and Private Attributes)

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

(pa1-composition)=
## Composition (Classes Containing Instances of Other Classes)

Composition is the practice of building complex objects by including instances of other classes as attributes. Unlike inheritance, where a class derives behavior from a parent class, composition models a 'has-a' relationship. It allows combining multiple objects to create more complex behavior. This allows you to model relationships where one object is "composed" of others.

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

(pa1-regular-expressions)=
## Regular Expressions

Regular expressions (regex) are powerful tools for pattern matching and string manipulation. They can be used to validate input, extract specific information, or perform complex text processing tasks.

For example, you can use regex to validate email addresses:

```python
import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def is_valid_phone_number(phone: str) -> bool:
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return re.match(pattern, phone) is not None
```

(pa1-date-time)=
## Date and Time Handling

Python's `datetime` module provides classes for working with dates and times. You can use these classes to handle timestamps, time differences, and date formatting.

```python
from datetime import datetime

current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
```

(pa1-value-error)=
## Raising a ValueError

When validating input or enforcing constraints, you can raise a `ValueError` to indicate that the input is invalid.

```python
def set_username(self, username: str) -> None:
    if len(username) > 3:
        self.username = username
    else:
        raise ValueError("Username must be at least 3 characters long.")
```

```{information}
Exceptions can then be caught using a `try-except` block for graceful error handling. You should not include this in your implementation, we will cover this more in the future.

```python
try:
    user.set_username("Jo")
except ValueError as e:
    print(f"Error: {e}")
```
```