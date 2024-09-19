# IPython Shell

IPython (Interactive Python) is an advanced command shell for Python that offers enhanced features beyond the standard Python interpreter. Unlike the built-in Python shell, IPython is a separate package that needs to be installed before use. It provides a significantly more powerful and user-friendly environment for interactive computing, making it a popular choice among data scientists, researchers, and Python developers.

## Installation

To use IPython, you need to install it first. You can easily install IPython using pip, Python's package installer:

### Option 1: Using pip (Python Package Installer)

You can easily install IPython using pip, which is the default package installer for Python:

```
pip install ipython
```

### Option 2: Using conda

If you're using Miniconda, you can install IPython using conda:

```
conda install ipython
```

Once installed through either method, you can launch IPython by simply typing `ipython` in your terminal or command prompt.


```{image} ../ipython-shell/ipython-shell.png
:alt: ipython-shell
:align: left
```

<br>

## Key Features

### Tab Completion

IPython offers intelligent tab completion, which helps you:
- Complete variable names, function names, and file paths
- View available methods for objects
- Explore module contents

Example:
```python
import math
math.<TAB>  # Shows all available methods and attributes in the math module
```

### Magic Commands

Magic commands are special commands prefixed with `%` (line magics) or `%%` (cell magics). They provide quick access to various system and IPython-specific functionalities.

Some useful magic commands:
- `%timeit`: Time the execution of a Python statement or expression
- `%run`: Run a Python script within the IPython environment
- `%paste`: Paste and execute code from clipboard
- `%history`: View command history

```python
%timeit [i**2 for i in range(1000)]
```

Now using cell magics:

```python
%%timeit
   ...: import random
   ...: numbers = [random.randint(1, 100) for _ in range(1000)]
   ...: sorted_numbers = sorted(numbers)
   ...: 
   ...: 
```

For a comprehensive list and detailed explanations of all available magic commands in IPython, refer to the official IPython documentation on [Built-in magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html).
 

### Rich Display System

IPython can display rich media outputs, including:
- Plots and graphics (with matplotlib integration)
- HTML
- LaTeX equations
- DataFrames (with pandas integration)

```python
from IPython.display import Math

Math(r'f(x) = \int_{-\infty}^x e^{-t^2} dt')
```

```{note}
When you see <IPython.core.display.Math object>, it means that IPython has created the Math object, but your current environment doesn't support rendering it visually. This typically happens in text-only interfaces.
``` 

### Shell Commands

Execute system shell commands directly from the IPython prompt using the `!` prefix.

```python
!ls -l  # List files in the current directory
```

### Dynamic Object Introspection

Use `?` after an object to view its docstring and other information:

```python
len?  # View information about the len() function
```

Use `??` to view the source code (if available):

```python
def greet(name):
    """A simple greeting function"""
    return f"Hello, {name}!"

greet??  # This will show both the docstring and the source code
```

```{note}
`??` works for viewing source code of functions defined in Python. It may not show source for built-in functions implemented in C (like len()) or for compiled libraries (like numpy).
```

### Input/Output History

IPython maintains a history of inputs and outputs:
- Access previous inputs with Up/Down arrow keys
- Reference previous outputs using `_`, `__`, or `_<n>` (where n is the output number)

```python
# First command
In [1]: 10 + 20
Out[1]: 30

# Second command
In [2]: "Hello, " + "World!"
Out[2]: 'Hello, World!'

# Third command - using previous output
In [3]: _ + "!!!"  # Uses the output of the previous command
Out[3]: 'Hello, World!!!'

# Fourth command - using output from two commands ago
In [4]: __ + 5  # Uses the output from two commands ago (the 30 from In [1])
Out[4]: 35

# Fifth command - referencing a specific previous output
In [5]: _2 + " How are you?"  # References the output of the second command
Out[5]: 'Hello, World! How are you?'

# Using Up arrow to recall and modify a previous command
# (Press Up twice to get to "10 + 20", then edit it)
In [6]: 10 + 25  # Modified from the first command
Out[6]: 35
```

### Debugger Integration

IPython provides powerful debugging capabilities through magic commands. Here's how you can use `%debug` and `%pdb` to debug exceptions:

#### Using `%debug`:

With `%debug`, you can enter the debugger after an exception has occurred.  When in the debugger, you can use various commands:

- `p` or `print`: Print the value of an expression
- `n` or `next`: Execute the next line
- `s` or `step`: Step into a function call
- `c` or `continue`: Continue execution until the next breakpoint
- `q` or `quit`: Quit the debugger


Example:
```python
In [1]: def divide(a, b):
   ...:     return a / b
   ...: 

In [2]: divide(10, 0)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
...

In [3]: %debug
> <ipython-input-1-4aaf9b4a8054>(2)divide()
      1 def divide(a, b):
----> 2     return a / b
      3 

ipdb> p a  # 'p' is a command meaning 'print'. This prints the value of 'a'
10
ipdb> p b  # This prints the value of 'b'
0
ipdb> p a + b  # You can also print expressions
10
ipdb> n  # 'n' means 'next', it will execute the next line
ZeroDivisionError: division by zero
ipdb> q  # 'q' means 'quit', it exits the debugger

In [4]: 
```

In this example:
- We use `p a` to print the value of `a`, not because `p` is a variable, but because `p` is the debugger command for "print".
- Similarly, `q` is used to quit the debugger, not because it's a variable, but because it's the command for "quit".


#### Using `%pdb`:

With `%pdb`, you can set IPython to automatically enter the debugger when an exception occurs:

```python
In [4]: %pdb on

In [5]: divide(10, 0)
Automatic pdb calling has been turned ON

---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-5-6528ad3c0aa6> in <module>
----> 1 divide(10, 0)

<ipython-input-1-4aaf9b4a8054> in divide(a, b)
      1 def divide(a, b):
----> 2     return a / b
      3 

ZeroDivisionError: division by zero

> <ipython-input-1-4aaf9b4a8054>(2)divide()
      1 def divide(a, b):
----> 2     return a / b
      3 

ipdb> p a
10
ipdb> p b
0
ipdb> q

In [6]: %pdb off

In [7]: 
```

Here, we turn on automatic debugging with `%pdb on`. When the exception occurs, we're immediately dropped into the debugger. After inspecting variables, we quit the debugger and turn off automatic debugging with `%pdb off`.

These debugging tools are invaluable for interactive troubleshooting, allowing you to inspect the state of your program at the point where an exception occurs.

## Configuration and Customization

IPython is highly configurable. You can create custom startup scripts, configure color schemes, and set up your own magic commands.  Refer to the official IPython documentation on [Configuration and customization](https://ipython.readthedocs.io/en/stable/config/index.html).
