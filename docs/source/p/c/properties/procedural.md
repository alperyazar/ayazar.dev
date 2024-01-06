# 〽 procedural

The procedural programming paradigm, known as 'prosedürel programlama' in
Turkish, is a subset of the broader imperative programming paradigm. Another
well-known category under imperative programming is object-oriented programming
(OOP), or 'nesne yönelimli programlama' in Turkish [^2f]. C serves as a prime
example of procedural programming, illustrating the paradigm's characteristics
effectively [^1f].

Procedural programming is a programming paradigm that embodies the idea of
[functional
decomposition](https://www.investopedia.com/terms/f/functional-decomposition.asp).
This approach is akin to the [divide and
conquer](https://en.wikipedia.org/wiki/Divide_and_rule) strategy, where larger
problems are broken down into smaller, more manageable functions or procedures.
Each of these functions addresses a specific part of the task, working together
to solve the overall problem.

```{figure} assets/Philip-ii-of-macedon.jpg
:align: center

Philip II of Macedon: "Did somebody say divide and conquer?" [Origin](https://upload.wikimedia.org/wikipedia/commons/a/a5/Philip-ii-of-macedon.jpg)
```

When programming in C, programmers typically approach a problem by breaking it
down into smaller, more manageable components. For each of these smaller
problems, specific C functions are written. These functions, each addressing a
distinct segment of the original problem, are then combined to form a complete
solution. It's worth noting that in different programming languages, the parts
of the program that solve these smaller problems may be referred to by various
terms, such as *function* (as in C), *procedure*, *routine*, *subroutine*, or
*method*.

Consider a simple task: we need to write a program that takes an integer input
from the user and prints 'true' if the number is divisible by 3, and 'false'
otherwise. Even though this is a straightforward example, it can still be
divided into sub-problems. For each sub-problem, we can create a dedicated C
function. These sub-problems could include functions for getting the user input,
checking divisibility by 3, and displaying the result. By addressing each of
these aspects separately, we effectively apply the procedural programming
approach in C.

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

In this procedural programming example, we create separate C functions (or
procedures) to handle different aspects of the problem. One function,
`get_input()`, is responsible for obtaining an integer from the user. This
addresses the sub-problem of user input. Another function, `isDivisibleby3()`,
checks whether the given number is divisible by 3, tackling another aspect of
the problem. These two functions operate independently; they do not interact
with or are aware of each other.

In the `main()` function, we call these procedures in a logical sequence to
solve the original task. The essence of procedural programming lies in this
methodology: break down the problem into smaller, manageable units (**divide**),
solve each unit separately (**conquer**)**, and then integrate these solutions
to address the overall problem (**build**). This approach allows for clear,
organized, and modular programming.

Alongside Procedural Programming, there are several other [programming
paradigms](https://en.wikipedia.org/wiki/Programming_paradigm), such as [Object
Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
(a form of imperative programming) and [Functional
Programming](https://en.wikipedia.org/wiki/Functional_programming) (a type of
declarative programming). It's important to note that many programming languages
support multiple paradigms. For instance, although C++ is renowned for its
object-oriented capabilities, it is possible to write C-style code in C++
adhering to procedural programming practices. Moreover, C++ incorporates some
functional programming features [^3f], which are even the subject of a
[dedicated
book.](https://www.amazon.com/Functional-Programming-programs-functional-techniques/dp/1617293814)

Similarly, languages like Python and PHP are also *multi-paradigm*, allowing
programmers to choose the most suitable approach for their needs. However, some
languages are designed with a specific paradigm in mind. A prime example is
[Smalltalk](https://en.wikipedia.org/wiki/Smalltalk), which is purely
object-oriented. This illustrates that while many modern languages offer
versatility in programming styles, some are still tailored for a singular
paradigmatic approach.

The decision to support certain programming paradigms within a language rests
with its designers. When a language is specifically designed for a particular
paradigm, programming within that style is typically more straightforward.
However, this doesn't mean that programmers are restricted to only the paradigms
natively supported by the language. Take C, for instance. Although it's not
inherently an object-oriented programming language, it's still possible to adopt
an object-oriented approach in C programming. This versatility is exemplified by
the existence of books and resources dedicated to object-oriented programming in
C.

```{figure} assets/procedural-oop-with-c.jpg
:align: center

Object-Oriented Programming With ANSI-C by Axel Schreiner
```

Indeed, if the primary goal is to employ an object-oriented approach, C might
not be the ideal choice. This is because object-oriented programming is not a
*native* feature of C. However, with some effort and adaptation, it is possible
to make object-oriented programming work within the context of C.

## Computer Architecture and Procedural Programming

Earlier, I mentioned that the imperative programming paradigm aligns naturally
with the way processor architectures are designed. This perspective considers
the sequential and direct order-driven nature of processor operations, which
is characteristic of imperative programming.

```{note}
Recommended: [](imperative.md)
```

Procedural programming, like imperative programming, naturally fits with how
processors operate. Processors, even the earliest models, inherently support
routines, akin to functions in C. Instructions such as `GOSUB` (go to subroutine)
or `RET` (return from subroutine) are commonplace in processor instruction sets.
Writing in assembly involves using these imperative instructions and organizing
code into subroutines or procedures. In essence, programming in C is similar to
assembly programming, but with a much higher level of abstraction and ease.

When compared to object-oriented programming, procedural programming can be seen
as more in line with the native functioning of computer architecture. However,
as I've previously mentioned, this doesn't imply that one paradigm is inherently
superior to the other. The choice largely depends on the specific requirements
of your project.

To summarize, C is a language that fundamentally supports the procedural
programming paradigm, aligning closely with the underlying architecture of
processors.

[^1f]: <https://en.wikipedia.org/wiki/Procedural_programming>
[^2f]: <https://en.wikipedia.org/wiki/Object-oriented_programming>
[^3f]: <https://learn.microsoft.com/en-us/archive/msdn-magazine/2012/august/c-functional-style-programming-in-c>

```{disqus}
:disqus_identifier: f69499cf-a57f-466d-a778-e7cdab51c44b
```
