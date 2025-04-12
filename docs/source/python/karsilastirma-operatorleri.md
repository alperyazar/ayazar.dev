---
giscus: aecfb6a3-ef4a-43b8-8c6d-a2c8dfc5412a
---

# ⚖️ Karşılaştırma Operatörleri

`11-1.02.02`

Python'da **6 adet** karşılaştırma operatörü vardır. Bu operatörlerin hepsi
iki operandlı araek yani binary infix operatörlerdir:

`<`, `>`, `<=`, `>=`, `==`, `!=`

Bu operatörler `bool` türden değer üretirler. Yani `True` ve `False` değer
üretirler. Örneğin:

```text
>>> 4 > 3
True
>>> 4 != 4
False
>>> 4.2 > 4.1
True
>>> 4.2 > 4
True
```

Örneğin `str` yani string türü de karşılaştırmaya sokulabilir. Ama `int` ile
`str` kıyaslanamaz.

```text
>>> "alper" > "yazar"
False
>>> "alper" > 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'str' and 'int'
```

---

`11-1.05.00`

`bool` türünden değerler karşılaştırmaya sokulduğu zaman, aslında diğer türlerle
işleme sokuldukları durumlarda daha da genelleştirirsek, önce `int` türüne
dönüştürülürler daha sonra işleme sokulurlar. Bu durumda `True`, `1` değerini
alırken `False` ise `0` değerini alır.

Örneğin:

```text
>>> True > False # 1 > 0 ile benzer
True
>>> True == True # 1 == 1 ile benzer
True
>>> 0 == False # 0 == 0 ile benzer
True
>>> 1 >= True # 1 >= 1 ile benzer
True
>>> True + 2 # 1 + 2 ile benzer
3
```

Tabii bunlar geçerli olsa da `bool` değerlerin `>` gibi operatörlerle
karşılaştırılması biraz *gariptir.* Yani `True > False` karşılaştırması yapmak
çok anlamlı olmayabilir ama geçerlidir. Normalde bu tarz bool değerleri sadece
`==` veya `!=` karşılaştırmak anlamlı olacaktır.

## ⛓️ Chained Comparisons, Zincirleme Karşılaştırmalar

`11-1.12.20`

Python'ın diğer programlama dillerinden ayrılan bir özelliği daha vardır. `15 <
x < 25` yazdığımız zaman, matematiksel olarak *x, 15'ten büyük 25'ten küçük mü?*
diye bir anlam oluşur. Programlama dillerinin çoğunda ise böyle değildir. Burada
tipik olarak `İ1 = 15 < x` işlemi yapılır ve bunu sonucu `İ2 = İI < 25` işlemine
sokulur. Java ve C# dillerinde ilk karşılaştırma işleminin sonucu bool türünden
olacağı için ikinci işlem hataya sebep olacaktır. O dillerde bool ile int
karşılaştırmaya sokulamaz. **Python'da ise gerçekten matematikteki anlama
gelmektedir.** Yani `15 < x and x < 25` gibi düşünebiliriz. Bu, Python'nun
matematiksel alana yakınlığı ile ilgilidir. `a == b < c` gibi ifadeler de
yazabiliriz, bu da `a == b and b < c` anlamına gelmektedir. Hatta `a > b < c ==
d` de yapabiliriz. Bu da `a > b and b < c and c == d` anlamına gelir. Pratikte
ise yakında göreceğimiz *mantıksal operatörler* kullanılır. Bu, **Pythonic** bir
şeydir yani Python'da böyledir diğer dillerde ise çoğunluk böyle değildir.

> [Python Ref](https://docs.python.org/3/reference/expressions.html#comparisons)

`11-1.22.45`
