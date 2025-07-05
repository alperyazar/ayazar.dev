---
giscus: e754ef12-ed98-4c40-a2dd-6d70696c30b6
---

# `str` ve Formatlı Yazım İşlemleri

`9911`

Diyelim ki 3 adet değişkeni ekrana basmak istiyoruz, `a`, `b` ve `c` olsun.

```python
s = 'a = ' + str(a) + ', b = ' + str(b) + ', c = ' + str(c)
print(s)
```

Bunu yapabiliriz ama çok da pratik değildir. Bu tarz işlemlere
**formatlı yazım** denmektedir. Bunun için dilde kullanılan temelde 3 adet
yöntem vardır.

1. `%` operatör metodu ile formatlı yazım
2. `str` sınıfının `format()` metodu ile formatlı yazım
3. String enterpolasyonu ile formatlı yazım.

String enterpolasyonu Python'a sonraları, 3.6 ile, gelmiştir. Diğer iki yönteme
göre hem daha pratik hem de hızlı bir formatlama sunmaktadır.

**Bu yüzden hemen hemen her zaman string enterpolasyonu kullanılır.**

## `str`nin `format()` Metodu

`format()` metodu istenildiği kadar argüman alabilmektedir. Bu metodda yazı
içerisinde `{n}` şeklinde *yer tutucular* olmalıdır. Bu metod argümanları
numaralarına göre yerleştirir. İlk argümanın numarası `0`dır.

Örneğin:

```text
>>> a = 10; b = 20; c = 30

>>> s = 'a = {0}, b = {1}, c = {2}'.format(a, b, c)

>>> print(s)
a = 10, b = 20, c = 30
```

Görüldüğü gibi burada `{n}` kalıpları argümanlarla değiştirilmiştir.

---

Eğer olmayan bir argümana erişmeye çalışırsak `IndexError` exception oluşmakta
ama kullanmadığımız bir argüman geçersek problem olmamaktadır.

```text
>>> print('a = {10}, b = {1}, c = {2}'.format(a, b, c))

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: Replacement index 10 out of range for positional args tuple

>>> print('{0}'.format(a, b, c))
10
```

---

Aynı yer tutucu birden fazla kez kullanılabilir ve `format()`ın argüman türleri
`int` vs olabilir.

---

Yer tutucularda `{}` şeklinde boş küme parantezi kullanabiliriz. Bu durumda
her `{}` sırası ile argümanlarla eşlenir. Fakat böyle bir kullanımda ya
yer tutucuların hepsi numarasız olmalı ya da numaralı olmalıdır.

Numarasız yer tutucu sıklıkla kullanılmaktadır. Fakat burada aynı yer tutucuyu
tekrarlamak mümkün değildir.

```text
>>> print('a = {}, b = {}, c = {}'.format(a, b, c))
a = 10, b = 20, c = 30
```

---

`format()` metodunda aslında daha ileri kullanımlar da mevcuttur. Bunlar
genelde `:` karakteri ile yapılır.

Örneğin:

```text
>>> day = 7
>>> month = 6
>>> year = 2025

>>> print('{0:02d}/{1:02d}/{2:04d}'.format(day, month, year))
07/06/2025
```

Ya da başka bir sayı sisteminde yazdırma yapabiliriz.

```text
>>> x = 100

>>> print('{:X}'.format(x))
64
```

Çeşitli kullanım senaryoları için:

<https://docs.python.org/3/library/string.html#formatspec>

adresine bakılabilir.

---

`10116`

`format()`içerisinde gerçekten `{` karakteri basmak istiyorsak `{{` ya da `}}`
şeklinde ikili kullanım yapmalıyız.

## String Enterpolasyonu - String Interpolation

Bu özellik birçok programlama dilinde olmasına rağmen Python'a versiyon 3.6 ile
beraber gelmiştir.

Bunun için string'e yapışık `f` veya `F` öneki getirilir. Burada yapılan işlem
`format()` metoduna benzer. Ama burada `{}` içerisinde bir ifade bulunmalıdır.
Yorumlayıcı akışta buraya geldiğinde bizzat `{}` içerisinde olan ifadelerin
değerini hesaplar ve yeni bir `str` oluşturarak yer tutucu ile değiştirir.

Örneğin:

```text
>>> a = 10; b = 20
>>> print(f'a = {a}, b = {b}')
a = 10, b = 20
```

---

`format()`, `str` sınıfının bir metodudur. Enterpolasyon ise doğrudan
yorumlayıcı tarafından yapılan bir şeydir. Bu yüzden göreceli daha hızlı
çalışmaktadır. O yüzden artık Python'da default olarak programcılar tarafından
hep bu kullanılır.

```text
>>> a = 10; b = 20; c = 30

>>> s = f'a = {a}, b = {b * b}, c = {c}'

>>> print(s)
a = 10, b = 400, c = 30
```

Hatta

```python
import math

x = 10
print(f"karekök {x} = {math.sqrt(x)}")       # karekök 10 = 3.1622776601683795
```

gibi kodlar da yazabiliriz.

---

String enterpolasyonda string'i `'` ile kullanıyorsak ve `{}` içerisinde de `'`
kullanılacaksa, bu karışma engellenmelidir.

```text
>>> s = f'{', '.join(a)}'
  File "<stdin>", line 1
    s = f'{', '.join(a)}'
            ^
SyntaxError: f-string: expecting '}'
```

Biz bu durumda çift tırnak ya da üç tırnak ile çözüm sağlayabiliriz örneğin.

```text
>>> a = ['alper', 'yazar']
>>> s = f"{', '.join(a)}"
>>> s
'alper, yazar'
```

---

Burada `{}` içerisinde `\` kullanılamamakta olup aşağıdaki ifade geçersizdir.

```text
>>> s = f'{\', \'.join(a)}'
  File "<stdin>", line 1
    s = f'{\', \'.join(a)}'
                           ^
SyntaxError: f-string expression part cannot include a backslash
```

---

`10211`

`format()` metodunun da kullanışlı olabildiği durumlar hala olabilir. Örneğin
tekrarlı ifadeleri yazmak `format()` ile daha kolay olabilir. Örnek:

```text
>>> x = 10

>>> print(f'{x * x}, {x * x}, {x * x}, {x * x}, {x * x}')
100, 100, 100, 100, 100

>>> print('{0}, {0}, {0}, {0}, {0}'.format(x * x))
100, 100, 100, 100, 100
```

---

Enterpolasyonda da `format()`taki `:` içeren kurallar geçerlidir.

```python
print(f'{day:02d}/{month:02d}/{year:04d}') # geçerlidir.
```

## `%` ile Formatlama

Python 2'de olan bir yöntemdir. Dil, C'nin etkisi altında olduğu için bu tercih
edilmiştir, `%d` ile `int` yazdır, `%f` ile `float` yazdır gibi.

Bu formatlamada `%` **operatörü** kullanılır, `str`nin dışında, ve bunun sağında
bir demet solunda ise `str` vardır. Yani `%` karakteri sadece `str`nin içinde
geçmez, ayrıca sonrasında bir operatör olarak da bulunur.

```text
>>> x = 10; y = 20

>>> 'x = %d, y = %d' % (x, y)
'x = 10, y = 20'
```

---

`%` operatörünün sağında tek bir ifade olabilir ya da demet olmalıdır. Tek bir
değeri formatlamak için demet kullanmaya gerek yoktur. Birden fazla için demet
şarttır. Demet yerine liste gibi başka bir dolaşılabilir nesne kullanamayız.

```text
>>> 'x = %d' % x
'x = 10'
```

`10300`
