---
giscus: e117184f-ebea-4439-831e-d161bb40658c
---

# Fonksiyon ve Metot Kavramı

Birçok programlama dilinde olduğu gibi Python'da da programlarımızı alt
parçalara bölmek mantıklıdır. Bu yaklaşım, Python'ın da desteklediği fakat C
gibi dillerle daha da özdeşleşmiş olan prosedürel (yapısal, structured)
programlama tekniğinin olmazsa olmazıdır. Elbette görece küçük programlar tek
parça olarak da yazılabilir, fonksiyonlara bölmek zorunlu değildir.

> İlginizi çekebilir: [](../c/properties.md)

---

Bir fonksiyon ya sınıf dediğimiz veri yapısının içerisinde bulunur ya da bir
sınıf içerisinde değildir. Sınıf içerisinde bulunan fonksiyonlara **method**
yani `metot 🇹🇷` denir. Sınıf içerisinde olmayan fonksiyonlara (tanım biraz
garip oluyor, farkındayım. *Yordam* da diyebiliriz) ise **function** yani
`fonksiyon 🇹🇷` adı verilir. Hatırlarsanız Python için multi-paradigm bir dil
demiştik. Yani hem nesne yönelimli (OOP) hem de prosedürel programlama
yapabiliyoruz.

Fonksiyon çağırma işlemi genel olarak şöyle yapılır:

```text
<fonksiyon ismi>([argüman listesi])
```

Burada `<fonksiyon ismi>` kısmı ve `()` zorunlu olup, `argüman listesi`
opsiyoneldir. Argüman herhangi bir ifade olabilir ama örneğin `if statement`
yani `if deyimi` olamaz, ifade olmalıdır.

> Bknz: [](token-keyword-expression-white-space.md)

Argümanlar birden fazla ise `,` atomu ile ayrılmalıdır.

```python
print(a)     # a bir argümandır.
print(a, b)  # İki argüman var: a ve b
print(a + b) # a + b ifadesi tek bir argüman oluşturur
```

---

Daha önceden de gördüğümüz gibi (bknz: [](standart-kutuphane-moduller.md)) bir
fonksiyon bir modülün içerisinde ise o fonksiyonu çağırmak için modül ismini
de kullanmalıyız.

```python
import math
math.sqrt(100)  # sadece sqrt() yazamayız, math.sqrt() diyoruz.
```

gibi.

---

Metot kavramına biraz bakalım. Bir fonksiyon doğrudan isim ile çağrılırken
bir metot o metotun ilişkin olduğu bir sınıfın türünden bir değişken olması
gerekmektedir. Burada genel sentaks şu şekildedir:

```text
<sınıf türünde değişken>.<metodun ismi>([argüman listesi])
```

Örneğin `str` bir sınıftır ve `upper()` isminde bir metot barındırır. Bu
durumda

```text
>>> 'alper'.upper()
'ALPER'
```

diye bir işlem yapabiliriz. Burada `'alper'`, `str` türden bir nesne olmaktadır.

Nesne yönelimli programlama ile konulara sonra bakacağımız için fazla detaya
girmiyoruz.
