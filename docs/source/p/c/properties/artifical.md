# 🤖 artificial

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

## Related

- A pleasant Stack Overflow question with interesting answers: [What programming
  language is most like natural
  language?](https://stackoverflow.com/questions/491971/what-programming-language-is-most-like-natural-language)

## Resources

- Personal notes from [Necati Ergin](https://github.com/necatiergin)'s C course

```{disqus}
:disqus_identifier: 2bd601f8-fcfe-43d9-ad90-73b43fde0ceb
```
