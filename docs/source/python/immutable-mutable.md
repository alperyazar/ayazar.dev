---
giscus: a587548b-198a-4c36-b006-136f7e48ba9c
---

# Immutable (Değiştirilemez) ve Mutable (Değiştirilebilir) Nesneler

Python'da türler **immutable** yani *değiştirilemez* ve **mutable** yani
*değiştirilebilir* olmak üzere ikiye ayrılmaktadır. Eğer bir nesneyi
yarattığımız zaman verdiğimiz ilk değeri daha sonradan başka bir değerle
değiştirebiliyorsak o nesne **mutable**, değiştiremiyorsak **immutable**
olmaktadır.

````{tip}
Bunu C'deki `const` gibi hayal edebiliriz.

```c
int x = 5; //Mutable
x = 6; //OK

const int y = 5; //Immutable
y = 6: //OK değil, Hata
```
````

Şimdiye kadar 6 adet temel tür gördük. Bunlar: `int`, `float`, `complex`, `str`,
`bool` ve `NoneType` idi. **Gördüğümüz 6 türün hepsi immutable türlerdir.** Yani
bu türlerden olan nesnelerin değerleri daha sonra değiştirilemez. Ömürlerinin
sonuna kadar aynı değeri tutarlar.

---

Bu durumun ilginç yansılamaları olabilir. Mesela:

```text
>>> x = 10
>>> id(x)
10869672

>>> x = 20
>>> id(x)
10869992
```

Başka değeri `10` olan `int` nesnesinin değeri `20` olarak güncellenmedi. Çünkü
bu immutable bir nesnedir. `20` değerinde ayrı bir `int` nesnesi yaratıldı.

Ya da:

```text
>>> i = 1
>>> id(i)
10869384

>>> i = i + 1
>>> id(i)
10869416

>>> i = i + 1
>>> id(i)
10869448
```

Burada `i` nin değerini birer birer arttırsak bile her seferinde farklı bir
nesne oluşmaktadır.

Eğer ileride değineceğimiz döngülerle işlem yaparsak işler biraz garip
gözükebilir

```python
i = 0
for i in range(10):
  print(i, id(i))  # hep farklı id basıyor.
  i = i + 1
```

Çıktı:

```text
0 94763267269512
1 94763267269544
2 94763267269576
3 94763267269608
4 94763267269640
5 94763267269672
6 94763267269704
7 94763267269736
8 94763267269768
9 94763267269800
```

Bir loop içerisinde arttırsak bile her seferinde yeni bir `int` nesnesi
oluşmaktadır. Elbette böyle basit kodlarda bile bu davranış bir performans
kaybına sebep olacaktır.

Yukarıdaki kodu C, C++, Java, C# gibi dillerde yapsaydık doğrudan değişkenin
içeriğini değiştiriyor olacaktık. Günün sonunda Python tarafında beklediğimiz
davranış gözükse de, yani kod beklediğimiz gibi çalışsa da, arka planda işler
farklı yürüyor. Örneğin Ruby de dinamik bir tür sistemine sahip dil olsa da
immutable olayları onda Python'dakinden farklıdır. Yani bu davranış tüm dinamik
tür sistemine sahip dillerde böyledir diyemeyiz.

---

Son olarak şu duruma bir bakalım:

```python
a = 10
b = a    # a nın gösterdiği 10 nesnesini gösteriyor
a = 20   # a nın gösterdiği 10 değişmediği için yeni 20 yaratılıyor
         # o yüzden b, 10'u göstermeye devam ediyor. a nın gösterdiği nesne
         # güncellenseydi b nin değeri de 20 olabilirdi.
```

Yukarıda bir noktada `b` ve `a` aynı `int` nesnesini gösteriyor, değeri `10`
olan. Eğer o nesne `a = 20` ile güncellenseydi `b` nin değeri de örtülü bir
şekilde `20` olarak değişecekti. Ama bu olmadığı için `b`, `10` değerini
korumaya devam ediyor. Arka planda ne olursa olsun buradaki semantik C, C++,
Java ve C# gibi dillerle sonuç itibariyle aynıdır.
