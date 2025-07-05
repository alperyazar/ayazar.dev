---
giscus: 22f295a0-b9c6-4ac8-b1ab-536342aeb91b
---

# Sözlük, Dictionary Veri Yapısı - 1

`8108`

Sözlükler yani dictionaries *anahtar-değer* çiftlerini tutan ve anahtar değeri
verildiği zaman hızlı bir biçimde değer'in bulunmasını sağlayan veri
yapılarıdır. Bunun olabilmesi için arka planda bu doğrultuda organize edilmiş
veri yapıları ve algoritmalar bulunur. Burada genelde **hash tables**,
**balanced binary tree**, **sorted arrays** gibi veri yapıları kullanılır.
CPython ise kümelerde olduğu gibi sözlüklerde de *hash tables* tercih eder.

## Sözlüklerin Yaratılması

Sözlükler kümeler gibi yaratılır, `{}` kullanarak. Fakat bu sefer
`anahtar:değer` şeklinde bir formda veririz. Şöyle ki:

```text
{anahtar:değer, anahtar:değer, anahtar:değer}
```

```python
d = {'ankara': 6, 'istanbul': 34, 'eskişehir': 26, 'izmir': 35, 'denizli': 20}
```

---

Sözlükler `dict` isimli sınıfla temsil edilir.

```text
>>> x = {'alper':'yazar'}
>>> type(x)
<class 'dict'>
>>> x
{'alper': 'yazar'}
```

## Anahtarlar

Sözlüklerde anahtarların hashlenebilir olması gerekmektedir. Değerler için ise
böyle bir koşul yoktur. Bu yüzden anahtarlar `int`, `float`, `str` gibi
türlerden olabilir ama `list` ve `set` türünden olamaz. `tuple` ve `frozenset`
ise eğer elemanları hash'lenebilir ise hash'lenebilir olmaktadır.

```text
>>> d = {[10, 20]: 100}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

>>> d = {(10, 20): 100}
>>> d
{(10, 20): 100}
```

Anahtar ve değerlerin aslında aynı sözlük içerisinde aynı türden olmasına gerek
yoktur. Ama pratikte genelde aynı türden olmaktadır.

```python
d = {'ali': 100, 200: 'veli', 20: 30.2} # geçerli
```

## Hashlenebilirlik

**Sözlükler hashlenebilir değildir.** O yüzden bir sözlük anahtar olamaz. Ama
değerler sözlük olabilir.

```text
>>> d = {'içanadolu': {'eskişehir': 26, 'konya': 42, 'ankara': 6},
         'ege': {'izmir': 35, 'aydın': 9},
         'marmara': {'istanbul': 34, 'kocaeli': 41}} # geçerli
```

## Değişkenler ve Sabitler

Liste, demet, küme ve sözlüklerin elemanları sabit olmak zorunda değildir, bunu
hatırlatma olarak ekleyelim. Elemanlar değişken olarak da verilebilir. Zaten biz
bir sabit oluşturduğumuzda o sabit için önce bir nesne yaratılmakta sonra o
nesnenin adresi kullanılmaktadır. Bunu doğrudan yapmak ile dolaylı yapmak
arasında bir fark yoktur.

```python
x = 26
d = {x: 'eskişehir'}

# ya da

d = {26: 'eskişehir'}
```

Hatırlarsan atama işlemini kolaylık olsun diye operatör gibi ele almıştık ama
aslında atama bir deyimdir. O yüzden `a = [x = 10 + 20, 20]` ifadesi geçerli
değildir. Ama burada Walrus operatörünü kullanabiliriz.

```text
>>> a = [x = 10 + 20, 20]
  File "<stdin>", line 1
    a = [x = 10 + 20, 20]
           ^
SyntaxError: invalid syntax
>>> a = [x := 10 + 20, 20]

>>> a
[30, 20]

>>> x
30
```

## `dict` Sınıfı

Sözlükler `dict` sınıfı ile temsil edilir. Diğer veri yapılarında olduğu gibi
`dict()` fonksiyonu ile sözlük nesnesi yaratabiliriz, `d = dict()` gibi.

Kümeler kısmında da konuştuğumuz gibi boş `{}` bir boş küme değil boş sözlük
yaratmaktadır. Boş küme için `set()` kullanmalıyız demiştik.

---

## `dict()` Fonksiyonu

Eğer `dict()` fonksiyonuna biz iki elemanlı dolaşılabilir nesnelerde oluşan bir
dolaşılabilir bir nesneyi argüman olarak verirsek, `dict()` fonksiyonu bu
nesneyi dolaşır. Her dolaşımda iki elemanlı bir dolaşılabilir nesne elde eder. O
iki elemanlı nesneyi de dolaşarak *ilk elemanı anahtar*, *ikinci elemanı değer*
olarak bir sözlük nesnesi oluşturur.

```text
>>> a = [('ali', 10), ('veli', 20), ('selami', 30), ('ayşe', 40), ('fatma', 50)]
>>> d = dict(a)
>>> d
{'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}
```

Örneğin burada `a` bir `list` yani dolaşılabilir bir nesne. Her elemanı da bir
`tuple` ve o da bir dolaşılabilir nesne. Sonuçta görünen değerler bir sözlük
oluşur.

Ama farklı şeyler de yapabiliriz tabii ki

```text
>>> a = (['selami', 30], ('ayşe', 40), ['fatma', 50], 'ak', 'tk', 'xy', range(2))
>>> d = dict(a)
>>> d
{'selami': 30, 'ayşe': 40, 'fatma': 50, 'a': 'k', 't': 'k', 'x': 'y', 0: 1}
```

Eğer dolaşılabilir nesnenin elemanları, iki elemandan daha fazla eleman içeren
dolaşılabilir nesneler ise bu durumda `ValueError` exception oluşur.

```text
>>> d = dict([('ali', 10), ('veli', 20, 30)])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: dictionary update sequence element #1 has length 3; 2 is required
```

`8321`

Aşağıdaki örnekler gibi farklı şekilde de dictionary oluşturabiliriz. Yeter ki
dolaşılabilir nesneler olsun.

```text
>>> a = [('ali', 10), ('veli', 20), ('selami', 30), ('ayşe', 40), ('fatma', 50)]>>> d = dict(a)
>>> d
{'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

>>> a = [['ali', 10], ['veli', 20], ['selami', 30], ['ayşe', 40], ['fatma', 50]]>>> d = dict(a)
>>> d
{'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}
```

---

`dict()` fonksiyonuna `değişken=değer` biçiminde argümanlar girersek fonksiyon
bize o değişkenin string halini *anahtar*, `=` operatörünün sağındakileri de
değer yaparak bize bir sözlük nesnesi oluşturur.

```{note}
Demek ki içeride bir yerde *stringify* yapabiliyoruz.
```

Örnek:

```text
>>> d = dict(x=10, y=20, z=30)
>>> d
{'x': 10, 'y': 20, 'z': 30}
```

Bu biçimde sözlük nesnesi oluşturma işlemi pek yaygın değildir. Burada değişken
ismi yerine başka bir şey getirilemez.

```text
>>> d = dict('ali'= 10, 'veli'=20, 'selami'=30)
  File "<stdin>", line 1
    d = dict('ali'= 10, 'veli'=20, 'selami'=30)
             ^
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

>>> d = dict(10='ali', 20='veli', 30='selami')
  File "<stdin>", line 1
    d = dict(10='ali', 20='veli', 30='selami')
             ^
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
```

Her ikisinde de hata aldık.

## Sözlük Nesnesinden Sözlük Nesnesi Oluşturma

`dict()` fonksiyonunu bu amaçla da kullanabiliriz.

```text
>>> d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}
>>> k = dict(d)

>>> d
{'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}
>>> k
{'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

>>> id(d)
548591851648
>>> id(k)
548591852736
```

## Değerlerin Elde Edilmesi

`[]` operatörü ile anahtar verip o anahtara karşılık gelen değeri elde
edebiliriz. Eğer ilgili anahtar sözlükte yoksa `KeyError` exception oluşur.

```text
>>> d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

>>> d['ayşe']
40

>>> d['fatma']
50

>>> d['alper']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'alper'
```

---

Elbette sözlüklerde anahtar ve değerlerin türleri aynı olmak zorunda değildir.

```text
>>> d = {'ali': 10, 20: 'veli', 1.5: 'selami'}
>>> d['ali']
10
>>> d[20]
'veli'
```

## `get()` Metodu

`dict` sınıfının `get()` isimli metodu da anahtar değerden değer bulmak için
kullanılır. Fakat ilgili anahtar yoksa bu sefer exception oluşmaz. Eğer ikinci
parametre geçersek, bu opsiyoneldir, bulunamadığı durumda bize bu değeri geri
döner.

Örneğin:

```text
>>> d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

>>> d.get('ayşe')
40

>>> d.get('sacit')

>>> d.get('ayşe', 'bulunamadı')
40

>>> d.get('sacit', 'bulunamadı')
'bulunamadı'

>>> d.get('sacit', 3.14)
3.14
```

```{important}
Sözlüklerde değer üzerinden anahtar değer araması yapılamaz. Yani değer
verilerek anahtar elde edilemez.
```

## `in` ve `not in` Operatörleri

Belli bir anahtarın sözlükte olup olmadığını anlamak için kullanılır. Kümelerde
olduğu gibi burada da bu operatörler hızlı çalışır. Buradan değer elde
edemeyiz.

```text
>>> d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

>>> 'ayşe' in d
True

>>> 20 in d
False

>>> 20 not in d
True
```

## `len()` Fonksiyonu

`8495`

Python'daki built-in `len()` fonksiyonu ile sözlük nesnesinin içerisinde kaç
tane anahtar-değer çifti olduğunu öğrenebiliriz.

```text
>>> d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}
>>> len(d)
5

>>> d = {}
>>> len(d)
0
```

## Sözlükler Dolaşılabilir Nesnelerdir

Sözlükler de iterable yani dolaşılabilir nesnelerdir. Bir sözlük nesnesi
dolaşıldığında yalnızca *anahtar* değerler elde edilir.

```{important}
Python 3.6'ya kadar (sanıyorum dahil) bu dolaşım sırasında anahtarlar rastgele
sırada elde edilebiliyordu. Fakat sonrasında sözlük nesneleri dolaşıldığı zaman
anahtarların eklenme sırası ile elde edileceği garanti edildi.
```

Örnek:

```text
>>> d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

>>> list(d)
['ali', 'veli', 'selami', 'ayşe', 'fatma']
```

Bu örnekte `list()` fonksiyonu dolaşılabilir bir nesne aldı fakat sadece
anahtar değerlerden bir liste elde etmiş olduk.

````{note}
`dict()` fonksiyonunu işlerken elemanlarının da dolaşılabilir olması
gerektiğinden bahsettik. Fakat şimdi sözlüklerin dolaşılınca sadece
anahtarlarının elde edildiğini söyledik. Oysa ki `dict()` ile bir sözlükten
başka sözlük elde edebiliyorduk. Yani `dict()`e sözlük verince farklı bir
durum mu oluşuyor?

Mesela
[Python dokümanlarında](https://docs.python.org/3/library/stdtypes.html#dict)
şöyle verilmiş:

```text
class dict(**kwargs)
class dict(mapping, **kwargs)
class dict(iterable, **kwargs)
```

Belki henüz anlayamadığım bir şeyler var?
````

## Sözlükler Değiştirilebilir, Mutable, Türlerdir

`8536`

Bir sözlüğe yeni bir anahtar-değer çifti ekleyebiliriz ya da silebiliriz. Mevcut
bir anahtarın karşılığı olan değeri değiştirebiliriz.

Bir sözlükte anahtarlar **unique** yani **tekil** konumdadır. Bir anahtardan
birden fazla olamaz. Yeni bir anahtar-değer çiftini aynı değer ile eklersek
önceki değer değiştirilmiş olur.

```text
>>> d = {'ali': 10, 'veli': 20, 'selami': 30, 'ali': 40, 'selami': 50}
>>> d
{'ali': 40, 'veli': 20, 'selami': 50}
```

Burada `ali` ve `selami` den iki adet eklememize rağmen teke düştüler.

---

Sözlüğe yeni bir anahtar-değer çifti eklemenin en kolay yolu `d[key] = value`
şeklinde bir atama yapmaktır. Var olan bir `key` ise değeri değişir, yoksa
eklenir.

```text
>>> d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

>>> d['sacit'] = 60
>>> d
{'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50, 'sacit': 60}

>>> d['sacit'] = 100
>>> d
{'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50, 'sacit': 100}
```

## Birden Fazla Anahtar-Değer Ekleme

Bunun için `update()` metodunu kullanabiliriz. Bu metod, `dict()` fonksiyonunun
kabul ettiği tarzda argümanlar almaktadır. Yani dolaşılabilir bir nesne
verilmeli ve dolaşım sonucunda elde edilen nesnelerin kendileri de iki elemanlı
dolaşılabilir nesneler olmalıdır. Yine `dict()` metodunda olduğu gibi ilk
nesne anahtar, ikincisi ise değer olmaktadır. Eğer anahtar halihazırda var ise
ekleme yapılmaz, güncelleme yapılır.

```text
>>> d = {'ali': 10 }

>>> d
{'ali': 10}

>>> d.update([('sacit', 100), ('mehmet', 200), ('sibel', 300)])

>>> d
{'ali': 10, 'sacit': 100, 'mehmet': 200, 'sibel': 300}
```

## Sözlükten Silme Yapılması

Bunun için `pop()` isimli metod kullanılabilir. Bizden anahtar alır ve ilgili
çifti siler. Silinen değeri de geri dönüş değeri olarak bize verir.

Eğer `pop()`u tek argüman ile çağırmışsak ve ilgili anahtarı bulamazsa
`KeyError` exception oluşur. İki argümanla çağırırsak ise böyle bir durumda
exception oluşmaz, bize ikinci argümanı verir.

Örnek:

```text
>>> d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

>>> d.pop('selami')
30

>>> d
{'ali': 10, 'veli': 20, 'ayşe': 40, 'fatma': 50}

>>> d.pop('sibel')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'sibel'

>>> d.pop('sibel', 'anahtar yok')
'anahtar yok'
```

`8647`
