---
giscus: c63d6055-94a1-4479-b482-4dbf829914d3
---

# 🟰 Atama "Operatörü", `=`

`11-2.22.00`

Daha önceden de belirttiğim gibi Python'da `=` sembolü ile oluşturduğumuz atama
işlemi bir ifade değildir, bir deyimdir. O yüzden `=` atomu da aslında bir
operatör değildir. C, C++ gibi dillerde böyle değildir. Orada atama işlemleri
birer ifade oluşturur, Python'da ise deyim yani statement oluşturur. Ama biz
yine de `=` atomunu bir operatörmüş gibi ele alabiliriz bazı şeyleri kolay
anlamak için, diğer dillere benzetebiliriz şimdilik.

Python'da `a = b = 20` yapabiliriz. Burada önce `b = 20` ataması yapılır, sonra
`a = b` ataması yapılır. Her iki değişkenin değeri de `20` olur. Elbette önceki
notlarda anlattığım gibi Python'daki atamalar adres atamasıdır ama o detaya
tekrar burada girmiyorum.

> Bknz: [](degiskenler-nesneler.md)

C, C++, Java, C# gibi dillerde atama operatörü bir değer üretmektedir. Örneğin
aşağıdaki C kodunu ele alalım:

```c
//C kodu, clang 20.1.0 -O0

#include <stdio.h>

int main(void)
{
    int a, c;
    c = (a = 10) + 20;
    printf("a = %d, c = %d\n", a, c); //a = 10, c = 30
}
```

Burada `a = 10` ifadesi ile `a` ya `10` değeri atanır ama bu ifade de `10`
değerini üretir. O yüzden `c = 10 + 20` ile `c = 30` ataması yapılır.
**Python'da bu yapılamaz** çünkü atama operatörü değer üretmez.

```text
>>> c = (a = 10) + 20
  File "<stdin>", line 1
    c = (a = 10) + 20
           ^
SyntaxError: invalid syntax
```

Python'da biraz ileride göreceğimiz **Walrus operatörü**, `:=` vardır bu amaç
için kullanabileceğimiz.

---

Bunun bize getireceği çeşitli dezavantajlar olabilir. Örneğin diğer dillerde
`while ((ch = foo()) != 0)` gibi ifadeler yazarken Python'da bu geçersiz bir
ifade olmaktadır. Çünkü atama operatörü bir değer üretmemektedir Python'da.
