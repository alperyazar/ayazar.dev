---
giscus: e36bf509-dee9-4030-8cd6-f7c0e6e1cb68
---

# Listeler, Optimizasyon ve İç İçe Listeler

`16-1.47.30`

Python'da köşeli parantez, `[]`, kullandığımızda ne zaman bir liste oluştursak
her zaman yeni bir liste yaratılmaktadır.

Örneğin:

```text
>>> x = [1, 2, 3]
>>> y = [1, 2, 3]
>>> z = [1, 2, 3]

>>> id(x)
133419689170176
>>> id(y)
133419689185280
>>> id(z)
133419689172672
```

Burada aynı içerikte listeler yaratsak bile listelerin kendileri farklıdır.
Listeler değiştirilebilir tür olduğu için Python implmenetasyonu burada bir
optimizasyon yapmaya çalışmamaktadır. Fakat değiştirilemez tür olan `int` gibi
türlerde durum genelde böyle değildir.

```text
>>> x = 5
>>> y = 5
>>> z = 5

>>> id(x)
133419699798384
>>> id(y)
133419699798384
>>> id(z)
133419699798384
```

---

Aşağıdaki örneğe bir bakalım. Burada `y` in her elemanı aynı `x`i gösterir
durumdadır.

```text
>>> x = [1,2]
>>> y = [x, x, x]

>>> id(y[0])
133419689172672
>>> id(y[1])
133419689172672
>>> id(y[2])
133419689172672

>>> y
[[1, 2], [1, 2], [1, 2]]

>>> x[0] = 100

>>> y
[[100, 2], [100, 2], [100, 2]]
```

Fakat aşağıdaki örnekte böyle değildir.

```text
>>> y = [[1,2], [1,2], [1,2]]

>>> id(y[0])
133419689170176
>>> id(y[1])
133419689170368
>>> id(y[2])
133419689011904
```

```{hint}
Özetle her `[]` gördüğümüzde yeni bir `list` nesnesi oluşturuluyor gibi
düşünebiliriz.
```

---

Şimdi de şu örneğe bakalım:

```text
>>> x = []
>>> y = [x, x, x]

>>> y
[[], [], []]

>>> id(y[0])
133419689171648
>>> id(y[1])
133419689171648
>>> id(y[2])
133419689171648

>>> x.append(10)

>>> y
[[10], [10], [10]]

>>> x.append(20)

>>> y
[[10, 20], [10, 20], [10, 20]]
```

Burada `y` nin elemanları aynı listeyi yani `x`i göstermektedir. İlk başta `x`
boş bir listedir. Biz `x`e `append()` metodu ile bir eleman eklediğimizde `y`
nin tüm elemanları aynı `x`i gösterdiği için örnekteki gibi bir durum oluşur.

---

Peki `x = [[]] * 3` durumunu düşünelim. Çarpma işlemi aynı şeyi eklemekti.
O yüzden her eleman yine aynı listeyi gösteriyor.

```text
>>> x = [[]] * 3

>>> id(x[0])
133419669508480
>>> id(x[1])
133419669508480
>>> id(x[2])
133419669508480

>>> x = [[], [], []]  # Hepsi ayrı liste

>>> id(x[0])
133419689185280
>>> id(x[1])
133419669796480
>>> id(x[2])
133419669338688
```

`16-2.16.45`
