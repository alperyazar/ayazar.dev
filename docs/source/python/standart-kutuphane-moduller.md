---
giscus: 3752417f-add4-42a9-a59e-67a69f1d5480
---

# Python Standart Kütüphanesi ve Modüller

Python için **batteries included 🔋** ifadesi de kullanılır. Python dağıtımları
ile beraber birçok kütüphane de gelmektedir. Bu yüzden, bu ifade kullanılır.
İşlerimizin önemli bir kısmını bu kütüphaneleri ile halledebiliriz. Bunları
kullanmak için bilgisayarımıza Python'u kurmamız yeterli olacaktır.

Python, aslında temel iki parçadan oluşur: Python dili ve bahsettiğimiz standart
kütüphane yani batarya kısmı. Standart kütüphane de fonksiyon dediğimiz
*callable nesnelerden* ve sınıflardan oluşmaktadır. Python'da dilersek nesne
yönelimli dilersek de prosedürel teknikte kodlar yazabiliriz.

```{note}
Dili anlatan **The Python Language Reference**:

<https://docs.python.org/3/reference/index.html>

ve Python standart kütüphanesini anlatan **The Python Standard Library**:

<https://docs.python.org/3/library/index.html>

dokümanlarına ilgili adreslerden ulaşılabilir.
```

Standart kütüphane de *modül*lerden oluşmaktadır. Bunun ne anlama geldiğini
ileride görürüz. Eğer kullanmak istediğimiz bir fonksiyon bir modülün içerisinde
ise öncelikle o modülün `import` edilmesi gerekmektedir.

Örneğin [math](https://docs.python.org/3.11/library/math.html) modülünde bulunan
`math.factorial()` fonksiyonunu kullanmak isteyelim. Bu fonksiyon bize bir
sayının faktöriyelini vermektedir. Bunun için `math` modülü import edilmelidir.

```python
import math # import bir anahtar sözcüktür.

print(math.factorial(5)) # 120 yazdırılacaktır
```

Bu işlemleri elbette interaktif yani REPL ortamında da yapabiliriz:

```text
>>> import math
>>> print(math.factorial(5))
120
```

## Built-in Fonksiyonlar

Standart kütüphanedeki bazı fonksiyon ve sınıflar hiçbir `import` işlemi
yapılmadan kullanılabilmektedir. Bunlara **built-in** sınıf ve fonksiyonlar
denmektedir. Örneğin şimdiye kadar kullandığımız `id()`, `type()` ya da
`print()` birer built-in fonksiyondu. Dikkat ederseniz bir `import` işlemi
yapmadık bunlar için.

```{tip}
Built-in fonksiyon listesi için
[tıklayınız.](https://docs.python.org/3/library/functions.html)
```
