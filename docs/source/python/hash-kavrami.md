---
giscus: b98c7953-13d6-4d71-a6db-811cb36f6c7e
---

# Hash Kavramı, hashable ve unhashable Türler

`6440`

Hash'i biliyorsun, kriptolojide falan olan. Hash değerleri bazı veri yapıları
içerisinde anahtar yani **key** value olarak kullanabiliyoruz.

Python'da bazı türler **hashable** yani *hashlenebilir* ya da **unhashable**
yani *hashlenemez* biçimdedir. Genel olarak değiştirilebilir türler
unhashable kategoridedir. Demet yani tuple değiştirilemez bir tür olduğu için
hashlenebilir bir türdür. Fakat her demet nesnesi de böyle değildir.
**Bir demet nesnesinin hashlenebilir olması için tüm elemanlarının böyle olması
gerekir.**

Gördümüz temel türler, `int`, `float`, `complex`, `bool`, `str`, `None`
hashlenebilir türlerdir. **Listeler hiçbir durumda hashlenebilir değildir.**
Eğer demet içerisinde liste varsa artık o demet de hashlenebilir olmaz.

## Hash değerinin elde edilmesi

Built-in fonksiyon olan `hash()` fonksiyonu ile hash değeri elde edilebilir.
Örneğin:

```text
>>> hash('alper')
-133024290317852522

>>> hash(3)
3

>>> x = 'alper'
>>> hash(x)

-133024290317852522

>>> hash((1, 2, 3))
529344067295497451

>>> hash((1, [2], 3))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

Fakat örneğin sonda tuple içinde list olduğu için tuple hashlenebilir olmadı.

## Hash değeri?

Bir nesnenin hash değerinin nasıl hesaplanacağı implementasyona bağlıdır
aslında. Ama CPython için şunları söyleyebiliriz.

- `int` nesnenin hash değeri ilgili değerdir.

Diğer nesneler ile ilgili detaylar Kaan Hoca'nın özet notlarda var ama buraya
yazmıyorum.

`6491`

FIN
