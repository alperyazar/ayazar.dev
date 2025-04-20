---
giscus: b2895859-a09d-4821-b599-6b945565b5c9
---

# Farklı Temel Türlerin Birlikte İşleme Sokulması

`13-0.39.50`

Python dahil olmak üzere birçok programlama dilinde farklı türdeki nesneler
beraber işleme sokulabilmektedir. Buradaki kuralları öğrenmemiz gerekir. C, C++,
Java, C#, Python gibi dillerde farklı türlerle işlem yapılabilirken Swift
dilinde bu özellik yoktur, Swift tür dönüştürmesini programcının yapmasını
istemektedir.

## `int` ve `float`

Aritmetik operatörlerde iki operand da `int` ise sonuç `int`, `float` ise
`float` çıkmaktadır. Ama bir `int` ile `float` işleme sokulursa sonuç `float`
çıkar.

| Operand 1 | Operand 2 | Sonuç (`/` Hariç)        |
|-----------|-----------|--------------------------|
| `int`     | `int`     | `int` (`/` için `float`) |
| `int`     | `float`   | `float`                  |
| `float`   | `int`     | `float`                  |
| `float`   | `float`   | `float`                  |

**`/` operatörü her zaman `float` değer üretmektedir.**

Örneğin:

```text
>>> type(3 + 4)
<class 'int'>

>>> type(3.5 + 4)
<class 'float'>

>>> type(4 / 2)
<class 'float'>
```

---

Elbette önceki yazılarda da konuştuğumuz gibi `int` bir değer `float` değerine
dönüştürülürken değerde (mantis) kayıplar oluşabilir, bu durum bir exception
sebebi değildir. Ama `OverflowError` gibi bir exception oluşursa yine aritmetik
işlem sırasında exception da oluşabilir.

---

Karşılaştırma operatörleri ise her zaman `bool` türden değer üretirler.

```text
>>> type(10 > 5.0)
<class 'bool'>
```

## `bool` Türü

Aritmetik işlemlere sokulurken `bool` türleri `int` türüne adeta otomatik
çevrilir. Bu çevrim sırasında `False`, `0`; `True` ise `1` olarak çevrilir.

Aritmetik işlemleri düşündüğümüz zaman:

| Operand 1 (veya 2) | Operand 2 (veya 1) | Sonuç (`/` Operatörüne Dikkat) |
|--------------------|--------------------|--------------------------------|
| `bool`             | `int`              | `int`                          |
| `bool`             | `float`            | `float`                        |
| `bool`             | `complex`          | `complex`                      |

```text
>>> type(True/True)
<class 'float'>

>>> type(True + 1)
<class 'int'>

>>> type(True + 1.0)
<class 'float'>

>>> type(True + False)
<class 'int'>
```

---

Java ve C# gibi dillerde `bool` türü hiçbir türle aritmetik işleme sokulamaz.
Ama Python dilinde, C dilinde olduğu gibi, bu geçerli bir durumdur.

```text
>>> (5 > 0) + 10
11
```

Burada `5 > 0`, `bool` türden `True` değerinde bir değer üretir ve `True`, `10`
ile aritmetik işleme sokulunca `1` olarak ele alınır ve sonuç `11` çıkar.

## `complex` Türü

`complex` türü ile `int` veya `float` veya `bool` türü işleme sokulursa sonuç
`complex` türden elde edilir.

## `str` Türü

`13-1.07.46`

İki `str` türünden değer toplama işlemine sokulabilir ama diğer aritmetik
işlemler yapılamaz. Toplama işlemi sonucunda yine `str` türünden bir nesne elde
edilir. Değer olarak da iki operandın birleşimi olan bir yazı vardır. Yani
*concatenate*, *concat*, işlemi yapılmış olur. Java ve C#'ta da bu özellik
vardır.

```text
>>> x = "alper" + "yazar"
>>> x
'alperyazar'
```

C# ve Java dilinde `+` operatörünün bir operandı `str` diğer operandı başka
türlerden olabilmektedir. Bu dillerde diğer tür otomatik olarak `str` türüne
dönüştürülür ve yine concat işlemi yapılır. Python'da ise bu işlem otomatik
olarak yapılmaz, programcının elle yapması gerekir.

```text
>>> print('Alper' + 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

>>> print('Alper' + str(2))
Alper2
```

---

Python'da bir `str`, `int` türden bir değerle çarpılabilir. Burada
**repetition** yani **yineleme** işlemi yaplmaktadır.

```text
>>> print('alper' * 3)
alperalperalper

>>> print(3 * 'alper')
alperalperalper

>>> s = ' ' * 5 + 'Ankara' + ' ' * 5
>>> s
'     Ankara     '
```

Negatif bir değer ile ya da `0` ile çarpılırsa boş string elde edilir.

```text
>>> print(0 * 'alper')

>>> print(-2 * 'alper')

>>> print(-2. * 'alper')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
```

`13-1.18.12`
