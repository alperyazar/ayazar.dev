---
giscus: 28b5999f-0f53-485d-b5c5-625264b68842
---

# Basic Arithmetic Operators

Let's begin with the four basic arithmetic operators: `*` (multiplication), `/`
(division), `+` (addition), and `-` (subtraction). All four of them are **binary
infix arithmetic operators**.

## Caution: The Division, `/`, Operator

The `/` operator behaves differently in Python compared to other languages like
C, C++, Java, and C#. Even if both operands of the `/` operator are `int`, the
result is always a `float`.

Consider the following expression.

```python
x = 5 / 2
```

In this expression, both operands, `5` and `2`, are integers. In C, C++, Java,
and C#, the result would be `2`, not `2.5`. However, in Python, the result is
`2.5`, and `x` references a `float` object. In Python, the `/` operator always
produces a `float` result, regardless of whether the operands are `int` or
`float`. Consider the following example:

```python
print(type(10 / 4))   # float
print(type(4 / 2))    # float
print(type(2.5 / 2))  # float
print(type(2 / 0.5))  # float
```

## floordiv Operator, `//`

This is a binary infix arithmetic operator. In Python, it performs integer
division but the result doesn't have to be an `int` object. Unlike the `/`
operator, if both operands are `int`, the result is also an `int`. However, if
either operand is a `float`, the result is a `float`. Regardless of the type,
the result is always **floored** to the nearest integer value.

When we *floor* a positive floating-point number, we simply discard the
fractional part. However, when we *floor* a negative number, we discard the
fractional part and subtract `1` from the result.

Consider the following example:

```python
x = 10 // 4
print(x, type(x)) # 2, int

x = 10.0 // 4
print(x, type(x)) # 2.0, float

x = -10 // 4
print(x, type(x)) # -3, int

x = 10.0 // -4
print(x, type(x)) # -3.0, float
```

This behavior differs from languages like C, C++, Java, and C#. In those
languages, truncation is done *toward zero* rather than *flooring*. While this
makes no difference for positive numbers, for negative numbers, those languages
only discard the fractional part without subtracting `1` from the result.
Consider the following example:

```c
// This is a C code

#include <stdio.h>

int main(void)
{
    printf("%d\n", (int)(10.0 / 4)); // 2, similar to Python
    printf("%d",  (int)(-10.0 / 4)); // -2 not -3, unlike Python
}
```

## Modulo Operator, `%`

The `%` (modulo) operator yields the remainder from the division of the first
argument by the second. The modulo operator always yields a result with the same
sign as its second operand (or zero); the absolute value of the result is
strictly smaller than the absolute value of the second operand. [^1f] It is
a binary infix arithmetic operator.

If both operands are `int`, the result is also an `int`. However, if at least
one operand is a `float`, the result is a `float`.

Please consider the following examples:

```python
x = 10 % 4
print(x, type(x)) # 2, int

x = 10.0 % 4
print(x, type(x)) # 2.0, float

x = -10 % 4
print(x, type(x)) # 2, int

x = -10.0 % 4
print(x, type(x)) # 2.0, float

x = 10.0 % -4
print(x, type(x)) # -2.0, float
```

---

Python differs from C and C++ in how the modulo operator works. In C and C++,
both operands of the modulo operator must be of an integer type, floating-point
types are not allowed, unlike in Python. Consider the following C code:

```c
//This a C code

#include <stdio.h>

int main(void)
{
    printf("%d\n", (int)(10 % 4));
    printf("%d", (int)(-10.0 % 4)); //Error
}
```

In Python, there is another major difference compared to C, C++, Java, and C#
regarding the modulo operator. Let's say `a` is divided by `b`, yielding
quotient `c` and remainder `d`, satisfying the equation `a = b * c + d`.

In Python, the quotient `c` is computed using the `//` (floor division)
operator, whereas in other languages, it is computed using `/`. Consider the
expression `-10 % 4`.

- In Python, `-10 // 4` results in `-3` due to floor division. This leads to
  `-10 = 4 * (-3) + 2`, so the remainder is `2`, meaning `-10 % 4` evaluates to
  `2`.
- In C and similar languages, `-10 / 4` results in `-2` due to truncation toward
  zero. This leads to `-10 = 4 * (-2) + (-2)`, meaning `-10 % 4` evaluates to
  `-2`.

This difference in handling negative numbers makes Python’s modulo operation
behave differently from those languages.

Consider the following cases:

```c
//This is a C code.

#include <stdio.h>

int main(void)
{
    printf("%d\n", (int)(-10 % 4));  // -2
    printf("%d\n", (int)(10 % -4));  //  2
    printf("%d\n", (int)(-10 % -4)); // -2
}

```

```python
# This is a Python code

x = -10 % 4
print(x, type(x)) # The result is 2 and type is int

x = 10 % -4
print(x, type(x)) # -2

x = -10 % -4
print(x, type(x)) # -2
```

| Expression | Python | C    |
|------------|--------|------|
| `-10 % 4`  | `2`    | `-2` |
| `10 % -4`  | `-2`   | `2`  |
| `-10 % -4` | `-2`   | `-2` |

Thus, in Python, when a negative number is divided by a positive number using
the modulo operator (`%`), the remainder is always positive.

The following expression is held in Python: [^1f]

`x == (x//y)*y + (x%y)`

[^1f]: <https://docs.python.org/3.3/reference/expressions.html#binary-arithmetic-operations>
