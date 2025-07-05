---
giscus: 6b66d1a1-df45-41a2-8da0-ea237c2813a6
---

# `str` Sınıfı ve İşlemleri - 2

`9101`

Şimdi de `str` sınıfının metotları üzerinde duracağız.

```{important}
Şimdi `str` sınıfının
değiştirilemez olduğunu söylemiştik. Burada metotlar sanki `str` nesnesinin
içeriğini değiştiriyor gibi gözükse de aslında mevcut nesneyi değiştirmezler,
bize değiştirilmiş yeni yazı verirler. İlerideki cümlelerde `str` değişiyormuş
gibi gözükse de aslında yeni nesneler elde edilmektedir.
```

## `capitalize()` Metodu

Bu metod bir parametre almaz, ilk harfi büyük yapıp bize geri verir.

```text
>>> s = 'alper'

>>> id(s)
547866001712

>>> s = s.capitalize()

>>> s
'Alper'

>>> id(s)
547865992240
```

Görüldüğü gibi farklı bir nesne elde etmiş olduk.

## `title()` Metodu

Bu metot da yazının tüm sözcüklerinin ilk harfini büyütür, sadece ilk
kelimenin değil.

```text
>>> 'bu bir başlıktır'.title()
'Bu Bir Başlıktır'
```

## `center()` Metodu

Bu metod, yazıyı belli bir genişlikte ortalar. Birinci parametre döndürülecek
yazı uzunluğunu belirtir. Yani sonuçta çıkan yazı bu uzunlukta olacaktır. Eğer
bu şekilde tek argümanlar çağırırsak yazının sağı ve solu boşluk karakteri
ile doldurulur. Ama ikinci argüman da geçebiliriz. Bu ikinci argüman girilirse
tek karakterli bir `str` olmalıdır. Eğer bu argüman verilirse sağ ve sol
boşluk karakteri ile değil, bu karakterler doldurulur.

Eğer sağa ve sola konması gereken karakter sayısının toplamı tek ise hangi
tarafa fazla karakter koyulacağı *Python Standard Library Reference*ta
belirtilmemiştir.

Örnekler:

```text
>>> 'alper'.center(10)
'  alper   '

>>> 'alper'.center(10,'*')
'**alper***'

>>> 'alper'.center(10,'**')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: The fill character must be exactly one character long
```

## `find()` Metodu

`9187`

Yazı içerisinde bir yazıyı aramak için kullanılır. Eğer yazı bulunursa bize
*ilk bulunduğu yerin* indeks numarasını döner. Eğer bulunamazsa `-1` değerini
döner.

```text
>>> s = 'ankara'

>>> s.find('k')
2

>>> s.find('nk')
1

>>> s.find('b')
-1
```

---

`find()` iki argüman da alabilir, ikinci argüman verilirse arama o indekseten
başlatılır. Üç argüman da verirsek aramanın bitirileceği indeks söylenir ama
aramaya bu indeks dahil edilmez.

Örnekler:

```text
>>> s = 'bugün hava çok güzel, evet evet hava çok güzel'

>>> s.find('hava')
6

>>> s.find('hava', 10)
32

>>> s.find('z', 10)
17

>>> s.find('z', 10, 15)
-1
```

## `rfind()` Metodu

Bu da `find()` gibidir ama aramayı tersten yapar ya da `find()`ın bulunan
son indeks numarasını veren versiyonu gibi düşünülebilir. Bu da tek, çift
ya da üç argümanla çağırılabilir.

```text
>>> s = 'adıyaman'

>>> s.rfind('a', 1, 6)
4

>>> s.rfind('a', 1)
6

>>> s.rfind('a')
6
```

---

Şimdi biraz daha gerçekçi bir örnek yapalım. Burada bir yol ifadesindeki dosya
adı elde edilmiştir. Eğer path `\` yoksa `rfind()`, `-1` döneceği için
tüm yol ifadesi elde edilir.

```text
>>> path = r'c:\windows\system\test.dll'

>>> index = path.rfind('\\')
>>> fname = path[index + 1:]

>>> fname
'test.dll'
```

## `index()` ve `rindex()` Metodları

Bu metodlar `find()` ve `rfind()`a benzer. Bunlar da tek, çift veya üç argümanla
kullanılabilir. Tek farkı bulamayınca `-1` ile dönmek yerine `ValueError`
exception oluşturmalırıdır.

```text
>>> s = 'ankara'

>>> s.find('b')
-1

>>> s.index('b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

## `count()` Metodu

`9305`

Bu metod ile `str` içerisinde bir yazı parçasının ya da tek bir karakterin
kaç adet olduğu bilgisi verilir. Bu da tek, çift ya da üç argümanla
kullanılabilir. Argümanların çalışma biçimi aynıdır.

```text
>>> s = 'ankara'
>>> s.count('a', 2, 5)
1
```

## `isxxx()` Metodları

Bir grup metod vardır. Bunlar yazının tüm karakterlerinin belirtilen koşulu
sağlayıp sağlamadığını belirtir. Python 3'ten itibaren UNICODE sisteme
geçilmiş olup metotlar UNICODE tablodaki bütün dillerin harflerini bu testte
dikkate alırlar.

Belli başlı metotlar şunlardır:

```text
isalpha (alfabetik mi?)
isupper (büyük harf mi?)
islower (küçük harf mi?)
isspace (boşuk karakterlerinden mi?)
isalnum (alfanümerik karakter mi?)
```

Örneğin:

```text
>>> 'ankara'.isalpha()
True

>>> 'ankara'.isdigit()
False
```

## Metotların Doğrudan Çağırılması

Pekala bir değişkene string atamadan da metotları çağırabiliriz, ki bunu
birçok yerde zaten yaptım: `'alper'.islower()` gibi

## `join()` Metodu

`9400`

Bu metod argüman olarak dolaşılabilir bir nesne alır. Fakat bu nesne
dolaşıldıkça `str` elde edilmelidir. `join()` metodu, metodu çağıran `str` yi
bu dolaşılabilir nesnenin elemanları arasına sokarak yazıyı birleştirir
ve yeni bir `str` nesnesi elde edilir.

Örnek:

```text
>>> ', '.join(['alper', 'yazar'])
'alper, yazar'
```

## `split()` Metodu

Bu da `join()` metodunun tersi gibidir. Bizden bir ayraç alır ve `str`lerden
oluşan bir liste yapar. Eğer argüman geçmezsek tüm boşluk karakterleri ayraç
olarak kabul edilir.

```text
>>> 'alper,yazar'.split(',')
['alper', 'yazar']

>>> '   ali     veli   \n\n\t \t    selami \t   '.split()
['ali', 'veli', 'selami']
```

## `strip()` Metodu

`9529`

Argümansız çağrılırsa diğer dillerdeki *trim* işlemini yapar, yazının başı ve
sonundaki boşluk karakterlerini atar, yani white space. Argüman geçersek strip
edilecek karakteri belirlemiş oluruz. Argüman birden fazla karakter içeriyorsa
tüm bu karakterler bireysel birer strip karakteri olur.

Örnekler:

```text
>>> '  alper yazar '.strip()
'alper yazar'

>>> '.  alper yazar '.strip()
'.  alper yazar'

>>> '.  alper yazar '.strip('.')
'  alper yazar '

>>> '.  alper yazar '.strip('. ')
'alper yazar'
```

Yani `strip('xyz')` dediğimizde `x`, `y` ve `z` ayrı karakterler olarak
ele alınır.

## `lstrip()` ve `rstrip()`

Left ve Right strip isimli iki metod daha vardır. Bunlar ise yazının sadece
solundaki veya sağındaki karakterler üzerinde işlem yaparlar.

## `partition()` Metodu

Yazı içerisinde aranacak bir yazıyı parametre olarak alır, eğer bulursa üçlü bir
demet ile geri döner. Demetin ilk elemanı yazıda bulunan yerin sol tarafındaki
yazıdan, sonraki elemanın bulunan yazının kendisinden ve sonraki eleman da
bulunan yazının sağ tarafındaki yazıdan oluşur. Eğer yazıyı bulamazsa birinci
eleman yazının tümü ve ikinci ile üçüncü elemanı boş str olan bir string
dönmektedir.

```text
>>> s = 'aliveliselami'

>>> s.partition('veli')
('ali', 'veli', 'selami')

>>> s.partition('hasan')
('aliveliselami', '', '')
```

## `replace()` Metodu

`9672`

Bu metod ile bir yazı içerisindeki belli bir yazıyı başka bir yazı ile
değiştirir. İki parametresi vardır, birincisi aranacak yazı ikincisi de
değiştirilecek yazıyı belirtir.

```text
>>> s = 'ali top at, ali ip atla'

>>> s.replace('ali', 'veli')
'veli top at, veli ip atla'

>>> s = 'ankara ankara güzel ankara seni görmek ister her bahtı kara'

>>> s.replace('a', '')
'nkr nkr güzel nkr seni görmek ister her bhtı kr'
```

Eğer üçüncü bir argüman girersek bu `int` olmak zorundadır. Bu toplamda kaç adet
değişim yapabileceğimizi sınırlar.

```text
>>> s = 'istanbul istanbul güzel istanbul'

>>> s.replace('istanbul', 'ankara', 2)
'ankara ankara güzel istanbul'
```

## `startswith()` Metodu

Yazının istediğimiz yazı ile başlayıp başlamadığını söyler. Geri dönüş değeri
`bool` türündendir.

Örnek:

```text
>>> s = '- bu bir denemedir'

>>> s.startswith('-')
True

>>> s.startswith('- ')
True

>>> s.startswith('- b')
True

>>> s.startswith('- ba')
False
```

## `endswith()` Metodu

`startswith()` metodunun yazının bitip bitmediğini arayan versiyonudur.

## `upper()` ve `lower()` Metodu

Yazıyı büyük harfe ya da küçük harfe çevirir.

```text
>>> 'AnKaRa-06'.upper()
'ANKARA-06'
```

---

Türkçe'de `i`nin UNICODE büyük harf karşılığı `I` biçimindedir. `I`nın da küçük
harf karşılığı `i`dir. Bu yüzden Türkçe karşılığı için sorunlar yaşanabilir.

```text
>>> 'iznik gölü'.upper()
'IZNIK GÖLÜ'
```

Bu problemi önceden `replace()` ederek çözebiliriz:

```text
>>> 'iznik gölü'.replace('i', 'İ').upper()
'İZNİK GÖLÜ'
```

`9799`
