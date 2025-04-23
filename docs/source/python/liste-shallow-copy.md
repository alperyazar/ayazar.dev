---
giscus: 1e4fbb89-2d07-4816-8027-d9c264aa2392
---

# Listeler ve Shallow Copy, Sığ Kopyalama Kavramı

`14-2.04.04`

Bir listeyi dilimlediğimiz zaman, slice, yeni bir `list` nesnesi oluşmaktadır.
Ancak bu yeni nesnenin liste elemanları da dilimlediğimiz listenin elemanlarında
tutulan adresleri tutmaktadır. Yani dilimleme esnasında listenin elemanlarının
gösterdiği nesnelerden yeni kopyalar oluşturulup daha sonra bu yeni kopyalar
yeni liste tarafından gösterilmez. Bu işlem **shallow copy** yani **sığ
kopyalama** olarak geçmektedir. Her iki liste, yeni ve orijinali, aynı nesneleri
gösterir.

Bunu hemen deneyebiliriz.

```text
>>> x = [1, 2, 3, 4, 5]
>>> y = x[2:4]

>>> y[0] is x[2]
True

>>> y[1] is x[3]
True
```

görüldüğü gibi aynı nesne gösterilmektedir liste elemanları tarafından.

Genel kültür: Eğer liste elemanlarının gösterdiği nesnelerden de yeni kopyalar
oluşturuluyor ve yeni liste bunları gösteriyor olsaydı bu sefer *deep copy* yani
*derin kopyalama* yapılıyor olacaktı. Python'da sığ kopyalama yapılmaktadır.

---

Bu davranışın getirdiği çeşitli bizi şaşırtabilen sonuçlar olabilir. Aşağıdaki
duruma bakalım:

```python
x = [1, [2, 3, 4], 5]
```

Burada liste içerisinde bir liste vardır.

```text
>>> y = x[0:2]
>>> y
[1, [2, 3, 4]]
```

yaptığımız zaman `x` ten bir dilim aldık ve `y`i oluşturduk.

```text
>>> y[1][0] = 100

>>> y
[1, [100, 3, 4]]

>>> x
[1, [100, 3, 4], 5]
```

`y[1][0] = 100` ifadesi ile içerideki listenin ilk elemanını `100` yaptık fakat
bu durumda `x` in içeriği de değişti. Listeler değiştirilebilir yani mutable
nesneler olduğu için böyle bir durum oluşmaktadır.

**Neden?** Biz dilimleme yapıp `y`yi oluşturduğumuz zaman `y[1]` aslında `x[1]`
in de gösterdiği 3 eleman barındıran iç listeyi göstermektedir. Hemen
ispatlayalım:

```text
>>> x[1] is y[1]
True
```

Biz `y[1][0] = 100` ile iç listenin ilk elemanının başka bir `int` nesnesini
göstermesini sağladık. Ama `x[1]` ile `y[1]` aynı 3 elemanlı iç listeyi
gösterdiği için aslında `x` in içeriği de güncellenmiş oldu.

Çizimlerle bellek organizasyonunu biraz daha iyi anlayalım:

```{figure} assets/list-slice-0.png
:align: center

İlk durum
```

```{figure} assets/list-slice-1.png
:align: center

Shallow copy yapıldığı için yeni listenin elemanları da orijinal listenin
elemanları ile aynı nesneleri gösteriyorlar.
```

```{figure} assets/list-slice-2.png
:align: center

`y[1][0] = 100` dediğimizde içerideki liste artık değeri 2 olan `int` nesneyi
değil, yeni yaratılan ve değeri 100 olan başka bir `int` nesneyi gösteriyor.
Ama artık `x` de günün sonunda aynı içeriği gösteriyor. Kullanılmayan ve
değeri 2 olan `int` nesnesi Python implementasyonu tarafından bir noktada
"çope atılacak", garbage collector ve benzeri yapılarla. `int` değiştirilemez
yani immutable bir nesne olduğu için yenisi yaratıldı ama `list`
değiştirilebilir olduğu için değeri güncellendi yani başka nesneyi gösterir
oldu.
```

Elbette `x[0]` ı değiştirirsek `y[0]` değişmeyecektir.

```text
>>> x[0] = 500

>>> x
[500, [100, 3, 4], 5]

>>> y
[1, [100, 3, 4]]
```

`15-0.00.00`
