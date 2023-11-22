# 🦴 statically typed

Almost all programming languages have a **type system** (`tür` in Turkish). For
example, variables and constants have types associated with them. Most of the
languages have rules regarding type system, like type conversion rules. These
rules can be checked at different times. In general, types of objects are
determined, and type rules are checked at compilation phase of **compiled
languages**. On the other hand, these steps are done at runtime for
**interpreted languages**. If type related steps (like determining types of
objects) are done at compile time, we call these languages  **statically typed**
languages. If those steps are done at runtime, then the language become an
example for **dynamically typed** language.

In statically typed languages, types of objects (like variables) are determined
at compile time and types of variables don't change during runtime. Typically,
in dynamically typed languages, types of variables are determined with the first
assignment. The variable gets the type of the first assigned value, but this
doesn't mean that variable's type can't change. During execution, if another
value with different type is assigned to the same variable, then the type of the
variable changes. This is not true for statically typed languages. In statically
typed languages, the type of variable always stays unchanged regardless of the
type of the assigned value.

Since types of objects stays constant in statically typed languages, compilers
can check type rules of the language during compilation. By doing so, most of
the type related errors can be caught at compilation time, prior to running the
program. In contrast, most of the dynamically typed languages can check their
rules at runtime. These languages can throw exceptions at runtime when a rule
violation is observed.

**C is a statically typed language.**

C, C++ and Java are statically typed languages whereas JavaScript, Python, and
PHP are dynamically typed [^1f], [^2f].

Let's look at some examples and start with a dynamically typed language, Python.
In Python, `type()` can be used to get an object's type.

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

As you can see, type of `x` is set and changed implicitly (by assigning values
with different types) during execution, in other words, at runtime. There are
identical expressions at different lines: `y = x + " yazar"` on line 4 and 8.
Although they are the same, the first one is OK since at that point type of `x`
is `str` and we can *add* two strings together. However, during execution of the
last line, type of `x` is float, and we can't add a `str` with a `float` value.
Since Python is a dynamically typed language, we were able to alter the type of
`x` at runtime. Notice that `TypeError` is caught when the program is run and
hits the last line, but not at the beginning of the execution. Why? Because
Python is a dynamically typed language and checks the type related rules at
runtime.

Now let's look at a statically typed language, C. Getting the type of variable
is not easy as in Python because C doesn't have a built-in function like
`type()`. However, with the help of some macro definitions and _generic
selection expression_support starting from C11, we can do something similar
[^3f], [^4f].

Let's look at the following example C program. You don't need to understand all
lines.

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

In this program, two variables are defined: `x` and `y`. Notice that the
definitions explicitly indicate the types of variables at compile time: type of
`x` is `int` and type of `y` is `float`. These types will stay constant during
the whole life of the program. Notice that in the middle of the flow we assign
value (3.4) of `y` which is a `float` type variable to variable `x` which is a
`int` type variable. But why this doesn't cause an error at compilation or
runtime? Because according to rules of C, during this assignment, an *implicit
type conversion* occurs and 3.4 is converted to a *hidden* and *temporary* `int`
object with value 3. This doesn't violate any rule and is not related to static
type checking concept. Notice that type of `x` is always `int` regardless of the
assigned values.

Let's see another C example. Compilation of the following codes fails. We can't
even get an executable file to test the code.

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

But why this program is invalid? Because, addition of two pointers in C is not a
valid operation. The reason behind this is out of scope for now, but the
important point is that the violation is caught during compilation phase. C is a
statically typed language and compiler can check type related rules during
compilation, no need to wait until execution.

## Related

- <https://www.baeldung.com/cs/statically-vs-dynamically-typed-languages>
- <https://medium.com/android-news/magic-lies-here-statically-typed-vs-dynamically-typed-languages-d151c7f95e2b>

The following video is about JavaScript but explains the concepts well.

```{youtube} C5fr0LZLMAs
:align: center
:width: 100%
```

Good and short explanation

---

## Resources

- <https://en.wikipedia.org/wiki/C_(programming_language)>
- Personal notes from [Necati Ergin](https://github.com/necatiergin/)'s C
  course.

[^1f]: <https://stackoverflow.com/a/1517670/1766391>
[^2f]: <https://developer.mozilla.org/en-US/docs/Glossary/Static_typing>
[^3f]: <http://www.robertgamble.net/2012/01/c11-generic-selections.html>
[^4f]: <https://stackoverflow.com/a/17290414/1766391>
