---
giscus: 09af55d3-4720-4f05-b388-98cc406b5fbc
---

# `list` * `int`

`16-1.27.30`

Bir `list` ile `int` bir değer çarpılabilir ama bölünemez. Öte yandan iki `list`
kendi arasında çarpılamaz, bölünemez ve çıkartılamaz.

`list * int` ve `int * list` geçerlidir yani operandlar kendi arasında yer
değiştirebilir. Bu işleme Python'da **yineleme** yani **repetition**
denmektedir.

`a` bir `list` ve `n` bir `int` belirtmek üzere `a * n` ile `n * a` tamamen aynı
anlamda olup *`a` yı kendisiyle `n` kere toplama* anlamına gelmektedir.
Yani `a* 3` aslında `a + a + a` ile aynı anlamdadır.
**Listeler toplanırken listelerin
elemanlarında tutulan adreslerin kopyalandığını** tekrar hatırlayalım.

Örneğin:

```text
>>> x = [1, 2]
>>> y = x * 3

>>> y
[1, 2, 1, 2, 1, 2]

>>> y[0] is y[2] is y[4]
True
```

```{figure} assets/int-x-list-0.png
:align: center

Yine bir *shallow copy* durumu vardır.
```

---

Bu özellik örneğin her elemanı `0` olan `100` elemanlı bir listenin
oluşturulması için kullanışlı olmaktdır. `a = [0] * 100` ile yapabiliriz
örneğin. Elbette bu durumda önce gördüğümüz gibi tüm elemanlar aynı `0` değerli
`int` nesnesini göstermektedir. Bu bir problem oluşturmaz, çünkü `int`
*immutable* olduğu için herhangi bir değer güncellemesinde o eleman yeni bir
`int` nesnesini gösterecektir, diğer elemanların değerleri bu durumdan
etkilenmez.

---

Eğer çarpılan `int` nesnesinin değeri negatif ya da `0` ise yineleme işleminden
boş bir liste elde edilir.

```text
>>> x = [1, 2, 3]

>>> x * 0
[]

>>> x * -1
[]
```

---

`16-2.07.05`

Peki `x` bir liste ise `x * 2 * 3` geçerli midir? Çarpma işlemi soldan-sağa
öncelikli olduğu için önce `x * 2` yapılacak ve bir liste elde edilecek ve
sonra bu yeni liste `3` ile çarpılacak, nihai liste elde edilecek. Ama günün
sonunda efektif olarak `x * 6` etkisini göreceğiz aslında.

Yani Python'da çarpmanın **değişme** yani **commutative**  ve **birleşme** yani
**associative** özelliği korunmuştur. Yukarıdaki işlem `3 * 2 * x` ile
eşdeğerdir.

---

`16-2.11.40`

Listelerde `a = a * n` ile `a *= n` aynı anlama **gelmemektedir.** Toplamada da
böyle değildi hatırlarsınız. `a = a * n` işleminde yeni bir liste yaratılır
ve `a` bunu gösterir. Ama `a *= n` işleminde `n - 1` tane `a`, `a`nın sonuna
yerleştirilir.

```text
>>> x = [1, 2]

>>> id(x)
133419689011904
>>> x = x * 3

>>> x
[1, 2, 1, 2, 1, 2]

>>> id(x) # farklı bir liste
133419689170368
```

AMA

```text
>>> x = [1, 2]

>>> id(x)
133419689011904

>>> x *= 3

>>> x
[1, 2, 1, 2, 1, 2]

>>> id(x)  # aynı x listesi
133419689011904
```

`16-2.16.30`

`16-1.47.30`
