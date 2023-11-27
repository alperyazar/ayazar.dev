# constant expression (sabit ifade)

An expression which its value can be calculated at compilation time by the
compiler.

See: [](expression.md)

Typically, these expressions don't contain any variable (or identifier) and they
consist of operators and constants.

```c
16             //constant expression
16 + 38        //constant expression
16 + 38 - 6/2  //constant expression

i       //NOT a constant expression where i is a variable
i + 10  //NOT a constant expression where i is a variable
foo()   //NOT a constant expression where foo is a function identifier
```

When we write `x = 10 + 10;`, the compiler doesn't generate machine code to
calculate `10 + 10` then assign the result to `x`. During compilation, `10 + 10`
calculated by the compiler and no machine code is generated for this addition.
This is equivalent to writing `x = 20`.

```c
int main()
{
    int x = 10 + 10 - 20 + 6*3 + 4/2; //20
}
```

The generated assembly code (x86-64 clang 16.0.0, godbolt.org):

```asm
main:                                   # @main
        push    rbp
        mov     rbp, rsp
        mov     dword ptr [rbp - 4], 20 # 20 is computed by the compiler
        xor     eax, eax
        pop     rbp
        ret
```

## `sizeof`

`sizeof` is an operator. I said that constant expressions do not have variables
*typically*. Expressions with `sizeof` are kind of an exception to this.

```c
int x = 20;
int y = sizeof x; //4 for my platform, sizeof x is a constant expression
```

The generated assembly code (x86-64 clang 16.0.0, godbolt.org):

```asm
main:                                   # @main
        push    rbp
        mov     rbp, rsp
        mov     dword ptr [rbp - 4], 20
        mov     dword ptr [rbp - 8], 4
        xor     eax, eax
        pop     rbp
        ret
```

```c
//x86-64 clang 16.0.0 -std=c11
int x = 20;
int y[sizeof x]; //OK, sizeof x is a constant expression
int z[x];        //ERROR, can't define a variable length array (VLA) at file
                 //file scope, x is not a constant expression.

int main(void)
{
    return 0;
}
```

## `const`

Expressions with `const` variables are not constant expressions in C.

```c
const int x = 20;
int y[x];
```

Compilation with x86-64 clang 16.0.0, `-std=c90 -pedantic-errors` (godbolt.org)
gives the following error meaning that `x` is not a constant expression:

```text
error: variable length arrays are a C99 feature [-Werror,-Wvla-extension]
```

AFAIK, in C++ this rules is different from C. In this case, since `x` is a
`const int`, `x` is a constant expression. But in C, it is not!

```{disqus}
:disqus_identifier: c92b221d-d3bf-4648-8608-4d0fd33bcafc
```
