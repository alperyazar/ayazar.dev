# 👜 portable

Portability is a measure of easiness of porting a program written for an
architecture/platform to another architecture/platform. One of the least
portable languages is assembly language. Assembly programs are considered to be
non-portable since Instruction Set Architecture (ISA) of each processor family
is different. C is different. In general, most C programs can be ported easily
(with relatively low effort) to another platform/processor, as long as there is
a compiler for the target system. This is why rewriting UNIX in C was a very
crucial step for UNIX history back in the 70s because it made porting the
operating system to other architectures much easier (comparing to porting an
operating system purely written in assembly).

Recommended: [](../history.md)

**C is a source-level portable language.** When a C program is compiled, it is
compiled for a specific platform or architecture. In general, the final
executable binary file is only compatible for the target system. For example, a
binary compiled for an x86/Windows system won't run x86/Linux or any ARM
architecture. The same source code has to be compiled for all target systems
separately with little or no modification. This is why C is portable at source
code level. Since C is a relatively low level language, sometime it is called as
a **portable assembly language**.

```{warning}
Keep in mind that, in theory C is portable, but in
practice due to different natures of operating systems, architectural details
and implementation defined behaviors of compilers, porting a fairly complex C
program is not as easy as it sounds.
```

Recommended: [](middle-low-level.md)

Source code level portability was a *miracle* for assembly programmers. However,
the industry has invented other portability levels. For example, programs
written in C# and Java are called binary portable languages. Compilers of those
languages create machine-independent intermediate code. Then, it is run by a
sort of runtime software (like Java Runtime Environment) on the target platform.
This makes running the same binary file on different platforms possible. Of
course, binary portable languages need different runtime software for each
target platform, just as different source-level portable languages need
different compilers for portability.

## Related

- [Software portability
  (Wikipedia)](https://en.wikipedia.org/wiki/Software_portability)
- [Java's three types of
  portability](https://www.infoworld.com/article/2076944/java-s-three-types-of-portability.html)
- [Write once, compile
  anywhere](https://en.wikipedia.org/wiki/Write_once,_compile_anywhere)
- [Write once, run anywhere (WORA)](https://en.wikipedia.org/wiki/Write_once,_compile_anywhere)
  Not a term for C, but for Java.

## References

- Personal notes from [Necati Ergin](https://github.com/necatiergin)'s C course
- Personal notes from [Kaan Aslan](https://csystem.org/)'s Unix/Linux System
  Programming Course
