---
giscus: 2b572ede-cd91-4d87-b19e-a8d6b394aaa6
---

# Demet, tuple Veri Yapısı - 1 (YARIM)

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
