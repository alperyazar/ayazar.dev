---
giscus: e267304f-958d-4bd6-a0b7-81aa4f4c24a1
---

# Liste, List Veri Yapısı - 1 (YARIM)

`13-1.40.50`

Python'da built-in veri yapıları içerisinde açık ara en çok kullanılanı
**liste** yani **list** veri yapısıdır. Birçok dildeki **array** yani **dizi**
veri yapısına benzemektedir, ama sadece benzer.

Aralarında öncelik ve sonralık ilişkisi olan veri yapılarına tipik olarak liste
denmektedir veri yapıları ve algoritma dünyasında.

Listeler elemanlara sahiptir ve elemanların birer indeks, indis yani index
değeri vardır ve elimizde bir liste nesnesi var ise biz indeks belirterek belli
bir elemana erişebiliriz.

Liste yaratmanın çeşitli yolları vardır ama en çok kullanılanı köşeli parantez
yani `[]` kullanımıdır. Köşeli parantez içerisinde `,` atomu ile ayrılmış
ifadeler girilirse bir liste nesnesi yaratılır. Örneğin

```text
>>> x = [10, 20, 30]

>>> type(x)
<class 'list'>
```

ile bir liste yaratmış olduk. Elbette bunlar sabit olmak zorunda değildir.

```text
>>> a = 10
>>> b = 20
>>> c = 30

>>> x = [a, b, c]

>>> type(x)
<class 'list'>
```

şeklinde de liste oluşturabiliriz, eleman yerine ifadeler yazabiliriz.
Ama burada genelde sabit ifadelerin kullanıldığını söyleyebiliriz.

---

Python'da C gibi dillerin aksine, dilin dinamik tür sistemine sahip bir dil
olmasının verdiği avantaj ile de, listeler içerisinde türler karıştırılabilir.

```text
>>> x = ['alper', 3.14, 3+4j, False, None]

>>> type(x)
<class 'list'>

>>> print(x)
['alper', 3.14, (3+4j), False, None]
```

gibi karışık türden eleman barındılar listeler tanımlayabiliriz. Ama elemanların
aynı türden olması daha yaygın bir durumdur.

## Liste Elemanlarına Erişim, `[]` Operatörü

Listelerin bellirli bir elemanına `[]` operatörü ile erişebiliriz. Eriştiğimiz
elemanları bağımsız nesneler gibi kullanabiliriz. İndeks, C dilinde olduğu gibi
`0` değerinden başlar. Bu durumda `n` elemanlı bir listenin son elemanının
indeksi de `n-1` olmaktadır. Köşeli parantez içerisine bir ifade
yerleştirilebilir. Örneğin `x` bir liste belirtiyorsa biz `x[4]`, `x[i + 2]`,
`x[i + k + 1]` gibi kullanımlar oluşturabiliriz.

**`[]` içerisindeki ifadenin türü `int` olmalıdır.** (ya da *slice*)

```text
>> x = [10, 20, 30]

>>> x[0]
10

>>> x[0+1]
20

>>> x[2*1]
30

>>> x[2/1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not float
```

`/` operatörünün operandları `int` olsa bile `float` türden değer ürettiğinden
`2/1` geçersiz bir indeks ifadesidir.

## `IndexError` Exception

Bir listenin olmayan elemanına erişirsek `IndexError` exception oluşur.

```text
>>> x = [10, 20, 30]

>>> x[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

## "Adres Tutan Dizi"

Bir liste içerisinde elemanların kendileri değil aslında adresleri
tutulmaktadır. Yani listeleri biz **nesnelerin adreslerinden oluşan bir dizi,
array, olarak düşünebiliriz.**

Örneğin

```text
>>> x = ['alper', 0.1, None]

>>> id(x)
133236395691200

>>> id(x[0])
133236415952432

>>> id(x[1])
133236425232528

>>> id(x[2])
95132527875040
```

Burada her bir eleman adeta birer pointer'dır.

## Listeler değiştirilebilir

Türleri immutable yani değiştirilemez ve mutable yani değiştirilebilir diye
ikiyi ayırmıştık. Şimdiye kadar temel türleri gördük, 6 adet, bunların hepsi
immutable türdür. Şimdi ilk defa değiştirilebilir bir tür görüyoruz. **Liste
türü değiştirilebilir bir türdür.**

```text
>>> x = [10, 20, 30]

>>> print(x)
[10, 20, 30]

>>> x[0] = 5

>>> print(x)
[5, 20, 30]
```

Ama `id()` bakarsak bu noktada değerin değiştiğini görmek olasıdır.

```text
>>> x = [10, 20, 30]

>>> id(x[0])
133236428964368

>>> x[0] = 5
>>> id(x[0])
133236428964208
```

Burada `x[0]` artık başka nesnesi gösteriyor aslında. Yan listenin
değiştirilebilir olması aslında farklı nesneleri gösterebildiği anlamına gelir.
Gösterdiği o nesnenin kendisinin değiştirilebilir olduğu anlamına gelmez.

## `len()` built-in Fonksiyonu

Bir listedeki eleman sayısını `len()` built-in fonksiyonu ile elde edebiliriz.
Bu fonksiyon bize bir `int` değer döner.

```text
>>> x = [10, 20, 30]

>>> len(x)
3

>>> x[len(x)-1]
30
```

## Boş Liste

Boş liste de söz konusu olabilir, uzunluğu `0` eleman olmaktadır.

```text
>>> x =[]
>>> len(x)
0
```

## `list()`

Daha önceden biraz gördük ama `T` bir tür olmak üzere `T()` hem `T` türüne bir
dönüşüm yapıyordu ama aynı zamanda `T` türünden bir nesne yaratmaktadır. Aslında
şimdiye kadar gördüğümüz türler de birer sınıftır ama bu detaylara henüz
girmedik. Nasıl `int()` ile değeri `0` olan bir `int` nesne yaratıyorsak
`list()` ile de boş bir liste almaktayız. Yani `a = list()` ile `a = []` özdeş
ifadelerdir.

```text
>>> x = list()

>>> len(x)
0

>>> type(x)
<class 'list'>
```

---

`list` sınıfının *tür fonksiyonu* olan `list()` fonksiyonuna biz dolaşılabilir
bir nesne verebiliriz. Bu durumda bu nesne dolaşılır ve dolaşım türünden elde
edilen değerler ile liste oluşturulur. Örneğin `str` nesnelerinin bir
dolaşılabilir nesne olduğunu söylemiştik. Yani `str` sınıfı dolaşılabilir
bir sınıftır. Bir `str` nesnesi dolaşıldığı zaman tek tek karakterler `str`
olarak elde edilir.

```text
>>> s = 'alper'
>>> x = list(s)

>>> len(x)
5

>>> x[2]
'p'

>>> type(x[2])
<class 'str'>
```

Örneğin burada 5 elemanlı bir liste oluşmuştur. Her bir elemanda türü `str`
olan bir karakter vardır.

`int` türü dolaşılabilir bir nesne olmadığı için `list()` fonksiyonunu bir
`int` türü ile çağıramayız. Bu durumda `TypeError` exception oluşur.

```text
>>> list(12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
```

## "`list` sınıfı da dolaşılabilir."

`list` sınıfı da iterable bir sınıftır, yani o özellikte nesneler türetir.
Peki listeyi dolaşınca ne elde ederiz? Bu durumda içerisindeki elemanları
dolaşmış oluruz.

```text
>>> x = [10, 20 , 30]
>>> y = list(x)

>>> x is y
False

>>> x[0] is y[0]
True
```

Burada gördüğümüz üzere aslında `x[0]` ile `y[0]` aynı nesneyi göstermektedir.

## `list` Nesnelerinin Bellek Orgranizasyonları

`a = [10, 'alper', 3.14]` dersek her bir liste elemanı da bir adres tutmaktadır.
Sırası ile `10` değerli `int` nesnenin adresi, `'alper'` değerli `str` nesnenin
adresi ve `3.14` değerli `float` nesnenin adresi tutulmaktadır.

Python dili liste elemanlarının adreslerinin de ardışıl olma zorunluğunu
getirmemektedir. C'de dizi elemanlarının adresleri ardışıldır, Python'da ise
böyle olmak zorunda değildir. Ama tipik olarak, CPython örneği, listeyi bir
*pointer array* yani pointer dizisi olarak düşünebiliriz. Elimizde `void *a[3]`
varmış gibi düşünebiliriz.

`a` nın gösterdiği adres `a[0]` ın gösterdiği adres genelde aynı olmaz. `a`
liste nesnesinin adresini tutar iken `a[0]` ilk elemanın gösterdiği nesnenin
adresini tutar. C dilinden gelenler için bu farklı gelebilir.

```text
>>> a = [10, 'alper', 3.14]

>>> a is a[0]
False
```

`14.0.00.00`
