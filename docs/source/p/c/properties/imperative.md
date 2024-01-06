# 👮 imperative

C is known as an imperative language, a term translated as 'buyurgan' in
Turkish. In imperative programming, like in C, programmers directly control the
program's state or flow by writing explicit statements — it's akin to **giving
orders to a computer** [^1f]. This style is also common in languages like C++
and Python.

On the flip side, we have declarative languages ('bildirimsel' in Turkish).
Here, programmers focus on describing *what should be done* rather than *how it
should be done.* In declarative programming, the program's flow isn't explicitly
controlled by the programmer. [SQL](https://en.wikipedia.org/wiki/SQL) and
[Make](https://en.wikipedia.org/wiki/Make_(software)) are classic examples of
declarative languages. Let’s delve into some examples to illustrate these
concepts.

The following code snippet is an example from a C program.

```c
//...

if (x > 20) {
    y = 5;
    foo();
} else
    bar();

//...

```

In this C program snippet, the imperative programming style is evident. We
directly control the program's flow using an `if` statement and dictate specific
actions through function calls to `foo()` and `bar()`. Additionally, we modify
the program's state by altering the value of `y`. The program's direction
changes based on the comparison result of `x` with `20`. Each line in this snippet
explicitly instructs the computer on the operations to perform, demonstrating
the characteristic "order-driven" nature of imperative programming.

## A Declarative Example

The following SQL code (query) fetches data from a table named `Users` stored in
a database.

```sql
SELECT * FROM Users WHERE username='admin' AND PASSWORD='admin' ORDER BY id DESC LIMIT 1;
```

In contrast to C, consider how we use SQL, which is a declarative language.
Here, we describe our desired outcome without specifying *how* the database engine
should achieve it. For example, suppose we want to retrieve a single row from
the `Users` table where both the username and password are `admin`, and in case
of multiple matches, we prefer the user with the highest `id`. In this scenario,
do we need to implement the sorting algorithm ourselves? Absolutely not! Our
focus is solely on the end result, not the underlying operations and flow
executed by the database engine. This contrasts with programming in C, where we
are required to explicitly give orders and control the program's flow.

## Computer Architecture and Imperative Programming

The imperative programming paradigm aligns closely with the fundamental nature
of computer programming, especially considering the basic design of computer and
processor architectures. Since the advent of the microprocessor era, the core
functioning of most processors hasn't drastically changed. They primarily
execute instructions sequentially, with certain instructions (like branch
instructions) altering the flow of execution. From this viewpoint, programming
in C closely mirrors programming in assembly language, albeit at a slightly
higher abstraction level.

Interestingly, programs written in declarative languages like SQL also run on
these same processors. In today, there isn't a special processor designed
exclusively for SQL or other declarative languages [^3f].

**The key difference between the imperative and declarative paradigms lies in the
programmer's perspective of computer interaction.**

Even though a database engine executing SQL code ultimately translates into
similar processor instructions as a C program, the engine itself might be
written in an imperative language like C. In essence, when you use a declarative
language, the underlying computer architecture becomes more *abstract* compared to
when you're programming in an imperative language. Whether this abstraction is
beneficial or not largely depends on the specific requirements and context of
your programming needs.

## Functional Programming

The functional programming paradigm falls under the broader category of
declarative programming. This approach is exemplified by purely functional
languages such as Haskell. In recent times, many modern programming languages,
including Python and C++, have incorporated features that support functional
programming. These include tools like lambda functions, enabling programmers to
adopt a functional style within these languages.

```{note}
It's important to note that a programming language doesn't have to strictly
belong to one paradigm. In fact, most programming languages today are
multi-paradigm, meaning they support various programming approaches to varying
degrees. This versatility allows programmers to choose the most suitable
paradigm — or a combination of them — depending on their specific project
requirements.
```

## Summary

It's interesting to note that some languages, like Python or C++ [^2f], allow
programming in both imperative and declarative styles. This dual capability
offers programmers the flexibility to choose the most appropriate approach for
their needs. However, it's important to remember that C is an imperative
language.

```{warning}
Unlike many modern languages, C does not inherently support the declarative
programming paradigm. While it is possible to introduce some declarative
features into C using third-party libraries, such extensions don't fundamentally
alter the language's paradigm or category. The crucial aspect here is that for a
language to be considered native to a certain paradigm, these features should be
built-in, not added externally.
```

## Resources

- <https://en.wikipedia.org/wiki/C_(programming_language)>
- [Necati Ergin](https://github.com/necatiergin)'s C Course, personal notes

[^1f]: <https://en.wikipedia.org/wiki/C_(programming_language)>
[^2f]: <https://www.educative.io/blog/declarative-vs-imperative-programming>
[^3f]: Historically, there were machines specifically designed for a programming
language like the [Lisp machine.](https://en.wikipedia.org/wiki/Lisp_machine)

```{disqus}
:disqus_identifier: 3cbe4fd2-cc82-496a-9c3b-b020d824187f
```
