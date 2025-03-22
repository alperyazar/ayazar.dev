---
giscus: 841c2d6a-ab7c-4c39-b6ea-ea639d25f953
---

# Temel Veri Türleri

Bir programlama dilindeki türleri yani **types** ya da **data types** bilmek
oldukça önemlidir. Tür, bir nesnenin bellekte ne kadar yer kapladığını, o
nesneye ait bellekteki verinin (1 ve 0'ların) hangi format ile nasıl
yorumlanması gerektiğini, hangi operatörler ile işleme girebileceğini belirten
temel bir özelliktir. Bu bağlamdaki "nesne" terimini "nesne yönelimli
programlama" daki "nesne" ile karıştırmamak lazım. Buradaki nesne yani object
kaba tabirle, kodumuzda erişebildiğimiz, bellekte duran *şeylerdir.* Python'da
değişkenlerin gösterdikleri, aslında birer nesnedir. C ile Python arasında bu
kavramlarda ufak nüans farklılıkları olabilir. Zamanla daha detaylandırırız.

Python temel türler açısından oldukça minimalist bir dildir. C'de 10'dan fazla
temel tür var iken (hoş, aynı türün laciverdi çoğu… ) **Python'da 6 adet temel
tür** bulunmaktadır.

Python'un, dinamik tür sistemine sahip olduğunu tekrar hatırlayalım. Yani
bir değişkenin türü, o değişkene atanan "şeyin" türüne göre değişmektedir.
En basitinden C dilinde `int x = 5;` yazıp, önce C derleyicisine `x` in türünün
`int` olduğunu belirtmemiz gerekir ve bu tür artık değişmez. Python'da ise `x`i
tanıtmamıza gerek yoktur, `x = 5` ile bunu yapabiliriz. Fakat herhangi bir `t`
anında bir değişken sadece bir türde olabilir ama zaman içerisinde türü
değişebilir.

```python
# x'in türü değişmekte sürekli ve bu Python'da geçerlidir.

x = 5
x = 3.14
x = "alper"
```

Python'da `type()` isimli bir built-in fonksiyon vardır. [^1f] Biz bu fonksiyonla
bir değişkenimizin türünü öğrenebiliriz. Üstteki kodu, interaktif modda yani
REPL ile çalıştırdığımızda aşağıdaki çıktıyı alırız:

```text
>>> x = 5
>>> type(x)
<class 'int'>
>>> x = 3.14
>>> type(x)
<class 'float'>
>>> x = "alper"
>>> type(x)
<class 'str'>
```

`x` in türü gördüğünüz üzere atamaya göre değişmektedir.

## 1 - `int`

Python'da, C'nin aksine tam sayıları tutan tek bir tür vardır, o da `int`.
`unsigned int`, `long` gibi türler yoktur. **Python'daki `int` türü istediğimiz
kadar uzun olabilmektedir.** Yani tutması gereken değer için bellekte kaç byte
harcaması gerekiyorsa o kadar harcar. Bu durum, özellikle C gibi dillerden
geliyorsanız biraz garip gelebilir, özellikle de arka planda nasıl
yapılabileceğini düşündüğünüz zaman. Ama yavaş yavaş bunları da göreceğiz.

> İlginizi çekebilir: [](../c/statik-dinamik-tur-kavrami.md)

```{attention}
Tabii Python'da her ne kadar `int` türünün bir sınırı yoksa da Python
implementasyonları kendi limitlerinden dolayı buna bir sınır getirebilmektedir.
```

## 2 - `float`

Kayar noktalı sayıları yani floating point numbers dediğimiz sayıları ifade
etmek için `float` türü kullanılır. Python'da C dilinin aksine `float` ve
`double` şeklinde iki farklı tür yoktur. Python'nun `float`u  C/C++/Java/C#'ın
`double` ına karşılık gelmektedir. Python'daki `float` türü [IEEE 754 double
precision floating-point
number](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)
türüdür, `FP64` ya da `float64` olarak da ifade edilebilir. Numerik anlamda bu
türün 8 byte ile ifade edildiğini düşünebiliriz. Ama Python'daki nesneler C'deki
gibi "yalın" olmadığı için bellekte daha fazla yer kaplayacaktır, ileride
değineceğiz.

```python
# Anlamaya çalışmayın
import sys
x = 3.14
print("x bellekte:",sys.getsizeof(x), "byte yer kaplıyor.") #Bende 24 byte çıktı!
```

---

Float sayılarda Python'a özgü olmayan bir problem vardır o da **yuvarlama
hataları** yani **rounding errors**tür. Float sayıların hepsi "tam olarak" bu
formatlarla gösterilemez. Böyle bir durumda sayı, gösterimi mümkün olan yakın
bir sayıya yuvarlanır ama bu da nümerik bir hata oluşturur. Burada oluşan hata,
uygulamanıza göre anlamsız ya da çok kritik olabilir. Bu hata durumu sayıyı
belleğe ilk kez depolarken çıkabileceği gibi aritmetik işlemler sonucu da
çıkabilir.

```python
0.3 + 0.1 # 0.4
0.3 - 0.1 # 0.19999999999999998 yuvarlama hatası var.
0.3 - 0.1 == 0.2 # False! Yuvarlama hatasından dolayı
```

```{tip}
Float sayıları karşılaştırmak için diğer dillerde de kullanılan bir teknik olan
sayıların tam eşitliği değil, bellirli bir yakınlıkta (epsilon) olup olmadığı
tekniği kullanılabilir. Sayılar "yeterince" aynı ise, aynı denilebilir. Ya da
Python'da Python 3.5 ile gelen
[math.isclose()](https://docs.python.org/3/whatsnew/3.5.html#pep-485-a-function-for-testing-approximate-equality)
kullanılabilir.
```

```{tip}
Eğer yuvarlama hataları uygulamamız için kritikse bu durumda Python'da bulunan
[decimal](https://docs.python.org/3/library/decimal.html) modülüne bakmak
iyi olacaktır. Fakat bu modül ile yapılan işlemler, işlemcilerin içerisinde
IEEE 754 float işlemlere göre daha yavaş çalışabilir.
```

```{tip}
Yine konu dışı olacak ama ihtiyaca göre *fixed point* de tercih edilebilir.
Burada yapılan işlemler aslında tam sayı işlemleridir. Günümüzdeki işlemcilerde
float sayılarla da pek bir performans kaybı olmadan çalışılabilse de *fixed
point* işlemlerin performans açısından tepe nokta olabilir.

Çok eski işlemcilerde floatin point unit denilen donanımda hızlandırılmış float
hesaplama desteği yoktu, örneğin 8086 işlemcilerde. Microsoft mesela DOS için
[Microsoft Binary Format
(MBF)](https://en.wikipedia.org/wiki/Microsoft_Binary_Format) isminde bir format
"uydurmuştu" ve bellekte bu sayıları tutmak için bu formatı kullanıyordu. Donanımda
hızlandırma desteği olmadığı sürece float sayıları IEEE gibi standart formatlarda
tutmanın pek de bir anlamı olmayabilir, yazılım tarafındaki hazır kütüphanelerin
getirebileceği diğer avantajları da yok sayarsak elbette.
```

## 3 - `bool`

`bool` türü, True ve False tutabilen bir türdür. Geçmişi taa [George
Bool](https://tr.wikipedia.org/wiki/George_Boole)a dayanmaktadır. `True` ve
`False` anahtar sözcüktür ve büyük harfle başlar.

```text
>>> x = True
>>> type(x)
<class 'bool'>
```

## 4 - `str`

`str`, String yani yazı türüdür. Sabit kısmına sonra bakacağız ama C'deki gibi
`''` ile `""` arasında bir fark yoktur. Python'da `char` türü bulunmamaktadır.
`'alper'` ile `"alper"` aynıdır. Peki hangisini kullanmalıyız? Fark etmez,
Python dünyasında pek genel geçer bir kabul yoktur.

## 5 - `complex`

Karmaşık yani imajiner sayıları yani imaginer number içerikleri göstermek için
kullanılan bir türdür. C diline C99 ile gellen `_Complex` e benzer.

Pyton'da karmaşık sayılarda `i` değil, mühendislik camiasında kullanılan `j`
kullanılmaktadır. `a = j` dersen normal değişken ataması olur. Bu durumda
`a = 1j` demen gerekecektir, `1` ile `j` arasında boşluk olmamalı.

> Meraklısına: [Why are complex numbers in Python denoted with 'j' instead of
> 'i'?](https://stackoverflow.com/a/24812657)

Örnek:

```text
>>> x = 4 + 3j
>>> type(x)
<class 'complex'>
```

## 6 - `NoneType`

Python'da `None` adında bir değer vardır, hiçlik ve yokluk anlamında kullanılır.
`None` bir anahtar sözcüktür. `NoneType` olan tek şey de `None`dır.

```text
>>> x = None
>>> type(x)
<class 'NoneType'>
```

Bu `None` işi, diğer dillerdeki `nul` ya da `nil` gibi kavramlara benzemektedir.

Değeri `None` olan bir değişken interaktif modda komut satırında
yazdırılmamaktadır. Yani adını yazıp ENTER tuşuna basınca bir çıktı
oluşmamaktadır ama `print()` ile yazdırılabilmektedir. Bu durumda ekrana `None`
yazısı çıkar.

```text
>>> x = None
>>> type(x)
<class 'NoneType'>
>>> x
>>> print(x)
None
```

## Çeşitli Sorular

***Python'da türlerin default değeri var mı?***

Bu soru Python'da bir miktar anlamsız çünkü bildirim (declaration) yok C'de
olduğu gibi tür sisteminden dolayı ama ileride sınıfsal olduğunu göreceğiz orada
default değerler var, `float()` dersek mesela bir varsayılan değer geliyor.

```text
>>> x = float()
>>> print(x)
0.0
```

---

## Özet

Özetle:

```text
>>> a = 4
>>> type(a)
<class 'int'>

>>> a = 3.14
>>> type(a)
<class 'float'>

>>> a = 'Alper'
>>> type(a)
<class 'str'>

>>> a = False
>>> type(a)
<class 'bool'>

>>> a = 3j+4
>>> type(a)
<class 'complex'>

>>> a = None
>>> type(a)
<class 'NoneType'>
```

Elbette bu Python'da kullanacağımız türler bundan çok daha fazladır. Ama burada
temel yani **fundamental types** olanları gördük.

[^1f]: <https://docs.python.org/3/library/functions.html#type>
