# 〰 weakly typed

```{hint}
I recommend reading [](statically-typed.md) first if you haven't read it yet.
```

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
It's important to remember that the concept of a language being 'strongly' or
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

## Related

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

---

## Resources

- <https://stackoverflow.com/a/46118248>
- <https://en.wikipedia.org/wiki/Type_system>
- <https://en.wikipedia.org/wiki/Strong_and_weak_typing>

```{disqus}
:disqus_identifier: 7e3d401d-a852-4fbd-8572-63e353ff00be
```
