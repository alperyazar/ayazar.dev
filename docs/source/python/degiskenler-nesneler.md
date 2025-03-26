---
giscus: dd416963-1697-4560-a77f-7ba78c22f3ce
---

# Değişkenler ve Nesneler

Python dilinin dinamik tür sistemine sahip olduğundan ve aynı değişkene
birden fazla türden değerler atanabildiğinden bahsetmiştik, tabii aynı anda
olmamak şartı ile

```python
x = 4
x = True
x = 'Alper'
x = 3.14
```

Yukarıdaki kod geçerli bir Python kodudur.

C gibi dillerden gelen bir programcıysanız bu size garip gelebilir. Çünkü
C gibi statik tür sistemine sahip dillerde değişkenin türünü önceden
belirtiyoruz.

```c
int x;
x = 4;
x = "Alper"; //C'de geçerli değil
```

Burada C derleyicisi `int x;` ile `x` için bellekte bir yer ayırıyor, diyelim
4 byte. Sonra biz her `x` dediğimizde aslında bu bellek alanına ulaşıyoruz.
`x = 4` dediğimizde de bu belli alana gidip `4` değerini yazıyoruz.

**Peki nasıl oluyor da Python'da farklı türden atamaları rahatça yapıyoruz?**

Python, Ruby gibi dinamik tür sistemine sahip dillerde **adres ataması
yapılmaktadır.** C'deki pointer'lar gibi düşünebiliriz. Yani
**Python'da tüm değişkenler C dilini düşünürsek birer pointer'dır.**
Yani Python'da **değişkenler, nesnelerin adresini tutar.**

```{important}
C ve C++'ta bellekte yer kaplayan her şeye nesne derdik.
Burada aslında `x` de
bellekte yer kaplıyor ama Python terminolojisinde bunlara nesne demiyoruz.
Bunlara değişken diyoruz.
```

Python'da `x = 4` dediğimiz zaman bellekte öncelikle değeri `4` olan bir `int`
nesne yaratılır ve daha sonra bu nesnenin adresi `x`e atanır. Sonra `x = 3.14`
dersek, değeri `3.14` olan bir `float` nesne yaratılır ve `x` artık `int`
nesnesini değil, yeni `float` nesnesini gösterir.

```{note}
Tanım olarak Python'da adres tutan varlıklara **değişken**, değişkenin
gösterdiği yere de **nesne** diyebiliriz.
```

## Tür Bilgileri?

Peki aşağıdaki kodu çalıştıralım:

```python
x = 4
print(type(x))

x = 'alper'
print(type(x))
```

Bu kodun çıktısı aşağıdaki gibi olmaktadır:

```text
<class 'int'>
<class 'str'>
```

Peki Python nasıl oluyor da tür bilgilerini bilebiliyor? İşte burada dinamik
tür sistemine sahip dillerde sıklıkla kullanılan bir teknikten bahsedebiliriz.
Python gibi dillerde nesnenin sahip olduğu değerle beraber *metadata* bilgileri
de tutuluyor. Örneğin `x = 4` ataması yapılınca `x` in gösterdiği yerde sadece
`4` değeri yok. C dilindeki `struct` ile oluşturulmuş bir veri yapısı var gibi
düşünebilirsiniz. Burada nesnenin türü, değeri gibi bilgiler yer alıyor.

```python
import sys

print(sys.getsizeof(0))
print(sys.getsizeof('a'))
```

Yukarıdaki kodda değeri `0` olan bir `int` nesne ile değeri `a` olan bir `str`
nesnenin bellekte kaç byte yer kapladığına bakıyoruz. Çıktı:

```text
28
50
```

Değeri `0` olan bir `int` e göre 28 byte, ve tek karakter yazı içeren `str`
türden nesneye göre 50 byte biraz fazla değil mi? C'de yazıyor olsaydık çok
daha az bellek tüketimi ile işimizi halledebilirdik. Bu bellek alanlarında
nesnelerin tür bilgileri ve başka bilgiler de tutulmak durumundadır.

İşte dinamik tür sisteminin getirdiği esnekliğin bir bedeli de bellek tüketiminde
çıkmaktadır. Ayrıca her seferinde bu bellek alanlarının okunup tür bilgilerini
elde edilmesi gerekebilir, bu da çalışma zamanında yavaşlığa da sebep olabilir.
Yani hem bellek tüketiminden hem de kod çalışma hızından gol yiyoruz gibi ⚽.

## `id()` Fonksiyonu

Python'da `id()` isminde bir built-in fonksiyon bulunmaktadır. Bu bize bir sayı
döner ve bir nesnenin *unique* bir numarasıdır, kimlik no gibi düşünebiliriz.
Fakat aynı anda var olmayan iki nesnenin id değeri aynı olabilir, yani tam
kimlik no gibi de değil sonuçta ölen birinin kimlik numarasını başkasına
vermiyoruz.

CPython'da ise `id()` nin nesnenin bellekteki gerçek adresi olduğu bilgisi
verilmiştir. [^1f] Elbette bunların da sanal bellek adresleri olduğunu
unutmayalım. Diğer Python implementasyonlarında dönülen değer bellek adres
değeri olmayabilir. CPython'da bir değişkenin tuttuğu adres değerini bu şekilde
alabiliriz.

```{tip}
İlginizi çekebilir: [](../sys/sanal-bellek.md)
```

Aşağıdaki Python kodunu çalıştıralım:

```python
x = 4
print(id(x))

x = 'alper'
print(id(x))

x = 3.14
print(id(x))
```

Çıktı:

```text
94775663043592
140138541178160
140138879044240
```

Sizde tamamen farklı sayılar çıkacaktır, muhtemelen. Gördüğümüz üzere her
atama sonucunda `x` in gösterdiği değer değişmektedir.

## Adres Atamaları

Python'daki tüm atamalar adres atamasıdır. Atama işleminde, atama operatörünün
yani `=` karakterinin solundaki değişkene bir adres atanmaktadır.

```python
x = 10
y = x

print(id(x))
print(id(y))
```

Python'da değişkenler adres tutar ve atamalarda her zaman adresler atanır.
Yukarıdaki programın çıktısı:

```text
94775663043784
94775663043784
```

olmaktadır. Sizdeki sayılar benden farklı fakat kendi içinde aynı olacaktır.

Yukarıda değeri `10` olan bir `int` nesne bellekte yaratılmış ve değeri `x` e
atanmıştır. Daha sonra aynı adres değeri `y` ye atanmıştır. Yani `x` ve `y` de
aynı nesneyi gösterir olmuştur.

---

Elbette değişkenleri gördüğümüz her yerde adresler üzerinde işlem yapılıyor
gibi düşünmememiz lazım.

```python
a = 10
b = 20

c = a + b # adresler toplanmaz, nesnelerin içeriği toplanır. 30 olan nesne
          # oluşturulur ve c bu nesneyi gösterir.

# Bu noktada bellekte değerleri sırası ile 10, 20 ve 30 olan 3 adet int nesne
# vardır.*

# *: Garbage collector gibi kavramları öğrenmedik
```

Yukarıdaki kodda `a` ve `b` nin tuttuğu adresler toplanmaz. `a` ve `b` nin
gösterdiği nesnelerin içerdiği değerler toplanır, değeri `30` olan yeni bir
`int` nesnesi yaratılır. `c` ise bu `30` değerli `int` nesnesini gösterir.

Deneyelim:

```python
a = 10
b = 20

c = a + b

print(id(a))
print(id(b))
print(id(c))
```

```text
94775663043784
94775663044104
94775663044424
```

Görüldüğü gibi 3 farklı nesne vardır.

## Garbage Collector - Çöp Toplayıcı 🗑️

Aklımıza şu nokta şöyle bir soru takılabilir: Yaptığımız işlemler sonucu ortada,
kontrolü pek de bizde olmayan bir şekilde, nesneler yaratılıyor içerisine
değerler konuluyor. Programın çalışma sırasında yaratılan birçok nesne oluyor.
Bunların, heap gibi bir alandan oluşturulduğunu düşünebiliriz. Peki bu
sürdürülebilir bir şey mi? Yani sürekli bellekten alan tahsis edip kullansak ve
hiç geri vermesek ve programımız da uzun süre çalışsa bellek tükenmez mi? İşte
Python nasıl otomatik olarak nesneler yaratıyorsa yine otomatik olarak nesneleri
silmektedir. Artık işi bitmiş, kullanım imkanı kalmamış olan nesnelerin otomatik
olarak bellekten temizlenme işlemi kavramsal olarak **garbage collection**
olarak geçmektedir. Programın bunu yapan parçasına da **garbage collector** adı
verilir.

Python standardı bu konuyu implementasyonlara oldukça geniş bir biçimde
bırakmıştır [^2f]:

> Objects are never explicitly destroyed; however, when they become unreachable
> they may be garbage-collected. An implementation is allowed to postpone
> garbage collection or omit it altogether — it is a matter of implementation
> quality how garbage collection is implemented, as long as no objects are
> collected that are still reachable.

Gördüğümüz üzere erişilebilir bir nesne ortadan kaldırılmadığı sürece
implementasyon bu konuda farklı çözümler sunabilir.

Örneğin *CPython* **reference counting** ve **cyclic garbage collector** gibi
mekanizmalar kullanırken, *PyPy* **tracing garbage collection** kullanır, yani
nesnelerin silinmesi geciktirilebilir. *Jython* ve *IronPython* ise kendi
platformları, sırası ile JVM ve .NET CLR, tarafından sunulan mekanizmaları
kullanır. CPython, kullandığı mekanizma sebebi ile bir nesne erişilemez bir
konuma geldiği zaman onu hemen bellekten kaldırmaktadır.

```{note}
Elbette yukarıdaki örnekte yaptığımız gibi küçük `int` sayılar gibi görece
küçük nesneler farklı, daha verimli yöntemlerle de ele alınıyor olabilirler.
Her bir nesne için arkada `malloc()/free()` çalışıyor gibi varsaymamıza gerek
yok ama kabaca konuştuğumuz gibi hayal edebiliriz.
```

Garbage collector konusuna ilerleyen kısımlarda (ama daha var) tekrar
değinebiliriz.

[^1f]: <https://docs.python.org/3/library/functions.html#id>
[^2f]: <https://docs.python.org/3/reference/datamodel.html#objects-values-and-types>
