---
giscus: 2b572ede-cd91-4d87-b19e-a8d6b394aaa6
---

# Demet, tuple Veri Yapısı - 1

`16-2.16.45`

Tuple yani demet, listeye benzeyen önemli bir veri yapısıdır. Bir demet,
parantez yani `()` kullanılarak yaratılır.

```text
>>> x = (1, 2, 3)

>>> type(x)
<class 'tuple'>
```

Demet de liste gibi bir *built-in* veri türüdür.

---

Biz bir demeti `tuple` sınıfının *tür fonksiyonu* olan `tuple()` fonksiyonu ile
de yaratabiliriz. Bir argüman girmezsek boş bir demet yaratılır. Eğer
dolaşılabilir bir nesne argüman olarak girilirse elemanlar dolaşılarak onun
elemanlarından bir demet oluşturulur.

```text
>>> x = tuple()

>>> x
()

>>> x = tuple('alper')

>>> x
('a', 'l', 'p', 'e', 'r')
```

---

`17-0.07.10`

**Demetler de dolaşılabilir nesnelerdir.** Bir demet dolaşılınca sıra ile onun
içerisindeki elemanlar elde edilir.

```text
>>> x = tuple('alper')
>>> y = list(x)

>>> x
('a', 'l', 'p', 'e', 'r')

>>> y
['a', 'l', 'p', 'e', 'r']
```

## Demetler ve Listeler

`tuple` ile `list` bir çok açıdan birbirine benzer:

- Her ikisinin elemanlarına `[]` operatörü ile erişilir.
- Demetlerde de negatif indeksler listelerdeki gibi anlam taşır.
- Demetlerde de dilimleme yani slicing yapılabilir tabii bu durumda bir demet
  elde edilir.
- `len()` built-in fonksiyonu ile eleman sayısı alınabilir.
- Demetler de dolaşılabilir yani iterable nesnelerdir.

Örneğin:

```text
>>> x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

>>> x[3]
4

>>> x[-1]
10

>>> x[2:6:2]
(3, 5)

>>> x[::-1]
(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

>>> len(x)
10
```

`17-0.14.40`

---

Demetleri oluştururken `()` kullandığımız zaman öncelik parantezi ile karıştırma
yapılabilir.

```text
>>> t = ()
>>> type(t)
<class 'tuple'>

>>> t = (10)
>>> type(t)
<class 'int'>

>>> t = (10,)
>>> type(t)
<class 'tuple'>
```

Burada `(10)` yazınca aslında öncelik parantezi oluyor ve `int` oluyor. Ama `,`
koyarsak tek elemanlı tuple yaratmış olduk. Yani `10` ile `(10)` arasında bir
fark yoktur, yani biz tüm ifadeleri öncelik parantezi içerisine alabiliriz.
Boş parantez, `()`, ise öncelik parantezi olarak ele alınmaz.

## Demet İçersinde Heterojen Türler

Demet içerisine de listelerde olduğu gibi karışık türler bulunabilir.
Ayrıca liste içerisinde demet, demet içerisinde liste de olabilir.

```text
>>> t = (10, 'alper', True, 20.55)
>>> type(t)
<class 'tuple'>

>>> x = [10, ('alper', 20), None]
>>> type(x)
<class 'list'>

>>> y = (10, ['alper', 20], None)
>>> type(y)
<class 'tuple'>
```

---

`6372`

Demet içerisinde de elemanların kendisi değil adresleri tutulur.

---

**Demetler ile listeler arasındaki tek fark listelerin değiştirilebilir, mutable
demetlerin ise immutable yani değiştirilemez olmasıdır.** Bir demet
yaratıldıktan sonra içeriği değiştirilemez.

```text
>>> t = (10, 20)

>>> t[0] = 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Yukarıda değiştiremedik çünkü demetler immutable nesnelerdir.

## `tuple` Sınıfının Metotları

Liste sınıfına benzer ama değişiklik yapan metotlar demetlerde bulunmaz.

Aşağıdaki metotlar demetlerde **bulunmaz.**

- `append()`
- `extend()`
- `pop()` ve `remove()`
- `clear()`
- `insert()`
- `sort()`
- `reverse()`
- Dilimleme yolu ile atama.

Fakat değişiklik yapmayan `index()` ve `count()` metotları bulunmaktadır.

```text
>>> t = (10, 20, 'alper')
>>> t.index(20)
1
>>> t.count(10)
1
```

FIN
