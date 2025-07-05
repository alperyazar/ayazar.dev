---
giscus: e2e7113d-9678-4434-a2c7-fdf35ebf0472
---

# `frozenset`

`8002`

Python'da seyrek kullanılan bir sınıf daha vardır: `frozenset`. Bu sınıf, `set`
sınıfının değiştirilemez yani *immutable* biimidir. Nasıl `tuple` sınıfı `list`
sınıfının değiştirilemez biçimi gibiyse `frozenset` sınıfı da `set` sınıfının
değiştirilemez biçimi olarak düşünebilir.

`set` ile `frozenset` arasındaki farklar şu şekildedir:

`8006`

- `frozenset` değiştirilebilir olmadığı için onun `add()`, `update()`,
  `intersection_update()`, `remove()` gibi metotları yoktur. Ama değiştirme
  yapmayan metotları aynıdır.
- `frozenset` sıfında `&=`, `|=`, `^=`, `-=` gibi operatörler soldaki nesne
  üzerinde işlem yapmazlar. Yeni nesne yaratırlar. Hal böyle olunca `a |= b` ile
  `a = a | b` işlemi eşdeğer
  olur.
- `frozenset` elemanları eğer hash'lenebilir ise **`frozenset` nesnesi de
  hashlenebilir durumdadır.** Normalde `set` elemanlarından bağımsız olarak
  hashlenemeyen bir veri türüydü.

## Yaratılması

Biz `frozenset` türden bir nesneyi küme parantezleri ile yaratamayız, sadece
`frozenset()` fonksiyonu ile yaratabiliriz. Bu fonksiyon diğerlerinde olduğu
gibi herhangi bir dolaşılabilir nesneyi parameter olarak alabilmektedir.

```text
>>> fs = frozenset(['alper', 12, 3.14, True])
>>> fs
frozenset({'alper', 3.14, 12, True})
```

## `set` ve `frozenset` İçeren İşlemler

Bu iki türden nesneler `|`, `&`, `-`, `^` işlemlere sokulabilmektedir. İşlemin
sonucu, sol operandın türüne bağlıdır, set ise set ya da frozenset ise
frozenset. Eğer operatör olarak değil de metot çağrımı ile bu işlemleri yaparsak
bu sefer sonucun türü her zaman metotun çağrıldığı nesnenin türü olmaktadır.

## Küme Elemanları ve `frozenset`

Kümenin bir elemanı bir set yani küme olamaz çünkü kümeler hash'lenebilir
değildir, **küme elemanlarının hash'lenebilir olmaları gerekir.** Fakat küme
elemanları birer `frozenset` olabilir. Çünkü `frozenset` hashlenebilir
biçimdedir.

```text
>>> s = {1, 2, {3, 4}, 5}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> s = {1, 2, frozenset({3, 4}), 5}
>>> s
{frozenset({3, 4}), 1, 2, 5}
```

`8108`
