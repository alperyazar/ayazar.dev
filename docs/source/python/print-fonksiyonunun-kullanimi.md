---
giscus: d7f2144e-c569-42ce-aafd-f3e8c6b56dfc
---

# 🖨️ `print()` Fonksiyonunun Kullanımı

`12-00.56.50`

`print()` fonksiyonunu zaten uzun süredir kullanıyoruz. Bu yazıda biraz daha
detaylı kullanımına bakalım.

Bu fonksiyon yazıları ekrana, asında `stdout` dosyasına, yazdırma işlemi
yapmaktadır. Bu fonksiyon yazdırma işleminin son aşaması olarak ekrana bir
de `\n` yazdırmaktadır. Dolayısı ile her bir `print()` çağrısı arasında
imleç, cursor, bir alt satıra geçmektedir.

```python
print('alper')
print('yazar')
```

Çıktı:

```text
alper
yazar
```

olmaktadır.

---

`print()` fonksiyonu değişken sayıda argüman alabilmektedir. Bu açıdan C'deki
bir *variadic function* olan `printf()` e benzer. Bir `print()` fonksiyonu ile
birden fazla ifadeyi yazdırabiliriz. Varsayılan olarak fonksiyon, her bir
argümanı yazdırdıktan sonra araya SPACE karakteri eklemektedir. Örneğin:

```python
a = 10
b = 20
c = 30
d = 40

print(a, b, c)
print(d)
```

kodunun çıktısı

```text
10 20 30
40
```

olmaktadır.

## `sep`

İleride göreceğimiz **isimli argüman** başlıklı bir konu vardır. `print()`
fonksiyonu, `sep`, separator ya da separation, isimli bir isimli argüman
alabilmektedir. Bu, opsiyoneldir. Biz bu argüman ile çoklu argüman bastırdığımız
durumda argümanlar arası boşluk yerine başka yazıların bastırılmasını
sağlayabiliriz.

Yukarıdaki örnekten devam edecek olursak:

```python
a = 10
b = 20
c = 30

print(a, b, c, sep=' - ')
```

çıktı

```text
10 - 20 - 30
```

olmaktadır. `sep` in varsayılan değerini `' '` gibi düşünebiliriz. Eğer
`sep='\n'` dersek bu sefer de argümanlar alt alta yazdırılacaktır.

## `end`

`print()` fonksiyonunun `sep` gibi bir parametresi daha vardır, `end`. Bu da
opsiyoneldir. Varsayılan değerini `\n` olarak düşünebiliriz. Bu da fonksiyonun
en son neyi yazdıracağını belirtir.

Örneğin:

```python
print('alper', end=' bitti ')
print('yazar')
```

sonuç

```text
alper bitti yazar
```

olmaktadır. İlk `print()`e `end` ile argüman geçtiğimiz için sonunda onu yazdı
ve alt satıra geçmedi.

---

Elbette Python'da bir fonksiyon çağırırken bunların nasıl olabildiğini,
değişken sayıda argüman geçirmeyi, opsiyonel argüman geçirmeyi burada konuşmadık.
Onlar ilerisinin konusu.

`12-1.18.20`
