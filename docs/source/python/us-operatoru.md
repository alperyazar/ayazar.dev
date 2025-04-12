---
giscus: eb7931f5-0ad2-47f2-9475-5412e9712ac9
---

# 💥 Üs Operatörü, `**`

`11-51.00`

Diğer programlama dillerinin aksine Python'da üs alma operatörü vardır. C'deki
`pow()` fonksiyonu işlevindedir. Burada `**` operatörü vardır. `a ** b` şeklinde
kullanılmaktadır, `*` karakterleri arasında boşluk olmaz. İki operandlı araek
bir operatördür.

```python
a ** 2   # a'nın karesini alma
a ** 0.5 # a'nın karekökünü alma
```

Matematikte `-3^2` yazdığımız zaman `-9` olmaktadır, `9` değil. Python'da
matematiksel yazıma benzetilmektedir ve Python'da da `-3**2` nin cevabı `-9`
olmaktadır. Yani önce üs alma işlemi yapılır sonra işaret eksi operatörü
uygulanır.

```text
>>> -3**2
-9
```

> Bknz: [](operator-oncelikleri.md)

C'de üs alma operatörü yok ama C'nin tercihi işaret eksi operatörünü daha yüksek
öncelikli tutmak olurdu, dilin tarzı bu şekilde yani.

---

Bu operatör ayrıca sağdan-sola önceliğe sahiptir. Yani ifadede en sağdaki
operatör önce işleme alınır. Örneğin `2 ** 3 ** 2` yazdığımız zaman öncelik
aslında bundan dolayı `2 ** (3 ** 2)` ile eşdeğer olmaktadır. `2 ** 9` dan sonuç
`512` çıkar. Soldan sağa yapmak istiyorsak öncelik parantezi kullanmalıyız.

```text
>>> 2 ** 3 ** 2
512
>>> (2 ** 3) ** 2
64
```
