---
giscus: 677f7826-043c-42dc-a63c-e02c7c7073e4
---

# Demet, tuple Veri Yapısı - 2

`6507`

Şimdi demetin bir elemanı liste olursa o listenin elemanını değiştirebiliriz,
sonuçta liste mutable bir türdür. İşte bu durumda sanki demetin içeriği
değişiyormuş gibi olur ama aslında demetin kendisi değişmez.

```text
>>> t = (1, [2, 3], 4)
>>> id(t[1])
2425387857152

>>> t[1][1] = 100
>>> t
(1, [2, 100], 4)

>>> id(t[1]) # hala aynı listeyi gösteriyor, tuple'de değişme yok.
2425387857152
```

Şimdi burada `t` nin `1` indeksli elemanı listeyi gösteriyor. Double pointer
gibi bir durum oluyor. Biz listenin içeriğini güncelliyoruz ama demet hala
aynı listeyi gösteriyor.

## Parantez kullanmayabiliriz

Demet oluştururken parantez kullanmayabiliriz.

```text
>>> t = (1, 2, 3)
>>> t = 1, 2, 3
>>> t = 10,
```

Yukarıdakilerin hepsi geçerlidir. Ama bazı durumlarda zorunluluk da olmaktadır.
Örneğin bir fonksiyona bir demet göndermek istiyorsak parantezi kullanmak
zorundayız.

```text
>>> print(10, 20)   # iki ayrı argüman oldu
10 20
>>> print((10, 20)) # tek bir demet argümanı geçirdik
(10, 20)
```

Boş bir demet oluştururken de `()` kullanmamız gerekir.

```text
>>> t = ,
  File "<stdin>", line 1
    t = ,
        ^
SyntaxError: invalid syntax
```

yukarıda sentaks hatası aldık.

## demetlerin toplanması, `+` operatörü

iki demeti `+` ile toplayabiliriz. **bu işlem sonrasında yeni bir demet
elde edilir.** listelerde olduğu gibi burada da uc uca ekleme yapılmış olur
aslında. yine benzer şekilde demetlerin içerisindeki adresler kopyalanmış
olur.

```text
>>> x = 10, 20, 30
>>> y = 40, 50, 60

>>> z = x + y

>>> print(z)
(10, 20, 30, 40, 50, 60)

>>> z[0] is x[0]
True

>>> z[3] is y[0]
True
```

görüldüğü üzere yeni demet içerisindeki nesnelerin adresleri ile orijinal
olanların adresleri aynıdır.

## `+=` ile `=+` burada aynı anlamda ❗

listelerde `a = a + b` ile `a += b` farklı anlamda demiştik. demetlerde ise
durum bu şekilde değildir. tuple değiştirilemez bir tür olduğu için zaten sondan
ekleme gibi bir seçene yoktur. yani biz `+=` kullansak bile mecburen yeni
bir tuple yaratılmış olacaktır.

```text
>>> x = 1, 2, 3
>>> id(x)
2425387506112
>>> y = 4, 5, 6
>>> x += y
>>> x
(1, 2, 3, 4, 5, 6)
>>> id(x)
2425396301248
```

görüldüğü üzere yukarıda örnekte `x` in id değeri değişmiştir çünkü yeni bir
nesne yaratılmıştır.

## demetlerde yineleme yani repetition

demetlerde de listelerde olduğu gibi yenileme yani repetition işlemi
yapabiliriz. yani bir demet `int` bir değerler çarpılabilir. bu durumda yine bir
demet nesnesi yaratılır, ne demiştik **demetler değiştirilemez türdür.** bu yeni
demet, çarpılan demetin elemanlarının yinelenmesi ile oluşur.

iki demeti çarpamayız, çıkartamayız ya da bölemeyiz. yineleme işleminde çarpılan
değeri 0 ise ya da negatif bir değer ise boş bir demet elde edilmektedir.
operandlar yine listelerde olduğu gibi yer değiştirilebilir.

bakınız:

```text
>>> t = 1, 2, 3
>>> 3 * t
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> t * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
```

## `*=` ile `=*` burada aynı anlamda ❗

Yine toplama kısmında olduğu gibi çarpmada da demetler değiştirilemez nesneler
olduğu için bu iki işlem arasında bir fark yoktur, her türlü yeni bir nesne
zaten elde edilir.

## `list` VS `tuple`

Bu kadar benzerlik var iken iki veri yapısı arasında, hangisini ne zaman tercih
etmeliyiz?

1️⃣ eğer veri yapısı üzerinde değişiklik yapacaksak zaten demet kullanamayız,
liste kullanmalıyız.

2️⃣ listeler değiştirilebilir olduğu için tipik olarak demetlere göre daha fazla
yer kaplarlar, arka planda tutulan veri yapısı görece daha büyüktür. o yüzden
değişiklik yapmayacaksak bellek verimliliği açısından demetleri tercih etmemiz
daha mantıklı olabilir. hoş, python için böyle *küçük hesaplar* genelde
programcılar tarafından yapılmaz, dilin kullanım amacına da biraz ters
düşebilir.

3️⃣ demetlerin hashlenebilir olduğundan bahsetmiştik. bu da onları henüz
görmediğimiz **sözlük** gibi veri yapılarında kullanılabilir yaparlar. listeler
ise hiçbir zaman hashlenebilir olmamaktadır.

4️⃣ bellek açısından demet vs liste önemsiz olsa da programcılar *ben değişiklik
yapılmasını istemiyorum* vurgusu yapmak için özellikle demet kullanabilmektedir.
örneğin ileride göreceğimiz bir durum ama bir fonksiyonunun birden fazla değeri
çağıran fonksiyona (?) iletmesi gerektiği durumlarda her iki veri yapısı da
kullanılabilse de demetler etkinlik ve okunabilirlik bakımından listelere göre
daha uygun birer veri yapısıdır.

`6174`

FIN
