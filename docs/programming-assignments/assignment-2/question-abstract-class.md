# `Question` Class

The `Question` class is an abstract base class that represents a quiz question in the Adaptive Review System. It provides a foundation for different types of questions and includes common attributes and methods.

Follow the specifications provided below to create a `Question` class in the `question.py` file within the `qtype` directory.

## Attributes

| Name          | Kind     | Access Level | Type               | Description                                    |
|---------------|----------|--------------|--------------------|------------------------------------------------|
| `_id`         | Instance | Protected    | `uuid.UUID`        | Unique identifier for the question             |
| `_question`   | Instance | Protected    | `str`              | The text of the question                       |
| `_answer`     | Instance | Protected    | `Any`              | The correct answer to the question             |
| `_last_asked` | Instance | Protected    | `Optional[datetime]` | Timestamp of when the question was last asked |

## Methods

| Name                 | Kind       | Return Type        | Parameters     | Description                                           |
|----------------------|------------|---------------------|----------------|-------------------------------------------------------|
| `__init__`           | Instance   | None                | `question: str, answer: Any` | Initialize a new Question instance       |
| `id`                 | Property   | `uuid.UUID`         | None           | Get the unique identifier of the question             |
| `last_asked`         | Property   | `Optional[datetime]` | None           | Get the timestamp of when the question was last asked |
| `ask`                | Abstract   | `str`               | None           | Return the question as a string                       |
| `check_answer`       | Abstract   | `bool`              | `answer: Any`  | Check if the provided answer is correct               |
| `incorrect_feedback` | Abstract   | `str`               | None           | Return feedback for an incorrect answer               |
| `reset`              | Instance   | None                | None           | Reset the last asked time                             |
| `__eq__`             | Instance   | `bool`              | `other: object` | Define equality based on the question's unique id     |
| `__hash__`           | Instance   | `int`               | None           | Define a hash value based on the question's unique id |
| `__repr__`           | Instance   | `str`               | None           | Return a string representation of the Question object |

### Implementation Details

**`def Question(ABC):`**
- Implement the `Question` class as an abstract base class using the `ABC` metaclass.

**`__init__(self, question: str, answer: Any) -> None`**
- Implement the `__init__` method to initialize a new `Question` instance.
- Set the `_question` attribute to the `question` parameter.
- Set the `_answer` attribute to the `answer` parameter.
- Generate a unique `UUID` for the `_id` attribute using `uuid.uuid4()`.
- Initialize the `_last_asked` attribute to `None`.

**`id(self) -> uuid.UUID`**
- Implement this property to return the value of the `_id` attribute.

**`last_asked(self) -> Optional[datetime]`**
- Implement this property to return the value of the `_last_asked` attribute.

**`ask(self) -> str`**
- Implement this method to return the question as a string.
- Update the `_last_asked` attribute with the current timestamp using `datetime.now()`.
- Return the value of the `_question` attribute.

**`reset(self) -> None`**
- Implement this method to reset the `_last_asked` attribute to `None`.

**`check_answer(self, answer: Any) -> bool`**
- Add this **abstract** method to check if the provided answer is correct.
- The implementation should be provided by subclasses.

**`incorrect_feedback(self) -> str`**
- Implement this **abstract** method to return feedback for an incorrect answer.
- The implementation should be provided by subclasses.

**`__eq__(self, other: object) -> bool`**
- Implement this method to define equality based on the question's unique id.
- Return `True` if `other` is an instance of `Question` and its `id` matches this question's `id`.
- Return `False` otherwise.

**`__hash__(self) -> int`**
- Implement this method to define a hash value based on the question's unique id.
- Return the hash of the `_id` attribute.

