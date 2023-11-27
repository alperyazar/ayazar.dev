# expression (ifade)

Expression can be defined as a combination of variables (could be extended to
identifiers), constants, and operators. An operator without any operand isn't an
expression. Let's see some examples:

```c
//Each line is an expression
a           //Assume that a is a variable
a + 10      //Assume that a is a variable
a + 10 - b  //Assume that a and b are variables.
c[i]        //Assume that c and i are variables.
e = f       //Assume that e and f are variables.
20
10 + 20
foo()       //Assume that foo is a function identifier. Remember that in this context
            //() is an operator called function call operator.

+           //NOT an expression
if(a)       //NOT an expression. NOT a combination of variable, constant, operator.
            //if is a reserved word. This is a part of if statement syntax.
```

Notice that there is no semicolon (terminator), `;`, at the end of the lines. Do
not confuse [](statement.md) with expression!. If we put a `;` after an
expression then we get an **expression statement**.

```c
a      //expression
a;     //expression statement
e = f  //expression
e = f; //expression statement
```

Expressions have:

- a type
- a value (except expressions with `void` type)
- a value category (L-Value or R-Value)

## References

- <https://raw.githubusercontent.com/CSD-1993/KursNotlari/master/C.pdf>
- <https://en.cppreference.com/w/c/language/expressions>
- Personal Notes

```{disqus}
:disqus_identifier: 953d8973-0ba0-4368-90a6-d39c3ed40bb3
```
