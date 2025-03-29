---
giscus: 6529296c-9b09-4380-9375-b7dfe789fa99
---

# Precedence of Operators

Remember, most expressions contain at least one operator, and it's common for
multiple operators to be involved in a single expression. But how are they
evaluated? Which operator takes precedence over the others? This is what we’ll
explore in the topic of *Operator Precedence*.

Consider the following expression: `c = a + b * c`. Based on basic math rules,
we know that the `*` operator takes precedence over the `+` operator. In this
case, we’re correct! However, this doesn’t mean that our intuition based on math
rules will always align with Python’s rules.

Here is the order of evaluation:

```text
I1: b * c
I2: a + I1
I3: c = I2
```

Now consider the expression `a = b + c + d`. Here is the order:

```text
I1: b + c
I2: I1 + d
I3: a = I3
```

This order still aligns with our mathematical expectations. But why does `b + c`
take precedence over `c + d`?

How can we determine the order of evaluation within an expression if it's not a
mathematical expression? This is why it's important to understand the precedence
rules of operators in any programming language, including Python.

## Parentheses, `()`

As we know from mathematics, parentheses `()` allow us to control the order of
precedence. Consider the expression `a = (b + c) * d`. Here, the `+` operator
takes precedence over `*` due to the parentheses. First, `b` is added to `c`,
and the result of the addition is then multiplied by `d`.

In general, programmers tend not to use parentheses when the desired order is
already achieved without them. However, especially for long expressions, even
when parentheses aren’t required for correctness, they can be used to improve
the readability of the code.

## The Operator Precedence Table

We will create a table to identify operator precedence in Python. **A lower
precedence number (higher rows) indicates higher precedence than a higher number
(lower rows).**

*TABLE IS IN PROGRESS*

| Precedence | Operator(s) | Description                                                       | Associativity |
|------------|-------------|-------------------------------------------------------------------|---------------|
| 1          |             |                                                                   | left-to-right |
|            | `()`        | Represents both function call operator and precedence parentheses |               |
| 2          |             |                                                                   | left-to-right |
|            | `*`         | Multiplication                                                    |               |
|            | `/`         | Division                                                          |               |
|            | `//`        | floordiv                                                          |               |
| 3          |             |                                                                   | left-to-right |
|            | `+`         | Addition                                                          |               |
|            | `-`         | Subtraction                                                       |               |
| 4          |             |                                                                   | right-to-left |
|            | `=`         | Assignment ‡                                                      |               |

‡: Indeed, unlike languages like C, in Python assignment is not an expression
but a statement. Therefore, including the `=` operator in the table doesn't make
much sense, unlike in other languages. However, for the sake of completeness, it
is included in the table. [^1f] [^2f]

### How to interpret the table?

When multiple operators are involved in a single expression, operators with
higher precedence (i.e., those with lower precedence numbers in the table) are
evaluated first. **But what happens if more than one operator shares the same
precedence?** This is where the concept of associativity comes into play. If
operators share the same precedence and have **left-to-right** associativity,
the leftmost operator is evaluated first; otherwise, if the associativity is
**right-to-left**, the rightmost operator is evaluated first. All operators at
the same precedence order share the same associativity.

## Examples

For example, consider the expression `a = b / c * d`. The operators `*` and `/`
share the same precedence. However, since their associativity is left-to-right,
`b / c` is evaluated first because the `/` operator is to the left of `*`.

`a = b = c` The associativity of `=` is right-to-left. Therefore, first
`I1: b = c` is executed, and then `I2: a = I1` is executed.

`a = foo() + 2` The `()` operator has higher precedence than others. Therefore,
first `I1: foo()` is executed, and then `I2: I1 + 2` is executed, return value
of `foo` function is added by `2`.

[^1f]: <https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-assignment_stmt>
[^2f]: <https://stackoverflow.com/a/2603981/1766391>
