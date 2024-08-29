# Basics of the Python Interpreter

The Python interpreter is a program that reads and executes Python code. It's the core component that allows developers to run Python programs.

Although Python is an interpreted language, it uses a hybrid approach that includes both interpretation and compilation. The source code is compiled into bytecode, which is then executed by the Python Virtual Machine (PVM).

## Interpreter Steps

When you run a Python script or enter code in the Python shell, the interpreter performs these main steps:

1. **Lexical Analysis (Tokenization):** The interpreter breaks the source code into tokens (like keywords, identifiers, and operators).

2. **Parsing:** It analyzes the tokens to ensure they form a valid Python program according to the language's grammar rules, creating an Abstract Syntax Tree (AST).

3. **Compilation to Bytecode:** The interpreter converts the AST into bytecode, an intermediate representation of the code. This bytecode is typically stored in `.pyc` files for faster future execution.

4. **Execution:** The Python Virtual Machine (PVM) executes the bytecode. It reads the instructions, interacts with the Python runtime environment, and runs the program.

```{note}
Syntax errors are detected during the parsing phase, while runtime errors occur during execution.
```