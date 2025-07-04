---
giscus: 890931c3-f810-47f1-926e-b2429582c9a7
---

# unpacking - açım kavramı

`6718`

dolaşılabilir bir nesnenin elemanlarını **unpacking** yani **açım** yöntemi
ile değişkenlere atayabiliriz. ruby ve python gibi dillerde bunlar uzun zamandır
vardır. c#, swift, c++ gibi dillere sonradan eklenmiştir.

eskiden açım işlemi yalnızca demetler üzerinde yapılabiliyordu ama daha sonra
tüm dolaşılabilir nesneler açılabilir hale getirilmiştir. yani açım sentaksı
genelleştirilmiş oldu.

**aşağıdaki 3 sentaks tamamen aynıdır**

- `(x, y, z, ...) = <dolaşılabilir nesne>`
- `x, y, z, ...   = <dolaşılabilir nesne>` yazması kolay olduğu için tercih
- `[x, y, z, ...] = <dolaşılabilir nesne>`

bu işlem sırasında sağdaki nesne dolaşılır ve elde edilen değerler sol taraftaki
değişkenlere sırası ile atanır.

```python
t = 10, 20, 30
x, y, z = t
```

ile aşağısı tamamen eşdeğerdir

```python
x = t[0]
y = t[1]
z = t[2]
```

mesela `[x, y, z] = 'ali'` ise her değişkene karakterler atanmış olur.

---

eğer dolaşılabilir nesnedeki eleman sayısı ile sol taraftaki değişken sayısı
tutmaz ise `ValueError` exception oluşur.

```text
>>> x, y = [10, 20, 30]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

---

açılan dolaşılabilir nesnenin elemanları karışık olabilir, kendileri de
dolaşılabilir nesne olabilir.

```text
>>> a, b, c = [10, [2, 3], 40]
>>> a
10
>>> b
[2, 3]
>>> c
40

>>> a, b, c = True, 'alper', 2.5
>>> a
True
>>> b
'alper'
>>> c
2.5
```

## recursive yani özyinelemeli açma işlemi

açılan bir eleman da dolaşılabilir nesne ise onu da açabiliriz.

```text
>>> a, [b, c], d = 10, (20, 30), 40
>>> a
10
>>> b
20
>>> c
30
>>> d
40
```

yine sol tarafta `()` ya da `[]` kullanabiliriz, fark etmez.

tabii bunu sonuna kadar devam ettirmemiz gerekmez.

```text
>>> a, b, c = 10, (20, 30), 40
>>> b
(20, 30)
```

---

**tüm atama işlemlerinin adres ataması olduğunu hatırlayalım.**

---

## swap işlemi

**pythonic way** olarak swap işlemi python'da `a, b = b, a` şeklinde yapılabilir.
sağdaki ifade aslında bir tuple yani demet bildirir. daha sonra sol taraftaki
değişkenlere atama yapılır.

burada işlemler `a = b` ve ardından `b = a` şeklinde yapılmaktadır. eğer böyle
yapılıyor olsaydı iki değişkende de `b` nin orijinal değeri olurdu. burada
aslında geçici bir demet oluşturulur. ilk başta `b` neyi gösteriyorsa `[0]` onu,
`a` neyi gösteriyorsa da `[1]` onu göstermektedir. Daha sonra `a`, `[0]` neyi
gösteriyorsa onu, `b` ise `[1]` neyi gösteriyorsa onu gösterir. yani günün
sonunda swap etmiş oluyoruz.

`6925`
