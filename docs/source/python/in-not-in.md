---
giscus: 4b72e799-82aa-4e4f-8969-41d100a09f7e
---

# `in` ve `not in` Operatörleri

`15-1.55.35`

Şimdi iki adet operatöre bakacağız: `in` ve `not in`. Bunlar birer operatördür,
deyim değildir.

## `in` Operatörü

Bu operatör, binary infix bir operatördür, yani sağında ve solunda bir operand
vardır.

Bu operatör birçok veri yapısı ile uygulanabilir, listelere özgü değildir.
Amacı bir veri yapısı içerisinde belli bir değerin olup olmadığına bakmaktır.
Sol tarafındaki operand aranacak değeri belirtirken sağ tarafındaki operand
ise arama yapılacak nesneyi belirtir. Eğer veri yapısında aranan değer varsa
`True` yoksa `False` dönmektedir. Yani `bool` türünden değer üretir.

Örneğin:

```text
>>> x = [1, 3.14, 'alper', 10]

>>> 3.14 in x
True

>>> 4 in x
False
```

`str` nesnelerde ise bu operatör yazının ardışıl kısımlarını aramak için de
kullanılabilir.

```text
>>> x = 'Ankara Ankara güzel Ankara'

>>> 'güzel' in x
True

>>> 'güzel a' in x # a değil A olmalıydı True olması için
False
```

**`in` operatörü `==` karşılaştırması yapmaktadır.**

### `list` ve `in`

İki listenin karşılaştırması konusuna sonra bakacağız. Ama `in` operatörünü
*bir liste içerisinde başka bir liste var mı?* diye araştırmak için de
kullanabiliriz.

Örneğin:

```text
>>> x = [1, 2, [3, 4, 5], 6]

>>> 1 in x
True

>>> 3 in x
False

>>> [3, 4]  in x
False

>>> [3, 4, 5]  in x
True
```

## `not in` Operatörü

`in` nasıl *var mı?* diyorsa bu operatör de *yok mu?* diye sormaktadır.

```text
>>> 3 not in [1, 2]
True
```

`not in` tek başına bir operatördür.

## `not` ve `not in`

`in` operatörü bir `bool` türden değer ürettiğine göre biz `not in` yerine `not`
operatörü de kullanabiliriz. `not`, mantıksal bir operatördür. `not in` ise
karşılaştırma operatörüdür.

`not x in y` ile `x not in y` aynı anlamdadır çünkü `in` ve `not in`
operatörlerinin önceliği `not` operatöründen yüksektir. `x not in y`
kullanımının okunabilirlik açısından daha iyi olduğunu söyleyebiliriz.

`15-2.11.45`
