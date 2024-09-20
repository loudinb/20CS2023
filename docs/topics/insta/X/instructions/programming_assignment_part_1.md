# Programming Assignment - Part 1

**Instagram-like Application Using Object-Oriented Programming (OOP)**

In this assignment, you will implement an Instagram-like application using **Object-Oriented Programming (OOP)** principles in Python. The application will simulate basic social media functionalities, including user creation, following, posting, commenting, and messaging. The focus will be on two core OOP principles: **encapsulation** and **composition**.

This application will demonstrate the following OOP concepts and Python syntax:

### 1. Instance Attributes and Methods

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

### 2. Class Attributes and Class Methods

Class attributes are shared among all instances of a class, meaning they maintain a single value across all objects. Class methods operate on the class itself and can modify class attributes but not instance attributes.

```python
class User:
    user_count = 0  # Class attribute shared among all instances

    @classmethod
    def get_user_count(cls) -> int:  # Class method
        return cls.user_count
```

### 3. Static Methods

Static methods are independent of the class state and do not modify class or instance attributes. They are typically utility functions that logically belong to the class but do not need to access or modify class/instance data.

```python
class User:
    @staticmethod
    def is_valid_username(username: str) -> bool:  # Static method
        # Validate the username
        return len(username) > 2
```

### 4. Properties

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

### 5. Data Encapsulation (Public, Protected, and Private Attributes)

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

### 6. Composition (Classes Containing Instances of Other Classes)

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