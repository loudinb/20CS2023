# Python Scripts

A Python script is a file containing Python code that can be executed by the Python interpreter. These scripts are used to automate tasks, process data, and create applications. Python scripts typically have a `.py` file extension.

## Basic Elements of a Python Script

### Statements

A Python script consists of a sequence of statements. A statement is one or more lines of code that performs an action. For example:

```python
print("Hello, World!")
```


### Indentation

Python uses indentation to define code blocks. Unlike many other programming languages that use braces or keywords, Python relies on consistent indentation. This makes the code more readable but requires careful attention to spacing.

```python
if True:
    print("This is indented")
    if True:
        print("This is further indented")
print("This is not indented")
```

- Use 4 spaces for each indentation level (do not use tabs).
- Must be consistent with your indentation throughout the script.

### Comments

Comments are used to explain code and are ignored by the interpreter. Python supports single-line and multi-line comments.

```python
# This is a single-line comment

print("Hello, World!")  # This is an inline comment

"""
This is a multi-line comment
or docstring that can span
multiple lines
"""
```

### Line Continuation

Python statements typically end with a newline, but you can extend a statement over multiple lines:

- Implicitly inside parentheses, brackets, or braces:

```python
total = (1 + 2 + 3 +
         4 + 5 + 6)
```

- Using the backslash character:

```python
long_string = "This is a very long string that \
spans multiple lines."
```

## Example Script

A typical Python script looks like this:

```python
#!/usr/bin/env/python3

# Import statements (if needed)
import math

# Constants (if any)
PI = 3.14159

# Function definitions
def circle_area(radius):
    return PI * radius ** 2

# Main script execution
if __name__ == "__main__":
    radius = 5
    area = circle_area(radius)
    print(f"The area of a circle with radius {radius} is {area:.2f}")
```

Key points:
- The hashbang line (`#!/usr/bin/env python3`) is optional but useful for Unix-like systems.  It is a special construct that specifies the interpreter to be used for executing the script.
- Imports, if needed, typically go at the top of the script.
- Constants are often defined in ALL_CAPS.
- Function definitions come before they are used.
- The `if __name__ == "__main__":` block is not strictly required for simple scripts, but it's highly recommended. Google's Python Style Guide emphasizes that all Python files should be importable. Therefore, using this block to define the main entry point is considered best practice, even for simple scripts.

## Running Scripts

To run a Python script, you can use the command line and execute the script file directly by specifying the script's filename as the first argument to the Python interpreter:

```bash
(base) %python script.py
```

```{image} ../python-scripts/run-script.png
:alt: run-script
:align: left
```
