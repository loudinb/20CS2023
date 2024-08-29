# String Type

[Strings](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) (a.k.a. text sequence type) are a fundamental data type in Python, representing sequences of characters.

- Represented by the `str` class
- Can be enclosed in single (`'`) or double (`"`) quotes.
- Double quotes: "allows embedded 'single' quotes"
- Triple quoted: '''Three single quotes''' or  """Three double quotes""" may span multiple lines.

```python
single_quoted = 'Hello, World!'
double_quoted = "Hello, World!"
multiline = """Hello,
World!"""
```

## Escape Sequences and Raw Strings
Sometimes you need to include special characters in strings. Escape sequences and raw strings help you achieve this.

### Escape Sequences
Escape sequences allow you to include special characters in strings:

- `\n`: Newline
- `\t`: Tab
- `\\`: Backslash
- `\'`: Single quote
- `\"`: Double quote

Example:
```python
print("Hello\nWorld")  # Outputs: Hello
                       #          World
print("Tab\tspace")    # Outputs: Tab     space
```

### Raw Strings
Raw strings treat backslashes as literal characters, useful for regular expressions and file paths:

```python
path = r"C:\Users\Alice\Documents"
print(path)  # Outputs: C:\Users\Alice\Documents
```
## Operations on Strings

The Python string type supports various operations, including concatenation, repetition, indexing, slicing, and more. 

### Concatenation
Use the `+` operator to concatenate strings:

```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # "John Doe"
```

### Repetition
Use the `*` operator to repeat strings:

```python
echo = "Hello" * 3  # "HelloHelloHello"
```

### Indexing and Slicing
Access individual characters or substrings:

```python
text = "Python"
print(text[0])     # "P"
print(text[1:4])   # "yth"
print(text[::-1])  # "nohtyP" (reverse)
```

## String Methods
Python provides many built-in methods for string manipulation, there are over **40** string methods available. Some common methods include:

- `upper()`: Convert to uppercase
- `lower()`: Convert to lowercase
- `strip()`: Remove leading and trailing whitespace
- `split()`: Split string into a list
- `join()`: Join list elements into a string
- `replace()`: Replace substrings

Examples:
```python
text = "  Hello, World!  "
print(text.upper())          # "  HELLO, WORLD!  "
print(text.strip())          # "Hello, World!"
print(text.split(","))       # ["  Hello", " World!  "]
print("-".join(["a", "b"]))  # "a-b"
print(text.replace("o", "0"))  # "  Hell0, W0rld!  "
```

## String Formatting
String formatting in Python allows you to create dynamic strings by inserting values into placeholders. There are three main methods for string formatting in Python:

- f-strings (formatted string literals, Python 3.6+)
- The `str.format()` method
- The `%` operator (old-style formatting, really should be avoided)

### f-strings (Formatted String Literals)

Introduced in Python 3.6, [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) provide a concise and readable way to embed expressions inside string literals.

Syntax:
```python
f"string with {expression} placeholders"
```

Examples:
```python
name = "Charlie"
age = 35
print(f"My name is {name} and I'm {age} years old.")
# Output: My name is Charlie and I'm 35 years old.

# Expressions in f-strings
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}.")
# Output: The sum of 10 and 20 is 30.

# Formatting options
pi = 3.14159
print(f"Pi rounded to two decimal places: {pi:.2f}")
# Output: Pi rounded to two decimal places: 3.14
```


### The `str.format()` Method

The [`str.format()`](https://docs.python.org/3/library/string.html#format-string-syntax) method allows you to insert values into placeholders within a string.  This method is suited for more complex formatting scenarios.

Syntax:
```python
"string with {} placeholders".format(value1, value2)
```

Examples:
```python
name = "Bob"
age = 25
print("My name is {} and I'm {} years old.".format(name, age))
# Output: My name is Bob and I'm 25 years old.

# Using numbered placeholders
print("The {1} is {0}.".format("blue", "sky"))
# Output: The sky is blue.

# Using named placeholders
print("The {color} is {object}.".format(color="blue", object="sky"))
# Output: The blue is sky.
```

### The `%` Operator (Old-String Formatting)

The [`%`](https://docs.python.org/3/library/stdtypes.html#old-string-formatting) operator is the oldest method of string formatting in Python. While it's still supported, it's generally considered less readable and flexible than newer methods.  It should be avoided in new code.

Syntax:
```python
"string with %s placeholder" % value
```

Examples:
```python
name = "Alice"
age = 30
print("My name is %s and I'm %d years old." % (name, age))
# Output: My name is Alice and I'm 30 years old.
```

### String Format Specifiers

Format specifiers define how values are formatted within placeholders. The format string method and f-strings share a common syntax for format specifiers.  Here's how the formatters translate across the methods:

| %-formatting | str.format() | f-strings | Description |
|--------------|--------------|-----------|-------------|
| `%s`         | `{}`         | `{}`      | String |
| `%d`         | `{:d}`       | `{:d}`    | Integer |
| `%f`         | `{:f}`       | `{:f}`    | Float |
| `%.2f`       | `{:.2f}`     | `{:.2f}`  | Float with 2 decimal places |
| `%r`         | `{!r}`       | `{!r}`    | Any object (uses `repr()`) |
| `%c`         | `{:c}`       | `{:c}`    | Character |
| `%x`         | `{:x}`       | `{:x}`    | Hexadecimal (lowercase) |
| `%X`         | `{:X}`       | `{:X}`    | Hexadecimal (uppercase) |

```{note}
For complete details on format specifiers, refer to the [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec) section in the official Python documentation.
```