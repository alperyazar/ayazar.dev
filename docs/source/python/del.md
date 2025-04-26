---
giscus: 6b1a6150-31e3-425f-863e-197eef52e109
---

# `del` Deyimi

`15-2.11.45`

`del` bir anahtar sözcüktür ve `del` ile veri yapılarından eleman silmek için
bir deyim, statement, oluştururuz. `del` deyimi sadece `list` veri yapılarında
değil değiştirilebilir yani mutable olan başka nesnelerde de kullanılabilir.

`del` deyimi ile bir listeden eleman silerken elemana indeksle erişiyormuş
gibi `[]` operatörü ile eşleriz. Örneğin:

```text
>>> x = [1, 2, 3, 4, 5]
>>> del x[2]

>>> x
[1, 2, 4, 5]
```

Burada `del` deyimini kullanmak yerine `list` sınıfının `pop()` metodunu da
kullanabilirdik argüman vererek. Olmayan bir elemanı silmek istersek
`IndexError` exception oluşur.

```text
>>> del x[200]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
```

`del` deyimi ile beraber yine negatif indeks semantiğini kullanabiliriz sanki
bir elemana erişiyormuş gibi.

---

`del` deyimi ile beraber dilimleme yani slicing semantiği ile silinecek birden
fazla eleman seçebiliriz. Bu durumda önce silinecek elemanlar seçilir ve
tek seferde silinir. Burada biraz *atomik* bir davranışa vurgu yapıyorum,
nedenini birazdan anlayacağız.

```text
>>> x = [1, 2, 3, 4, 5, 6, 7]

>>> del x[1:6:2]

>>> x
[1, 3, 5, 7]
```

## `del` ve `,`

`del` deyimi ile `,` atomu ile ayrılmış birden fazla silme işlemi yapabiliriz.
Bu durumda silem işlemleri **soldan sağa ve ayrı ayrı** yapılmaktadır.

```text
>>> x = [1, 2, 3, 4, 5, 6, 7]

>>> del x[2], x[3] # işlemler ayrı ayrı yapılıyor!

>>> x
[1, 2, 4, 6, 7]
```

Burada önce `del x[2]` ve daha sonra `del x[3]` yapılmaktadır. Ama ikinci
`del` işlemi yeni `x` listesi üzerinde yapıldığı için, 3 nolu indeks en başta
değeri 4 olan elemana denk geliyorken ilk silme işleminden sonra değeri 5
olan elemana denk gelmeketdir. Yukarıdaki dilimleme ile silme işlemi örneği
aksine burada bir *atomik* davranıştan söz edemiyoruz.

`15-2.25.20`
