---
giscus: 189907c4-8c77-4bfe-8269-3a16f208ab98
---


# ♻️ Temel Tür Dönüşümleri

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
| `int`                | 🟢     | ✅       | ✅      | ✅     | ✅        | 🚫          |
| `float`              | ✅     | 🟢       | ✅      | ✅     | ✅        | 🚫          |
| `bool`               | ✅     | ✅       | 🟢      | ✅     | ✅        | 🚫          |
| `str`                | ✅     | ✅       | ✅      | 🟢     | ✅       | 🚫          |
| `complex`            | 🚫    | 🚫      | ✅      | ✅     | 🟢         | 🚫          |
| `NoneType`           | 🚫    | 🚫      | ✅      | ✅     | 🚫        | 🚫          |

- ✅ ile işaretlenen dönüşümler bu yazıda anlatılmaktadır ve legaldir.
- 🚫 ile işaretlenen dönüşümler bu yazıda anlatılmakta fakat illegaldir.
- 🟢 `NoneType` hariç diğer türler kendi içinde dönüştürülebilmektedir. Hoş,
  pek anlamlı değildir.

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

---

## `int` → `float` ✅

`12-2.02.30`

`int` bir değer `float` türüne dönüştürülürken eğer sayı [IEEE 754
double-precision
format](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)
ile "kayıpsız" ifade edilebiliyorsa sayının sonuna `.0` gelmiş gibi
dönüştürülür. Fakat Python'da `int` sayıların aslında bir sınırının olmadığnı
söylemiştik, diğer programlama dillerinina aksine. İşte bu durumda bir `int`
değer `float` değerin tutamayacağı kadar büyük bir değeri tutuyor olabilir. Bu
durumda ise `OverflowError` exception oluşmaktadır. Mesela C'deki `long long`
türünü ele alalım, tipik olarak 8 byte olmaktadır. Bu byte adedinin tutabileceği
tüm sayılar zaten kayar noktalı formatta ifade edilebilmektedir.

Bundan bağımsız olarak bu dönüşümde bir durum daha vardır kayar noktalı
sayıların formatı ile ilgilidir ve dilden bağımsızdır. Daha önceden de
konuştuğumuz gibi kayar noktalı sayılar tüm sayıları kusursuzca ifade
edememektedir. Bu durumda `int` bir sayı `float` olarak ifade edilemese bile
mantis, fraction, yani hiç noktalı kısımlar olmasaydı sayı nasıl olurdu kısmı,
kaybıyla en yakın `float` sayı ile ifade edilir. Bu durumda bir exception
oluşmaz.

Örneğin

```text
>>> x = 12345678901234567890
>>> y = float(x)
>>> int(y)
12345678901234567168
>>> x - int(y)
722
```

Bu örnekte `x` e atadığımız değer önce `float` bir değere çevrilmiş daha sonra
bu değerden tekrar `int` değere dönünce ilk orijinal değere ulaşılamamıştır.
Nedeni, ilk `int → float` dönüşüm sıraında kayıp yaşanmasıdır. Ama bu durum
bir exception oluşturmaz.

Özetle `int → float` dönüşümünde:

1️⃣ Sayı `float` formatı ile kayıpsız ifade edilebiliyorsa sonuna `.0` konmuş
olur.

2️⃣ Kayıplı ifade edilebilir, en yakın değere dönüştürülür ama exception
oluşmaz. "En yakın değer", dönüştürülen sayıdan büyük ya da küçük olabilir,
bunun detayları ayrıca ele alınmalıdır.

3️⃣ Değer sınırı aşıyorsa `OverflowError` Exception oluşur.

## `bool` → `float` ✅

`bool` bir nesne iki farklı değer tutabilir, `True` ve `False`. Eğer `float`a
dönüşüm yapılırsa, `True` değer `1.0`, `False` ise `0.0` olarak dönüştürülür.

```text
>>> print(float(True))
1.0

>>> print(float(False))
0.0
```

## `str` → `float` ✅

`str` → `int` dönüşümü gibi bu dönüşüm de benzer bir şekilde yapılır. Eğer
stringin içerisindeki karakterler yani tutulan yazı `float` türden ifade edilen
bir sayı biçimindeyse dönüşüm yapılır. Eğer karakterler anlamsız ise
`ValueError` exception oluşur.

Dönüşüm yaptığımız `float()` fonksiyonu tek parametrelidir, `int()`
fonksiyonunun aksine ikinci argüman ile taban bilgisi geçilmez.

Bu dönüşüm sırasında `float` türü ile ifade edilemeyecek çok büyük ya da çok
küçük sayıların yazısal karşılıklarının nasıl dönüştürüleceği *Python Standard
Library Reference* içerisinde açıkça belirtilmemiştir. CPython
implementasyonunun bu gibi durumlarda `+inf` ya da `-inf` değerlerini ürettiğini
söyleyebiliriz. Yine `int`e dönüşümde olduğu gibi yazı içerisindeki *leading
space* ya da *trailing space* göz ardı edilir.

Örneğin:

```text
>>> x = ' 123.567  '
>>> y = float(x)
>>> y
123.567

>>> x = '123.a'
>>> float(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '123.a'

>>> x = '0x10'
>>> float(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '0x10'
```

## `complex` → `float` 🚫

`complex` tür, `float` türüne dönüştürülememektedir.

```text
>>> print(float(3+4j))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float() argument must be a string or a real number, not 'complex'
```

## `NoneType` → `float` 🚫

`NoneType` türünde olan tek değer olan `None`, `float` e dönüştürülememektedir.

```text
>>> print(float(None))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float() argument must be a string or a real number, not 'NoneType'
```

---

Şimdi `bool` türüne olan dönüşümlere bakalım.

---

## `int` → `bool` ✅

`13-0.00.00`

Eğer `int` değer `0` dışı bir değerse, pozitif ya da negatif fark etmez, `True`
eğer `0` ise `False` olarak dönüştürülür.

```text
>>> print(bool(3))
True

>>> print(bool(-3))
True

>>> print(bool(0))
False

>>> print(bool(-0))
False
```

## `float` → `bool` ✅

`int` dönüşümü ile benzerdir. Sayı `0.0` değilse `True`, `0.0` ise `False` olur.

```text
>>> print(bool(3.5))
True

>>> print(bool(-3.0))
True

>>> print(bool(0.0))
False

>>> print(bool(-0.0))
False
```

## `str` → `bool` ✅

Eğer string boş ise dönüşüm `False`, dolu ise `True` olarak yapılır. Burada
string içerisindeki yazıya bakılmaz. Yani `'False'` yazısı dolu bir yazı
olduğu için `True` olarak dönüştürülür.

```text
>>> print(bool('False'))
True

>>> print(bool(''))
False

>>> print(bool(' '))
True
```

## `complex` → `bool` ✅

Eğer hem gerçek hem de sanal kısmı `0` değilse dönüşüm `True`, her iki kısım
da `0` ise `False` olarak yapılır.

```text
>>> print(bool(3 + 4j))
True

>>> print(bool(3 + 0j))
True

>>> print(bool(0 + 4j))
True

>>> print(bool(0 + 0j))
False
```

## `NoneType` → `bool` ✅

`NoneType` türünde olan tek değer olan `None`, `bool` türüne `False` olarak
dönüştürülür.

```text
>>> print(bool(None))
False
```

## Diğer Veri Türleri → `bool` ✅

Henüz görmedik ama yakında göreceğimiz liste, demet, sözlük, küme gibi veri
yapıları eğer boş ise `False`, dolu ise `True` olarak `bool` türüne
dönüştürülür.

```text
>>> x = (10, 20)

>>> type(x)
<class 'tuple'>

>>> print(bool(x))
True
```

---

## `int` → `complex` ✅

`13-0.19.38`

Bu dönüşüm yapılabilir, sanal kısmı `0` olan bir `complex` sayı elde edilir.

```text
>>> print(complex(3))
(3+0j)
```

## `float` → `complex` ✅

Bu dönüşüm yapılabilir, sanal kısmı `0` olan bir `complex` sayı elde edilir.

```text
>>> print(complex(3.0))
(3+0j)
```

## `bool` → `complex` ✅

Bu dönüşüm yapılabilir, sanal kısmı `0` olan bir `complex` sayı elde edilir.
Eğer `bool` türünün değeri `True` ise gerçek kısım `1`, `False` ise `0`
olmaktadır.

```text
>>> print(complex(True))
(1+0j)

>>> print(complex(False))
0j
```

```{attention}
`complex` türündeki sayıların gerçek ve sanal kısımları aslında ayrı ayrı
birer `float` sayı olarak düşünülebilir. Fakat yazdırılırken düzgün gözüksün
diye eğer sayıda nokta yoksa `.` kullanılmamaktadır. Ama her durumda arka planda
iki adet `float` sayıdan oluştuğunu düşünebiliriz. Dönüşüm ile elde ediyorsak
kaynak tür ne olursa olsun bu böyledir.
```

## `str` → `complex` ✅

Bu dönüşümün olması için yazının `a±bj` formatında olması gerekmektedir. Yine
diğer dönüşümlerde olduğu gibi leading ve trailing space karakterleri dikkate
alınmaz ama yazının ortasında boşluk olmamamlıdır.

```text
>>> print(complex('3+4j'))
(3+4j)

>>> print(complex('  3+4j '))
(3+4j)

>>> print(complex('3-4j'))
(3-4j)

>>> print(complex('3- 4j'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: complex() arg is a malformed string

>>> print(complex('4j+3'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: complex() arg is a malformed string

>>> print(complex('4j-3'))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: complex() arg is a malformed string
```

## `NoneType` → `complex` 🚫

`NoneType` türünde olan tek değer olan `None`, `complex` e dönüştürülememektedir.

```text
>>> print(complex(None))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: complex() first argument must be a string or a number, not 'NoneType'
```

## `int` → `str` ✅

Sayının yazı formu elde edilir.

```text
>>> x = str(5)
>>> x
'5'
```

## `float` → `str` ✅

Sayının yazı formu elde edilir.

```text
>>> x = str(5.5)
>>> x
'5.5'
```

## `bool` → `str` ✅

`True` değer `'True'`, `False` değer ise `'False'` olarak çevirilir.

```text
>>> x = str(True)
>>> x
'True'

>>> x = str(False)
>>> x
'False'
```

## `complex` → `str` ✅

Sayının yazı formu elde edilir.

```text
>>> x = str(4j + 3)
>>> x
'(3+4j)'
```

`complex` sayıların `bj + a` formunda da ifade edilebildiğine fakat dönüşümün
`a+bj` formatında yapıldığında dikkat ediniz.

## `NoneType` → `str` ✅

`NoneType` türünde olan tek değer olan `None`, stringe `'None'` olarak
dönüştürülür.

```text
>>> x = str(None)
>>> x
'None'
```

---

## `NoneType` Türüne Dönüşüm 🚫

`NoneType` türünden tek değer olan `None` dahil olmak üzere hiçbir tür
`NoneType` türüne dönüştürülemez.

```text
>>> print(NoneType(None))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'NoneType' is not defined

>>> print(NoneType(4))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'NoneType' is not defined
```

`13-0.39.50`

## Argümansız Tür Dönüşüm Fonksiyonları

Tür dönüşümü için gördüğümüz `int()`, `float()` gibi fonksiyonları argümansız
çağırdığımız zaman bize sabit değerli nesneler verirler.

| Fonksiyon   | Değer   |
|-------------|---------|
| `int()`     | `0`     |
| `float()`   | `0.0`   |
| `str()`     | `''`    |
| `complex()` | `0j`    |
| `bool()`    | `False` |

```text
>>> print(int())
0
>>> print(float())
0.0
>>> print(str())

>>> print(complex())
0j
>>> print(bool())
False
```

gibi.
