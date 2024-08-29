# Variables and Data Types

This topic covers the basics of declaring variables, naming conventions, basic data types, type conversion, multiple assignments, and constants in Python.

## Variables
Variables are fundamental building blocks in Python programming. They allow you to store and manipulate data in your programs.

### Declaring Variables
In Python, you don't need to explicitly declare a variable's type. Simply assign a value to a variable name, and Python will infer its type:

```python
x = 5  # Integer
y = 3.14  # Float
name = "Alice"  # String
is_student = True  # Boolean
```

```{admonition} Duck Typing
Python uses "duck typing," meaning it focuses on an object's behavior rather than its type. If an object has the methods and properties needed for a particular operation, Python allows it, regardless of the object's actual type. This approach is based on the saying: _"If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."_
```

### Naming Conventions
- Use lowercase letters, numbers, and underscores
- Start with a letter or underscore, not a number
- Be descriptive but concise
- Use snake_case for multi-word names

Examples:
```python
user_name = "John"
total_score = 95
_private_variable = "Secret"
```

#### Reserved Keywords

Python has 33 reserved keywords that cannot be used as variable names. These keywords are used to define the structure and logic of the program.

```
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
```

## Data Types

Python uses dynamic typing, where the data type is automatically determined based on the value assigned to a variable. 

### Basic Data Types

The most fundamental of the built-in data types include:

1. Numeric Types:
   - int (integer): Whole numbers, e.g., `5`, `-3`, `1000000`
   - float (floating-point): Decimal numbers, e.g., `3.14`, `-0.001`, `2.0`
   - complex: Complex numbers, e.g., `1 + 2j`, `3 - 4j`

2. Boolean Type:
   - bool: Represents truth values, either `True` or `False`

3. String Type:
   - str: Sequence of characters, e.g., `"Hello, World!"`, `'Python'`

### Other Data Types

Python also provides several built-in composite data types, including:

1. Sequence Types:
   - list: Ordered, mutable sequence, e.g., `[1, 2, 3]`, `['a', 'b', 'c']`
   - tuple: Ordered, immutable sequence, e.g., `(1, 2, 3)`, `('x', 'y', 'z')`
   - range: Immutable sequence of numbers, e.g., `range(5)`, `range(1, 10, 2)`

2. Mapping Type:
   - dict (dictionary): Key-value pairs, e.g., `{"name": "Alice", "age": 25}`

3. Set Types:
   - set: Unordered collection of unique elements, e.g., `{1, 2, 3}`
   - frozenset: Immutable version of set, e.g., `frozenset([1, 2, 3])`

4. None Type:
   - NoneType: Represents the `None` object, which indicates absence of a value

5. Binary Types:
   - bytes: Immutable sequence of bytes, e.g., `b'hello'`
   - bytearray: Mutable sequence of bytes, e.g., `bytearray([65, 66, 67])`

```{note}
External libraries like NumPy and Pandas provide additional data types for scientific computing and data analysis.
```

## Type Conversion
You can convert between types using built-in functions:

```python
x = 5
y = float(x)  # Convert int to float
z = str(x)  # Convert int to string
```

## Multiple Assignments
Python allows you to assign values to multiple variables in one line:

```python
a, b, c = 1, 2, 3
x = y = z = 0
```

## Constants
Python doesn't have built-in constant types, but it's a convention to use uppercase names for constants:

```python
PI = 3.14159
MAX_USERS = 100
```
