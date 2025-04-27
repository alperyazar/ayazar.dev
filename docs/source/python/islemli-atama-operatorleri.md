---
giscus: 3952acd5-f2b4-4894-b9bf-fcc240204442
---

# İşlemli Atama "Operatörleri", `+=`, `*=` vb

`12-00.31.00`

Önceki notlarda belirtmiştim ama bu konu başlığı altında tekrar vurgulamak
istiyorum. **C gibi dillerin aksine, Python'da `++` ve `--` operatörleri
yoktur.** Olan dillerde bu operatörleri bir değişkenin değerini bir arttırmak
ya da eksiltmek için kullanıyoruz. Python'da ise bunu yapmanın iki yolu vardır.
Birincisi:

```python
x = x + 1
y = y - 1
```

kullanmak.

İkincisi ise bu yazının konusu olan **işlemli atama operatörleri** yani
**augmented assignment statements** (işlevi arttırlmış anlamdında, C'de mesela
*compound assignments* diyoruz) kullanmaktır. Dikkat ederseniz başlıkta
`"Operatör"` yazıyor. Python'da atama işlemi nasıl bir deyim ise, yani aslında
`=` bir operatör değil ve ifade oluşturmuyorsa işlemli atama operatörleri de
aslında operatör değildir, onlar da `=` gibi birer deyim yani statement
oluşturur. Ama anlarken kolaylık olsun diye nasıl atama operatörü dediysek
bunlara da operatör diyoruz kolaya kaçıp. Bu operatörler de atama operatörü
gibi bir değer üretmezler.

İşte ikinci yol da şu olmaktadır:

```python
x += 1
y -= 1
```

```{note}
Python'da neden `++` ve `--` operatörlerinin olmadığı ile ilgili internette
tartışmalar vardır, örneğin [burası](https://stackoverflow.com/a/3654936/1766391).
Temel söylenen Python'daki programlama şekli yani *Pythonic* tarzda kod yazarken
C gibi dillerin aksine bu operatörlere ihtiyaç duyulmamasıdır. Örneğin Python'da
bulunan `range()` fonksiyonunun yaygın kullanılması ve `i++` gibi işlemlere
bu yüzden ihtiyaç duyulmaması gibi. Elbette bu olsa hiç işe yaramazdı demek değil
ama eksikliğini çok fazla hissediyorsak yazdığımız kodlara bakıp, *Pythonic way*
de miyiz diye kontrol etmek iyi olabilir.

C dili ile uğraştıysanız `++` ve `--` operatörleri yan etki, side effect, ten
dolayı bazen size göremediğiniz sürprizler yapabiliyor. Python'daki olmayış,
programcının hata yapmasını bir nebze azaltıyor diyebiliriz.
Mesela Swift dilinde de bu operatörler varmış ama versiyon 2 ile beraber
dilden çıkartılmış.

Python da biraz fonksiyonel programlama tarzını daha çok benimsediği için
görece, bu tarz yan etki yaratan operatörleri barındırmama tercih edilebiliyor.
```

---

Python'da `+=`, `-=`, `*=`, `/=`, `//=`, `%=` şeklinde işlemli atama "operatörü"
bulunmaktadır. Burada arada boşluk olmamalıdır, `* =` geçerli değildir örneğin.
Bu operatörler binary infix operatörlerdir. `op` bir operatör dersek

```text
a op= b
```

bu ifade

```text
a = a op b
```

ile eşdeğer olmaktadır.

```{important}
Python'da `a op= b` ile `a = a op b` nin denk olmadığı bazı durumlar vardır,
örneğin listelerin toplanması. Buradaki eşdeğerlik daha genel geçer bir
kavramdır, istisna durumları vardır: Bknz: [](listelerin-toplanmasi.md)
```

Ben yukarıda tüm kombinasyonları yazmadım. Tam liste için [dilin referans
açıklamasına](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-augmented_assignment_stmt)
bakabilirsiniz. Birçok operatörün bu formu bulunsa da örneğin `and`, `or`, `not`
gibi operatörlerin bu şekilde işlemli biçimi yoktur.

---

Python'da bir değişkeni arttırmak için tercih edilen yöntem gerçekten de
`a += 1` şeklinde işlemli atama operatörü kullanmaktır. Elbette bu tarz işlemli
atama operatörleri burada olduğu gibi temel bir veri türü olan `int` gibi
değiştirilemez yani immutable türlerle kullanıldığında bu işlem arka planda
yeni nesne oluşmasına sebep olur.

```text
>>> a = 4
>>> id (a)
1754405759376
>>> a += 1
>>> a
5
>>> id (a)
1754405759408
```

Yukarıdaki örnekte `id` değerlerinin farklı olduğuna dikkat ediniz.

---

Önceliği düşük olduğu için `a *= 2 + 3` ün eşdeğeri, `a = 2 * a + 3` DEĞİL
`a = 5 * a` olmaktadır, önce toplama işlemi yapılır.

## Kaynaklar

- <https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-augmented_assignment_stmt>

`12-00.56.35`
