# statement (deyim)

C is an imperative language. When we write a C program, we give orders to the
compiler that are executed one by one.

```{note}
If you don't feel comfortable with the term **imperative language**, I recommend
reading my blog post: [C is imperative, procedural and statically
typed](https://mixtum.ayazar.dev/c-is-imperative-procedural-statically-typed)
```

Statement can be defined as the (smallest) execution unit or *order* given to
the compiler. A C program is formed by writing statements one after another.

Let's look at a simple code snippet

```c
int a;     //declaration statement
int b;     //declaration statement
a = 5;     //expression statement
//...
if (a > b) //conditional or control or if statement
  foo();   //expression statement
return;    //control or return statement
```

We write a simple C program by writing different types of statements one after
another. By combining different statements, we form working C programs.

As you can see, there are different types of statements. Depending on the
resource you study, there could be minor differences between them in terms of
naming convention or categorization. For example, an `if()` statement could be
categorized as an *if statement*, a *conditional statement*, or a *control
statement*. At the end of the day, the exact category name is not so critical.

## Recommended

- [C is imperative, procedural and statically
  typed](https://mixtum.ayazar.dev/c-is-imperative-procedural-statically-typed)

## References

- <https://raw.githubusercontent.com/CSD-1993/KursNotlari/master/C.pdf>
- <https://en.wikibooks.org/wiki/C\_Programming/Statements>
- <https://learn.microsoft.com/en-us/cpp/c-language/overview-of-c-statements?view=msvc-170>
- Personal Notes

```{disqus}
:disqus_identifier: b1fae336-164d-408b-9926-eab2d822e038
```
