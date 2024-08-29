# Style Guide

Style guides help developers write clean, consistent code. They are essential in programming for several reasons:

- Improve code readability
- Make collaboration easier
- Maintain consistency across projects
- Prevent certain classes of errors

Various Python style guides exist, including:

- [Python Enhancement Proposal (PEP) 8](https://pep8.org) (the official Python style guide)
- [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org)

While these guides may differ in specifics, they all promote clean, readable, and maintainable code.

## Consistency

The most crucial aspect of following a style guide is applying it consistently throughout your project or organization. Consistency reduces cognitive load for developers and facilitates easier collaboration and maintenance.

## Google's Python Style Guide

We will adopt [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html) in this course. It's based on PEP 8 but includes modifications for Google's specific needs, especially for collaboration and large-scale codebases.

```{note}
Become familiar with [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html).
```

### Preliminary Aspects to Follow

Here are the preliminary aspects of the style guide that you should follow as you begin your Python programming journey:

#### Line Length

- Maximum line length is 80 characters
- Exceptions allowed for long import statements and URLs in comments

```python
# Good
short_string = "This is a short string."

# Bad (exceeds 80 characters)
long_string = "This is a very long string that exceeds the recommended 80 character limit and should be broken up."
```

#### Indentation

- Use 4 spaces per indentation level
- Never use tabs or mix tabs and spaces

```python
# Good
def good_function():
    if True:
        print("Properly indented")

# Bad
def bad_function():
  if True:
        print("Inconsistent indentation")
```

#### Whitespace

- Follow standard typographic rules for spaces around punctuation
- No whitespace inside parentheses, brackets, or braces

```python
# Good
spam(ham[1], {eggs: 2})

# Bad
spam( ham[ 1 ], { eggs: 2 } )
```

#### Strings

- Use format method or f-strings for string formatting
- Avoid using `+` and `+=` operators to accumulate strings in loops

```python
# Good
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I'm {age} years old."

# Bad
bad_string = "My name is " + name + " and I'm " + str(age) + " years old."
```

#### Comments and Docstrings

- Use docstrings for modules, functions, classes, and methods
- Use inline comments sparingly
- All comments should be complete sentences
- Use `TODO` comments for temporary code or short-term solutions

```python
def calculate_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    # TODO: Consider using a more precise value of pi
    return 3.14 * radius ** 2
```

#### Naming Conventions

- `module_name`, `package_name`, `ClassName`, `method_name`, `ExceptionName`, `function_name`, `GLOBAL_CONSTANT_NAME`, `global_var_name`, `instance_var_name`, `function_parameter_name`, `local_var_name`

```python
class UserAccount:
    def __init__(self, username):
        self.username = username

    def display_info(self):
        print(f"Username: {self.username}")

MAX_USERS = 100
```

#### Imports

- Use `import x` for importing packages and modules
- Use `from x import y` where `x` is the package prefix and `y` is the module name
- Use `from x import y as z` if two modules named `y` are to be imported or if `y` is an inconveniently long name

```python
import os
from math import sqrt
from very_long_module_name import specific_function as sf
```

## Static Analysis Tools

Static analysis tools are software programs that examine source code without executing it. They analyze the structure, syntax, and sometimes the logic of the code to identify potential issues, bugs, or violations of coding standards. These tools are valuable across various programming languages for improving code quality, maintaining consistency, and catching errors early in the development process.

### Style Checkers

In Python, some static analysis tools focus on checking style guide consistency without modifying the code. Tools like Pylint, Flake8, Pycodestyle, Pyflakes, and Pydocstyle analyze Python code for adherence to style conventions, such as PEP 8. They identify issues like improper indentation, naming violations, and docstring formatting problems. These style checkers provide reports that help developers understand and manually correct style inconsistencies.

### Code Formatters

Code formatters can be considered a specialized type of static analysis tool. Unlike style checkers, they automatically modify the code to adhere to style guidelines. They fix indentation, spacing, alignment, line breaks, and other aspects of code appearance. These tools work by automatically reformatting the code (typically on file save) to preemptively avoid many basic style errors. While they perform static analysis, their distinguishing feature is the automatic modification of the source code.