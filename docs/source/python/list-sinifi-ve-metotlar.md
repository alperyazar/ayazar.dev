---
giscus: d3dc8f9c-8b90-4b93-b869-19fcaca2557e
---

# `list` Sınıfı ve Metotlar (YARIM)

`15-0.03.24`

Sınıf ve metot (method) kavramından biraz ucundan bahsetmiştik. Bir sınıf
içerisindeki fonksiyonlara **method** yani **metot** denmektedir. Bir metotu
çağırmak için `.` operatörünü kullanmaktayız. Örneğin `a` bir sınıf üzerinden
nesneyi gösteren değişken olsun. Eğer o sınıfın `foo` isimli bir metodu varsa
onu `a.foo()` şeklinde çağırabiliriz. C++'ta örneğin metot yerine genelde
*member function* terimi kullanılmaktadır.

Metotlar belli bir nesne üzerinde işlem yapan fonksiyonlardır. `a.foo()`
dediğimiz zaman `foo` metodu `a` değişkeninin gösterdiği nesne üzerinde işlem
yapar. Eğer fonksiyonlar bir sınıf içerisinde değilse, belli bir nesne üzerinde
işlem yapmak yerine genel işlemleri yapmak üzere yazılmış, elbette parametre
olarak değişken alabilirler, olurlar.

---

`list` bir sınıftır ve bize kullanabileceğimiz çeşitli metotlar sunar. Biz de
bunları `list` türünden nesneler üzerinde kullanabiliriz.

## `append()`

`list` sınıfının `append` isimli bir metodu vardır. Bu metod, çağırıldığı
listenin sonuna yeni bir eleman ekler.

```text
>>> x = [1, 2, 3, 4, 5]

>>> x
[1, 2, 3, 4, 5]

>>> x.append('alper')

>>> x
[1, 2, 3, 4, 5, 'alper']
```

---

`append()` ile liste eklemeye çalışırsak elemanları tek tek eklenmez, liste
iç bir liste olarak eklenir.

```text
>>> x = [1, 2]
>>> y = [3, 4, 5]

>>> x.append(y)

>>> x
[1, 2, [3, 4, 5]]
```

## `extend()`

`extend` metodu `append`e benzer. `extend` birden fazla eleman eklemek için
kullanılmaktadır. Parametresinin dolaşılabilir bir nesne olması lazımdır ki
şimdiye kadar iki adet dolaşılabilir yani iterable nesne gördük: `str` ve
`list`. Dolaşılamayan bir argüman verirsek `TypeError` exception alırız.

```text
>>> x = [1, 2]

>>> x.extend(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable

>>> x.extend('alper')

>>> x
[1, 2, 'a', 'l', 'p', 'e', 'r']
```

Örneğin bir `str` verdiğimizde karakterleri tek tek eklenmiş oldu çünkü
`str`yi dolaştığımız zaman onu oluşturan harfleri elde ederiz.

Benzer şekilde `list` verdiğimizde de elemanları tek tek eklenmiş olur.

```text
>>> x = [1, 2]
>>> y = [3, 4, 5]

>>> x.extend(y)

>>> x
[1, 2, 3, 4, 5]
```

Burada elemanlar tek tek eklenmiş oldu.

```text
>>> x = [1, 2]

>>> x.extend([[3,4], [5, 6]])

>>> x
[1, 2, [3, 4], [5, 6]]
```

Burada içinde iki adet liste barındıran yeni bir liste verdik. Listeyi dolaşınca
alt listeleri elde ettik. `extend` bunları bir daha dolaşmıyor, yani recursive
bir yapı yok. Bu durumda listeler eklenmiş oluyor.

## `index()`

Bu metot ile ilgili liste içerisinde arama yapabiliriz. Bu tarz metotlar
dillerin çoğunda vardır.

Eğer arama başarılı olursa metot bize bulduğu indeksin numarasını verir, `int`
türünden. Eğer bulamazsa `ValueError` exception oluşur. Dolayısı ile zaten var
olduğunu bildiğimiz bir elemanın yerini bulmak için genelde kullanılır.

```text
>>> x = [10, 20, 30]

>>> x.index(20)
1

>>> x.index(21)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 21 is not in list
```

---

**Burada önemli bir noktaya vurgu yapalım.** İleride göreceğiz ama biraz
konuşalım.

Python'da farklı sınıflar türünden fakat `int`, `float` ve `bool` haricinde
değişkenler `==` ve `!=` operatörleriyle karşılaştırıldığında `==` her zaman
`False`, `!=` ise `True` döner. Mesela:

```text
>>> 'alper' == 16
False
```

sonucu almaktayız. Çünkü tam anlamıyla elma 🍎 ile armutu 🍐 kıyaslıyoruz. `int`
ve `float` tam elma 🍎 - armut 🍐 değil de kırmızı elma 🍎 ve yeşil elma 🍏 gibi
olduğu için bu şekilde kafadan `False` oluşturmazlar. Örneğin:

```text
>>> 16 == 16.0
True
```

Bu bilgiler ışında `index` metodunun her zaman `==` araması yaptığını
düşünebiliriz. Buyrunuz:

```text
>>> x = [16, '16']

>>> x.index(16)
0

>>> x.index('16')
1

>>> x.index(16.0)  # 16 == 16.0 True
0

>>> x.index('16.0')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: '16.0' is not in list
```

---

Eğer aranan değer birden fazla elemanda bulunuyorsa ilk bulunan yer yani indeksi
en küçük olan elemanın indeks değeri geri döndürülür.

```text
>>> x = [0, 1, 1, 2]

>>> x.index(1)
1
```

---

`index` metodu iki argümanlı şekilde de kullanılabilmektedir. İki argümanla
çağırırsak ikinci argüman aramanın başlatılacağı indeksi belirtir.

```text
>>> x = [0, 1, 1, 1, 1, 2]

>>> x.index(1)
1

>>> x.index(1,2)  # Indeks 2'den başlar ve hemen bulur.
2
```

---

Üç argümanlı kullanım da vardır. Bu da aramanın bireceği indeksi gösterir.
Bu indeks, aramaya dahil değildir.

Tüm kullanımları aşağıdaki örnekte görebiliriz:

```text
>>> x = [0, 1, 1, 1, 1, 1, 1, 2]

>>> x.index(1)
1

>>> x.index(1, 3)
3

>>> x.index(2)
7

>>> x.index(2, 3)
7

>>> x.index(2, 3, 6)  # 6'da sonlandığı için 2 bulunamadı
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 2 is not in list
```

## `count()`

`15-0.42.35`

`count` metodu da bir noktada `index` metoduna benzer. Bize o elemandan kaç
adet olduğunu söyler.

```text
>>> x = [0, 1, 1, 1, 1, 1, 1, 2]

>>> x.count(1)
6

>>> x.count(0)
1

>>> x.count(2)
1

>>> x.count(3)
0
```

Olmayan bir şey verirsek exception almıyoruz, `0` değeri dönülüyor.

## `pop()`

`15-0.45.35`
