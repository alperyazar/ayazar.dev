---
giscus: 20e68424-765a-4aaf-81ac-0ab909bd9357
---

# `str` Sınıfı ve İşlemleri - 3

`9799`

## String'lerin Karşılaştırılması

İki string `>`, `>=`, `<`, `<=`, `==` ve `!=` opertörleriyle
karşılaştırılabilir. Karşılaştırma leksikografik olarak yapılmaktadır. Yani
sözlükteki sıraya göre karşılaştırma yapılır. Karşılaştırma karşılıklı
karakterler aynı olduğu sürece ilerlenir. Farklı olunca da UNICODE sıra
numaralarına bakılır. Hangi numara büyükse o karakter diğerinden büyüktür.
Elbette genelde eşitlik veya değillik kısmına bakıyoruz, küçük ve büyük kısmını
pek kullanmayız.

Örnek:

```text
password = 'maviay'
s = input('Enter password:')

result = s == password
print(result)
```

---

Karşılaştırma UNICODE numaralara bakılarak yapıldığı için Türkçe'de bulunan ç,
ü, ö, ı, ğ, ş karakteleri ve bunların büyük harf karşılıkları, I hariç, UNICODE
tabloda tüm İngilizce karakterlerden daha ileride bulunmaktakdır.

```text
>>> 'ayça' < 'aysel'
False
```

Normalde bunun `True` olmasını bekleriz bizim sözlüğümüze göre.

---

Eğer bir yazı diğerini kapsıyorsa uzun olan yazı daha büyük olur.

```text
>>> 'aliye' > 'ali'
True
```

`9845`

---

UNICODE tabloda önce büyük harfler sonra küçük harfler gelir. Zaten UNICODE
tablonun ilk 128 karakteri ASCII tablosu ile aynıdır, ASCII tablosunda da durum
böyledir zaten. Sonraki 128 karakter ise ASCII Latin-1 Code Page ile aynıdır.

## `ord()` Fonksiyonu

`ord()` built-in fonksiyonu ile bir karakterin UNICODE tablodaki sıra numarasını
öğrenebilir.

```text
>>> ord('a')
97

>>> ord('ş')
351

>>> ord('aş')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ord() expected a character, but string of length 2 found
```

Eğer birden fazla karakteri olan `str` geçersek `TypeError` exception alırız.

```{note}
Hoca'nın yorumu şu: `TypeError` biraz doğru değil, zaten `char` yok. Onun
yerine `ValueError` verilmeliydi.
```

---

C, C++, Java ve C# gibi dillerde bir karakteri `''` içerisine alınca zaten o
ifade ilgili karakterin tablodaki sıra numarasını belirti. Bu dillerde zaten
`char` türleri vardır. Dillerde `char` türleri aritmetik işlemlere de
sokulabilmektedir. Bu dillerde `ord()` fonksiyonu bulunmaktadır.

## `chr()` Fonksiyonu

`ord()` fonksiyonunun tersidir. Bizden bir `int` değer alır, tek karakterli
bir `str` nesnesi verir.

```text
>>> chr(65)
'A'
```

`9911`
