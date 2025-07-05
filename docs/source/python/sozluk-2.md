---
giscus: cf02c626-de03-41a7-9823-184c502d6b7c
---

# Sözlük, Dictionary Veri Yapısı - 2

`8647`

## `keys()` ve `values()` Metodu

Bir sözlüğün tüm anahtarlarını `keys()` metodu ile elde edebiliriz. Benzer
şekilde `values()` metodu ile de değerleri alabiliriz. Her iki nesne de
dolaşılabilir nesneler vermektedir.

```text
>>> d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

>>> d
{'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

>>> list(d.keys())
['ali', 'veli', 'selami', 'ayşe', 'fatma']

>>> list(d.values())
[10, 20, 30, 40, 50]
```

Önceki kısımlarda konuştuğumuz gibi Python 3.6 ve sonrasında anahtar ve değerler
eklenme sırası ile gelmektedir. Öncesinde ise bu garanti edilmez.

Burada zaten `keys()` metodu çok da gerekli değildir çünkü biz bir sözlük
nesnesini dolaştığımız zaman zaten anahtarları elde ederiz. `values()`
bu açıdan daha *değerlidir.*

Örneğin aşağıda dolaşınca zaten anahtarları elde ettik:

```text
>>> d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

>>> list(d)
['ali', 'veli', 'selami', 'ayşe', 'fatma']
```

---

Bu iki metod ile elde edilen nesneler **dolaşılabilir** nesnelerdir yani
iterable, dolaşım yani iterator nesneleri değillerdir. Bir kere dolaşınca
bitmezler. Örneğin:

```text
>>> d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

>>> list(d.values())
[10, 20, 30, 40, 50]

>>> list(d.values())
[10, 20, 30, 40, 50]
```

## `view` Nesneleri

`8694`

Python'da *view nesnesi* kavramı karşımıza çeşitli konularda çıkmaktadır.
`keys()` ve `values()` metodlarının bize verdiği dolaşılabilir nesneler aynı
zamanda *view* nesneleridir. Yani biz bu metodlarla dolaşılabilir nesneleri elde
edince ana nesne yani sözlük üstüne yapacağımız ekleme ve silme gibi işlemleri
yaptığımızda daha önce elde ettiğimiz view nesnesi son duruma ilişkin bir
dolaşım sağlar.

Örnek:

```text
>>> d = {10: 'ali', 20: 'veli', 30: 'selami', 40: 'ayşe', 50: 'fatma'}

>>> d
{10: 'ali', 20: 'veli', 30: 'selami', 40: 'ayşe', 50: 'fatma'}

>>> x = d.keys()
>>> x
dict_keys([10, 20, 30, 40, 50])

>>> list(x)
[10, 20, 30, 40, 50]

>>> d[60] = 'alper'
>>> list(x)
[10, 20, 30, 40, 50, 60]
```

Burada `x`i elde ettikten sonra `d` nesnesini güncelledik. Ondan sonra `x`i
tekrar elde etmemiş olsak da `x`in de güncellendiğini gördük.

## `items()` Metodu

Bu metod da bize bir *view nesnesi* verir. Bu nesneyi dolaştığımız zaman
anahtar-değer çiftleri iki elemanlı demetler, tuple, biçiminde elde edilir.

```text
>>> d = {10: 'ali', 20: 'veli', 30: 'selami', 40: 'ayşe', 50: 'fatma'}

>>> x = d.items()

>>> list(x)
[(10, 'ali'), (20, 'veli'), (30, 'selami'), (40, 'ayşe'), (50, 'fatma')]

>>> d[60] = 'alper'

>>> list(x)
[(10, 'ali'), (20, 'veli'), (30, 'selami'), (40, 'ayşe'), (50, 'fatma'), (60, 'alper')]
```

Burada öncelikle `x`ten bir `list` oluşturduk ama `d`yi güncelleyince `x` de
otomatik olarak güncellendi.

Yine `items()` ile çiftlerin eklenme sırasına göre elde edileceği garantisi
Python 3.6 ile gelmiştir.

## `clear()` Metodu

`8787`

Bu metod sözlüğün içerisindeki çiftlerin hepsini siler.

Örnek:

```text
>>> d = {10: 'ali', 20: 'veli', 30: 'selami', 40: 'ayşe', 50: 'fatma'}

>>> id(d)
548398352384
>>> d.clear()
>>> d
{}

>>> id(d)
548398352384
```

## `copy()` Metodu - Shallow Copy

Bu metod ile sözlüğün bir kopyasını çıkartırız. Bu yine *sığ kopya* yani
*shallow copy* olacaktır. Yani value'ların id değerleri aynı olacaktır.

Örnek:

```text
>>> d = {10: 'ali', 20: 'veli', 30: 'selami', 40: 'ayşe', 50: 'fatma'}

>>> id(d)
548398352384

>>> x = d.copy()

>>> id(x)
548397374016

>>> x
{10: 'ali', 20: 'veli', 30: 'selami', 40: 'ayşe', 50: 'fatma'}

>>> x[10] is d[10]
True

>>> x is d
False
```

Burada görüldüğü gibi her iki sözlüğün `id` değerleri farklı olsa da yani
farklı sözlükler olsalar da, elemanlar aynı elemanlardır.

## `setdefault()` Metodu

`8836`

Daha önce sözlükten değer elde etmek için iki yol görmüştük: `[]` operatörü ve
`get()` metodu. Aslında bu metod da bu işe yarayabilir. Bu metod bize ilgili
anahtarın değerini verir. Eğer anahtar bulamazsa bu metod o anahtarı bizim
verdiğimiz değerle sözlüğe ekler ve bize yine bu değeri verir. Bu şekilde
iki argüman geçmek zorunda değiliz, tek argüman da geçebiliriz. Eğer ikinci
argüman girmezsek bu sefer sözlüğe o anahtar için `None` değerini ekler.
Bu durumda bize `None` değerini geri döner. Eğer sözlükte anahtar değer bulunursa
ikinci argüman etkisiz olmaktadır.

```text
>>> d = {10: 'ali', 20: 'veli', 30: 'selami'}

>>> d.setdefault(20, 'kaya')
'veli'

Yukarıda zaten 20 anahtarlı veli olduğu için kaya'nın anlamı yok.

>>> d
{10: 'ali', 20: 'veli', 30: 'selami'}

>>> d.setdefault(60, 'kaya')
'kaya'

Yukarıda 60 anahtarla kimse olmadığı için kaya'yı ekledi ve döndü.

>>> d
{10: 'ali', 20: 'veli', 30: 'selami', 60: 'kaya'}

>>> d.setdefault(30)
'selami'

>>> d
{10: 'ali', 20: 'veli', 30: 'selami', 60: 'kaya'}

>>> d.setdefault(70)

Aslında None döndü

>>> d
{10: 'ali', 20: 'veli', 30: 'selami', 60: 'kaya', 70: None}
```

## `del` Deyimi

`pop()` metodu ile anahtar-değer çifti silebiliyoruz. Bunu `del` deyimi ile de
yapabiliriz. Burada elemana erişiyormuş gibi silebiliriz, `del d[10]` gibi.

Eğer anahtar yoksa `KeyError` exception oluşur.

Örnek:

```text
>>> d = {10: 'ali', 20: 'veli', 30: 'selami', 40: 'ayşe', 50: 'fatma'}

>>> del d[40]

>>> d
{10: 'ali', 20: 'veli', 30: 'selami', 50: 'fatma'}

>>> del d[41]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 41
```

`8905`
