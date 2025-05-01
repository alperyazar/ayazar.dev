---
giscus: 05661206-29e4-4a21-ba3d-f58556316edd
---

# Listelerin Toplanması

`15-2.25.20`

İlginç gelebilir, Python'da iki listeyi `+` operatörü ile toplanabilir. Fakat
çıkartılamaz, çarpılamaz ya da bölünemez.

İki listeyi topladığımız zaman yeni bir liste elde ederiz. Bu yeni listenin
elemanları `+` operatörünün sol operandındaki liste elemanlarına sağındaki liste
elemanlarının uc uca eklenmesi ile oluşur yani bir *concat* işlemi vardır. Yeni
listenin `len()` uzunluğu bu durumda `len(sol) + len(sağ)` olmaktadır.

Örneğin:

```text
>>> x = [1, 2, 3]
>>> y = [10, 20, 30]

>>> x + y
[1, 2, 3, 10, 20, 30]
```

Burada bir çeşit *sığ kopyalama* yani *shallow copy* işlemi yapılır. Yeni
listedeki elemanlar aslında orijinal listedekiler ile aynı nesneleri gösterir.
Yani:

```text
>>> x = [1, 2, 3]
>>> y = [10, 20, 30]

>>> z = x + y

>>> z[0] is x[0]
True

>>> z[3] is y[0]
True
```

---

Bir örnek daha:

```text
>>> a = [1, 2, 3]
>>> b = [[10, 20, 30]]

>>> a + b # Liste olarak eklendi, dikkat!
[1, 2, 3, [10, 20, 30]]
```

---

İki liste toplanabildiği gibi üç ya da daha fazla da toplama yapılabilir. `+`
işlemi soldan sağa öncelikliği olduğu için `a + b + c` dersek önce `a + b`
yapılır sonra bu liste ile `c` toplanır.

`16-0.14.15`

```{figure} assets/list-toplama-bellek.png
:align: center

İki liste toplandığında oluşan yeni liste aslında toplanan listelerin gösterdiği
nesneleri gösterir, *shallow copy* mantığına benzer buradaki yaklaşım vardır.
```

Bu durumda listeler değiştirilemez bir nesne türü olan `int` nesnesini göstermektedir.
Biz bir listeyi güncellediğimizde, örneğin `x[0] = 5` diyerek, değeri `5`
olan yeni bir `int` nesnesi oluşur ve `x[0]` artık bu nesneyi gösterir ama
`z[0]` hala eski nesneyi göstermektedir.

```text
>>> x = [1, 2]
>>> y = [10, 20]

>>> z = x + y

>>> x[0] is z[0]
True

>>> x[0] = 5

>>> x
[5, 2]

>>> z
[1, 2, 10, 20]

>>> x[0] is z[0]
False
```

Aşağıdaki gibi düşünebiliriz:

```{figure} assets/list-toplama-bellek-immutable.png
:align: center

Tüm `int` nesneleri hala "kullanıldığı" için garbage collector gibi bir
mekanizma ile "çöpe atılmazlar."
```

Fakat iç içe listeler gibi mutable nesnelerin yer almaya başladığı durumlarda
işler değişmeye başlayacaktır. Aşağıdaki kodu ele alalım:

```text
>>> x = [1, 2, [3, 4]]
>>> y = [5, 6]
>>> z = x + y

>>> x[2][0] is z [2][0]
True
```

Gösterimine bakalım:

```{figure} assets/list-toplama-bellek-icice.png
:align: center

Durum C'deki *double pointer dereference* durumlarına benzemeye başladı 🤔
```

Şimdi içerideki listede güncelleme yapalım ve duruma bakalım.

```text
>>> z[2][0] = 10

>>> x[2][0] is z [2][0]
True

>>> x
[1, 2, [10, 4]]
```

Bu durumda biz `z` yi güncelledik ama `x` de değişti. Bellekteki görünüm
aşağıdaki gibi olmaktadır.

```{figure} assets/list-toplama-bellek-icice-update.png
:align: center

Artık bir referansı kalmayan 3 değerli `int` nesnesi bir noktada otomatik olarak
*çöpe* atılacaktır.
```

`16-0.30.00`

```{note}
**Ek bilgi**

Eğer **deep copy** yapmak istiyorsak `copy` modülü içerisindeki
`copy.deepcopy()` fonksiyonunu kullanabiliriz.
```

## Boş Listelerin Toplanması

Toplama sırasında iki listenin biri ya da her ikisi de boş liste olsa bile
toplama işlemi sonucunda yeni bir liste yaratılmaktadır. Programlama dünyasında
**observable side effect** yani **gözlemlenebilir yan etki** kavramı vardır.
Böyle bir durumda Python implementasyonu bir optimizasyon yapabilir.

Aşağıdaki durum geçerlidir:

```python
x = [1, 2, 3] + []
```

Bir listeyi doğrudan toplayarak oluşturursak bu optimizasyon kapsamında
Python implementasyonu doğrudan birleştirilmiş listeyi tek seferde yapabilir,
yani iki listeyi ayrı ayrı oluşturup toplamayabilir.

```python
x = [1, 2, 3] + [4, 5] # doğrudan [1, 2, 3, 4, 5] yaratılabilir
```

## `+=` ≠ `= +` ❗

Python'da ve birçok programlama dilinde `a += b` işleminin `a = a + b` ile
eşdeğer olduğunu söylüyoruz. Fakat Python'da **bu denklik listeler için geçerli
DEĞİLDİR.**

`16-1.10.45`

`a = a + b` dediğimizde aslında yeni bir liste oluşuyor ve `a` artık yeni
bir listeyi göstermeye başlıyor. Örneğin:

```text
>>> a = [1, 2, 3]
>>> b = [4, 5]

>>> id(a)
133419689172608

>>> a = a + b

>>> a
[1, 2, 3, 4, 5]

>>> id(a)   # ilk id(a) ile aynı değil
133419689173952
```

`a += b` nin anlamı ise listelerde farklıdır. *`b` listesinin elemanlarının
mevcut `a` listesinin sonuna eklenmesi* anlamı çıkmaktadır. Yani aslında
`a.extend(b)` gibi bir etki yaratmaktadır. Örneğin:

```text
>>> a = [1, 2, 3]
>>> b = [4, 5]

>>> id(a)
133419689170176

>>> a += b

>>> a
[1, 2, 3, 4, 5]

>>> id(a)  # a'nın id değeri değişmedi
133419689170176
```

Yani konu listeler olunca `a = a + b` ile `a += b` aynı anlamda değildir.

## `a.extend(b)`

Python dokümanlarına göre [^1f] `a` bir `list` türden olmak üzere `a.extend(b)` ile
`a += b` tamamen aynı anlamdadır. `extend()` metodun parametresinin herhangi
bir dolaşılabilir nesne olabileceğini söylemiştik. Bu durum `a += b` için de
geçerlidir.

```text
>>> a = [1, 2]

>>> a
[1, 2]

>>> a += 'alper'

>>> a
[1, 2, 'a', 'l', 'p', 'e', 'r']

>>> a.extend('yazar')

>>> a
[1, 2, 'a', 'l', 'p', 'e', 'r', 'y', 'a', 'z', 'a', 'r']
```

`16-1.27.30`

[^1f]: <https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types>
