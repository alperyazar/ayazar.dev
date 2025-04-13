---
giscus: 189907c4-8c77-4bfe-8269-3a16f208ab98
---


# ♻️ Tür Dönüşümleri (YARIM)

`12-1.18.24`

Tür dönüştürme, **type conversion** ya da **type cast** olarak geçmektedir.

Python'da tüm atama işlemlerinin adres ataması olduğunu konuşmuştuk.

`a = 3.14` dediğimiz zaman aslında değeri `3.14` olan bir `float` nesnesi
oluşuyor ve adresi `a` değişkenine atanıyordu.

Bazen şunu da isteyebiliriz: `a` nın gösterdiği yerdeki nesnenin türü `float`
ama biz onu `int` olarak ele almak isteyebiliriz. İşte bu işlem **tür
dönüştürmedir.**

Tür dönüştürme, bir nesnenin içerisindeki değeri değiştirerek başka bir türden
bir nesne biçiminde elde edilmesi olarak tanımlanabilir.

---

Python'da gördüğümüz `int`, `float`, `bool` gibi türler aslında birer sınıftır
ve biz bu sınıflardan birer nesne (OOP'deki O anlamında nesne) yaratmış
oluyoruz.

Tür dönüştürme

`<dönüştürülecek hedef tür>(<ifade>)`

şeklinde yapılmaktadır.

Örneğin

```python
a = 3.14
b = int(a)
```

şeklinde yapmaktayız. Bunu bir fonksiyon çağrısı olarak ele alabiliriz.

---

Tür dönüştürme işlemiyle yeni bir nesne yaratılmaktadır. Her tür dönüştürme
işlemi, yeni bir nesne yaratır. Yani var olan nesnenin türü değiştirilerek
yapılmamaktadır, nesnenin immutable ya da mutable olması konusu değil. Var olan
nesnenin değerinden yeni bir nesnenin yaratılmasını sağlamaktadır.

```text
>>> x = 10
>>> y = float(x)

>>> print(id(x), id(y))
1754405759568 1754415633136

>>> print(type(x), type(y))
<class 'int'> <class 'float'>
```

Görüldüğü gibi ikisi de farklı nesnedir.

---

`T` bir tür belirtmek üzere `T` türünden bir nesnenin yaratılması `T(...)`
biçiminde bir ifadeyle yapılmaktadır. Bu ileride göreceğimiz bir konudur.

---

Eğer bir ifade aynı türe dönüştürülüyorsa ve o tür değiştirilemez bir tür ise,
temel türler gibi, Python implementasyonu yeni bir nesne yaratmayabilir. Bu,
ilgili implementasyonun kendi içerisinde yaptığı optimizasyon ile ilgilidir.

```text
>>> x = 4
>>> y = int(4)
>>> x is y
True
```

Örneğin yukarıda görebileceğimiz gibi CPython benim sistemimde yeni bir nesne
yaratmadı, yaratabilirdi ama.

---

Python'daki temel türler, yani şimdiye kadar gördüklerimiz, `T(...)` biçiminde
birbirlerine dönüştürülebilmektedir. Elbette programcının bu dönüşümün sonucunda
nelerin olacağını bilmesi gerekir. Hadi gelin, durumlara bir bakalım.

| Nereden ↓ / Nereye → | `int` | `float` | `bool` | `str` | `complex` | `NoneType` |
|----------------------|-------|---------|--------|-------|-----------|------------|
| `int`                |   -  | ✅       | -      | -     | -         | -          |
| `float`              | ✅     | -      | -      | -     | -         | -          |
| `bool`               | ✅     | -       | -     | -     | -         | -          |
| `str`                | ✅    | -       | -      | -    | -         | -          |
| `complex`            | 🚫     | -       | -      | -     | -        | -          |
| `NoneType`           | 🚫     | -       | -      | -     | -         | -         |

- ✅ ile işaretlenen dönüşümler bu yazıda anlatılmaktadır ve legaldir.
- 🚫 ile işaretlenen dönüşümler bu yazıda anlatılmakta fakat illegaldir.

---

## `float` → `int` ✅

Bu dönüşümde nokta, `.`, dan sonraki kısım atılır. Bu, **truncation toward zero**
yaklaşımıdır. Herhangi bir tarafa yuvarlama, *floor* ya da *ceil*, yapılmaz.
Sayının negatif ya da pozitif olması sonucu değiştirmez.

```text
>>> int(3.89)
3

>>> int(-3.89)
-3
```

---

Burada C gibi dillerden farklı olarak lehimize bir durum vardır. C gibi dillerde
bir `int` nesne, `float` bir sayının tam sayı kısmını tutamayabilir, aralığı
yeterli olmayabilir, tanımsız davranış oluşabilir. Python'da ise `int`
nesnelerin tutabileceği değerlerin bir sınırı olmadığı için böyle bir derdimiz
yoktur.

## `bool` → `int` ✅

`12-1.37.10`

`bool` bir nesne iki farklı değer tutabilir, `True` ve `False`. Eğer `int`e
dönüşüm yapılırsa, `True` değer `1`, `False` ise `0` olarak dönüştürülür.

```text
>>> print(int(True))
1

>>> print(int(False))
0
```

## `str` → `int` ✅

`12-1.38.35`

Eğer bir string içerisinde, tam sayıya dönüşüm için anlamlı olacak karakterler
varsa yeni bir `int` nesne yaratılır ve yazı aslında sayıya dönüştürülmüş
olur. Fakat sayıya dönüştürülemeyecek karakterler içeriyorsa bu durumda bir
*exception*, `ValueError`, oluşur. Exception konusunda biraz konuşmuştuk.
Programcı bunu ele almazsa bu durumda program sonlanmaktadır.

Bir yazının başındaki boşluk karakterlere *leading space*, yazının sonundaki
karakterler ise *trailing space* denmektedir. Bu dönüşüm sırasında ilgili
boşluklar, white space, dikkate alınmaz, problem oluşturmaz.

```text
>>> print(int('120'))
120

>>> print(int(' 1234     '))
1234

>>> print(int('-42'))
-42

>>> print(int('120.55'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '120.55'

>>> print(int('alper'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'alper'
```

---

Burada yazının onluk sayı sisteminde olması şart değildir. İstersek `int()`
fonksiyonunu çağırırken ikinci parametre olarak dönüşümün hangi tabanda
olacağını belirtebiliriz.

```text
>>> print(int('0f'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '0f'

>>> print(int('0f', 16))
15

>>> print(int('0x0f', 16))
15
```

Hatta `print(int('g', 17))` gibi gariplikler de yapabiliriz. 😬

## `complex` → `int` 🚫

`complex` tür, `int` türüne dönüştürülememektedir.

```text
>>> print(int(3+4j))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't convert complex to int
```

## `NoneType` → `int` 🚫

`NoneType` türünde olan tek değer olan `None`, `int` e dönüştürülememektedir.

```text
>>> print(int(None))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
```

---

`int` bir ifadenin `int` türüne dönüştürülmesi geçeli fakat anlamsızdır, aynı
değer elde edilir.

## `int` → `float` ✅

`12-2.02.30`
