---
giscus: 28b5999f-0f53-485d-b5c5-625264b68842
---

# Basic Arithmetic Operators (IN PROGRESS)

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

## floordiv Operator: `//`

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

```{todo}
IN PROGRESS
```
