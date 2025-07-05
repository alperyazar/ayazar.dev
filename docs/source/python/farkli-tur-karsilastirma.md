---
giscus: 53b6b217-20f8-4509-b362-9d9d0b83d718
---

# Farklı Türlerin Karşılaştırılması

`10404`

Python'da farklı türleri her zaman `==` ve `!=` operatörleri ile
karşılaştırılabilir. Karşılaştırılan türler `int`, `float` ve `bool` değilse
farklı türleri karşılaştırma, içerikleri ne olursa olsun, `==` ile yapıldığında
`False`, `!=` ile yapıldığında `True` değerini verir.

Örnek:

```text
>>> a = [1, 2, 3]
>>> b = (1, 2, 3)

>>> a == b
False
>>> a != b
True
>>> a == 3.14
False
```

**Yani elma, 🍏, ile armudu, 🍐, karşılaştırdığımızda `False` cevabını alırız.**

---

Önceden de belirttiğimiz gibi `int`, `float` ve `bool` türleri kendi aralarında
*tüm* karşılaştırma operatörleri ile karşılaştırılabilirler. Bu durumda değerler
karşılaştırılmaktadır.

```text
>>> 10 == 10.0
True

>>> 1.0 == True
True

>>> 3.14 > 3
True
```

---

`int`, `float` ve `bool` dışındaki türlerin, farklı türlerle `>`, `<`, `>=`,
`<=` operatörleri ile karşılaştırılması geçersiz bir durumdur ve exception'a yol
açar.

```text
>>> [1, 2] > (1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'list' and 'tuple'
```

## Demet ve Listelerin Karşılaştırılması

İki demeti ve iki listeyi kendi arasında karşılaştırabiliriz. Bu durumda
string'lerde olduğu gibi *leksikografik* karşılaştırma yapılır. Karşılaştırma,
eşit olmayan elemana kadar devam eder.

```text
>>> [1, 2, 3, 4, 5] > [1, 2, 3, 5, 1]
False

>>> [1, 2] < [1, 2, 3]
True
```

Demetler ve listelerin elemanları değişik türlerden olabilmektedir. Eğer
karşılıklı elemanlar karşılaştırılabilir türden değilse `TypeError` exception
oluşur.

```text
>>> [10, 'ali', 20] > [10, 20 ,30]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'str' and 'int'
```

Ama karşılaştırma erken biterse, örneğin ilk elemanda, bir exception oluşmaz:

```text
>>> [10, 'ali', 20] > [11, 20 ,30]
False
```

---

Eğer listenin elemanları başka bir liste ya da demet, ya da demetin elemanları
liste veya demet ise karşılaştırma özyinelemeli biçimde yapılır.

```text
>>> [1, [2, 3, 4], 5] > [1, [2, 3, 5], 2]
False
```

## Sözlüklerin Karşılaştırılması

İki sözlük nesnesi kendi aralarında sadece `==` ve `!=` operatörleri ile
karşılaştırılabilir. Bu durumda iki sözlüğün anahtar-değer çiftlerinin birebir
aynı olup olunmadığına bakılır, sadece anahtar değil.

```text
>>> {'ali': 10, 'veli': 20, 's': 30} == {'ali': 10, 'veli': 20, 's': 50}
False
```

---

**Dikkat!** Python 3.7 ve sonrasında sözlük elemanlarında dolaşım sırasında bir
sıra söz konusu olsa da `==` ve `!=` operatörleri bu biçimde leksikografik bir
karşılaştırma yapmazlar. Yani eşitlik için karşılıklı anahtar-değer çiftlerinin
eşitliğine değil tüm anahtar-değer çiftlerinin eşitliğine bakılmaktadır.

```text
>>> {'ali': 30, 'veli': 30, 's': 40} == {'ali': 30, 's': 40, 'veli': 30}
True
```

Örneğin yukarıda bizim gördüğümüz sıralar farklı olsa da iki sözlük eşittir.

## Kümelerin Karşılaştırılması

İki küme `==` veya `!=` ile karşılaştırılabilir. Tüm elemanlar tamamen aynı ise
karşılaştırma başarılı olur.

```text
>>> {'ali', 100, 'veli', 120} == {100, 120, 'veli', 'ali'}
True
```

---

Kümelerde `>`, `>=`, `<` ve `<=` operatörleri küme işlemi yapmaktadır. Yani
öz alt küme, öz üst küme, alt küme ve üst küme işlemleri gibi.

```text
>>> {10, 'ali', 'veli'} > {10, 'veli'}
True

>>> set() < {'alper'}
True
```

`set()`, boş bir küme oluşturur.

`10612`
