# Lecture 10, Sep 26, 2024

This is our final lecture on OOP in Python, focusing on abstraction, classes as decorators, magic methods, and the lifecycle of an object.

```{admonition} Lecture Slides
[https://20cs2023-fs24.github.io/slides/docs/lectures/lecture-10-26SEP2024.html](https://20cs2023-fs24.github.io/slides/docs/lectures/lecture-10-26SEP2024.html)
```

**Magic Methods**
- Overview of special methods in Python
- Common special methods like `__init__`, `__str__`, `__eq__`, etc.
- Implementing custom special methods in classes

**Abstraction**
- Concept of abstraction in OOP
- Abstract classes and methods using the `abc` module
- Importance of abstraction in large systems

**Classes as Decorators**
- Maintaining state across function calls
- More sophisticated decoration pattern

**Object Lifecycle**
- Object creation, initialization, and destruction
- The `__new__`, `__init__`, and `__del__` special methods
- Garbage collection and memory management in Python

**Files**
- [shape.py](/docs/repos/26SEP2024/shape.py)
- [memoize.py](/docs/repos/26SEP2024/memoize.py)
- [timer.py](/docs/repos/26SEP2024/timer.py)
- [lifecycle.py](/docs/repos/26SEP2024/lifecycle.py)