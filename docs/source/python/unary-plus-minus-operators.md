---
giscus: 27cc9225-1c49-48ff-952b-2cbf564916ff
---

# Unary Plus `+` and Minus `-` Operators

The `+` and `-` tokens represent two distinct types of operators. One group
consists of binary infix operators, such as addition (`5 + 2`) and subtraction
(`5 - 2`). The other group consists of unary prefix operators, which indicate
the sign of a number, such as `+5` and `-2`. In this article, we will focus on
the second category.

The unary `-` operator negates its operand, while the unary `+` operator returns
its operand unchanged. The unary `+` is primarily used for code readability.
These unary operators have a higher precedence than basic arithmetic operators
like addition and subtraction.

> Check out: [](precedence-of-operators.md)

Consider the example:

```python
b = -----3
```

In this expression, all `-` symbols represent unary minus operator. Since
the associativity of that operator is righ-to-left, order of evaluation follows
that:

```text
E1: -3
E2: -E1
E3: -E2
E4: -E3
E5: -E4
E6: b = E5
```

and then it is equivalent to `b = -3`.

Unlike C and similar languages, Python does not have `--` and `++` operators.
This also means that the maximal munch rule does not cause ambiguities in such
cases.

Consider the following example:

```python
a = 4----2
```

In this case, the first `-` symbol is the subtraction operator and the remaining
ones are the unary minus operators. The order is:

```text
E1: -2
E2: -E1
E3: -E2
E4: 4 - E2
E5: a = E4
```

It is equivalent to `a = 4 - (-2)` and the result is `6`. Again, please keep
in mind that there is no `--` operator in Python.
