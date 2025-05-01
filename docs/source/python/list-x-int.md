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

`16-1.47.30`
