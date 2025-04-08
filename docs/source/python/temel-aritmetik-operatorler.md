---
giscus: 28b5999f-0f53-485d-b5c5-625264b68842
---

# Temel Aritmetik Operatörler

İlk olarak toplama `+`, çıkarma `-`, çarpma `*` ve bölme `*` operatörlerini ele
alalım. Temel dört işlem operatörleri ile ilgili çok söylenebilecek bir şey yok,
biraz bölme operatörüne bakacağız. Bu 4 operatör de *binary infix arithmetic
operator* yani *iki operandlı araek aritmetik operatör* kategorisindedir.

## Bölme, `/`, Operatörüne Dikkat

Python dilinde bölme, `/`, operatörünün davranışı C, C++, Java ve C# diline göre
farklılık göstermektedir. Python'da her iki operand da `int` türünden olsa da
sonuç `float` olmaktadır.

Aşağıdaki ifadeye bir bakalım:

```python
x = 5 / 2
```

Bu ifadede `5` ve `2`, `int` türdendir. C, C++, Java, C# gibi dillerde
yukarıdaki işlemin sonucu `2` olmaktadır, bu dillerde *integer division*
yapılmaktadır. Python'da ise sonuç `2.5` çıkmakta ve tür de doğal olarak `float`
olmaktadır. Python'da `/` operatörü operandların `int` veya `float` olmasından
bağımsız olarak her zaman `float` sonuç üretmektedir.

Aşağıdaki örneklere bakalım.

```python
print(type(10 / 4))   # float
print(type(4 / 2))    # float
print(type(2.5 / 2))  # float
print(type(2 / 0.5))  # float
```

## floordiv Operatörü, `//`

Bu da diğerleri gibi *binary infix arithmetic* bir operatördür. Python'da bu
operatör bir *tamsayı bölmesi* yapmak için kullanılır ama sonucun `int` türden
olması garanti değildir. `/`, bölme, operatörünün aksine eğer her iki operand da
`int` türden ise sonuç da `int` türden çıkmaktadır. Fakat en az bir operand
`float` türden ise bu sefer sonuç `float` türden olmaktadır.

Tür konusuna ek olarak çıkan sonuç da `/` operatörüne göre farklıdır. Bu
operatör işlem sonucunu en yakın tam sayı değere *aşağıya doğru yuvarlar* yani
*floor* işlemi gerçekleştirilir.

Sayının "aşağıya doğru yuvarlanması" ondalık kısmının atılıp tam sayı kısmının
kullanılması değildir. Eğer sayı pozitif ise bu şekilde olur, örneğin `3.4`
sayısını aşağıya yuvarladığımız zaman `3` sayısını elde ederiz. Aslında negatif
sayılarda da böyledir, sayıdan küçük ilk tam sayıyı elde ederiz. `-3.4` sayısını
*floor* işlemine maruz bıraktığımızda sonuç `-4` olmaktadır, `-3` değil.

Aşağıdaki örneklere bir bakalım:

```python
x = 10 // 4
print(x, type(x)) # 2, int

x = 10.0 // 4
print(x, type(x)) # 2.0, float

x = -10 // 4
print(x, type(x)) # -3, int

x = 10.0 // -4
print(x, type(x)) # -3.0, float
```

Bu davranış C, C++, Java ve C# gibi dillerden farklıdır. Burada yuvarlama
işlemleri *sıfıra doğru* yapılırken, towards zero, Python'da ise *floor* işlemi
yapılır. Pozitif sayılar için bu iki yöntem de aynı sonucu verir. Negatif
sayılarda ise sonuç ayrışır. Towards zero işlemlerde işaretten bağımsız olarak
`.` nın sağı atılır gibi düşünebiliriz.

Aşağıdaki örneğe bir bakalım:

```c
// C kodu

#include <stdio.h>

int main(void)
{
    printf("%d\n", (int)(10.0 / 4)); // 2, Python'a benzer
    printf("%d",  (int)(-10.0 / 4)); // -2 C'de, Python'da -3 çıkıyor.
}
```

## Mod Alma Operatörü, Modulo Operator, `%`

Önceki operatörler gibi binary infix bir aritmetik operatördür. Mod alma
operatörü, `%`, iki sayının birbirine bölümünden kalan, kalan kısmı hesaplamak
için kullanılır. Bu işlemin sonucunun işareti her zaman ikinci operandın yani
bölen kısmın işareti ile aynıdır, ya da sıfırdır. Sonucun mutlak değeri ise her
zaman ikinci operandın mutlak değerinden küçüktür. [^1f]

Eğer her iki operand da `int` ise sonuç da `int` türden olmaktadır. En az bir
operand `float` ise sonuç da `float` türdendir.

Aşağıdaki örneklere bakalım:

```python
x = 10 % 4
print(x, type(x)) # 2, int

x = 10.0 % 4
print(x, type(x)) # 2.0, float

x = -10 % 4
print(x, type(x)) # 2, int

x = -10.0 % 4
print(x, type(x)) # 2.0, float

x = 10.0 % -4
print(x, type(x)) # -2.0, float
```

---

Python'da mod alma operatörünün davranışı, C ve C++ dillerine göre farklılık
göstermektedir. C ve C++ gibi dillerde bu operatörün her iki operandının türünün
bir tam sayı türü olması gerekmektedir. Python'da ise operandlar floating-point
türlerden olabilir.

Aşağıdaki C koduna bir bakalım:

```c
//C kodu

#include <stdio.h>

int main(void)
{
    printf("%d\n", (int)(10 % 4));
    printf("%d", (int)(-10.0 % 4)); //Hata
}
```

---

Python'da önemli bir fark daha vardır. `a` bölünen, `b` bölen, `c` bölüm ve `d`
de kalan olsun. Bu durumda `a = b * c + d` eşitliği sağlanmaktadır.

Python'da `c` yani bölüm hesaplanırken arka planda biraz yukarıda öğrendiğimiz
`//` yani floordiv operatörü kullanılır. Diğer dillerde ise `/` operatörü ile
*integer division* işleminin yapıldığını düşünebiliriz.

`-10 % 4` ifadesini ele alalım.

- Python'da `-10 // 4`, işleminin sonucu floordiv işleminden dolayı `-3`
  olmaktadır. Bu durumda `-10 = 4 * (-3) + 2` sağlanır, yani kalan `2` olur.
  Sonuç olarak `-10 % 4` işleminin sonucu `2` olur.
- C ve benzeri dillerde ise `-10 / 4` işleminin sonucu *sıfıra doğru yuvarlama*
  yaklaşımından dolayı `-2` olur ve `-10 = 4 * (-2) + (-2)` sağlanır. Bu yüzden
  bu dillerde `-10 % 4` işleminin sonucu `-2` olur.

Bu farklılık mod alma operatörü ve negatif sayılarla çalışırken Python'da diğer
dillerden farklı sonuçlar almamıza neden olabilir.

Aşağıdaki örneğe bakalım:

```c
// C kodu

#include <stdio.h>

int main(void)
{
    printf("%d\n", (int)(-10 % 4));  // -2
    printf("%d\n", (int)(10 % -4));  //  2
    printf("%d\n", (int)(-10 % -4)); // -2
}

```

```python
# Python kodu

x = -10 % 4
print(x, type(x)) # Sonuç 2 ve tür int'tir

x = 10 % -4
print(x, type(x)) # -2, int

x = -10 % -4
print(x, type(x)) # -2, int
```

Özetle

| İfade      | Python | C    |
|------------|--------|------|
| `-10 % 4`  | `2`    | `-2` |
| `10 % -4`  | `-2`   | `2`  |
| `-10 % -4` | `-2`   | `-2` |

tablosu oluşmaktadır.

Bu yüzden Python'da bir negatif sayının bir pozitif sayıya bölümünden kalan mod
alma operatörü, `%`, ile bulunduğu zaman kalan yani bu operatörün sonucu her
zaman pozitif olmaktadır.

Aşağıdaki denklik Python'da sağlanmaktadır: [^1f]

`x == (x//y)*y + (x%y)`

[^1f]: <https://docs.python.org/3.3/reference/expressions.html#binary-arithmetic-operations>
