# null statement (boş deyim)

Let's consider [](expression-statement.md) and think that there is no
[](expression.md), and only `;`. This single `;` is called **null statement**.
We can think this like `NOTHİNG;`. No machine code is generated for
a null statement.

```c
x = 5;; //First ; is part of the expression statement, the second ; is a null statement
; //null statement
;;;;;;; // Lots of null statements
if (i > 10); //Do nothing when the if statement is evaluated as true
while(x); //Do nothing inside the while loop
```

Typically, the null statement is used in places where a statement is required by
the rules. We don't want to do anything, we are just satisfying the syntax
requirements of C.

**Let's do** an example:

In C90, no variable declaration is allowed after a statement. The following
code is invalid in C90 but valid after C99 (including).

```c
int main(void)
{
int x = 20;
++x;

int y = 10;
}
```

The compiler, x86-64 clang 16.0.0 (godbolt.org) with `-std=c90 -pedantic-errors`
gives the following error:

```text
error: mixing declarations and code is a C99 extension [-Werror,-Wdeclaration-after-statement]
```

However, the following code is also invalid in C90 gives the same error since
the second `;` is a statement, similar to `++x;`.

```c
int main(void)
{
int x = 20;; //The second ; is not a part of variable declaration, it is a null statement
int y = 10;
}
```
