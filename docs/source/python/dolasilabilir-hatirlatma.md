---
giscus: df9b9c3c-6d8c-4fbc-9382-9a28ee0ad0ed
---

# Dolaşılabilir ve Dolaşım Nesneleri - Hatırlatma

Dolaşılabilir yani **iterable** nesneler her dolaşıldığında yeniden aynı
değerleri veriyordu, yani dolaş dolaş dur, bitmiyorlar. Dolaşım nesneleri ise
yani **iterator** nesneler bir kez dolaşınca biten, ikinci kez dolaşılınca değer
üretmeyen nesnelerdir.

Teknik olarak her dolaşım nesnesi, dolaşılabilir bir nesne gibi de
kullanılabilir. Bir başka deyişle, bir kez biten dolaşılabilir nesnelere dolaşım
nesneleri yani **iterator** denmektedir, bir alt kümesidir.

## `range()`

`range` nesnesi dolaşılabilir bir nesnedir, dolaşım nesnesi değildir. Yani
dön dön dur, sıkıntı olmaz.

```text
>>> r = range(10)
>>> x = list(r)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> y = list(r)
>>> y
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Fakat built-in `reversed()` fonksiyonunun verdiği nesne bir dolaşım nesnesidir,
iki kere dolaşamazsın.

```text
>>> x = [1, 2, 3, 4, 5]
>>> y = reversed(x)
>>> list(y)
[5, 4, 3, 2, 1]
>>> list(y)
[]
```

İkinciye dolaşamadın işte.

`7217`
