---
giscus: e02ba565-acef-49db-a474-68fa38ab2482
---

# List Comprehension - Liste İçlemi

`16-2.16.45`

Son olarak bir örnek daha yapalım. Elemanları `0` olan `10x10`luk bir matrisi
pratik yolla gerçekleştirmeye çalışalım.

İlk şu aklımıza gelebilir:

```python
x = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * 10
```

Ama burada şu problem vardır, aslında aynı liste 10 kere tekrarlanmıştır.
Biz `x[0][0] = 1` ile ilk elemanı değiştiridiğimizde birçok yerde değişiklik
olur.

## Döngü Kullanmak

Henüz döngülere değinmedik ama konu bütünlüğü olması açısından burada listeler
konusunda biraz bakacağız. Buradaki bir yöntem, `for` döngüsü ile listeye
yeni listenin `append()` edilmesidir.

```python
x = []
for _ in range(10):
  x.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
```

Şimdi `x[0][0] = 1` dersek sadece bir eleman değişecektir.

## List Comprehension

List comprehension ya da liste içlemi bu amaçlar için kullanabileceğimiz özel
bir sentakstır.

Aynı işlemi

```python
x = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(10)]
```

şeklinde yapabiliriz. Yine `x[0][0] = 1` dersek sadece bir eleman değişecektir.

---

Bknz:
<https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions>

`16-2.16.45`
