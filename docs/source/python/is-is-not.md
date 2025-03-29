---
giscus: 9e1df69c-6fc7-43e4-aff9-7603620c5bd1
---

# `id()`, `is`, `is not` ve Optimizasyon

İki değişkenin aynı nesneyi gösteriyor olması demek, `id()` değerlerinin
aynı olması anlamına gelmektedir. `id()` fonksiyonuna önceden bakmıştık.

Benzer şekilde `is` operatörü iki değişkenin aynı nesneyi gösterip
göstermediğini anlamak için kullanabiliriz. Bu operatör `bool` türden bir
değer üretmektedir. Aynı ise `True`, değil ise `False` değerini üretir.

`a is b` ile `id(a) == id(b)` aynı anlamdadır.

```python
a = 10
b = 20
print(a is b)

a = b
print(a is b)
```

Yukarıdaki kodu çalıştırdığımızda

```text
False
True
```

çıktısını alırız.

## `is not` Operatörü

`is` in tersi `is not` operatörüdür, `not is` değil. Bu operatör, iki anahtar
sözcükten oluşmaktadır: `is` ve `not`. `is` ve `not` ayrı birer atom olmasına
rağmen, token, `is not` tek bir operatör oluşturmaktadır.

```python
a = 10
b = 20
print(a is b)
print(a is not b)

a = b
print(a is b)
print(a is not b)
```

Çıktı:

```text
False
True
True
False
```

olmaktadır.

## `==` ve `is`

`==` operatörü ile `is` operatörü farklıdır. `is` operatörü aynı yeri mi
göstermektedir diye bakarken `==` operatörü nesnelerin değerini kıyaslamaktadır.

```python
a = 10
b = a/2 + 5 # Dikkat, int değil float

print(a == b)  # True
print(a is b)  # False, başka nesneler
```

Yukarıdaki kodun çıktısı

```text
True
False
```

olmaktadır.

## Tek Bir `None` Nesnesi

Python'da `None` değerini içeren tek bir nesne vardır. Biz değişkenlere `None`
değerini atadıkça aslında aynı nesneyi göstertmiş oluruz.

```python
a = None
b = None

print(a is b) # Her zaman True
```

## Optimizasyon Kavramı

Derleyici ve yorumlayıcılar yazılan kodları daha hızlı çalıştıracak ya da
bellekte daha az yer kaplayacak şekilde optimize edebilirler. Burada kritik olan
nokta, kodun optimize edilirken anlamının değişmemesidir. Yazdığımız kod,
optimize edilmeden önce nasıl çalışıyorsa daha doğrusu dışarıdan nasıl
gözlemleniyorsa optimize edildikten sonra da aynı davranışları sergilemelidir.
Bu noktada Python implementasyonları çeşitli tekniklerle bu işlemleri
yapabilirler.

Aşağıdaki kodu ele alalım

```python
a = 10
b = 10
print(a is b)
```

`int` nesnelerin değiştirilmez yani immutable olduğunu söylemiştik. Bu durumda
iki farklı fakat değeri aynı yani `10` olan `int` nesnesinin yaratılmasına gerek
yoktur. Gerçekten de CPython'da bu ikisi aynı nesneyi göstermekte ve çıktı
`True` olmaktadır. Elbette böyle olmak zorunda değildir. Optimizasyon yapmayan
bir Python implementasyonu her iki `10` değerli `int` nesnesi için ayrı nesneler
oluştursa ve `a` ile `b` farklı nesneleri gösterse bu da kurallara aykırı
değildir.

Birçok Python implementasyonu [constant
folding](https://en.wikipedia.org/wiki/Constant_folding) yani *constant
propagation* gibi tekniklerle optimizasyon yapabilmektedir.

```python
a = 10
b = 8 + 2
print(a is b) # True, bu da
```

```{attention}
Her bir değişken ataması nesne ataması dedik ama her bir atamada yeni bir nesne
yaratılıyor demedik ❗
```

Örnekler:

```python
a = 5
b = 10
c = a + a

print(b is c) # Bende True yazdı
```

```python
a = 5
b = int(input('Sayı giriniz: '))

print(a is b) # Bende 5 girersem True yazıyor, diğer türlü False
              # Girdi 5 ise a'nın gösterdiği 5 ile
              # benim yazdığım 5 "aynı" oluyor.
```

---

Kod optimizasyonu dediğimiz zaman varsayılan **hız** optimizasyonudur. Yani
bellek tüketimi ile hız karşı karşıya geldiğinde aksi belirtilmediği sürece
seçilen genelde hız olmaktadır. Elbette bazen hızlandırırken bellek tüketimi
de azalabilir, yani her zaman bunlar birbiriyle yarışacak diye bir şey yok,
bazen beraber de hareket edebilirler.
