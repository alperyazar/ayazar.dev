---
giscus: e8abe2b1-f71d-4350-af22-5c411ba483bc
---

# `print()` ve `input()`

Python'da ekrana yani aslında `stdout` a çıktı üreten tek bir fonksiyon
vardır: `print()` Benzer şekilde klavyeden girdi alan yani `stdin` i okuyan
da tek bir fonksiyon bulunur: `input()` Her ikisi de built-in fonksiyonlardır
ve bir `import` işlemi olmadan kullanılabilirler.

`print()` fonksiyonunu önceden görmüştük, biraz `input()` a odaklanalım.

## `input()`

`input()` fonksiyonu argüman olarak bir yazı alabilir. Eğer böyle kullanırsak
önce yazı ekrana basılır. Sonra imleç yazının sonuna götürülür ve sonra giriş
beklenir. Kullanıcı bir yazı girerek ENTER tuşuna basar. Fonksiyon da girilen
yazıyı bize bir `str` nesnesi olarak verir.

```python
s = input('Bir şeyler yazınız..')
print(s)
```

Çıktı:

```text
Bir şeyler yazınız..hebele hübele
hebele hübele
```

Yukarıdaki kodu çalştırınca `hebele hübele` yazdım ve ENTER tuşuna bastım.

Fonksiyona argüman olarak bir yazı geçmeyip, parantez içini boş da bırakabiliriz:

```python
s = input()
print(s)
```

````{note}
Bir fonksiyonun aynı isimde olup, iki farklı türden parametre alması C ile
ilgilenen biriyseniz garip gelebilir. Bu durum C'de şuna benzeyecektir:

```c
char *input(void);
char *input(const char *prompt);

int main(void)
{
    return 0;
}
```

Yukarıdaki C kodu hatalıdır, *function redeclaration* problemi vardır. Python'da
ise bir fonksiyon böyle davranabilir. Bu konu henüz değinmediğimiz *function
overloading*, *polymorphism*, *default arguments* gibi konularla ilgilidir.
````

---

Python'da tüm atamalar birer adres ataması demiştik. Benzer şekilde `input()`
fonksiyonun geri dönüş değerini aslında bir değişkene atadığımızda,
`input()` fonksiyonu tarafından oluşturulmuş bir `str` nesnesinin adresini
o değişkene atamış oluruz.

```python
x = input()
```

Burada, `x` değişkeni `input()` fonksiyonu tarafından oluşturulmuş bir `str`
nesnenin adresini tutmaktadır.

```{note}
`str` nesnelerin immutable olduğunu hatırlayalım: [](immutable-mutable.md)
```

## `input()` ve Tür Dönüşümleri

`input()` fonksiyonu bize her zaman `str` nesnesini verir. Biz eğer `int` ya
da `float` gibi başka bir türden girdi istiyorsak bu `str` nesnesini bu türlere
çevirmeliyiz. Dönüştürmek istediğimiz tür `T` olsun. O zaman

```text
x = T(input())
```

dediğimiz zaman `T` türüne dönüşüm yapılmış olacaktır.

Eğer bir tam sayı okumak istiyorsak:

```python
sayı = int(input('Tam sayı giriniz: '))
print(sayı)
```

gibi bir kod yazabiliriz. Örnek girdi ve çıktı:

```text
Tam sayı giriniz: 42
42
```

```{hint}
Genel olarak `T` bir tür belirtmek üzere `T(...)` ifadesi aslında *`T` türüne
dönüşüm* anlamına gelmektedir.
```

Benzer şekilde `float(input())` gibi denemeler yapabilirsiniz.

## Exception

Programın çalışma zamanında yani runtime sırasında çıkan ciddi hatalara
**exception** denmektedir. Bu noktada programcı exception'u *yakalayıp*
programın çalışmasına devam edebilir. Ancak exception yakalanmazsa programın
çalışması sonlanır. Bu konulara ileride bakarız.

`T(input())` şeklindeki kullanımlarda eğer girdiğimiz girdinin `T` türüne
dönüşümünde bir problem yaşanırsa exception oluşacaktır.

```python
int(input())
```

Çalıştırıp, girdi olarak `Alper` yazdım:

```text
>>> int(input())
Alper
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'Alper'
```

Bu `str`, `int` türüne dönüştürülemediği için exception oluştu ve bunu
yakalamadığımız için de programımız sonlandırıldı.

---

Exception'ların türleri vardır. Genelde `XXXError` şeklindedir. `ValueError`,
`TypeError`, `IndexError` gibi.

## `print()`

Bu fonksiyonu serinin başından beri neredeyse hep kullandık. `print(x)` şeklinde
yazdığımız zaman `x` in gösterdiği nesnenin içeriğini ekranda gördük.

Burada eklemek istediğim ufak bir nokta aslında `print()` fonksiyonun C'deki
*variadic functions* gibi olduğudur. Yani birden fazla değişkeni ekrana
basabiliriz:

```python
x = 10
y = 20
z = 'hebele'

print(x, y) # Çıktı: 10 20 hebele
```

Bunun dışında `print()` in alabileceği başka argümanlar da vardır. Bunun için
[dokümantasyona](https://docs.python.org/3/library/functions.html#print)
bakılabilir. Ama henüz görmediğimiz kavramlar olduğu için şimdilik geçiyorum.
