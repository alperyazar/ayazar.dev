---
giscus: 780c29d3-c7ce-44e2-8359-c3af2a79c694
---

# 🦭 Walrus Operatörü, `:=`

`12-00.05.00`

Walrus'un Türkçe karşılığı [Mors](https://tr.wikipedia.org/wiki/Mors) hayvanıdır.
Bu operatöre yandan bakınca morsların dişlerine benzediği için bu isim verilmiştir.

```{figure} assets/mors.jpg
:align: center

Aynı `:=` di mi!
[Kaynak](https://commons.wikimedia.org/wiki/File:Pacific_Walrus_-_Bull_(8247646168).jpg)
[Ayrıca 😄](https://en.wikipedia.org/wiki/I_Am_the_Walrus)
```

Python'a 2019 yılında 3.8 sürümü ile gelmiş bir operatördür. [^1f] Bu atama,
`=`, operatörüne benzer olup farklı olarak bir değer üretir.
[](atama-operatoru.md) yazısında konuştuğumuz, Python'da `=` operatörünün
aslında bir operatör olmaması, bir ifade değil bir deyim oluşturmasının
dezavantajarı `:=` ile ortadan kaldırılmıştır. Sanıyorum ki buna idiomatic C
kodu gibi Python kodu yazmak isteyen programcılar en çok sevinmiştir. *Hoş, dile
2019'da eklenmiş bunca yıl dayanıldıysa artık böyle gitseymiş olmaz mıymış?
Bilmiyorum...*

Walrus operatörü de atama operatörü gibi binary infix bir operatördür.

```python
a = ( b := 5) + 4 # Python 3.8 ile geçerli, b = 5, a = 9 oldu
```

---

`12-00.14.00`

Genel olarak atama operatörü ile işimizi yapamadığımız yerde walrus operatörünü
kullanmamız gerekmektedir. Yani atamadan elde edilen değer kullanılmayacaksa
walrus kullanılamamkatadır.

```text
>>> a := 10
  File "<stdin>", line 1
    a := 10
           ^
SyntaxError: invalid syntax
```

Mesela burada `a := 10` sentaks hatası olmaktadır, sadece `a = 10` diyebiliriz.
Ama yukarıda da gördüğümüz `a = ( b := 5) + 4` ifadesinde `:=` bu kullanım için
gereklidir ve bir hata durumu oluşmaz.

```{note}
Walrus operatöründe niye böyle bir kısıt olduğunu tam olarak bilmiyorum ama
[The Zen of Python](https://peps.python.org/pep-0020/) içerisinde geçen
*There should be one-- and preferably only one --obvious way to do it.* ile
ilgili olabilir. 🤔
```

```text
>>> a := b := 4
  File "<stdin>", line 1
    a := b := 4
           ^
SyntaxError: invalid syntax
```

Burada da atamanın değeri kullanılıyormuş gibi gözükse de aslında `a = b = 4`
ile yapılabileceği için hata oluşmaktadır.

**Walrus operatörü paranteze, `()`, alınırsa her zaman geçerli kabul
edilmektedir.**

```text
>>> a := 4
  File "<stdin>", line 1
    a := 4
          ^
SyntaxError: invalid syntax
>>> (a := 4)
4
```

Çünkü bu bağlamda `()` da adeta bir operatör görevi görmektedir. Öncelik
parantezi dediğimiz şey aslında bir değer üretir. Daha doğrusu *elde edilen
değerin kullanılması* anlamına gelmektedir. O yüzden `(a = 4)` ifadesi
hatalıdır, `()` içerisinde değer üreten bir ifade olması gerekir. Bundan dolayı
`()` içerisinde `:=` gerekli bir kullanım olmaktadır, hata değildir.

```python
b := (a := 4)   # hata
b = (a := 4)    # geçerli
(b := (a := 4)) # geçerli
print(a := 4)   # geçerli, 4 yazdırır, a = 4; print(a) ile eşdeğerdir.
```

---

Elbette walrus operatörünü kullanmak için her zaman parantez, `()`, içine
almak gerekmez. Örneğin `if`, `while` gibi deyimlerde zaten atama operatörü
kullanamadığımız için walrus operatörünü ekstra bir parantez kullanmadan
kullanabiliriz. Örneğin

```python
while x := input():
  pass
```

kodu geçerlidir.

---

Son olarak unutmayalım ki `:=` operatörünün önceliği düşüktür ve uygun yerlerde
öncelik parantezi kullanmamız gerekir. Örneğin:

```python
while (a := int(input('Bir değer giriniz:'))) != 0:
    print(a * a)
```

Bu kod, biz klavyeden `0` değeri girene kadar girdiğimiz sayıların karesini
alacaktır. Ama en dıştaki parantezleri yazmazsak

```python
while a := int(input('Bir değer giriniz:')) != 0:
    print(a * a)
```

operatör önceliğinden dolayı önce `!=` yapılacağından, `a`, `bool` türden bir
değer tutacaktır ve istediğimiz gibi çalışmayacaktır.

[^1f]: <https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions>
