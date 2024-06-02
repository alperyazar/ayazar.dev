---
og:description: 'C has a member of procedural programming languages. "Divide and conquer" is the heart of this paradigm.'
giscus: d5df8b76-515c-4313-b1f2-ee59d9244d78
---

# C is a procedural language

**Procedural programming** (**prosedürel programlama** in Turkish) paradigm is a
subset of the imperative programming paradigm. Another famous paradigm under
imperative programming is **object-oriented programming (OOP)** (**nesne
yönelimli programlama** in Turkish) [^2f]. **C is a very good example of
procedural programming.** [^1f]

Procedural programming is a paradigm based on the [functional
decomposition](https://www.investopedia.com/terms/f/functional-decomposition.asp)
idea. Procedural programming reflects the
[divide-and-conquer](https://en.wikipedia.org/wiki/Divide_and_rule) approach.

```{figure} assets/procedural-philip-ii.jpg
:align: center

Philip II of Macedon: "Did somebody say divide and conquer?" [Origin](https://en.wikipedia.org/wiki/File:Philip-ii-of-macedon.jpg)
```

As programmers programming in C, we take the problem and break it down into
smaller problems. Then we write C functions to solve each smaller problem.
Finally, these C functions which solve a smaller part of the original problem
are combined to solve the given original problem. Depending on the programming
language, part of the program that solves the smaller problem can be called
*function* (as in C), *procedure*, *routine*, *subroutine*, *method*, etc.

For example, let's say that our problem is getting an integer from the user and
printing `true` if the given value is divisible by 3 and `false` otherwise.
Although this is a very simple example, we can divide it into sub-problems and
write a C function for each sub-problem.

```c
#include <stdio.h>

int get_input(){
    int x;
    printf("Please enter an integer: ");
    scanf("%d",&x);
    return x;
}

int isDivisibleby3(int a){
    return !(a%3);
}

int main(void) {
    int y;
    y = get_input();
    if (isDivisibleby3(y))
        printf("true\n");
    else
        printf("false\n");
}
```

As you can see, we write C functions (procedures) to get an integer from the
user and check divisibility by 3. Then we *call* the functions from the main
flow to solve the original problem. Calling procedures by controlling flow is
the fundamental idea behind procedural programming. For example, `get_input()`
asks the user to enter a number and returns that number. This is a part of the
problem, getting a number from the user. The other function, `isDivisibleby3()`,
solves another part of the problem: checking the divisibility of a number by 3.
These two functions are completely independent of each other, and they are not
aware of other's existence. In `main()`, there are called in a logical order.
This is the main motivation behind procedural programming: divide, conquer and
build the solution.

Along with Procedural Programming, there are many [programming
paradigms](https://en.wikipedia.org/wiki/Programming_paradigm) like [Object
Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
(a kind of imperative programming), [Functional
Programming](https://en.wikipedia.org/wiki/Functional_programming) (declarative
programming), etc. Notice that a programming language can support coding in
multiple paradigms. For example, one can write C programming style C++ codes
following procedural programming practices. However, C++ is a very well-known
multi-paradigm language. C++ supports both object-oriented and procedural
approaches. Furthermore, C++ supports some functional programming features
[^3f]. There is even a [separate
book](https://www.amazon.com/Functional-Programming-programs-functional-techniques/dp/1617293814)
for that. Most of the programming languages like C++, Python, and PHP are
multi-paradigm languages though Python and Java are intended to use with an
object-oriented approach than a procedural style. But we can say that some
languages like [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk) are intended
to use with a single paradigm. For example,
[Smalltalk](https://en.wikipedia.org/wiki/Smalltalk) is a pure object-oriented
programming language.

It is the language designer's choice that a programming language will or will
not support a certain paradigm. For a given language, programming in a supported
paradigm is easier because the language is designed to support that paradigm.
But this doesn't mean that one can't write a program in a not natively supported
paradigm. For example, C is not an object-oriented programming language. But one
can write C programs with an object-oriented approach. There is even a book for
that!

```{figure} assets/procedural-oop.jpg
:align: center

Object-Oriented Programming With ANSI-C by Axel Schreiner
```

Of course, if the main aim is programming with an object-oriented approach then
C isn't a good choice because this approach is not *native* in C. But you can
make it work…

[Previously]({% post_url 2023-05-06-c-is-imperative %}), I said that the
imperative programming paradigm is a natural way of programming if we consider
processor architectures.

This is also true for procedural programming. All processors (including ancient
ones) natively support routines (functions in C). Almost all processors have
instructions like `GOSUB` (go to subroutine) or `RET` (return from subroutine).
If we write an assembly code, that program will consist of (imperative)
instructions and some subroutines (procedures). At the end of the day,
programming in C is similar to programming in assembly but of course much
easier.

Compared to object-oriented programming, procedural programming is a more native
way of programming considering computer architecture. However, as I said
previously, this doesn't mean that one is a better way of programming than the
other. It solely depends on your needs.

**In summary, C is a programming language that supports the procedural
programming paradigm.**

## resources

- <https://en.wikipedia.org/wiki/C_(programming_language)>
- Personal notes from [Necati Ergin](https://github.com/necatiergin/)'s C course.

[^1f]: <https://en.wikipedia.org/wiki/Procedural_programming>
[^2f]: <https://en.wikipedia.org/wiki/Object-oriented_programming>
[^3f]: <https://learn.microsoft.com/en-us/archive/msdn-magazine/2012/august/c-functional-style-programming-in-c>
