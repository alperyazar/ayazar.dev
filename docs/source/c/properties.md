---
og:description: What kind of language is C? What are the properties? Which paradigms does it belong to? How can we categorize it?
giscus: 8005ad99-496b-45ad-b5ad-ed97718bd8d2
---

# 🌈 15 Features of The C Programming Language

```{figure} assets/properties.jpg
:align: center
:figclass: thmbnl
```

---

**What kind of language is C?** Programming languages can be categorized from
various perspectives, often referred to as **paradigms**. The characteristics of
the C programming language and the paradigms it belongs to are listed below.

Just as in real life, characteristics of programming languages aren't simply
binary (0/1); they often exist on a spectrum. For a given feature 'x', one might
say, 'The C language doesn't embody feature x as strongly as language Y.'
Moreover, different sources might classify C under varying paradigms or
categories, and some of these classifications can be subjective. The following
points reflect my personal understanding of these aspects.

## 🤖 artificial

C is an **artificial language**. You might say

> Hmm..., that is not very
> interesting, it should be artificial since it is a programming language, a
> language for computers not for humans, right?

Indeed, this argument holds merit. However, it's noteworthy that some
programming languages bear a closer resemblance to natural languages, such as
English or Turkish, compared to others. Take, for instance, our venerable
[COBOL](https://en.wikipedia.org/wiki/COBOL), which dates back to the 1960s.

```cobol
ADD 1 TO x
ADD 1, a, b TO x ROUNDED, y, z ROUNDED

ADD a, b TO c
    ON SIZE ERROR
        DISPLAY "Error"
END-ADD

ADD a TO b
    NOT SIZE ERROR
        DISPLAY "No error"
    ON SIZE ERROR
        DISPLAY "Error"
```

It sounds closer to English, right? Or consider
[SQL](https://en.wikipedia.org/wiki/SQL)

```sql
SELECT * FROM users WHERE name = '' OR '1'='1';
```

It sounds like an English sentence. Now let's look at some C code

```c
while(n--)
  *p1++=*p2++;
```

This looks more artificial than COBOL or SQL, only `while` sounds like English.

Almost all programming languages are artificial, but like many programming
languages, C is closer to a machine than a human.

### Related

- A pleasant Stack Overflow question with interesting answers: [What programming
  language is most like natural
  language?](https://stackoverflow.com/questions/491971/what-programming-language-is-most-like-natural-language)

## 🔨 compiled

Like C++ and Java, **C is a compiled language.**

At the heart of compiled languages is the process of transforming source code
into native machine code before execution. C, a venerable and powerful language,
epitomizes this category. Before a C program can run, it is compiled into the
instruction set architecture (ISA) of the target processor. This direct
translation to machine code allows C programs to execute efficiently and
directly on the processor, without any intermediary.

C++, sharing a lineage with C, follows a similar path. It is directly compiled
into the target processor's instructions, enabling it to leverage the full
capabilities of the hardware.

Java, another compiled language, introduces a twist in the compilation process.
Java code is compiled into Java bytecode, an intermediate representation. This
bytecode is then executed by the Java Virtual Machine (JVM), which can be
thought of as the ISA for a virtual processor. This layer of abstraction allows
Java to be platform-independent, a key feature that distinguishes it from C and
C++.

On the other side of the spectrum are **interpreted languages** like JavaScript and
Python. These languages are typically not compiled into machine code beforehand.
Instead, they are executed line-by-line by an interpreter, which translates the
code into machine-readable instructions on the fly during runtime. This approach
offers flexibility and ease of development but often at the cost of execution
speed.

Python, traditionally known as an interpreted language, illustrates the evolving
nature of language execution. Implementations like PyPy use Just-In-Time (JIT)
compilation, a technique that compiles Python code during execution to enhance
performance. This demonstrates how Python blurs the lines between interpreted
and compiled languages, though it is generally categorized as the former.

### Portability Considerations

Being a compiled language, C presents unique challenges in terms of portability.
For every different combination of target architecture and operating system,
such as x86/Windows, x86/Linux, ARM/Linux, ARM/Baremetal, or Risc-V/Linux, a C
program must be recompiled. This requirement stems from the fact that compiled
languages like C translate code into machine-specific instructions, which vary
depending on the hardware and operating system.

In contrast, interpreted languages typically operate at the source level.
Languages like Python or JavaScript are processed by an interpreter, which reads
and executes the source code directly. This source-level operation means that as
long as the target system has a compatible interpreter, the same code can run
across different architectures and operating systems without modification. This
attribute makes interpreted languages generally more portable than compiled
languages like C.

### Performance Trade-offs

However, the compiled nature of C brings significant advantages in terms of
performance. When a C program is compiled, it is transformed into optimized
machine code specific to the target hardware. This direct translation results in
increased execution speed and reduced memory usage, as the program can interact
more efficiently with the hardware.

Compiled languages are often preferred for applications where performance is
critical, such as system programming, game development, or any scenario where
resource constraints are a major consideration. The efficiency of machine code
means that compiled programs can execute faster and more efficiently than their
interpreted counterparts, in general.

### Related

- [Software portability
  (Wikipedia)](https://en.wikipedia.org/wiki/Software_portability)
- [Java's three types of
  portability](https://www.infoworld.com/article/2076944/java-s-three-types-of-portability.html)
- [Write once, compile
  anywhere](https://en.wikipedia.org/wiki/Write_once,_compile_anywhere)
- [Write once, run anywhere (WORA)](https://en.wikipedia.org/wiki/Write_once,_compile_anywhere)
  Not a term for C, but for Java.

## 💚 efficient

C is known for its efficiency. When discussing efficiency in programming, it's
important to specify the type of efficiency being referred to. In this context,
'efficiency' relates to the number of instructions generated during the
compilation of code. Low-level languages like C and C++, are typically more
efficient in terms of execution speed and memory usage compared to high-level
languages. This efficiency in resource utilization leads to lower energy
consumption during operation, which is why such languages are sometimes labeled
as **energy-efficient** or even 🌍 **green languages**, symbolizing their lesser
impact on the environment.

From a different perspective, high-level languages can also be considered more
efficient, depending on the ease and speed with which a program performing the
same task can be written. In this regard, from a developer's viewpoint,
high-level languages like Python may offer greater efficiency compared to
languages like C. This efficiency is in terms of coding productivity - achieving
more in less time. However, while code writing in high-level languages is more
time-efficient, their execution may not be as efficient in terms of speed and
resource utilization as in low-level languages like C. Therefore, it's not
accurate to label any one programming language as universally 'best' or 'most
efficient' in every aspect.

Owing to its efficiency and "near hardware" — both in terms of performance
and its mid-to-low-level nature — the C language stands as an ideal choice for
system programming and operating system development.

## 🎨 expressive

C is an expressive language. What does this mean, exactly? Expressiveness in
programming is all about how easily a language lets you communicate your ideas.
This includes conveying your intentions and goals to both the compiler and other
programmers. Thanks to its well-thought-out design, clear rules, intuitive
syntax, and semantic precision, C excels in this area. These qualities enable
programmers to write algorithms and programs in a way that is both
straightforward and unambiguous. This clarity and power are key reasons why C
has had such a significant influence on many other programming languages. For
those interested in exploring this topic further, there's an [insightful
article](https://www.embedded.com/expressive-vs-permissive-languages-is-that-the-question/)
available. Here's a notable quote from that article:

> A language is expressive when it allows a programmer to easily convey his/her
> intent, with errors detected early. In contrast to assembly languages, C allows
> one to constrain variables to hold values from specific types, so it is more
> expressive here. In contrast to C, Java allows to test if a value is within the
> length a.length of an array a, so it is more expressive here. Contrary to Java,
> Ada allows one to constrain scalar variables to hold values from specific
> ranges, so it is more expressive here.

Conversely, many newer programming languages, such as C++, are generally
regarded as being more expressive than C. It's important to note that
expressiveness in programming languages exists on a spectrum rather than as a
binary characteristic.

### Related

- [What does "expressive" mean when referring to programming languages?](https://stackoverflow.com/questions/638881/what-does-expressive-mean-when-referring-to-programming-languages)
- [Expressive vs. permissive languages: Is that the question?](https://www.embedded.com/expressive-vs-permissive-languages-is-that-the-question/)

## ⭕ general purpose

C is a [General-purpose programming
language](https://en.wikipedia.org/wiki/General-purpose_programming_language).
Its efficiency across various platforms — including embedded systems,
Windows/Linux operating systems, and diverse architectures like x86, ARM, and
RISC-V — and various problems stems from its design. Unlike languages tailored
for specific problem types or architectures, C is broadly applicable. This
characteristic is shared by many well-known languages such as C++, C#, Java,
JavaScript, and Python, all of which fall under the general-purpose category.

However, there are languages specifically designed for certain domains or to
program specialized hardware, such as FPGAs. These are known as [Domain-Specific
Languages (DSLs)](https://en.wikipedia.org/wiki/Domain-specific_language). For
instance, SQL is tailored for database queries, while HDLs like Verilog and VHDL
are used for programming FPGAs.

### Related

- [List of some domain-specific
  languages](https://en.wikipedia.org/wiki/Category:Domain-specific_programming_languages)

## 👮 imperative

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

### A Declarative Example

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

### Computer Architecture and Imperative Programming

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

### Functional Programming

The functional programming paradigm falls under the broader category of
declarative programming. This approach is exemplified by purely functional
languages such as Haskell. In recent times, many modern programming languages,
including Python and C++, have incorporated features that support functional
programming. These include tools like lambda functions, enabling programmers to
adopt a functional style within these languages.

```{important}
It's important to note that a programming language doesn't have to strictly
belong to one paradigm. In fact, most programming languages today are
multi-paradigm, meaning they support various programming approaches to varying
degrees. This versatility allows programmers to choose the most suitable
paradigm — or a combination of them — depending on their specific project
requirements.
```

### Summary

It's interesting to note that some languages, like Python or C++ [^2f], allow
programming in both imperative and declarative styles. This dual capability
offers programmers the flexibility to choose the most appropriate approach for
their needs. However, it's important to remember that C is an imperative
language.

```{attention}
⚠️ Unlike many modern languages, C does not inherently support the declarative
programming paradigm. While it is possible to introduce some declarative
features into C using third-party libraries, such extensions don't
fundamentally alter the language's paradigm or category. The crucial aspect
here is that for a language to be considered native to a certain paradigm,
these features should be built-in, not added externally.
```

## ⬇ middle-low level

The 'level' of a programming language indicates how close it is to human
understanding versus how close it is to a computer's processing capabilities.
**Lower-level** languages are closer to the machine's language, while
**high-level** languages are more abstracted and closer to human language. For
instance, an assembly language specific to a processor represents one of the
lowest-level languages for that system. Conversely, GUI-based languages like
[Scratch](https://en.wikipedia.org/wiki/Scratch_(programming_language)) are
among the highest-level languages. In high-level languages, abstracted models of
the computer are created, allowing programmers to focus less on the intricacies
of CPU architecture and memory organization. However, when using low-level
languages, a deeper understanding of the computer's workings is often necessary
to fully leverage the benefits these languages offer.

Programming languages can typically be classified into three categories based on
their levels: low-level, middle-level, and high-level. **C is often regarded as a
middle-level language**, though it leans closely towards the lower end of the
spectrum. This positioning reflects its balance between providing direct
hardware control, characteristic of low-level languages, and offering some level
of abstraction, common in high-level languages.

When a C program is compiled, the resulting assembly code often closely mirrors
the original C source code, line-by-line. This close correlation has led to C
being sometimes referred to as a **portable assembly language**. C is known for
its compactness, avoiding the
[bloat](https://en.wikipedia.org/wiki/Software_bloat) often associated with
high-level languages. Unlike many high-level languages that offer sophisticated
mechanisms like garbage collection to simplify programming tasks, C places the
full responsibility on the programmer. This includes managing aspects like
memory allocation and deallocation, making C both powerful and demanding.

The categorization of a programming language's level can evolve with
technological advancements. As noted in
[History of C]({% post_url 2023-12-16-a-brief-history-of-c-programming-language %}),
`Unix and C` part, the rewrite of UNIX in C in 1973 was a revolutionary move. At
that time, C was considered a high-level language. Today, however, with the
emergence of languages like Python and Java, as well as GUI-based languages like
Scratch or Simulink, C is seen as occupying a lower level by comparison. These
newer languages are considered to be at a much higher level than C in the
current technological landscape. It's interesting to consider that in the
future, what we now regard as high-level languages might shift to be seen as
middle-level, as the field of programming continues to evolve and grow.

### Related

- [Why is C called a middle-level
  language?](https://www.quora.com/Why-is-C-called-a-middle-level-language)
- The close relation between C and machine language:

```{youtube} yOyaJXpAYZQ
:align: center
:width: 100%
```

[YouTube Link](https://www.youtube.com/watch?v=yOyaJXpAYZQ)

## 🆓 non-proprietary

C is a non-proprietary language, meaning it isn't owned or controlled by a
single group or company. In contrast, some languages are proprietary, developed
and maintained primarily to meet the needs of a specific organization. An
example of a proprietary language is
[MATLAB](https://en.wikipedia.org/wiki/MATLAB), which is developed by
[MathWorks](https://en.wikipedia.org/wiki/MathWorks). It's important to note
that being proprietary doesn't inherently imply a negative aspect; it simply
reflects a different model of development and control. In contrast to
proprietary languages, many well-known and widely used languages like C, C++,
and Python are non-proprietary. Their development is overseen by committees or
communities rather than being dictated by a single corporate entity.

## 🎊 popular

There's no question about C's popularity. It's the language behind the kernels
of almost all operating systems, like Linux, and is extensively used in embedded
systems that utilize microcontrollers. Despite being 50 years old, C remains a
top choice for software that needs to operate closely with hardware, demands
high performance, and requires minimal space. Both C and C++ are favored in
system programming applications that run on operating systems but also have
stringent performance requirements. One of the key advantages of writing in C is
the ability to understand precisely how your code interacts with the hardware,
providing a clear insight into the execution process.

Certainly, C isn't a one-size-fits-all solution for every programming challenge.
If such a universal language existed, it would dominate all software
development, and the vast array of languages we see today wouldn't be necessary.
However, there are specific domains where C excels and few alternatives can
match its performance. Its popularity is particularly evident among
professionals working in these areas. Despite this, there's often a desire to
quantify such subjective perceptions of popularity with numerical data. So, the
question arises: **How do we objectively measure the popularity of a programming
language like C?**

One numerical indicator of a programming language's popularity is the [TIOBE
Index.](https://www.tiobe.com/tiobe-index/) While there are various discussions
and debates about the methodology and accuracy of this measurement, which I'll
delve into in later sections, it serves as a useful starting point for our
discussion. Let's explore what the TIOBE Index reveals about programming
language trends for now.

### TIOBE Index

As of December 2023, when this article was written, [the TIOBE
Index](https://www.tiobe.com/tiobe-index/), which is updated monthly, ranks
programming languages by their global popularity. According to this index, the C
programming language holds the position of **the second most popular language**,
with Python leading at first place and C++ following closely in third. A review
of the index over the past 35 years reveals a consistent trend: **the C language
has always been among the top two most popular languages according to this
measure.**

The TIOBE Index employs a measurement method that has sparked controversy. It
quantifies the popularity of programming languages based on the number of search
engine results related to each language. [^4f] This approach has been a subject of
significant debate, with various opinions questioning its validity and
meaningfulness. I have delved into this topic extensively in a detailed article.

In conclusion, the question arises: Is C a popular language and does its
popularity matter to us? Consider this - languages like Verilog and VHDL,
crucial in FPGA and ASIC design, may not rank high on popularity scales. Does
this mean they're not worth learning? Absolutely not! For professionals in these
fields, mastery of these languages is essential. The key takeaway is that the
necessity of learning a language should be based on your specific needs and
interests, not merely its popularity. C, as I mentioned earlier, is a standout
in certain domains. If you're planning to work in those areas or are simply
curious, learning C is invaluable. Beyond that, I'd suggest not to fixate too
much on popularity metrics.

### Further Read

- [A Hacker News discussion on TIOBE Index](https://news.ycombinator.com/item?id=19767725)

## 👜 portable

Portability refers to how easily a program written for one architecture or
platform can be transferred to another. Assembly language is typically at the
lower end of the portability spectrum. This is because assembly programs are
closely tied to the Instruction Set Architecture (ISA) of specific processor
families, which varies greatly. C, on the other hand, stands in stark contrast.
Generally, most C programs can be relatively easily ported to different
platforms or processors, provided there's a compatible compiler available for
the target system. This characteristic of C was a pivotal factor in the history
of UNIX. In the 1970s, rewriting UNIX in C was a critical step, as it
significantly simplified the process of porting the operating system to various
architectures, unlike an operating system written purely in assembly.

C is characterized as a source-level portable language. This means that while a
C program must be compiled for a specific platform or architecture, the original
source code itself is highly portable. The compiled executable, however, is
typically only compatible with the target system for which it was compiled. For
instance, a binary file compiled for an x86/Windows system will not run on
x86/Linux or any ARM architecture. To make the program run on different systems,
the same source code needs to be compiled separately for each target system,
usually with little to no modification. This attribute is why C is considered
portable at the source code level. Given its relatively low-level nature, C is
sometimes referred to as a **portable assembly language.**

```{attention}
⚠️ While C is theoretically a portable language, the practicalities of porting
a complex C program can be challenging due to several factors. These include
differences in operating systems, specific architectural details, and the
implementation-defined behaviors of various compilers. As a result, while the
core language is designed for portability, the real-world process of adapting
a C program for different systems might not be as straightforward as it
initially seems.
```

The concept of source code level portability, as seen in C, was revolutionary
for programmers accustomed to assembly language. However, the industry has since
developed other levels of portability. For instance, languages like C# and Java
are known for their binary portability. The compilers for these languages
generate machine-independent intermediate code, which is then executed on the
target platform by a runtime environment, such as the Java Runtime Environment.
This approach enables the same binary file to run across different platforms.
It's important to note, however, that just as source-level portable languages
like C require different compilers for each target platform, binary portable
languages like C# and Java need specific runtime environments for each platform
to ensure their portability.

### Related

- [Software portability
  (Wikipedia)](https://en.wikipedia.org/wiki/Software_portability)
- [Java's three types of
  portability](https://www.infoworld.com/article/2076944/java-s-three-types-of-portability.html)
- [Write once, compile
  anywhere](https://en.wikipedia.org/wiki/Write_once,_compile_anywhere)
- [Write once, run anywhere (WORA)](https://en.wikipedia.org/wiki/Write_once,_compile_anywhere)
  Not a term for C, but for Java.

## 〽 procedural

The procedural programming paradigm, known as 'prosedürel programlama' in
Turkish, is a subset of the broader imperative programming paradigm. Another
well-known category under imperative programming is object-oriented programming
(OOP), or 'nesne yönelimli programlama' in Turkish [^6f]. C serves as a prime
example of procedural programming, illustrating the paradigm's characteristics
effectively [^5f].

Procedural programming is a programming paradigm that embodies the idea of
[functional
decomposition](https://www.investopedia.com/terms/f/functional-decomposition.asp).
This approach is akin to the [divide and
conquer](https://en.wikipedia.org/wiki/Divide_and_rule) strategy, where larger
problems are broken down into smaller, more manageable functions or procedures.
Each of these functions addresses a specific part of the task, working together
to solve the overall problem.

```{figure} assets/procedural-philip-ii.jpg
:align: center

Philip II of Macedon: "Did somebody say divide and conquer?" [Origin](https://en.wikipedia.org/wiki/File:Philip-ii-of-macedon.jpg)
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
solve each unit separately (**conquer**), and then integrate these solutions
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
functional programming features [^7f], which are even the subject of a
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

```{figure} assets/procedural-oop.jpg
:align: center

Object-Oriented Programming With ANSI-C by Axel Schreiner
```

Indeed, if the primary goal is to employ an object-oriented approach, C might
not be the ideal choice. This is because object-oriented programming is not a
*native* feature of C. However, with some effort and adaptation, it is possible
to make object-oriented programming work within the context of C.

### Computer Architecture and Procedural Programming

Earlier, I mentioned that the imperative programming paradigm aligns naturally
with the way processor architectures are designed. This perspective considers
the sequential and direct order-driven nature of processor operations, which
is characteristic of imperative programming.

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

## 📓 standard

C stands out as a programming language with formal standardization. It has
official standard documents recognized by the International Organization for
Standardization (ISO). This formal standardization sets it apart from widely
used languages like Python and Perl, which, although not formally standardized,
have documents that act as *de facto* standards. It's noteworthy that before its
formal standardization, C was guided by a de facto standard, primarily the book
[The C Programming
Language.](https://en.wikipedia.org/wiki/The_C_Programming_Language) This book
served as the unofficial standard for C from 1978 until the language's first
official standardization in 1989.

The official C standards are designated using the format `ISO/IEC 9899:<YEAR>`.
For instance, the C11 standard is officially named [ISO/IEC
9899:2011](https://www.iso.org/standard/57853.html).

Thanks to the established standards, there are high-quality C compilers
available, developed both by communities and companies. Examples include [GCC
(GNU Compiler Collection)](https://gcc.gnu.org/),
[Clang/LLVM](https://clang.llvm.org/), and [MSVC (Microsoft Visual
C++)](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B). Compilers that
adhere to the rules defined in these standards are referred to as **conforming
compilers.** This standardization ensures a level of consistency and reliability
in compiler behavior across different platforms and use cases.

History of C standards are explained in
[History of C]({% post_url 2023-12-16-a-brief-history-of-c-programming-language %})
post.

### Related

- [What do you mean by conforming and non-conforming
  compiler?](https://stackoverflow.com/questions/67310135/what-do-you-mean-by-conforming-and-non-conforming-compiler)
- [Python not a standardized language?](https://stackoverflow.com/a/1535727)

## ⚓ statically typed

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
and can change as the program executes [^8f], [^9f].

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
variable in a way that aligns with C's statically typed nature [^10f], [^11f].

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

### Related

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

## 🏗️ structured

C is a [structured
programming](https://en.wikipedia.org/wiki/Structured_programming) language. The
opposite of structured programming is [non-structured
programming](https://en.wikipedia.org/wiki/Non-structured_programming) or
unstructured programming. Here there are 5 typical characteristics of a
structured language:

1. **Control Structures**: Enables clear flow control using loops and conditional
   statements, improving readability and maintainability. C has control
   structures like `if`, `switch..case`, `for`, `while`.
2. **Modularity**: Supports dividing code into reusable, independent functions or
   modules for better organization and testing. In C, we use mainly functions to
   obtain modularity. C includes a standard library that provides a set of
   predefined functions for performing various tasks, further supporting
   structured and modular programming.
3. **Local Variable Scope**: Encourages variables to be declared within their usage
   scope, reducing side effects and enhancing code safety.
4. **Sequential Execution**: Maintains a predictable and straightforward flow of
   program execution within each structure.
5. **Limited Use of GOTO Statements**: Discourages the use of GOTO statements,
   preventing complex and unmanageable "spaghetti code." Although C allows GOTO
   statements, it should be used with caution.

While C is a structured programming language, it's also flexible and allows for
different programming styles. This flexibility means that it's possible to write
unstructured code in C, but the language itself provides all the necessary
features to support structured programming practices.

## 〰 weakly typed

Nearly all programming languages implement some form of type-checking and
enforce type-related rules, but they vary in the degree of strictness with which
they do so. Languages that are more *paranoid* about types tend to have
stringent rules. These **strongly typed languages** require programmers to
explicitly declare type conversions and minimize implicit type conversions. In
contrast, **weakly typed languages** take a more lenient approach to type rules.
They readily perform implicit conversions as needed, often prioritizing
convenience or flexibility over strict type adherence. This distinction ties
into the broader concept of [type
safety](https://en.wikipedia.org/wiki/Type_safety), which concerns how a
language prevents type errors and manages conversions between different types.

The concept of a type system's *strength* in programming languages exists on a
continuum, with some languages enforcing *stronger* type rules than others. This
categorization can be quite controversial. When it comes to C, for instance,
you'll find a diverse range of opinions online. Some sources categorize C as
weakly typed, while others assert it is strongly typed. This disparity in views
makes the discussion particularly interesting. To gain a clearer understanding,
let's explore what the authors of The C Programming Language book (often
referred to as K&R C) have to say on this topic.

> C is not a strongly-typed language in the sense of Pascal or Algol 68. It is
> relatively permissive about data conversion, although it will not
> automatically convert data types with the wild abandon of PL/I. Existing
> compilers provide no run-time checking of array subscripts, argument types,
> etc.

The quote we'll be examining is from the third page of the first edition (1978)
of The C Programming Language book.

From the authors' perspective, it is clear that they did not categorize C as a
strongly typed language. However, it's also noteworthy that they did not
explicitly label C as a weakly typed language either. In 'The C Programming
Language' book, they recommend the use of [linter
tools](https://en.wikipedia.org/wiki/Lint_(software)) to enhance the strength of
the type system and type checking rules in C. This suggests an acknowledgment of
C’s flexibility in type enforcement, and the potential to bolster its type
safety through additional tools.

The second edition of The C Programming Language published in 1988, aligns
closely with the ANSI C standard. In this edition, the authors provide updated
insights and perspectives that reflect the developments and standardizations in
C programming. They state:

> C is not a strongly-typed language, but as it has evolved, its type-checking
> has been strengthened.

In the subsequent sections, the book delves into the enhancements made to
strengthen the type system in C. One of the core philosophies of the C language
is to offer maximum freedom to the programmer, which, in turn, places a high
degree of responsibility on them. C does not extensively police the programmer's
actions. This design choice is rooted in C's intended use for developing
operating systems and low-level tools, where the ability to perform memory
manipulation and other advanced techniques is crucial. The book continues to
explain this philosophy, stating:

> Nevertheless, C retains the basic philosophy that programmers know what they
> are doing; it only requires that they state their intentions explicitly.

As highlighted, programming in C requires a deep understanding of what you are
doing, given the language's design philosophy. If we envision a continuum
representing type system strength, with *strongly typed* at one end and *weakly
typed* at the other, C would be placed nearer to the *weakly typed* end.
Therefore, **it can be characterized as a weakly typed language**, reflecting its
emphasis on programmer freedom and responsibility, rather than stringent type
enforcement.

```{important}
❗ It's important to remember that the concept of a language being 'strongly' or
'weakly' typed is distinct from it being 'statically' or 'dynamically' typed.
These are separate dimensions of classifying programming languages. For
instance, Python is categorized as a dynamically typed language, yet it is also
considered strongly typed due to its strict enforcement of type rules at
runtime. On the other hand, C is a statically typed language, as types are
determined at compile time, but it is often viewed as weakly typed because of
its more permissive approach to type conversions and enforcement. Understanding
this distinction helps in comprehensively grasping the type systems of various
programming languages.
```

C is considered as a weakly typed language because it does some implicit type
conversions to help the programmer. From memory safety perspective, it almost
does not check anything regarding memory access. For example, one can easily
access beyond array bounds.

JavaScript is a pretty weakly typed language. Let's look at the following code.
Your mind may blow off!

```javascript
// https://www.programiz.com/javascript/online-compiler/

console.log(4 + '7');
console.log(4 * '7');
console.log(2 + true);
console.log(false - 3);
```

The output is:

```text
47
28
3
-3
```

This is very interesting. At the first line, the addition does a string
concatenation. At the second line, the character 7 is interpreted as an integer
and a multiplication is performed.

You will never think of the C language as a weakly typed language again once you
see JavaScript.

### Related

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

## 📚 Resources

- Personal notes from [Necati Ergin](https://github.com/necatiergin)'s C course
- Personal notes from [Kaan Aslan](https://csystem.org/)’s Unix/Linux System
  Programming Course
- <https://en.wikipedia.org/wiki/C_(programming_language)>
- <https://stackoverflow.com/a/46118248>
- <https://en.wikipedia.org/wiki/Type_system>
- <https://en.wikipedia.org/wiki/Strong_and_weak_typing>

[^1f]: <https://en.wikipedia.org/wiki/C_(programming_language)>
[^2f]: <https://www.educative.io/blog/declarative-vs-imperative-programming>
[^3f]: Historically, there were machines specifically designed for a programming language like the [Lisp machine.](https://en.wikipedia.org/wiki/Lisp_machine)
[^4f]: <https://www.tiobe.com/tiobe-index/programminglanguages_definition/>
[^5f]: <https://en.wikipedia.org/wiki/Procedural_programming>
[^6f]: <https://en.wikipedia.org/wiki/Object-oriented_programming>
[^7f]: <https://learn.microsoft.com/en-us/archive/msdn-magazine/2012/august/c-functional-style-programming-in-c>
[^8f]: <https://stackoverflow.com/a/1517670/1766391>
[^9f]: <https://developer.mozilla.org/en-US/docs/Glossary/Static_typing>
[^10f]: <http://www.robertgamble.net/2012/01/c11-generic-selections.html>
[^11f]: <https://stackoverflow.com/a/17290414/1766391>
