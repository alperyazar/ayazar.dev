---
giscus: 842cf18c-571d-43de-94fd-801b21e2de65
---

# `del` Deyimi - 2

`10300`

Bu konuya biraz [değinmiştik.](del.md)

`del` deyimi genel bir silme semantiği sağlar.

```text
del <değişken listesi>
del a[ifade], ...
```

gibi bir yapısı vardır. Bir değişkeni `del` deyimi ile silersek o sanki hiç
yaratılmamış gibi olur. Sonrasında o değişkeni kullanırsak `NameError` exception
oluşur.

```text
>>> a = 10
>>> del a
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```

`del` deyiminde `,` atomu ile tek hamlede birden fazla değişken silebiliriz,
`del a, b` gibi.

---

**Bir konuyu tekrar hatırlayalım:** Python'da değişken ile nesne yani object
kavramı farklı anlamlara gelmektedir. **Python'da adres tutan yani bir nesneyi
gösteren isimlere değişken denir.** Değişkenin gösterdiği yere nesne denir.
**`del` deyimi değişkenleri siler, nesneleri değil.** Nesnelerin silinmesi
yorumlayıcı tarafından yürütülen *çöp toplama, garbage collection* mekanizmaları
ile yapılır. Bir nesneyi gösteren bir değişken kalmazsa o nesne silinir.

---

`del` ile `[]` ile erişebildiğimiz veri yapıları elemanları da silinebilir.
`del a[3]` gibi. Elbette demet gibi değiştirilemez veri yapılarında silme
işlemi yapılamaz.

Yine önceki yazıda da belirttiğimiz gibi `del a[2], a[5]` dediğimiz zaman
işlemler soldan sağa yapılır. Önce `del[2]` yapılır, sonra **yeni listenin,
örneğin** `5` indeksli elemanı silinir. Yani orijinal listenin `6` indeksli
elemanı aslında silinir.

---

`del x[2:5]` gibi dilimleme, slicing ile de silme işlemi yapılabilir.

---

Sözlüklerden silme işlemi yapınca sadece `del x[anahtar]` dediğimizde anahtar
değil anahtar-değer çifti silinir.

`10404`
