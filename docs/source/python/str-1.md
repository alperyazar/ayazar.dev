---
giscus: 0e615794-11df-4b61-9d4b-bb206a400198
---

# `str` Sınıfı ve İşlemleri - 1

`8905`

String yani `str` dediğimiz şey Python'da aslında bir sınıftır, adı da `str`
sınıfıdır. Biz stringleri tek tırnak, iki tırnak, üç tek tırnak ya da üç çift
tırnak ile yarattığımızda aslında `str` sınıfı türünden bir nesne yaratmış
olmaktayız.

`str` sınıfının bir **değiştirilemez, immutable** bi sınıf olduğunu görmüştük.
Yani bir nesne yarattıktan sonra onun üzerinde bir değişiklik yapamayız.

## `str` de Seqeunce Type'tır

Tıpkli listeler, demetler gibi string'ler de Python'da **seqeunce type**
grubundadır. Yani onu oluşturan karakterlerden oluşan bir dizilim gibi
düşünülebilirler.

String'lerin karakterlerine de liste ve demetlerde olduğu gibi `[]` operatörü
ile erişebiliriz. Örneğin

```text
>>> s = 'alper'

>>> s[2]
'p'

>>> type(s[2])
<class 'str'>
```

Python'da, Java ve C# gibi bazı dillerde olduğu gibi tek bir karakteri temsil
eden, `char` gibi, bir tür yoktur. İndeksle eriştiğimiz zaman da yine tek
bir karakter içeren `str` nesnesi elde etmiş oluruz.

String'ler immutable olduğu için indeksle erişsek de değişim yapamayız.

```text
>>> s = 'alper'

>>> s[2] = 'k'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

## `len()` Fonksiyonu

Built-in `len()` fonksiyonu ile bir string'in uzunluğu elde edilebilir.
Örneğin:

```text
>>> s = 'alper'
>>> len(s)
5

>>> k = ''
>>> len(k)
0
```

## Negatif İndeks

Demet ve listelerde olduğu gibi burada da negatif indeks kullanabiliriz.

`8958`

```text
>>> s = 'ankara'

>>> s[-1]
'a'

>>> s[-2]
'r'
```

## Dilimleme, Slicing

String dilimlendiği zaman yine bir string elde ederiz. Dilimlemeyi de demet
ve listelerde olduğu gibi yapabiliriz. Yine `[::-1]` ile ters çevirebiliriz.

```text
>>> s = 'ankara'

>>> s[2:6]
'kara'

>>> s[1:3]
'nk'

>>> s[2:-2]
'ka'

>>> s[::-1]
'arakna'
```

## Stringlerin Toplanması, `+`

İki string'i topladığımız zaman bir string nesnesi yaratılır. Bu string
nesnesi toplanan nesnelerin birleştirilmesi ile oluşturulur.

```text
>>> x = 'alper'
>>> y = 'yazar'
>>> x + y
'alperyazar'
```

Java ve C# gibi dillerde bir string ile başka bir türden nesne toplanabilir.
Python'da ise böyle bir özellik yoktur. Yani Python'da biz `int` ile `str`yi
toplayamayız örneğin. Bu tür durumlarda bizim explicit olarak `str` nesnesine
dönüştürme yapmamız gerekir.

```text
>>> a = 10

>>> 'a = ' + a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

>>> 'a = ' + str(a)
'a = 10'
```

Örneğin `a`yı biz `str`ye elle çevirerek bir `str` ile toplamış olabiliyoruz.

---

String'ler immutable olduğu için biz `s += k` yazsak bile `s`yi uzatmış
olmuyoruz, yeni bir `str` oluşmuş oluyor. Yani `s += k` ile `s = s + k` aynı
anlamdadır string'ler için. Oysa listelerde durum farklıydı, sona ekleme
yapıyordu çünkü listeler değiştirilebilir nesnelerdir.

```text
>>> s = 'alper'
>>> k = 'yazar'

>>> id(s)
547866001712

>>> s += k

>>> s
'alperyazar'

>>> id(s)
547867745008
```

Görüldüğü gibi `s` artık başka bir `str` nesnesini gösteriyor.

## Yineleme - Repetition İşlemi

Liste ve demetlerde oldğu gibi string'lerde de yineleme yani repetition işlemi
yapılabilir. Bu durumda string, `n` defa kendisi ile toplanmış olur.
Eğer çarpılan değer pozitif bir değer değilse boş bir string elde edilir.

Örneğin:

```text
>>> '*' * 10
'**********'

>>> '*' * 0
''

>>> '*' * -4
''
```

`9101`
