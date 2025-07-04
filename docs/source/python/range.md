---
giscus: 7ccb8cc7-0b23-4253-b6c9-4c1cf4902a40
---

# `range()`

`6928`

`range()` isimli fonksiyon, `range` aslında bir sınıftır bize `range` isimli
bir sınıf türünden dolaşılabilir bir nesne vermektedir. bu dolaşılabilir nesne
dolaşıldığında `start` değerinden başlayarak `stop` değerine kadar , `start`
dahil ama `stop` değil `step` miktarı arttırımlarla `int` değerler elde edilir.
Tek, iki ya da üç argümanlı kullanabiliriz.

```text
range(stop)
range(start, stop)
range(start, stop, step)
```

Tek argümanlı kullanım sırasında `0` dan başlanır.

```text
>>> print(list(range(10)))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Diğer kullanımlar:

```text
>>> print(list(range(10, 20)))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> print(list(range(10, 20, 3)))
[10, 13, 16, 19]
```

---

`range()` fonksiyonunu 3 parametresi de `int` türden olmalıdır, o da bize
dolaştığımız zaman `int` türden değerler verir, `float` desteği yoktur.
Olsaydı floating point yuvarlamalardan kaynaklı hatalar olabilirdi.
Fakat örneğin *NumPy* kütüphanesinin `arange()` isimli bir sınıfı vardır,
bu arkadaş float değerler alabilir.

---

`range()` e negatif `step` değeri verirsek bu sefer büyükten küçüğe değerler
elde edilir.

```text
>>> print(list(range(20, 10, -3)))
[20, 17, 14, 11]
```

gibi...

## Sequence Container

`range` sınıfı Python Standart Kütüphanesinde **sequence container** olarak ele
alınmaktadır. Bu terim, Python'da elemanları arasında öncelik ve sonralık
ilişkisi olan ve elemanlarına `[]` operatörü ile erişilen veri yapılarını
betimler. **`list` ve `tuple` sınıfları da birer sequence container'dır.**

`range` sınıfı da bir *sequence container* belirttiği için listeler ve demetler
üzerinde yapılabilen bazı işlemler `range` nesneleri üzerinde de yapılabilir,
örneğin dilimleme gibi. Bu durumda yine `range` nesnesi elde edilir.

```text
>>> x = range(10)[3:8:2]
>>> x
range(3, 8, 2)
>>> print(list(x))
[3, 5, 7]
```

`range` nesnelerinin dilimlenmesi pek sık kullanılan bir şey değildir.

---

`range` nesnelerinin belli bir elemanına `[]` operatörü ile erişilebilir ama bu
nesneler değiştirilememektedir. Teknik olarak `range` değiştirilemez yani
immutable bir sınıftır. Yine de `index()` ve `count()` metotları kullanabiliriz.

```text
>>> r = range(100)
>>> r[23]
23
>>> r[23] = 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'range' object does not support item assignment
```

---

`in` ve `not in` operatörleri `range` nesnelerinde de kullanılabilir.

```text
>>> r = range(30, 60, 3)
>>> 39 in r
True
>>> 40 in r
False
>>> 41 not in r
True
```

---

`start`, `stop` ve `step` örnek öznitelikleri **instance attributes** ile elde
edilebilir.

```text
>>> r = range(30, 60, 3)
>>> r.start
30
```

`7184`
