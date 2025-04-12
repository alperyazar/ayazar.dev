---
giscus: ef3fa31a-be4b-406c-a59b-45fe9ede6cd1
---

# 🧠 Mantıksal Operatörler

`11-1.24.15`

Mantıksal işlemleri yapan operatörlerdir. Genelde programlama dillerinde
3 adet mantıksal işlem olur: *and*, *or* ve *not* işlemi. Python'da bu
operatörler `and`, `or` ve `not` anahtar sözcüğü ile gösterilir. Diğer dillerde
ise şöyledir (tabloda C örnek olarak verilmiştir):

| İşlem | C | Python |
| ----- |--- | ------ |
| AND, ve | `&&` | `and` |
| OR, veya | `\|\|` | `or` |
| NOT, değil | `!` | `not` |

`and` ve `or` operatörleri binary infix operatörler iken `not` operatörü
unary prefix operatördür.

Bu temel mantıksal opreatörlerin doğruluk tablosunu, truth table, ayrıca
vermiyorum, zaten biliyoruz. Bu operatörlerin temelde bool türünden değerler
üzerinde işlem yapmasını bekleriz. Python'da ise bu operatörlerin operandları
herhangi bir türden olabilir.

```text
>>> 3 and -4.5
-4.5
```

Java ve C# gibi dillerde ise mantıksal operatörlerin operand'ları bool türden
olmak zorundadır.

```c
//C kodu, clang 20.1.0 -O0

#include <stdio.h>

int main(void)
{
  // Implicit conversion?
  printf("%d\n", 3 && -4.5); //Sonuç 1
}
```

## ⚡ Kısa Devre Özelliği, Short Circuit

Diğer programlama dillerinde de olan bir özelliktir. `and` ve `or` operatörünün
her zaman sol tarafındaki ifade önce değerlendirilir. Bu operatörler bir ifadeyi
değerlendirdiği zaman onları `True` ve `False` olarak yorumlarlar. `int` ve
`float` türden operandlar için sıfır değeri `False`, sıfır dışı değerler `True`
anlamına gelmektedir. Eğer `and` operatörünün sol operandının değeri `False`
olarak değerlendirilirse sağ taraftaki ifade hiç yapılmaz, operatör sol
tarafındaki ifadenin değerini üretir. `and` operatörünün sol tarafındaki değer
`True` ise bu kez sağ tarafındaki ifade yapılır. Bu durumda operatör sağ
taraftaki ifadenin değerini üretir. `or` operatörü de benzerdir. Yine önce sol
taraftaki ifade yapılır. Bu ifade `True` ise sağ tarafındaki ifade hiç yapılmaz,
operatör sol tarafındaki ifadenin değerini üretir. Eğer sol tarafındaki ifade
`False` ise bu sefer sağ tarafındaki ifade değerlendirilir ve operatör sağ
tarafındaki ifadenin değerini üretir.

Kısa devre özelliği yanıltıcı olabilmektedir. Örneğin `foo() or bar()` gibi
bir ifade yazarsak burada önce `foo()` çalıştırılır ve geri dönüş değeri `True`
olarak değerlendirilirse `bar()` hiç çalıştırılmaz bile.

Yukarıda verdiğimiz `3 and -4.5` örneğinde sol taraf `3`, `True` olarak
yorumlandığı için sağ taraf da değerlendirilir ve `and` operatörünün oluşturduğu
değer bu durumda `-4.5` olur ve ifade de `float` türden olur.

```python
x = 3 and -4.5
print(x, type(x)) # -4.5 <class 'float'>

x = 0 and -4.5
print(x, type(x)) # 0 <class 'int'>

x = 0 or 0
print(x, type(x)) # 0 <class 'int'>

x = False and -10
print(x, type(x)) # False <class 'bool'>
```

```{attention}
Burada dikkat ederseniz operandların `True` ya da `False` olarak
değerlendirilmesi başka bir şeydir ama `and` ve `or` operatörleri `True` veya
`False` vermez, ya sağdaki ya soldaki değeri olduğu gibi verir. C ve C++'ta
böyle değildir, Swift ve Ruby'de böyledir.
```

---

`11-1.37.24`

Mantıksal operatörlerin önceliği karşılaştırma operatörlerinden küçüktür.

> Bknz: [](operator-oncelikleri.md)

Bu durumda `a > b and c > d` dediğimiz zaman gerçekten de *a, b'den büyük mü
ve aynı zamanda c de d'den büyük mü* diye bir işlem yapmış oluruz. Muhtemelen
algımız da bu şekilde olacaktır. Karşılaştırma operatörlerinin her zaman
`bool` türden değer oluşturduğunuz anımsayalım.

## `not` Operatörü

`11-1.45.20`

`and` ve `or` operatörlerinin sağ veya sol operandlarının değerlerini verdiğini
söylemiştik. `not` operatörü böyle değildir, her zaman `True` ya da `False`
verir.

Örneğin:

```python
x = not False
print(x, type(x)) # True <class 'bool'>

x = not True
print(x, type(x)) # False <class 'bool'>

x = not 4.5
print(x, type(x)) # False <class 'bool'>

x = not -3.5
print(x, type(x)) # False <class 'bool'>

x = not 0
print(x, type(x)) # True <class 'bool'>

x = not 0.0
print(x, type(x)) # True <class 'bool'>
```

## `and` ve `or` Operatörlerinin Birlikte Kullanımı

`11-1.55.20`

Bu operatörleri beraber kullanırken dikkatli olmaktada fayda vardır. `and`
operatörü, `or` operatöründen yüksek önceliklidir. Ama kısa devre özeliğinden
dolayı beklenti dışı sonuçlar oluşabilmektedir.

`ifade1 and ifade2 or ifade3`

dediğimiz zaman öncelikle `ifade1 and ifade2` işlemi yapılır ve bunun sonucu
`ifade3` ile `or` işlemine sokulur. Yani `(ifade1 and ifade2) or ifade3` ile
eşdeğerdir.

```python
x = 10 and 0 or 5
print(x) # 5
```

Örneğin burada ilk olarak `10 and 0` yapılır. Bunun değeri `0` dır. Sonra
`0 or 5` yapılır ve sonuç `5` olmaktadır.

Ya da `ifade1 or ifade2 and ifade3` yazdığımız zaman
`ifade1 or (ifade2 and ifade3)` demiş olmaktayız.

---

Kısa devre özelliği ile de birleştiği zaman şöyle bir durum oluşmaktadır.
Örneğin `ifade1 and ifade2 or ifade3` ifadesinin `(ifade1 and ifade2) or ifade3`
ile eşdeğer olduğunu söylemiştik. Burada `or` operatörünün solundaki
`(ifade1 and ifade2)` ifadesi önce yapılacaktır. `and` operatöründen dolayı da
önce `ifade1` yapılır ama eğer `False` ise `ifade2` yapılmaz, `ifade3` yapılır:

```python
def bir():
    print("bir")
    return 0

def iki():
    print("iki")
    return 1

def uc():
    print("uc")
    return 1

bir() and iki() or uc() # ekrana bir ve uc geliyor
```

Eğer `ifade1`, `True` ise `ifade2` yapılır. `ifade2` de `True` ise `and`
işleminin sonucu `True` döneceği için `or` işleminde olacak kısa devre
özelliğinden dolayı `ifade3` yapılmaz. Eğer `ifade2`, `False` ise `ifade3`
yapılır.

`ifade1 and ifade2 or ifade3` için aşağıdaki tablo geçerlidir:

| `ifade1` | `ifade2` | `ifade3` | Sıra    |
|----------|----------|----------|---------|
| `False`  | `False`  | `False`  | 1, 3    |
| `False`  | `False`  | `True`   | 1, 3    |
| `False`  | `True`   | `False`  | 1, 3    |
| `False`  | `True`   | `True`   | 1, 3    |
| `True`   | `False`  | `False`  | 1, 2, 3 |
| `True`   | `False`  | `True`   | 1, 2, 3 |
| `True`   | `True`   | `False`  | 1, 2    |
| `True`   | `True`   | `True`   | 1, 2    |

---

`ifade1 or ifade2 and ifade3` şeklinde bir ifade de işlem sırası aslında
şöyledir operatör önceliğinden dolayı `ifade1 or (ifade2 and ifade3)` anlamına
gelmektedir. İşte burada bir kafa karışıklığı olabilir. Çünkü ilk izlenim
`ifade2 and ifade3` ün önce yapılması gerektiği olmaktadır. Oysa ki `or`
operatörünün kısa devre özelliğinden dolayı önce `ifade1` değerlendirilir.
Aynı tabloyu oluşturalım.

`ifade1 or ifade2 and ifade3` için aşağıdaki tablo geçerlidir:

| `ifade1` | `ifade2` | `ifade3` | Sıra    |
|----------|----------|----------|---------|
| `False`  | `False`  | `False`  | 1, 2    |
| `False`  | `False`  | `True`   | 1, 2    |
| `False`  | `True`   | `False`  | 1, 2, 3 |
| `False`  | `True`   | `True`   | 1, 2, 3 |
| `True`   | `False`  | `False`  | 1       |
| `True`   | `False`  | `True`   | 1       |
| `True`   | `True`   | `False`  | 1       |
| `True`   | `True`   | `True`   | 1       |

Görüldüğü üzere `ifade1`, `True` olduğu zaman doğrudan kısa devre özelliğini
görmekteyiz. `ifade2` ve `ifade3` ile de `and` operatörünü kısa devre özelliğini
gözlemleyebiliyoruz.

Bu durum C dilinde de geçerlidir. Örneğin:

```c
//C kodu, clang 20.1.0 -O0

#include <stdio.h>

int bir(void) {
    puts("bir");
    return 1;
}

int iki(void) {
    puts("iki");
    return 0;
}

int uc(void) {
    puts("uc");
    return 1;
}

int main(void)
{
    // Implicit conversion?
    printf("%d\n", bir() || iki() && uc()); // "bir"
}
```

Kodunu ele alalım. C dilinde de `&&` operatörünün önceliği `||` operatöründen
yüksektir. Ama burada da önce `bir()` fonksiyonu çağrılır ve kısa devre
özelliğinden dolayı diğer fonksiyonlar çağrılmaz.

```{hint}
`and` ve `or` operatörlerinin her zaman sol tarafı önce yapılır. İfadelerin
değerlendirilme sırasını bulurken bu gerçeği göz önünde bulundurabiliriz.
```

---

Kendimize şu hatırlatmaları yapabiliriz:

1️⃣ Operatör önceliği, operator precedence, ile çalışma sırası yani
*order of evaluation* konuları paralel ama aynı konular değildir. Özellikle
kısa devre özelliği olan `and` ve `or` operatörlerinin kullanıldığı durumda
sonuç aynı olsa da order of evaluation beklentimizden farklı olabilir. Bu
Python implementasyonun yaptığı optimizasyon tekniklerden farklıdır, daha
*deterministik* bir davranıştır.

2️⃣ Kod yazarken *order of evaluation* konusunda varsayımlar yapmak ve kodumuzu
buna bağlı olacak şekilde yazmak, özellikle Python gibi yüksek seviyeli dillerde,
iyi bir tercih olmayabilir. Tek `and` ve `or` da durum net ama `and` ve `or`
tek bir ifadede karışmaya başlayınca bizim de kafamız karışabilir.

---

Özetle Python'da `and` ve `or` operatörleri aynı ifadede kullanıldığında
aslında her zaman soldaki operatörün sol tarafı önce yapılmaktadır. Diğer
taraflar sonuca göre yapılır yapılmaz.

Örnek:

```text
>>> 5 and 2.4 or 8 # 5 yapıldı True, 2.4 True. 2.4 or 8 de 2.4 sonucunu verdi
2.4

>>> 2 and 0 or 4 # 2 yapıldı True, 0 false. 0 or 4
4

>>> 2 or 4 or 6 # 2 yapıldı True, 2
2

>>> 0 or 10 and 0 # 0 yapıldı False, 10 yapıldı True sonra 10 and 0 yapıldı 0
0
```

`11-2.09.20`
