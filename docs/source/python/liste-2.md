---
giscus: 869ff52f-c279-4f16-8054-5732bad91cbb
---

# Liste, List Veri Yapısı - 2

`14-0.23.00`

## Liste İçerisinde Liste

Bir listenin elemanı başka bir liste olabilir. Mesela

```python
x = [1, [2, 3, 4], 5]
```

olabilir. Neden olmasın ki? Sonuçta liste de bir türdür ve listeler nasıl
diğer türleri tutabiliyorsa kendi türlerini de tutabilirler.

```text
x ------------> list_nesnesi
                ------------------> 1 (int)
                ------------------> list_nesnesi
                                    -----------------> 2 (int)
                                    -----------------> 3 (int)
                                    -----------------> 4 (int)
                ------------------> 5 (int)
```

şeklinde bir bellek organizasyonu olmaktadır.

```text
>>> x[1] is x[1][0]
False
```

---

```text
>>> x = [1, [2, 3, 4], 5]

>>> len(x)
3

>>> type(x[0])
<class 'int'>

>>> x[0]
1

>>> type(x[1])
<class 'list'>

>>> x[1]
[2, 3, 4]

>>> x[1][2]
4
```

---

Bir listenin içerisindeki listenin elemanlarına ikinci bir köşeli parantez
ile erişebiliriz, yukarıdaki `x[1][2]` ifadesi gibi.

## Python'da Matrisler (Matrix)

`14-0.36.50`

Python'da matrisler iç içe listeler şeklinde temsil edilmektedir. Mesela
`3x3`lük bir matris oluşturalım.

```python
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Elbette listeler farklı uzunlukta da olabilir, Python açısından bir engel
yoktur.

```python
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]] # geçerlidir.
```

## Negatif İndeks Değerleri

`14-0.44.00`

Python'da liste elemanlarına `[]` operatörü ile erişirken negatif indeks
değerleri de verebiliriz, bu programlama dillerinde çok yaygın değildir ama yeni
dillerde yaygındır.

Eğer negatif bir değer verilirse gerçek indeks, listenin uzunluğu ile bu değer
toplanarak elde edilir. Yani `i` bir negatif değer ise `x[i]` ile bir elemana
erişmeye çalıştığımız zaman aslında `x[len(x) + i]` elemanına erişmiş oluruz.

Örneğin:

```text
>>> x[4]
5

>>> x[-1]
5

>>> x[4] is x[-1]
True

>>> x[0] is x[-5]
True
```

---

Eğer bir gerçekten mutlak değerce büyük bir negatif sayı verirsek bu sefer
`len() + i` işleminin sonucu gerçekten negatif çıkabilir ve bu durumda
`IndexError` exception oluşur.

```text
>>> x[-10]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

---

İç içe dizilerde de bu özellik kullanılabilmektedir.

```text
>>> a = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

>>> a[-1][-1]
90
```

Negatif indeksleme özelliği bazı durumlarda listeyi sondan başa doğru dolaşmak,
uzunluğunu alıp tekrar hesaplama ile uğraşmamak gibi faydalar
sağlayabilmektedir.

## Dilimleme, Slicing

`14-1.01.08`

Bir liste içerisindeki bir grup elemanı yine bir liste olarak elde edebiliriz.
Buna Python'da slicing yani dilimleme denmektedir. İndeks erişimi gibi
dilimleme de `[]` içerisinde yapılmaktadır. Genel biçimi

```text
x[start:stop]
VEYA
x[start:stop:step]
```

şeklindedir. `step` kısmı belirtilmeyebilir. Dilimlemede `start` indeksli eleman
**dahil** fakat `stop` indeksli eleman ise dahil **DEĞİLDİR**. **Dilimleme
sonucunda yeni bir liste oluşturulur.** Bu 3 parametrenin de `int` türden
ifadeler olması gerekmektedir.

Örneğin

```text
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> x[2:5]
[3, 4, 5]

>>> x[2:5][0] is x[2]
True
```

yapılabilmektedir.

Slicing yaparken negatif indeks de kullanılabilmektedir.

```text
>>> x[2:-5]
[3, 4, 5]

>>> x[-8:-5]
[3, 4, 5]

>>> x[-8:5]
[3, 4, 5]
```

gibi.

---

Slicing yaparken `start` ya da `stop` değerleri liste uzunluğundan büyük olursa
otomatik olarak limitlenmektedir. Burada bir exception oluşmamaktadır.

```text
>>> x[2:100]
[3, 4, 5, 6, 7, 8, 9, 10]

>>> x[-200:2]
[1, 2]
```

gibi.

Eğer `start` ve `stop` değer girerken negatif değerler kullanıyorsak bu değer
`len()` ile toplanup gerçek indeks bulunurken sonuç negatif çıkarsa bu değer
yerine `0` kullanılır. Yani çok büyük negatif değerler kullanırsak `start`
ya da `stop` yerine aslında `0` yazmış olmaktayız.

---

Slicing yaparken `:`nin soluna bir şey yazmazsak `0` yazmışız gibi olur. Sağına
bir şey yazmazsak da *geri kalan hepsi* yani `len()` yazmışız demek. İki
tarafına da bir şey yazmazsak *listenin hepsi* anlamı çıkacaktır.

```text
>>> x[:2]
[1, 2]

>>> x[:]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> x[2:]
[3, 4, 5, 6, 7, 8, 9, 10]
```

---

`start` ile `stop` aynı değerdeyse ya da `start` değeri `stop` tan büyükse
boş liste elde edilmektedir.

```text
>>> x[2:2]
[]

>>> x[3:2]
[]
```

gibi.

---

Bir de ikinci `:` atomu sağına konulabilecek `step` değeri vardır. Bu, atlama
miktarını belirtmektedir. Yazılmazsa `1` değeri kabul edilir. Elde edilecek
değerlere hiçbir zaman `stop` dahil olmaz.

```text
>>> x[2:7:2]  # indeks 2, 4, 6 alındı.
[3, 5, 7]

>>> x[2:8:3] # indeks 2, 5 alındı, 8 hariç bırakıldı.
[3, 6]
```

---

`step` negatif değer de alabilir. Bu durumda ilerleme ters yönde olur. Bunun
anlamlı olması için `start` değerinin `stop` değerinden büyük olması gerekir.
Yine `start` dahil, `stop` hariç olmaktadır.

```text
>>> x[7:2:-1]
[8, 7, 6, 5, 4]
```

`step` negatif ise `start` indeksinin boş bırakılması `len() - 1` anlamına
gelmektedir.

```text
>>> x[:5:-1]
[10, 9, 8, 7]
```

`step` negatif ise `stop` indeksinin boş bırakılması ise *ilk elemana kadar
(ilk eleman dahil)* anlamına gelmektedir.

```text
>>> x[5::-1]
[6, 5, 4, 3, 2, 1]
```

## Listeyi Ters Çevirme

Negatif `step` ile bir listeyi ters çevirebiliriz ve `[::-1]` bunun için
sıklıkla kullanılmaktadır.

```text
>>> x[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

gibi.

## Dilimleme Yolu ile Listenin Güncellenmesi

`14-1.29.30`

Dilimleme yani slice yöntemi ile liste elemanları güncellenebilir.

```text
x[start:stop] = <dolaşılabilir nesne>
```

genel sentaksı ile yapılabilir. Burada basitlik açısından `step`
gösterilmemiştir. Sağ tarafın mutalaka dolaşılabilir yani iterable olması
gerekir.

```text
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> x[2:4] = 20
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
```

Yukarıdaki örnekte `20` yani `int` iterable olmadığı için hata aldık.

---

Bu durumda **önce** dilimlenen elemanlar silinir, **sonra** onların yerine
dolaşılabilir nesnedeki elemanlar `start` indeksinden itibaren yerleştirilir. Bu
işlemin aslında iki basamaklı olduğunu hatırlamak sonraki kısımlarda bazı
durumları anlamamızı kolaylaştıracaktır.

**Silinen eleman sayısı ile dolaşılabilir nesnedeki eleman sayısı aynı olmak
zorunda değildir.**

```text
>>> x[2:8] = [4]

>>> x
[1, 2, 4, 9, 10]
```

Burada `[2:8]` ile geniş bir eleman silinmiş ama yerine daha az eleman
sokuşturulmuştur. Tersi de mümkündür:

```text
>>> x[2:4] = [1, 2, 3, 4 ,5]

>>> x
[1, 2, 1, 2, 3, 4, 5, 10]
```

---

Biraz kafa karıştırıcı durumlar oluşabilmektedir:

```text
>>> x = [1, 2, 1, 2, 3, 4, 5, 10]

>>> x[2:7] = [['alper', 'yazar']]

>>> x
[1, 2, ['alper', 'yazar'], 10]
```

Burada iç içe liste elde etmiş olduk.

Ya da

```text
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> x[-1:] = ['alper', 'yazar']

>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'alper', 'yazar']
```

Burada son eleman silindi ve yerine yeni listeden elemanları yerleştirdik.

Ya da

```text
>>> x[1:1] = ['alper', 'yazar']

>>> x
[1, 'alper', 'yazar', 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Burada `1:1` ile hiçbir eleman seçemedik o yüzden silme yapmamış olduk sadece
yerleştirme yaptık. İlginç di mi? Bu bir metin editörde hiç metin seçmeyip,
cursor yerine `CTRL-V` yapmaya benziyor.

Ya da

```text
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> x[2:7:2] = [100, 200, 300]

>>> x
[1, 2, 100, 4, 200, 6, 300, 8, 9, 10]
```

Burada da silme ve yerleştirme atlaya atlaya yapıldı.

Eğer atladığımız durumda yerleştirmeye çalıştığımız kısım daha uzun olursa
`ValueError` exception oluşmaktadır.

```text
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> x[2:5:2] = [100, 200, 300]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 3 to extended slice of size 2
```

ama `step` belirtmezsek az silip çok sokuşturmak problem olmaz.

```text
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x[2:4] = [100, 200, 300]
>>> x
[1, 2, 100, 200, 300, 5, 6, 7, 8, 9, 10]
```

Benzer durup çok silip az sokuşturduğumuzda da oluşmaktadır.

```text
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> x[2:5:2] = [100]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 1 to extended slice of size 2

>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> x[2:5] = [100]

>>> x
[1, 2, 100, 6, 7, 8, 9, 10]
```

---

Bu şekilde **silme** de yapabilmekteytiz. Dolaşılabilir nesnede hiç eleman yoksa
bu durum silme anlamına gelecektir.

```text
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> x[2:5] = []

>>> x
[1, 2, 6, 7, 8, 9, 10]
```

Niye böyle oluyor? Çünkü önce siliyor sonra iş yerleştirmeye gelince görüyor ki
**Aaa, sokuşturacak hiçbir şey yok!* Biz de efektif olarak silmiş oluyoruz.

---

Eğer `step` negatif bir değer olursa bu sefer yerleştirme işlemi ters yönde
yapılır. Yine seçilen ve silinen eleman sayısı ile atanan eleman sayısının
aynı olması gerekmektedir.

```text
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x[5:2:-1] = [10, 20, 30]
>>> x
[1, 2, 3, 30, 20, 10, 7, 8, 9, 10]
```

## Walrus, `:=`, Operatörünün Kullanımı

Listelere atama yapılırken Walrus operatörü "şartlar uygunsa"
kullanılabilmektedir.

```text
>>> (x := [1, 2])
[1, 2]
```

Walrus operatörü ile `[]` ile *subscript* belirterek atama yapılamamaktadır.

```text
>>> (x[0] := [1, 2])
  File "<stdin>", line 1
    (x[0] := [1, 2])
     ^^^^
SyntaxError: cannot use assignment expressions with subscript
>>> (x[0:1] := [1, 2])
  File "<stdin>", line 1
    (x[0:1] := [1, 2])
     ^^^^^^
SyntaxError: cannot use assignment expressions with subscript
```

`14-2.04.04`
