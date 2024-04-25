---
og:description: 'Programming in C is similar to giving "orders" to a computer'
giscus: 85bedd3c-085a-4c7a-83ff-20190f2c0a98
---

# C is an imperative language

The C language (or any programming language) can be characterized from many
different perspectives. One property of the C language is being an **imperative
language.**

## imperative vs declarative

C is an **imperative** (**buyurgan** in Turkish) language. As programmers, we
explicitly control the state or flow of the program by writing statements [^1f].
Writing in C is similar to *giving orders to a computer.* Codes in C++ and
Python are also *usually* written imperatively. The opposite is **declarative**
(**bildirimsel** in Turkish). When we are programming with declarative
languages, we describe *what* should be done, but not *how.* With declarative
languages, we do not control the flow of the program explicitly.

The following code may be a part of a C program.

```c
//...

if (x > 20) {
  y = 5;
  foo();
} else
  bar();
```

As you can see, we explicitly control the flow of the program by an if statement
and give *orders* by calling functions `foo()` and `bar()` and somehow modify
the program state by changing the value of `y`. Depending on the result of the
comparison of `x` by `20`, the flow of the program takes a different direction.
Each line tells the computer what to do explicitly.

## a declarative example

The following SQL code (query) fetches data from Users table which is stored in
a database.

```sql
SELECT * FROM Users WHERE username='admin' AND pass='admin' ORDER BY id DESC LIMIT 1;
```

Unlike C, in that case, we describe *what* we want but not *how* the database
engine should work to satisfy our query. We want a single row from the table
Users where both username and password are admin and if multiple users are
found, the user with the highest id is returned. Did we implement the sorting
algorithm used to sort entries? No! We don't care about the exact operations and
flow executed by the database engine, we only care about the result. But while
programming in C, we must give *orders* and control the flow.

## computer architecture and imperative programming

The imperative programming paradigm is the natural way of computer programming.
The basics of computer and processor architectures haven't changed too much
since the beginning of the microprocessor era. Almost all processors work by
executing orders (instructions) sequentially. Some instructions (branch
instructions) change the flow that the processor follows. From that perspective,
programming in C is very parallel to programming in assembly language, only at a
*slightly* higher level.

Programs coded in a declarative language run on the same processors. There is no
different processor to run SQL code or a procedural language. The difference
between these two paradigms comes from the perspective that a programmer sees
the computer. Of course, the database engine executing SQL codes runs similar
instructions on the processor as a C program. The engine itself could be
programmed in an imperative language, like C. In general, if you use a
declarative language, computer architecture becomes more abstract to you
compared to programming in an imperative language. This doesn't have to be
necessarily a good or a bad thing. As always, it depends on your needs…

## functional programming

The functional programming paradigm is a subset of the declarative programming
paradigm. There are purely functional languages like Haskell. Nowadays, most
modern programming languages like Python or C++ have some tools that allow us to
program in a functional programming fashion (like lambda functions).

```{note}
💡 A programming language does not have to be in either category. Most
programming languages are multi-paradigm languages supporting both paradigms
more or less.
```

## summary

Notice that a language may support programming in both imperative and
declarative fashion. For example, in Python or C++, one can program in both
paradigms [^2f]. **But of course, C is an imperative language.**

Unlike many modern languages, C does not support the declarative programming
paradigm inherently. It is possible to add some declarative programming features
to C with 3rd party libraries. However, extending a language with 3rd party
libraries doesn't change its paradigm or category. The key point is that the
features should be native to that language.

## resources

- <https://en.wikipedia.org/wiki/C_(programming_language)>
- Personal notes from [Necati Ergin](https://www.linkedin.com/in/necatiergn)'s C
  course

[^1f]: <https://en.wikipedia.org/wiki/C_(programming_language)>
[^2f]: <https://www.educative.io/blog/declarative-vs-imperative-programming>
