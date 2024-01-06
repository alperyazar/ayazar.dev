# ❓ FAQ

On this page, I will answer frequently asked questions that I've encountered,
either through direct queries or from discussions I've heard.

## Is it possible to learn C by studying the standards?

**Probably not.** The C standard documentation is tailored for individuals who
already have a grasp of the C language. Its primary audience is those involved
in writing C compilers, not beginners learning the language. Even for someone
familiar with C, the standards can be challenging to understand. The technical
language and complex terminology used in these documents are akin to legal
texts, which can be difficult to comprehend without specialized knowledge. This
complexity often leads to discussions and debates among experts, even on
platforms like Stack Overflow, indicating that the standards can be open to
interpretation and may contain ambiguously explained sections.

**In summary:** For someone looking to learn C, it's not practical to rely
solely on the standard documents. These are reference materials best utilized
for consultation and deeper understanding once the language has been learned,
rather than as primary learning resources.

## Do C standards maintain backward compatibility?

Another way to ask about C standards' backward compatibility is: *Can a program
written in accordance with an older standard be smoothly compiled and run using
a compiler that adheres to a newer standard?* While C standards are generally
careful to maintain backward compatibility, it wouldn't be accurate to describe
them as 'absolutely backwards compatible'. There are instances where features
are removed from the language or standard library in new standards.

Before a feature is completely removed, it is typically marked as **deprecated**
in the newer standard. This marking serves as a warning to programmers to cease
using these features, as they are slated for eventual removal in future updates.

The approach of compilers to backward compatibility can differ slightly. Often,
compilers are more *lenient* in this regard. They may continue to support
features that have been removed from the language in their newer versions. This
behavior, whether it's a strict adherence to the latest standards or a more
flexible approach, can usually be controlled externally through compiler
switches (not to be confused with the `switch` statement in `switch case`).

## Does the C included in C++ correspond exactly to 'the C programming language'?

C++ is a more expansive programming language compared to C. It includes a 'C
core', meaning that codes can be written in C++ in a way that is *reminiscent* of
writing in C. However, it's important to understand that the 'C' within C++ and
the standalone C programming language are not identical. Roughly speaking, there
is about a 70-80% similarity between them. Notably, some features introduced in
C99 are not incorporated into C++, which requires careful consideration when
writing C-style code in C++ or transferring such code from C++ to C.

It's crucial to recognize that C++ is **not** merely an updated version of C; it
is a distinct language with its own set of rules and features.

## What is MISRA C?

ChatGPT:

> MISRA C is a set of software development guidelines for the C programming
> language developed by MISRA (Motor Industry Software Reliability Association).
> Originally created for the automotive industry, MISRA C has gained widespread
> use in various safety-critical and high-integrity systems across industries such
> as aerospace, medical devices, and industrial automation.

[Wikipedia](https://en.wikipedia.org/wiki/MISRA_C)

```{disqus}
:disqus_identifier: 8866bf49-9bce-4bce-9c51-b189ef04aeb5
```
