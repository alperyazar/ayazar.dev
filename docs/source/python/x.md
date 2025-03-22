---
giscus: c7024e58-1a48-4bed-9607-16ca199c83d7
---

# Sabitlerin Türleri (BİTMEDİ)

Programlama dillerini öğrenirken değişkenlerin türleri olduğunu genelde fark
ederiz fakat sabitlerin, literals, bir türü yokmuş gibi düşünebiliriz. Fakat
Python örneğinde gördük ki bir değişkene bir sabit ile değer atadığımız zaman o
değişkenin türü de o anda belli olmaktadır, dinamik tür sistemi. O zaman bunun
olabilmesi için atadığımız sabitin de bir türü olması gerekmez mi? Yani bir türü
olacak ki onu atadığımız değişken de onun türünü aslın, değil mi?

```text
>>> x = 5

>>> type(x)
<class 'int'>

>>> type(5)
<class 'int'>
```

Görebileceğimiz üzere `x` in türü `int` oldu çünkü `5` in türü de `int`.

Şimdi [önceki yazıda](temel-veri-turleri.md) olduğu gibi bu sefer sabitlerin
türlerine bakalım.

## 1 - `int` Türden Sabitler

Bir sayı nokta, `.`, ve `e/E` içermiyorsa o sayı `int` türden olmaktadır. Başına
`0x` yazarsak 16lık yani hexadecimal sistemde sayılar yazabiliriz. `0o` veya
`0O` yazarsak da 8lik yani octal sistemde sayı yazmış oluruz. C'de bunun için
başına `0` koymamız yetiyordu ama Python'da `o/O` da koymalıyız. Bu bence güzel
bir şey çünkü bir sayıyı `0` ile başlattığınızda yanlışlıkla octal sayı
tanımlamış olmuyoruz bu sayede.

C dilinde C23'e kadar standartlarda binary sayı gösterimi yoktu. [^1f] Hoş,
birçok derleyici bunu extension olarak yılllardır destekliyordu. Bildiğim
kadarıyla Java ve C#'a hiç gelmedi. Fakat Python'da vardır, `0b` ya da `0B` ile
ikilik sistemde sabitler oluşturulabilir.

Aşağıdaki ifadelerin hepsi `x`'i `42` yapar.

```python
x = 42

x = 0b101010
x = 0B101010

x = 0x2A
x = 0X2A

x = 0o52
x = 0O52

print(x) # Hepsinde 42
```

---

Büyük sayıları yazarken basamakları gözle rahat ayırmak mümkün olmayabilir.
Birçok programlama dilinde de olan basamak ayırma seçeneği Python'da da vardır.
İstersek `_` karakteri ile basamakları ayırabiliriz.

```python
a = 1_000_000    # geçerli
b = 0b1010_1010  # geçerli
c = 0x1234_5678  # geçerli
```

Burada `_` karakterleri adeta görmezden gelinir. Elbette `1__0` gibi ifadeler
geçerli değildir, iki adet `__` ardarda gelmemelidir.

```text
>>> x = 1__0
  File "<stdin>", line 1
    x = 1__0
         ^
SyntaxError: invalid decimal literal
```

## 2 - `float` Türden Sabitler

Bir sayı nokta, `.`, ve `e/E` içeriyorsa `float` türden olmaktadır.

50'li yıllarda çıkan, yüksek seviyeli ilk dil olarak kabul edilen FORTRAN'dan
beri olan ve dillerin çoğunda olan (C#'ta yok) bir kural vardır. Bir sayı `.`
ile bitiyorsa sağında `0` varmış gibi davranılır. Eğer `.` ile başlıyorsa da
solunda `0` varmış gibi düşünülür.

```python
3.2  # 3.2
.2   # 0.2
2.   # 2.0
```

Bir `int` sabiti pratik olarak `float`a çevirmek için sonuna `.` koymamız
yeterlidir.

```python
123  # int
123. # float
```

Çok büyük sayıları yazarken `e/E` ile bilimsel notasyon yani **scientific form**
ya da **scientific notation** kullanabiliriz.

```python
15.25e-5 # 15.25 x 10^(-5)
3.23E7   # 3.23 x 10^7
1E6      # dikkat bu int değil float. 1000000.0
```

`int`te gördüğümüz `_` karakterini burada da kullanabiliriz.

```python
1_00_0000.3_14_54646 # geçerli
```

---

C dili ile uğraştıysanız sayıların sonuna `f` konulduğunu görmüş olabilirsiniz.
Bu dillerde sabitin sonuna `f` konulması türünün `float` olmasını sağlamaktadır,
diğer türlü `double` olmaktadır. Benzer durumlar C++, Java ve C# dilinde de
vardır. Python'da ise bu geçersizdir, `23.4f` diye bir şey yoktur.

```text
>>> print(23.4f)
  File "<stdin>", line 1
    print(23.4f)
             ^
SyntaxError: invalid decimal literal
```

## 3 - `bool` Türden Sabitler

[^1f]: <https://c-for-dummies.com/blog/?p=6173>
