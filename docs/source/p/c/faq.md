# ❓ FAQ

On this page, I will be answering frequently asked questions that I come across
(that I have been asked directly or that I have heard being asked).

## Can I learn C from reading the standards?

**Probably not.** C standard documentation is written in a way that people who
know C can understand it. The main target audience of these documents is people
or institutions that write C compilers. Standard documents are not prepared to
explain the language step by step to people learning the language. Even if you
know the C language, there will be many moments when you will have difficulty
reading the standards. Even the English used in these documents makes it
difficult to understand. For example, just as we ordinary people cannot
understand legal concepts and terms without being a lawyer, even if they are in
English, it is not easy for C programmers to understand standard documents. It
is not surprising to see discussions where there is no full consensus on
standards, even in expert environments such as Stack Overflow. Even standards
may have parts that are explained incompletely. Even though their accuracy is
very high, they do not serve "the absolute truth."

**In summary:** It is not practically possible for a person who wants to learn C
to learn the language by reading the standards. Standard documents are reference
documents that can be understood after learning the language and are consulted
not too frequently.

## Are C standards backward compatible?

*Can I smoothly compile and run a program I wrote in accordance with an old
standard with a compiler that works in accordance with a new standard?* question
is a different way of asking this question. Although C standards are very
sensitive about backward compatibility, it would not be correct to call it
"absolutely backwards compatible". There may also be features that are removed
from the language with new standards. Similarly, there may be some components
that are removed from the standard library.

When a feature is to be removed from the language, they are not removed
immediately. Features to be removed are usually marked as **deprecated** in
advance. If a feature is marked as deprecated in a new standard, we as
programmers need to stop using them. Because these features will be completely
removed in the near or distant future.

With compilers, the topic is little bit different. Compilers can often be even
more *lenient* about backwards compatibility. Even if various features are
removed from the language, compilers can act as if these features are still
supported in their new versions. Of course, this behavior of compilers (strictly
adhering to standards or turning a blind eye to certain things) is usually
controllable externally (with compiler switches, not mentioning about `switch`
in `switch case`).

## Is C in C++ language the same as "the C programming language?"

C++ is a much larger programming language than C. We can say that there is a "C
core" in C++. We can write codes in C++ as if we were writing in C. But C in C++
and the separate programming language we call "C" are not exactly the same.
Still, it wouldn't be wrong to say that there is a 70-80% similarity. Some of
the features added to the C language, especially with C99, are not available in
C++. Therefore, we must be careful when writing C-style code in C++ and when
transferring C-style codes written in C++ to the C language.
C++ **is NOT** a new version of C. C++ is a separate language.

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
