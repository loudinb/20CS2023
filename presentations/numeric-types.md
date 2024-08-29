# Numeric Types

Python provides several built-in numeric types to represent different kinds of numbers. 

## Integers

Integers in Python are whole numbers without a fractional component. They can be positive, negative, or zero.

- Represented by the `int` class
- Unlimited precision (can be arbitrarily large)
- Examples: `42`, `-7`, `0`

```python
x = 10
y = -5
big_number = 1234567890123456789
```

## Floating-Point Numbers

Floating-point numbers represent real numbers with a decimal point.

- Represented by the `float` class
- Usually implemented using double-precision (64-bit) format
- Examples: `3.14`, `-0.001`, `2.0`

```python
pi = 3.14159
avogadro = 6.022e23  # Scientific notation
```

### Precision and Rounding Errors

Floating-point arithmetic can sometimes lead to unexpected results due to the way computers represent real numbers:

```python
0.1 + 0.2 == 0.3  # False
print(0.1 + 0.2)  # 0.30000000000000004
```

For precise decimal calculations, use the `decimal` module.

## Infinite and Not a Number (NaN)

Python's `float` type includes special values to represent infinity and undefined results.

### Infinity

- Represented as `float('inf')` or `-float('inf')`
- Can result from division by zero or overflow

```python
positive_infinity = float('inf')
negative_infinity = -float('inf')
print(1.0 / 0.0)  # inf
```

### Not a Number (NaN)

- Represents undefined or unrepresentable results
- Represented as `float('nan')`

```python
nan = float('nan')
print(0.0 / 0.0)  # nan
```

## Underflow (Machine Epsilon)

Machine epsilon is the smallest positive number that, when added to 1.0, gives a result different from 1.0.

- In Python, you can find it using `sys.float_info.epsilon`
- Important for understanding the limits of floating-point precision

```python
import sys

epsilon = sys.float_info.epsilon
print(epsilon)  # Typically around 2.220446049250313e-16 on most systems

print(1.0 + epsilon != 1.0)  # True
print(1.0 + epsilon / 2 == 1.0)  # True
```

## Complex Numbers

Complex numbers have both a real and an imaginary part.

- Represented by the `complex` class
- Written as `a + bj`, where `a` is the real part and `b` is the imaginary part
- `j` represents the square root of -1

```python
z1 = 2 + 3j
z2 = complex(1, -1)

print(z1 + z2)  # (3+2j)
print(z1 * z2)  # (5+1j)
print(abs(z1))  # 3.605551275463989 (magnitude)
```

### Operations with Complex Numbers

Python supports various operations and functions for complex numbers:

```python
import cmath

z = 1 + 2j

print(z.real)  # 1.0 (real part)
print(z.imag)  # 2.0 (imaginary part)
print(z.conjugate())  # (1-2j) (complex conjugate)
print(cmath.phase(z))  # 1.1071487177940904 (phase angle in radians)
```

Remember to `import cmath` for advanced complex number functions like `sqrt`, `exp`, and trigonometric functions that support complex arguments.