# `Message` Class

Create a `message.py` file and implement the `Message` class as follows:

### [Instance Attributes](#pa1-instance-attributes):

- **`__content`**: A **private** string for message content, limited to 2000 characters.
- **`timestamp`**: A **public** `datetime` object for message creation time.

### [Instance Methods](#pa1-instance-methods):

1. **`__init__(self, content)`**: 
   - Parameters: `content` (str)
   - Set `__content` using the `content` property setter (which will validate the length).
   - Set `timestamp` to the current date and time using `datetime.now()`.

### [Instance Properties](#pa1-properties):

Properties are methods defined with the `@property` decorator to allow controlled access to the attributes and add validation logic.

2. **`content(self) `**: 
   - Implement a getter that returns the `__content` value.
   - Implement a setter that accepts a string value. If the new content is longer than 2000 characters, raise a `ValueError`. Otherwise, set `__content` to the new value.
