# 〰 weakly typed

```{hint}
I recommend reading [](statically-typed.md) first if you haven't read it yet.
```

Almost all languages do some type checking and apply type related rules. Some
languages are more *paranoid* on types. They have strict rules and want
programmers to explicitly indicate type conversions and do minimal implicit type
conversions. They are **strongly typed** languages. On the other hand, **weakly
typed** languages are more permissive towards type rules, they do not hesitate
to do an implicit conversion wherever it is needed. This is related to a concept
called [type safety](https://en.wikipedia.org/wiki/Type_safety) concept.

Unlike most of the categories and paradigms, *strength* of the type system is a
continuum. Some languages have *stronger* type rules than others. IMHO, this is
one of the most controversial categories. Considering C, you can find many
resources on the Internet on this topic. Some of them say that C is weakly typed
and others say the opposite. Interesting, right? Let's see what the authors of
The C Programming Language book (K&R C) about this topic.

> C is not a strongly-typed language in the sense of Pascal or Algol 68. It is
> relatively permissive about data conversion, although it will not
> automatically convert data types with the wild abandon of PL/I. Existing
> compilers provide no run-time checking of array subscripts, argument types,
> etc.

This quote is from the 3rd page of the first edition (1978) of the book.

As we can see that the *bosses* didn't put C in the strongly typed languages.
But also, they didn't tag the C language as a weakly typed language explicitly.
In the book, they suggest usage of
[linter](https://en.wikipedia.org/wiki/Lint_(software)) tools to make the
type system and type checking rules stronger.

The second edition of the book was published in 1988 and this edition almost
covers ANSI C. In that book, the authors say that

> C is not a strongly-typed language, but as it has evolved, its type-checking
> has been strengthened.

After that, improvements taken to make the language type system stronger are
explained.

The C language set the programmer free as much as possible. The programmer has
the highest responsibility. The language itself doesn't check what the
programmer is doing too much. Since it is designed to write an operating system
and very low level tools, the programmer should be able to do some memory
tricks. This is the philosophy behind the language. The book follows as:

> Nevertheless, C retains the basic philosophy that programmers know what they
> are doing; it only requires that they state their intentions explicitly.

As you see, if you program in C you should know what are you doing.

**If we think of a line with two ends, the C language is positioned close to the
weak end. So, C is a weakly typed language.**

```{important}
Please keep in mind that this topic isn't related to being a statically typed or
dynamically typed language. Python is a dynamically and strongly typed language,
whereas C is a statically and weakly typed language.
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
