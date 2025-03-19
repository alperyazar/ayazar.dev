---
giscus: 5419f952-657d-4d3f-b74b-442879df0a3a
---

# Merhaba Python

Python, Java'ya göre basit (sanırım) C ve özellikle C++'a göre oldukça basit bir
dil. Görece basit ve kolay öğrenilebilir olması onun işlevselliğini asla
azaltmıyor ve TIOBE Index'e göre onu en popüler programlama dili yapıyor, Mart
2025'te durum bu şekilde. [^1f] Elbette o dilde *idiomatic* kodlar yazmak ve
kültürünü öğrenmek ayrı bir şey.

> [](../blog/23/tiobe-index-nedir-guvenebilir-miyiz.md) yazıma bakmak
> isteyebilirsiniz.

## Python nasıl bir dildir?

1991 yılında Guido van Rossum geliştirilmesine başlanmıştır. İsminin yılanlar
üzerine olan bir TV programından esinlenildiği rivayet edilir. 2006'lı
yıllara kadar çok da fazla popüler değildi.

---

Python tipik olarak **interpreted** yani `yorumlanan 🇹🇷` bir programlama
dilidir. Tipik olarak derlenip bir makina koduna çevrilmez, çalışma sırasında
**interpreter** yani `yorumlayıcı 🇹🇷` tarafından yorumlanır.

---

Python **dynamically typed** yani `dinamik tür sistemine sahip 🇹🇷` bir
programlama dilidir. Programlama dillerini statik ve dinamik tür sistemine sahip
olarak ikiye ayırabiliriz. C, Pascal, C#, C++, Java gibi diller statik tür
sistemine sahiptir. Burada değişken tanımlarken o değişkenin türünü de açıkça
belirtiriz. Dinamik tür sistemine sahip dillerse ise böyle bir bildirim
bulunmaz. Değişkenin türü atama ile belirlenir.

```python
a = 'Ali'
a = 123
a = 12.3
```

Üstteki geçerli bir Python kodudur. `a` değişkeninin türü kod içerisinde yapılan
atama ile değiştirilebilir. JS, R, Perl, Ruby gibi diller de dinamik tür
sistemine sahiptir. Genel bir kural olmasa da dinamik tür sistemine sahip
dillerin, interpreted diller olduğunu söyleyebiliriz.

```{hint}
İlginizi çekebilir: [](../c/statik-dinamik-tur-kavrami.md)
```

---

Python, **high level** yani `yüksek seviyeli 🇹🇷` bir programlama dilidir.
Makinadan yani işlemciden ziyade insana daha yakındır. Bu sebeple, daha kolay
öğrenilebilen bir dil olduğunu söyleyebiliriz.

```{hint}
İlginizi çekebilir: [](../c/properties.md)
```

---

Alt programların birbirini çağırması şeklinde olan modele **procedural model**
denir. Buna uygun dile de **procedural language** `prosedürel dil 🇹🇷` denir.
Bunların dışında **object oriented**, `nesne yönelimli 🇹🇷` ve **functional**
yani `fonksiyonel 🇹🇷`  programlama dilleri vardır. Eğer bir dil birden fazla
programlama paradigmasını yani modelini desteklerse o zaman o dil, `çok modelli
🇹🇷` yani **multi paradigm** dil olur, Python da böyledir. Python'da hiç sınıf
kullanmadan, fonksiyonlarla yazarsan prosedürel tarzda yazmış olursun. Nesne
yönelimli tekniği kullanabilirsin. Fonksiyonel programlama tekniği de
kullanılabilir.

```{note}
Her programlama dili zamanla az ya da çok evrim geçirir. C dili de geçirmiştir,
Python'da geçirmiş ve hala geçirmektedir. Bu süreçte genelde eklemeler yapılır,
pek çıkartma yapılmaz.
```

---

Python, **general purpose** yani `genel amaçlı 🇹🇷` bir dildir. Mesela PHP ile
mühendislik programı yazmak istemezsin. Python'u ise veritabanı uygulamalarında,
web sayfası tasarımında, bilimsel işlemlerde vs kullanabilirsin.

Standart kütüphanesi oldukça geniştir, **batteries included** denir. Bu
kütüphanenin bir kısmı prosedürel bir kısmı sınıflardan oluşuyor, multi-paradigm
demiştik 😉.

Dilin önemli özelliklerinden biri de matematiksel alanda tercih ediliyor
olmasıdır.

---

R dili S dilinden türetilmiş bir dildir (C gibi B'den sonraki harfi vermemişler
de öncekini vermişler komiklik olsun diye). Bu dil istatistik alanında sıklıkla
kullanılıyor. Python kullananlar genel de R dili konusunda da bilgi sahibi
olabiliyorlar. R, genel amaçlı bir değil yalnız. R daha yüksek seviyeli ama
Python daha geniş bir kullanıma sahip. R, MATLAB'ın rakibi olarak düşünülebilir.

---

Fonksiyonel diller saf (**pure functional**) ve saf olmayanlar diye ikiye
ayrılır. Saf olanlar Haskell ve Scheme örnek olabilir. Bunlar her problem için
çok uygun değil, bazılarına da çok uygun. O yüzden endüstride çok kullanılmıyor.
Ama son 15 senedir falan eski programlama dillerine bu dillerde olan bazı
özellikler kısmen eklendi. Python da buna örnek olabilecek bir dil. C++'a da
2011 ile beraber bu özellikler eklendi. C# ve Java'da da var. Ama pure
functional gibi değil, onlarda *akış* bile yok. Bu diller *saf olmayan* (aptal
anlamında değil, İngilizce *pure* kelimesinin karşılığı) fonksiyonel programlama
dilleri olarak değerlendirilebilir.

---

**Python dilinin standartı var mı?** C, C# gibi diller ISO tarafından
standartize ediliyor. Java ve Python gibi dillerin ise ISO gibi kurumlarca
verilmiş standartları yoktur. Python Software Foundation, python.org, kendi
dokümanlarını oluşturuyor. Standard lafı yerine **spesifikasyon** ya da
**referans** adı kullanılıyor. **Python Language Reference** gibi. Python'nun
ana yasası da python.org içinde yer alır.

<https://docs.python.org/3/reference/>

ve

<https://docs.python.org/3/library/> adresi de **standart kütüphane**
dokümantasyonudur.

Python'nun standart kütüphanesinin ve interpreter'larının cross platform
olduğunu rahatlıkla söyleyebiliriz.

## Tarihsel gelişim

Guido van Rossum Python'un tasarımına ve gerçekleştirimine 1989 yılının
sonlarında başlamıştır. Bu tarihten itibaren dilin pek çok versiyonu
oluşturulmuştur: [^2f]

```text
Aralık 1989     Tasarım ve gerçekleştirime başlandı
1990            İlk versiyonlara içsel numnaralar verilmiştir
Şubat 1991      0.9
Ocak 1994       1.0
Ekim 1994       1.1
Ekim 1995       1.3
Ekim 1996       1.4
Ocak 1998       1.5
Eylül 2000      1.6
Ekim 2000       2.0
Nisan 2001      2.1
Aralık 2001     2.2
Temmuz 2003     2.3
Kasım 2004      2.4
Eylül 2006      2.5
Ekim 2008       2.6
Temmuz 2008     2.7
Aralık 2008     3.0
Haziran 2009    3.1
Şubat 2011      3.2
Eylül 2012      3.3
Mart 2014       3.4
Eylül 2015      3.5
Aralık 2016     3.6
Haziran 2018    3.7
Mart 2019       3.7.3
Ekim 2019       3.8.3
Ekim 2020       3.9
Kasım-2022      3.10
Mart-2022       3.10.4
Ekim 2022       3.11.9
Ekim 2023       3.12.4
Ekim 2024       3.13.2
```

Python'da 2'den 3'e geçiş geriye dönük uyumluluğun bozulduğu büyük bir geçiştir.
Bu geçiş yıllarında Linux dağıtımlarında da işler biraz zor olmuştu. Günümüzde
Python dendiğinde artık aklımıza Python 3 gelmektedir.

## Python Gerçekleştirimleri ve Dağıtımları

**Implementation**, `gerçekleştirim 🇹🇷` ve **distribution** da `dağıtım 🇹🇷`
demektir.

Python kodunun çalışması için bir yorumlayıcıya yani interpreter'a ihtiyaç
vardır. *Ete kemiğe bürünmüş* yorumlayıcılar da birer implementation olmaktadır.
Piyasada birden fazla implementation vardır. Bunların hepsi Python programcısı
açısından hemen hemen aynı çalışır fakat arka planda nasıl yapıldıkları hangi
teknolojiyi kullandıkları farklılık gösterir.

İlk gerçekleştirim ve hala bilgisayarımıza Python kurma dediğimiz aktivitede
kurduğumuz gerçekleştirim **CPython** dur. CPython'un kendisi C dilinde
yazılmıştır.

**Jython** isminde bir gerçekleştirim vardır. Bir Java gibi burada Python kodları
derlenir ve Java Byte Code'a dönüştürülür. Bu sayede Java sınıfları doğrudan
Python kodu içerisinden kullanılabilir.

**IronPython** ise Jython mantığındadır fakat C# ile yazılmıştır. Java platformu
için değil .NET platformu için düşünülmüştür. Visual Studio tarafından doğrudan
desteklenir.

**PyPy** ise hız konusunda iddialı bir implementasyondur.

Dağıtım kavramını ise Linux dağıtımlarına benzetebiliriz. Python dağıtımlarında
implementasyon yanında başka araçlar da olabilir, mesela bir IDE gibi. Örneğin
**Anaconda** bir Python dağıtımıdır örneğin. PyCharm ise bir IDE'dir, dağıtım
değildir. Anaconda dağıtımının default IDE'si de Spyder'dır.

CPython aslında hem bir implementasyon hem de bir dağıtımdır, kendi içinde
**IDLE** isimli bir IDE vardır. Fakat büyük bir dağıtım değildir. CPython ile
gelen `pip` de dağıtımın bir parçasıdır.

```{note}
Bakılabilecek ilginç bir konu:
<https://en.wikipedia.org/wiki/Stackless_Python>
```

[^1f]: <https://www.tiobe.com/tiobe-index/>
[^2f]: <https://github.com/CSD-1993/KursNotlari/blob/master/Python-OzetNotlar-Ornekler.txt>
