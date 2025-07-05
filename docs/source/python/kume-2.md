---
giscus: 052ec72a-d2c8-45e9-8696-c908bb0781af
---

# Küme, Set Veri Yapısı - 2

`7708`

Kümeler üzerinde çeşitli işlemler yapabiliriz.

## Kesişim - Intersection

İki kümenin ortak elemanlarının bulunması işidir. `intersection()` metodu ile
ya da `&` operatörü ile bu işlemi yapabiliriz.

```python
c = a.intersection(b)
# aynısı:
c = a & b
```

Fakat şöyle bir ufak fark vardır. `&` operatörünün sağ operandı yalnızca *set*
ya da ileride göreceğimiz **frozenset** olmalıdır. Fakat `intersection()`
metodunun parametresi herhangi bir *dolaşılabilir nesne* olabilir. Dolaşılnca
elde edilen değerler bir küme elemanıymış gibi işleme sokulur.

```text
>>> s = {'ali', 10, 'veli', 'eskişehir'}
>>> k = {10, 'eskişehir', 'adana', 20}

>>> s.intersection(k)
{10, 'eskişehir'}

>>> s.intersection(['ali', 'hasan', 10.0])
{'ali', 10.0}

>>> s & k
{10, 'eskişehir'}
```

Mesela aşağıdaki program klavyeden girilen iki sözcüğün ortak karakterini
bulmak için kullanılabilir.

```python
word1 = input('Bir sözcük giriniz:')
word2 = input('Bir sözcük daha giriniz:')

s = set(word1)

result = s.intersection(word2)
print(result)

# ya da
result = set(word1) & set(word2)
```

---

Intersection metoduna birden fazla dolaşılabilir nesneyi argüman olarak
verebiliriz.

```text
>>> s = {'ali', 'veli', 'selami', 'ayşe', 'fatma'}
>>> k = ['ali', 'fatma', 'hüseyin', 'ayşe']
>>> m = ['ayşe', 'ali', 'fatma', 'can']
>>> result = s.intersection(k, m)
>>> result
{'ali', 'ayşe', 'fatma'}
```

Yani aslında `s & k & m` işlemini yapmış olduk.

## Birleşim - Union

`set` sınıfının `union()` metodu ya da `|` operatörü ile iki kümenin birleşimini
elde edebiliriz. Yine `|` operatörünün sağ tarafındaki operand `set` ya da
`frozenset` türünden olabilir. Fakat metodun parametresi herhangi bir
dolaşılabilir nesne olabilir. Metoda birden fazla dolaşılabilir nesneyi argüman
olarak verebiliriz.

```text
>>> s = {'ali', 'veli', 'selami', 'ayşe', 'fatma'}
>>> k = {'ali', 'can', 'veli', 'hüseyin', 'sibel'}

>>> result = s.union(k)
>>> result
{'veli', 'fatma', 'sibel', 'can', 'ayşe', 'ali', 'hüseyin', 'selami'}

>>> result = s | k
>>> result
{'veli', 'fatma', 'sibel', 'can', 'ayşe', 'ali', 'hüseyin', 'selami'}

>>> result = s.union(['kaan', 'ali', 'sacit'])
>>> result
{'veli', 'kaan', 'ayşe', 'fatma', 'ali', 'selami', 'sacit'}

>>> result = s.union(['kaan', 'ali', 'sacit'], ['umut', 'şükran'])
>>> result
{'veli', 'şükran', 'fatma', 'kaan', 'ali', 'sacit', 'umut', 'ayşe', 'selami'}
```

## Fark - Difference

İki kümenin farkını `-` operatörü ile `difference()` metodu ile bulabiliriz.
Yine `-` operatörünün sağ operandı `set` ya da `frozenset` türünden olmalıdır.
Metodun parametresi ile herhangi bir dolaşılabilir nesne olabilir.

```text
>>> s = {'ali', 'veli', 'selami', 'ayşe', 'fatma'}
>>> k = {'ali', 'sacit', 'fatma', 'hüseyin', 'bora'}

>>> result = s - k
>>> result
{'selami', 'ayşe', 'veli'}

>>> result = s.difference(k)
>>> result
{'veli', 'ayşe', 'selami'}
```

Metoda ise birden fazla dolaşılabilir nesne argüman olarak verilebilir.

## Ortak Olmayan Elemanlar - Symmetric Difference

İki kümenin ortak olmayan elemanlarının elde edilmesine *exor* işlemi
denmektedir ve `^` operatörü ile yapabiliriz. Yine bu operatörün sağ operandı
`set` ya da `frozenset` olmalıdır. Fakat `symmetric_difference` metodunun
parametresi herhangi bir dolaşılabilir nesne türünden olabilir.

```text
>>> s = {'ali', 'veli', 'selami', 'ayşe', 'fatma'}
>>> k = {'hüseyin', 'ali', 'sacit', 'selami'}

>>> result = s ^ k
>>> result
{'veli', 'fatma', 'sacit', 'ayşe', 'hüseyin'}

>>> result = s.symmetric_difference(['ali', 'jale', 'mahmut'])
>>> result
{'veli', 'fatma', 'jale', 'mahmut', 'ayşe', 'selami'}
```

**Diğer metotların aksine bu metot tek bir argüman almaktadır.**

## `update`li Versiyonlar

Gördüğümüz temel küme işlemlerinin `update`li versiyonları vardır.

- `a &= b` ya da `a.intersection_update(b)`
- `a |= b` ya da `a.update(b)`
- `a -= b` ya da `a.diffrence_update(b)`
- `a ^= b` ya da `a.symmetric_difference_update(b)`

Operatör versiyonlarının sağ operandı `set` ya da `frozenset` türünden
olmalıdır. Metot olanların ise herhangi bir dolaşılabilir nesne olabilir.
`symmetric_difference_update()` dışındaki metotlar ise birden fazla argüman
alabilmektedir.

Burada başka bir nesne elde edilmez, soldaki nesne değiştirilir.

```text
>>> a = {10, 'ali', 20, 'veli', 'selami', 30}
>>> b = {30, 'veli', 'ayşe', 40, 20, 'fatma'}

>>> id(a)
1956642719552
>>> id(b)
1956642720224

>>> a &= b
>>> id(a)
1956642719552

>>> a
{20, 'veli', 30}
```

Dikkat edersen `union_update()` diye bir metot yoktur, `update()` vardır.

## Alt Küme Kavramı

Bir `a` kümesinin elemanları `b` kümesinde varsa `a` kümesi `b` kümesinin
**subset**i olmaktadır. Bunun tersi üst küme yani **superset**tir. Öz alt küme,
yani **proper subset** ise kendisi dahil olmayan alt kümedir. Her küme
kendisinin alt kümesidir ama öz alt kümesi değildir. Benzer biçimde her küme
kendisinin üst kümesidir ama *öz üst kümesi* değildir.

Alt küme kontrolü `<=` operatörü ile ya da `issubset()` metodu ile
yapılabilmektedir. Yine burada da operatorun sag tarafındakı operand `set` ya da
`frozenset` turunden olabilir. Metodun argumani ise herhangi bir dolasilabilir
nesne olabilir.

Ust kume kontrolu de `>=` ya da `issuperset()` metodu ile yapilabilir. Yine
burada da sag operand `set` ya da `frozenset` turunden olmalidir. Metodun
argumani ise herhangi bir dolasilabilir nesne olabilir.

Oz alt kume ve oz ust kume islemleri icin ise metotlar yoktur, bu islemler
sadece `<` ya da `>` operatorleri ile yapilabilir.

Örneğin:

```text
>>> s = {'ali', 'veli', 'selami', 'ayşe', 'fatma'}
>>> k = {'ali', 'veli', 'selami'}
>>> print(k < s)
True
>>> print(s < s)
False
>>> print(s <= s)
True
```

## Ayrık Küme Kavramı

İki kümenin hiçbir ortak elemanı yoksa bu iki kümeye **ayrık kümeler** yani
**disjoint sets** denmektedir. Bu kontrol `set` sınıfının `isdisjoint()` metodu
ile yapılabilir. Bu metodun parametresi herhangi bir dolaşılabilir nesne
olabilir. Bu işlemin bir operatör karşılığı yoktur. Ama istersek `s && k ==
set()` biçiminde yapabiliriz, yani intersection boş bir set mi dönüyor diye...

```text
a = {10, 20, 30, 40, 50}
b = {100, 200}

result = a.isdisjoint(b)
print(result)       # True
```

`8002`
