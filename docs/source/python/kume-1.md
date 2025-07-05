---
giscus: 87c6a85c-dfba-47d6-b639-a760db0e64d6
---

# Küme, Set Veri Yapısı - 1

`7235`

Matematikte farklı, distinct, elemanların oluşturduğu topluluğa küme yani
**set** denilmektedir. Python'da da bu matematiksel anlamı destekleyecek biçimde
bir küme veri yapısı bulunmaktadır.

Bir küme, *küme parantezleri içerisinde*, eleman listesi girilerek oluşturulur.

```text
>>> s = {'alper', 3, 3.14, True, None}
>>> s
{True, 3, 3.14, 'alper', None}

>>> type(s)
<class 'set'>
```

Kümeler `set` isimli sınıfla temsil edilir.

---

**Kümelerde elemanlar arasında öncelik ve sonralık ilişkisi yoktur.**
Kümelerde sıra yoktur, matematikte olduğu gibi. Yani biz küme elemanlarına
`[]` ile erişemeyiz ya da dilimleyemeyiz. Yukarıda da sıranın bozulduğunu
görebilirsiniz.

---

Kümeye var olan bir elemanı tekrar tekrar yazmak bir exception oluşturmaz,
eklenmez.

```text
>>> s = {1, 2, 2, 3, 4, 4, 5, 1, 5, 4, 4}
>>> s
{1, 2, 3, 4, 5}
```

Küme veri yapısı bu özelliğinden dolayı *yinelenleri ortadan kaldırmak* amaçlı
sıklıkla kullanılmaktadır.

## Boş Küme Oluşturma

Boş bir küme olabilir ama `{}` ile oluşturulmaz, böyle yaparsak boş bir sözlük
yani dictionary oluşur, buna daha sonra bakacağız.

```text
>>> type({})
<class 'dict'>
```

Bu dilin bir tasarımıdır, bu tercih edilmiştir. Sözlükler, tipik olarak dilde
kümelere göre daha fazla kullanılır.

Boş kümeyi `set()` fonksiyonunun argümansız çağrılması ile elde edebiliriz.

```text
>>> type(set())
<class 'set'>
```

## `set()` Fonksiyonu

Bu fonksiyon önceki gördüğümüz nesnelerin fonksiyonları gibi bizden
dolaşılabilir bir nesne alıp o nesneyi dolaşarak o değerlerden bir küme
oluşturabilir.

```text
>>> x = set('alper')
>>> x
{'r', 'l', 'p', 'e', 'a'}
```

---

**Kümeler de iterable yani dolaşılabilir nesnelerdir.** Dolaşınca onun
elemanlarını elde ederiz. Tabii hangi sırada elde edeceğimiz belli değildir.

## `in` ve `not in` Operatörleri

Bir elemanın küme içerisinde varlığını bu operatörler ile test edebiliriz.
Kümeler arka planda genelde **hash table** ya da **binary tree** olarak
gerçekleştirilir. Örneğin CPython **hash table** kullanır. Bu yüzden kümelerde
*var mı yok mu* testleri liste ve demetlere göre çok daha hızlı yapılır. Duruma
göre bunu aklımızda tutabiliriz. Liste ve demetlerde ise *sequential search*
kullanılır.

## Hashlenebilirlik ve Kümeler

Bir `set` nesnesinin oluşturulabilmesi için elemanlarının hashlenebilir olması
gerekmektedir. O yüzden **listeler bir küme elemanı olamaz.**

```text
>>> x = {1, 2, [3, 4]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

Demetin de hashlenebilir olması için gördüğümüz üzere, birkaç ders önce,
tüm elemanlarının hashlenebilir olması gerekir.

**Fakat kümelerin kendisi hashlenebilir değildir.**

O yüzden bir küme, bir kümenin elemanı olamaz fakat demet olabilir. Elbette
demet hashlenebilir değilse, örneğin içinde liste varsa problem olur.

```text
>>> x = {1, 2, {3, 4}}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'

>>> x = {1, 2, (3, 4)}

>>> x = {1, 2, (3, 4, [5, 6])}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

## Karşılaştırmaya Dikkat ❗

Bir elemanın bir kümede olup olmadığı `==` karşılaştırması ile belirlenir.
Şunu hatırlayalım:

```text
>>> 1 == True
True

>>> 1.0 == 1
True
```

İşte `True` gibi bir elemanı kümeye eklerken dikkatli olmak lazım.

```text
>>> print({1, 'alper', True})
{1, 'alper'}
```

Burada kümeye `True` eklenmemiştir çünkü kendisi zaten "vardır" (sanıyorum
diğerlerinden biri de gidebilirdi yoksa sıralı olacağı garanti mi? 🤔)

`float` ve `int` arasında da benzer durumlar olabilir:

```text
>>> print({1, 'alper', 1.0})
{1, 'alper'}
```

## Kümeler değiştirilebilir ❗

Kümeler yani sets değiştirilebilir yani mutable türlerdir.

## `add()`

```text
>>> s = {1, 2}
>>> s.add(3)
>>> s
{1, 2, 3}
```

Hatırlayalım ki listelerde sona ekleme diye bir şey vardı ve biz `append()` ile
bunu yapıyorduk. Kümelerde baş, son gibi kavramlar olmadığı için *append*
sözcüğü yerine, *ortaya oralara bir yere ekleme* anlamında olan `add()`
kullanılmaktadır.

## `update()`

Bir grup elemanı tek seferde eklemek için kullanılır. Listelerdeki `extend()`
metoduna bu açıdan benzer, elbette burada baş ve son ilişkisi yoktur. Bu
metot, dolaşılabilir bir nesneyi parametre olarak alır ve dolaşıp elde
ettiği değerleri kümeye ekler.

```text
>>> s = {1, 2}
>>> s.update('alper')
>>> s
{1, 2, 'r', 'l', 'p', 'e', 'a'}
```

## `remove()`

Kümedeki bir elemanı silmek için kullanılır. Eğer eleman yoksa `KeyError`
exception oluşur.

```text
>>> s = {10, 20, 30}
>>> s.remove(20)
>>> s.remove(20)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 20
```

gibi...

## `discard()`

Bu metot da `remove()` ile aynı çalışır fakat eleman yoksa exception oluşturmaz.

```text
>>> s = {10, 20, 30}

>>> s.discard(20)

>>> s
{10, 30}

>>> s.discard(20)
>>>
```

## `pop()`

Bir de bu metot vardır. Kümede sıra kavramı olmadığı için bize gelişigüzel
bir elemanı siler ve sildiği elemanı bize geri dönüş değeri olarak verir.
Küme boş ise `KeyError` exception oluşur.

```text
>>> s = {10, 20, 30}

>>> s.pop()
10

>>> s.pop()
20

>>> s.pop()
30

>>> s.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pop from an empty set'
```

```{note}
Listelere kıyasla kümelerde silme işlemi daha hızlıdır. Listede silme yaparken
**kaydırma** yani **shrink** işlemi yapılır. Kümelerde ise buna gerek yoktur,
arka planda hash tabloları ile tutulduğu için silme çok hızlı olur.
```

## `clear()`

Tüm elemanları silmek için kullanılan bir metottur, parametre almaz.

## `copy()`

Bir set'in kopyasını çıkarmak için yapılır. Yine burada **shallow copy** yani
**sığ kopyalama** yöntemi kullanılır.  Diğer veri türlerinde olduğu gibi
kümelerde de adres tutarlar ve kopyalama sırasında bu adresler kopyalanır.

`7706`
