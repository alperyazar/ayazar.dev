# ⚓ statically typed

Almost all programming languages feature a **type system**, referred to as 'tür'
in Turkish. For example, variables and constants have types associated with
them. Most of the languages have rules regarding type system, like type
conversion rules. These rules can be checked at different times. Generally, in
**compiled languages**, the types of objects are determined and type rules are
checked during the compilation phase. In contrast, for **interpreted languages**,
these steps are performed at runtime.

Therefore, if a language determines object types and enforces type rules at
compile time, it is classified as a **statically typed language**. Conversely,
if these steps occur at runtime, the language is considered **dynamically
typed**. This distinction is crucial in understanding how different languages
manage and apply their type systems.

In statically typed languages, the types of objects, such as variables, are
determined at compile time, and these types remain constant throughout the
runtime. Once a variable's type is set, it does not change, regardless of the
type of value subsequently assigned to it. This consistency in variable types is
a defining characteristic of statically typed languages.

Conversely, in dynamically typed languages, a variable's type is typically
established with its first assignment. The variable assumes the type of the
initial value assigned to it. However, unlike in statically typed languages,
this type can change during execution. If a value of a different type is later
assigned to the same variable, the variable's type will adjust to reflect this
new assignment. This flexibility in variable types is a key feature of
dynamically typed languages.

In statically typed languages, because the types of objects remain constant,
compilers are able to verify the language's type rules during the compilation
process. This capability allows for the detection and resolution of most
type-related errors before the program is even run. On the other hand,
dynamically typed languages typically perform their type rule checks at runtime.
As a result, these languages may encounter and throw exceptions during execution
when a rule violation occurs.

**C is a statically typed language.**

C, C++, and Java are examples of statically typed languages. In these languages,
the types of variables are determined at compile time and remain unchanged
during execution. On the other hand, JavaScript, Python, and PHP are dynamically
typed languages. In these languages, variable types are determined at runtime
and can change as the program executes [^1f], [^2f].

Let's delve into examples to better understand dynamically typed languages,
starting with Python. In Python, you can use the `type()` function to determine
the type of an object. This feature is particularly useful in a dynamically
typed language, as it allows us to observe how the types of variables can change
at runtime. Let's explore some Python code snippets to see this functionality in
action.

```python
x = 3
print (type(x))
x = "alper"
y = x + " yazar"
print (type(x))
x = 3.5
print (type(x))
y = x + " yazar"
```

The following output is produced when the program runs

```text
<class 'int'>
<class 'str'>
<class 'float'>
Traceback (most recent call last):
  File "<string>", line 8, in <module>
TypeError: unsupported operand type(s) for +: 'float' and 'str'
```

In this Python example, we can observe how the type of the variable `x` changes
implicitly during execution, or at runtime, through assignment of values of
different types. Consider the expression `y = x + " yazar"` appearing on both
line 4 and line 8. Initially, this operation is successful because, at that
point, `x` is of type `str`, and concatenating (*adding*) two strings is
permissible. However, by the time we reach the last line, the type of `x` has
changed to `float`, and Python does not allow adding a `str` to a `float`.

This change in `x`'s type and the resulting `TypeError` on the last line
underscore Python's dynamically typed nature. The error is only caught when the
program is executed and reaches that line, not at the start. This is because
Python, being dynamically typed, enforces type-related rules during runtime.

Now, let's shift our focus to a statically typed language: C. In C, determining
the type of a variable isn't as straightforward as in Python, since C lacks a
built-in function akin to Python’s `type()`. Nevertheless, with the introduction
of C11, C gained support for *generic selection expressions*, which, when
combined with macro definitions, can be used to achieve something similar to
Python's `type()` functionality. This approach allows us to infer the type of a
variable in a way that aligns with C's statically typed nature [^3f], [^4f].

Let’s examine the following example of a C program. It's not necessary to
understand every line in detail. The primary focus is to illustrate how certain
concepts are implemented in C, particularly in the context of a statically typed
language. This example will provide insights into how C handles types and other
programming constructs, even if you're not fully familiar with all the aspects
of the language.

```c
// See: https://stackoverflow.com/a/17290414/1766391
// Tested with x86-64 gcc 12.2 with default flags on https://godbolt.org/
#include <stdio.h>
#include <stddef.h>
#include <stdint.h>

#define typename(x) _Generic((x),        /* Get the name of a type */             \
                                                                                  \
        _Bool: "_Bool",                  unsigned char: "unsigned char",          \
         char: "char",                     signed char: "signed char",            \
    short int: "short int",         unsigned short int: "unsigned short int",     \
          int: "int",                     unsigned int: "unsigned int",           \
     long int: "long int",           unsigned long int: "unsigned long int",      \
long long int: "long long int", unsigned long long int: "unsigned long long int", \
        float: "float",                         double: "double",                 \
  long double: "long double",                   char *: "pointer to char",        \
       void *: "pointer to void",                int *: "pointer to int",         \
      default: "other")

int main(void){
    int x;
    double y = 3.4;
    printf("x is %s\n",typename(x));
    printf("y is %s\n",typename(y));
    x = y; //Why not error?
    printf("x is still %s\n",typename(x));
    printf("x = %d\n",x);
}
```

The output is:

```text
x is int
y is double
x is still int
x = 3
```

In this C program, we define two variables: `x` and `y`. Right from the start,
their types are explicitly declared: `x` is an `int` and `y` is a `double`. These
types remain unchanged throughout the program's execution. Interestingly,
partway through the program, we assign the value of `y` (which is a `double`) to
`x` (an `int` type variable). Why doesn’t this cause an error, either at
compilation or runtime?

The reason is C's handling of implicit type conversion. During the assignment,
the `double` value 3.4 is implicitly converted to an `int`. This results in a
*hidden* and *temporary* integer object with the value 3. This implicit
conversion aligns with C's type rules and is distinct from the concept of static
type checking. It's crucial to note that despite this value assignment, the type
of `x` remains `int`, showcasing the constancy of types in statically typed
languages.

Let's examine another C programming example where the code fails to compile. In
this case, we encounter an error that prevents the creation of an executable
file, stopping us from even testing the code.

```c
// Tested with x86-64 gcc 12.2 with default flags on https://godbolt.org/
int main(void){
    int *p1, *p2, *p3;
    p3 = p1 + p2;
}
```

Output from the compiler (not the output of the program) follows:

```text
<source>: In function 'main':
<source>:3:13: error: invalid operands to binary + (have 'int *' and 'int *')
    3 |     p3 = p1 + p2;
      |             ^
ASM generation compiler returned: 1
```

The reason this C program is invalid lies in the attempted operation: adding two
pointers. In C, pointer addition is not a valid operation. While the underlying
rationale for this is beyond the current scope, the key takeaway is that this
violation is caught during the compilation phase. As C is a statically typed
language, its compiler is able to check and enforce type-related rules during
compilation. This means that errors can be identified and addressed before the
program even reaches the execution stage.

## Related

- <https://www.baeldung.com/cs/statically-vs-dynamically-typed-languages>
- <https://medium.com/android-news/magic-lies-here-statically-typed-vs-dynamically-typed-languages-d151c7f95e2b>
  There is one point about this article that puzzles me. My knowledge of C++ is
  limited, but I don't think that C++ is more weakly typed than C, as indicated
  in this article. C++ has stricter rules regarding implicit type conversion
  compared to C.

The following video is about JavaScript but explains the concepts well.

```{youtube} C5fr0LZLMAs
:align: center
:width: 100%
```

Good and short explanation

[^1f]: <https://stackoverflow.com/a/1517670/1766391>
[^2f]: <https://developer.mozilla.org/en-US/docs/Glossary/Static_typing>
[^3f]: <http://www.robertgamble.net/2012/01/c11-generic-selections.html>
[^4f]: <https://stackoverflow.com/a/17290414/1766391>

```{disqus}
:disqus_identifier: a872244f-d897-4432-923d-efc25d11375f
```
