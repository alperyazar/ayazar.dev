---
giscus: ac266181-ea3d-4066-84bc-784e7996015e
---

# `if` Deyimi

`10819`

Genel biçimi

```text
if <ifade>: <suite>
[else: <suite>]
```

biçimindedir.

Burada iki adet `suite` vardır. Biri doğruysa biri de yanlışsa kısmı içindir.
`else` kısmı hiç olmayabilir. Aşağıdaki yazım geçerlidir:

```text
if ifade:
  ifade1
  ifade2
else:
  ifade3
  ifade4
```

Aşağıdaki da geçerlidir:

```text
#geçerli

if ifade: ifade1; ifade2
else:
  ifade3
  ifade4

###

#geçerli

if ifade:
  ifade1; ifade2
else
  ifade3
  ifade4

###

#geçerli, suitler farklı seviyede olabilir

if ifade:
    ifade1
    ifade2
else:
  ifade3
  ifade4
```

En son verdiğimiz örnek elbette geçerlidir ama okunabilir değildir.

---

`:` atomu bileşik deyimlerde kontrol kısmının sonunda olmaktadır genel olarak.
Bu atom, ifadeye yapışık olmak zorunda değildir fakat aynı satırda olmalıdır.

```text
#geçerli

if ifade           :
        ifade1; ifade2
else                 : ifade3; ifade4
```

Bu da geçerlidir ama iyi değildir, **`:` atomunun boşluk bırakılmadan yapışık
yazılması tavsiye edilir.**

---

*Suite* tanımına tekrar bir bakalım. Aynı satır üzerine yazmış olduğumuz birden
fazla basit deyim ya da farklı satırlara yazılmış olan aynı girinti düzeyine
sahip birden fazla deyim bir suite oluşturuyordu. Bu açıdan bakınca

```text
# geçersiz

if ifade: ifade1
  ifade2
else: ifade3; ifade4
```

geçersizdir. Çünkü `ifade1` ayrı bir suite, `ifade2` ayrı bir suite gibi oluyor.

```text
# geçersiz

if ifade:
  ifade1
    ifade2
else: ifade3
```

Burada da `ifade1` ve `ifade2` ayrı girinti seviyelerinde olduğu için tek bir
suite oluşturmaz.

```text
# geçerli

if ifade: ifade1; ifade2
else: ifade3; ifade4
ifade5
```

Burada bir sıkıntı yoktur. `ifade5` ise `if` deyimine ait değildir.

```text
# geçersiz

if ifade:
  ifade1
  ifade2
else:
  ifade3
  ifade4
 ifade5
```

Burada `ifade5` ise `if` dışında değildir. `ifade5`in dışarıda olması için
`if` ile aynı hizada olması gerekir. Hizası da yanlış olduğu için suite kuralına
aykırıdır.

```text
# geçersiz

if ifade: ifade1 else: ifade2
```

Bu da geçersizdir. Çünkü `else` ile `if` aynı girinti seviyesinde olmalıdır.

## `if` nasıl çalışır

Yorumlayıcı önce `if` anahtar sözcüğünün yanındaki ifadenin türüne bakar. Eğer
`bool` türünden değilse onu `bool` türüne dönüştürür. Bu dönüşümden sonra `True`
elde edilirse `if` deyiminin doğru kısmındaki *suite* çalıştırılır. `False` ise
`else` kısmındaki *suite* çalıştırılır. Burada `if` deyiminin çalışması biter.

```python
x = 10
if x > 0:
  print('ankara')
  print('izmir')
else:
  print('adana')
print('eskişehir')
```

Burada `x > 0` zaten `bool` türündendir.

---

```{note}
Boş bir listenin, demetin ya da string'in `bool` türüne `False` olarak doluların
ise `True` olarak dönüştürüldüğünü hatırlayalım.

Sıfırdan farklı `int` ve `float` değerleri de `bool` türüne `True`; `0` değeri
ise `False` olarak dönüştürülür.
```

---

`if`, tek bir deyimdir.

```text
if ifade:
  ifade1
  ifade2
ifade3
```

Burada `if` bir deyimdir ve `ifade3` de basit bir deyim oluşturur. Burada `else`
yoktur.

---

Dikkat edersen C, C++, Java ve C# gibi dillerde `if()` formu vardır. Ama
Python'da `()` parantezler yoktur. C'de olmasaydı eğer `if a > 10 b = 20;`
yazdığımızda neresi koşul neresi başka yer derleyici ayıramayacaktır. `()`
kullanımı C'de bunu sağlamaktadır. Python'da ise `:` atomu zorunlu olduğu için
`if a > b: b = 20` görüldüğü zaman yorumlayıcı bunu ayrıştırabilir.

Swift, Kotlin gibi dillerde ise `{}` kullanımı zorunlu olduğu için `()`
kullanımı gerekmemektedir. C'de ise `{}` da zorunlu değildir.

```text
# Swift ve Kotlin

if a > 10 {
  b = 20;
}
```

**İstersek Python'da da `()` kullanabiliriz, her ifade de olduğu gibi.**

```python
# Geçerli

if (a > 10):
  b = 20
```

Geçerlidir ama `()` gerekli değildir.

## Nested `if` ve Dangling `else`

`if` deyimi içerisinde başka bir `if` deyimi olabilir.

```text
ifade1
if ifade2:
  ifade3
  if ifade4:
    ifade5
    ifade6
  else:
    ifade7
  ifade8
else:
  ifade9
ifade10
```

En dıştan baktığımızda 3 adet deyim vardır: `ifade1`, `if` deyimi ve `ifade10`

`if` deyiminin içinde de başka `if` deyimleri vardır.

---

Bir de [dangling else](https://en.wikipedia.org/wiki/Dangling_else)
konusuna bir bakalım.

C, C++, Java, C# gibi dillerde hizalama anlamsız olduğu için *dangling else*
denilen bir durum oluşabilmektedir. Bu durum, iki `if` için tek bir `else`
bulunması durumudur. Python'da ise girinti düzeyleri sayesinde böyle bir
kararsızlık oluşmaz.

```text
if ifade1:
  if ifade2:
     ifade3
     ifade4
else:
  ifade5
```

Burada `ifade5`, en dıştaki `if`in `else` kısmındadır.

```text
if ifade1:
  if ifade2:
     ifade3
     ifade4
  else:
    ifade5
```

Burada ise içerdeki `if` in `else` kısmındadır.

## Ayrık Koşullar - Discerete Conditions

`11144`

Biri doğru iken diğerlerinin doğru olma olasılığı yoksa bu koşullara
**ayrık koşullar** denmektedir. Mesela `a > 0` ve `a < 0` gibi.

Programlamada bunların ayrı `if` ile kontrol edilmesi **kötü bir tekniktir.**

```python
if a > 0:
  ifade
if a < 0:
  ifade
if a == 0:
  ifade
```

Örneğin `a` pozitif bir değerse gereksiz yere iki karşılaştırma daha
yapılacaktır. Bunlar önemsiz de olsa gereksiz zaman harcamasına yer açar.
Daha doğru olan `else-if` kullanımıdır.

```python
if a > 0:
  ifade
else:
  if a < 0:
    ifade
  else:
    if a == 0:
      ifade
```

## `elif`

Görüldüğü gibi `else-if` merdiveni kullandığımızda görüntü bozulmaktadır. Bunun
için Python'da `if` deyiminin `elif` kısmı da olabilir, `else if`in kısaltılmış
halidir. **`if` ile aynı girinti düzeyinde olmak zorundadır.** `elif` sonrası
`else` de kullanılabilir.

```python
if a == 1:
  print('bir')
elif a == 2:
  print('iki')
elif a == 3:
  print('üç')
else:
  print('hiçbiri')
```

`11262`
