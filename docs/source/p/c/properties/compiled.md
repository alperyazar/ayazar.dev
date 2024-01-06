# 🔨 compiled

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

## Portability Considerations

Being a compiled language, C presents unique challenges in terms of portability.
For every different combination of target architecture and operating system,
such as x86/Windows, x86/Linux, ARM/Linux, ARM/Baremetal, or Risc-V/Linux, a C
program must be recompiled. This requirement stems from the fact that compiled
languages like C translate code into machine-specific instructions, which vary
depending on the hardware and operating system.

Recommended Read: [](portable.md)

In contrast, interpreted languages typically operate at the source level.
Languages like Python or JavaScript are processed by an interpreter, which reads
and executes the source code directly. This source-level operation means that as
long as the target system has a compatible interpreter, the same code can run
across different architectures and operating systems without modification. This
attribute makes interpreted languages generally more portable than compiled
languages like C.

## Performance Trade-offs

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
:disqus_identifier: f7d2edf6-a31e-452e-8043-8f2bbd0ca851
```
