---
giscus: d3dc8f9c-8b90-4b93-b869-19fcaca2557e
---

# `list` Sınıfı ve Metotlar

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

`pop()` metodu listeden silme yapmak için kullanılmaktadır. Eğer metoda
argüman geçmezsek son eleman silinir. Argüman olarak da indeks kabul etmektedir.
Eğer argüman geçersek o indeksteki eleman silinir. `pop()` geri dönüş olarak
bize listeden çıkarılan elemanı vermektedir. Liste boşsa ya da argüman olarak
verilen indeks sınır dışı ise `IndexError` exception oluşur. `pop()` metodu da
negatif indeks kabul etmektedir ve negatif indeksler daha önce bahsettiğimiz
gibi ele alınır. `pop(-1)` son elemanı siler örneğin. `pop()` a argüman olarak
bir indeks aralığı veremeyiz.

Örnek:

```text
>>> x = [1, 2, 3, 4, 5]

>>> print(x.pop())
5

>>> x
[1, 2, 3, 4]

>>> print(x.pop(2))
3

>>> x
[1, 2, 4]

>>> print(x.pop(-2))
2

>>> x
[1, 4]

>>> print(x.pop(2))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range

>>> x = [1, 2]

>>> x[1] is x.pop(1) # UB? :)
True
```

## `remove()`

`15-0.56.30`

Bu da silme yapan bir metottur. Burada `pop()`un aksine silinecek elemanı
indeks değeri ile değil bizzat değeri ile berlitiyoruz. `remove()` ilk olarak
argüman olarak geçerdiğimiz değeri liste içerisinde arar. Eğer onu bulursa
yalnızca ilk bulduğu yerde siler, bulamazsa `ValueError` exception oluşur.
Herhangi bir geri dönüşü değeri yoktur.

```text
>>> x = [1, 2, 3, 4, 5]

>>> x.remove(3)

>>> x
[1, 2, 4, 5]

>>> x.remove(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list

>>> print(x.remove(1))  # Geri dönüşü yoktur.
None
```

## `clear()`

Bu metot listenin tüm elemanlarını siler, liste boş bir liste haline gelir.
Bir parametresi veya geri dönüş değeri yoktur.

```text
>>> x = [1, 2, 3, 4, 5]

>>> print(x.clear())
None

>>> x
[]
```

## `reverse()`

Listeyi ters yüz eder, bu metot bize geri dönüş değeri vermez. Ters yüz etme
işlemi nesnenin üzerinde yani **in-place** yapılmaktadır. Bu, `x[::-1]` ile ters
çevirmekten farklıdır. `x[::-1]` bize ters edilmiş yeni bir liste verir, `x`
nesnesi yani listesi değişmemiş olur yani *in-place* değildir. Oysa ki
`reverse()` *in-place* çalışır yani çağırıldığı nesnenin içeriğini değiştirir.

Örnek:

```text
>>> x = [1, 2, 3, 4, 5]

>>> x.reverse()

>>> x
[5, 4, 3, 2, 1]

>>> x = [1, 2, 3, 4, 5]

>>> x[::-1]
[5, 4, 3, 2, 1]

>>> x
[1, 2, 3, 4, 5]

>>> x = x[::-1]  # x.reverse() ile benzer etki

>>> x
[5, 4, 3, 2, 1]
```

## `sort()`

Bu metot listenin elemanlarını in-place şekilde sıraya dizer. Varsayılan durumda
sıralama küçükten büyüğe yapılır. Bu metot bize bir değer vermez. **Stable** bir
sıralama algoritmasıdır. [^1f]

---

*Stable sorting* kavramı Python'a özgü değildir, genel bir kavramdır. Diyelim ki
elimizde bir dizi var biz bunu sıralıyoruz. Amacımız kelimeleri sıralamak olsun
ve kriterimiz de sadece ilk harfleri olsun. Elimizde `['alper', 'yazar', 'ali']`
varsa sadece ilk harfe göre sıraladığımızda `['alper', 'ali', 'yazar']` ı elde
edebiliriz ama `['ali', 'alper', 'yazar']` da bu kriterlerde doğru bir
sıralamadır. İşte algoritmamız *stable* ise burada orijinal dizideki sıra
korunur, yani `['alper', 'ali', 'yazar']` elde edilir. Eğer *stable* değilse
bu sonuç da elde edilebilir ya da diğeri. Bu özellik, ihtiyacınıza göre anlamlı
olabilir ya da olmayabilir.

---

`sort()` metodu dizme işlemi sırasında elemanlar arasında `<` operatörü ile
karşılaştırma işlemi yapmaktadır, bu şekilde düşünebiliriz. Eğer iki eleman tür
uyuşmazlığı gibi durumdan dolayı karşılaştırılamıyorsa `TypeError` exception
oluşmaktadır.

`index()` metodundan bahsederken farklı türlere ait nesnelerin `==` veya `!=`
ile karşılaştırılabildiğinden bahsetmiştik. Fakat küçüklük-büyüklük
karşılaştırması bu kadar kolay değildir. 🍎 ile 🍐 un eşit olmadığını
söleyebilirsiniz fakat hangisi diğerinden daha küçük ya da büyüktür?

`str` türünden nesneler `<` ile karşılaştırılabilmektedir.

Örnekler:

```text
>>> x = [1, 2, True, 1.2]
>>> x.sort() # True da 1 fakat stable sort olduğu için 1, True'dan önce gelecek.

>>> x
[1, True, 1.2, 2]

>>> x = [True, 2, 1, 1.2]
>>> x.sort() # True da 1 fakat stable sort olduğu için True, 1'den önce gelecek.

>>> x
[True, 1, 1.2, 2]

>>> x = ['a', 'l', 'p', 'e', 'r']
>>> x.sort()

>>> x
['a', 'e', 'l', 'p', 'r']

>>> x = ['a', 1]

>>> x.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str'
```

---

Eğer listeyi tersten dizmek istersek `reverse=True` isimli parametresinin
kullanılması gerekir, varsayılanı `reverse=False` olarak düşünülebilir.
Bu durumda yine `<` operatörü kullanılır arka planda, `>` kullanılmaz.
Test edelim:

```text
>>> x = ['a', 1]

>>> x.sort(reverse=True) # yine < kullanıyor.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'

>>> x = [2, 3.4, 1]
>>> x.sort(reverse=True)

>>> x
[3.4, 2, 1]
```

Python dokümanları bu işlem sırasında hangi algoritmanın kullanılacağını, hangi
karmaşıklıkta olacağını belirtmemiştir ama tipik olarak "iyi" bir sıralama
algoritmasının kullanılacağını düşünebiliriz elbette.

`15-1.39.20`

[^1f]: <https://stackoverflow.com/a/1517824/1766391>
