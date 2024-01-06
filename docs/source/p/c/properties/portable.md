# 👜 portable

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

Recommended: [](../history.md)

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

```{warning}
While C is theoretically a portable language, the practicalities of porting a
complex C program can be challenging due to several factors. These include
differences in operating systems, specific architectural details, and the
implementation-defined behaviors of various compilers. As a result, while the
core language is designed for portability, the real-world process of adapting a
C program for different systems might not be as straightforward as it initially
seems.
```

Recommended: [](middle-low-level.md)

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

## Related

- [Software portability
  (Wikipedia)](https://en.wikipedia.org/wiki/Software_portability)
- [Java's three types of
  portability](https://www.infoworld.com/article/2076944/java-s-three-types-of-portability.html)
- [Write once, compile
  anywhere](https://en.wikipedia.org/wiki/Write_once,_compile_anywhere)
- [Write once, run anywhere (WORA)](https://en.wikipedia.org/wiki/Write_once,_compile_anywhere)
  Not a term for C, but for Java.

```{disqus}
:disqus_identifier: 26064ba0-766f-438a-b8d3-ec4fc66222d5
```
