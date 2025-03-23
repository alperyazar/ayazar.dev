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

`bool` türden iki adet sabit vardır: `True` ve `False` (baş harflerinin büyük
olduğuna dikkat). Bu iki kelime de anahtar kelimedir.

## 4 - `str` Türden Sabitler

Bir yazıyı, `""` veya `''` karakterleri arasına alırsak `str` yani string türden
bir sabit elde etmiş oluruz. Python'da ikisi arasında bir fark yoktur.

```python
x = ''  # bu da geçerlidir
```

Python 2'de string'ler ASCII kodlama ile saklanıyordu. Python 3 ile beraber
[UNICODE](https://en.wikipedia.org/wiki/Unicode) [code
point](https://en.wikipedia.org/wiki/Code_point) kullanılmaktadır. Yani artık
Unicode'da tanımlı tüm karakterler rahatça kullanılabilmektedir. Arka planda ise
bu karakter numaralarının hangi encoding ile saklandığı yıllar içerisinde
değişmiştir. Bellekte nasıl saklandığı, aslında Python dilinin doğrudan problemi
değildir. Python implementasyonları farklı yöntemler seçebilir. Referans
implementasyon olan CPython'u ele alacak olursak Python 3.3 öncesinde Windows'ta
UTF-16, Linux'ta UTF-32 kullanılırken bellek verimliliğini arttırmak adına
Python 3.3 ile beraber *dynamic per-character storage model* denen bir
encoding'e geçilmiştir. Burada yazının içeriğine göre en az bellek tüketecek
kodlamanın otomatik seçilmesi CPython tarafından yapılır. Aşağıdaki deneyden
buna ait ipuçları yakalayabiliriz:

```text
>>> import sys

>>> sys.getsizeof('')
49
>>> sys.getsizeof('a')
50
>>> sys.getsizeof('ş')
76
>>> sys.getsizeof('🙂')
80
```

Öte yandan arka planda bunların nasıl tutulduğu bizler için çoğu zaman önemli
değildir, latin-1/ISO 8859-1 (ASCII), UTF-8, UTF-16, UTF-32 vs.

```{note}
İlginizi çekebilir:

- <https://www.linode.com/docs/guides/how-to-use-unicode-in-python3/>
- <https://docs.python.org/3/howto/unicode.html>
- <https://deliciousbrains.com/how-unicode-works/>
- <https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/>
```

### Escape Sequences - Ters Bölü, `\`, Karakterleri

ASCII ve UNICODE tablodaki ilk 32 karakter ekranda görünmeyen kontrol
karakterlerinden oluşmaktadır. Bu karakterleri yazdırınca ekranda bir şey
göremeyiz ama bir *eylem* oluşur. Peki bu karakterleri kendi yazı sabitlerimizin
içerisine nasıl koyacağız? Bu özel karakterlerin bir kısmını *escape sequence*
yani *ters bölü tekniği*, `\`, ile yerleştirmek mümkündür.

| Sekans | Eylem                                                              | Kod Numarası (ASCII, UNICODE) | Türü              | Gösterim |
|--------|--------------------------------------------------------------------|-------------------------------|-------------------|----------|
| `\a`   | Alert, bip sesi çıkar                                              | 7                             | Kontrol Karakteri | ␇        |
| `\b`   | Backspace, imleç bir geri atar                                     | 8                             | Kontrol Karakteri | ␈        |
| `\f`   | Form feed, printer sayfa atar, terminaldeki `CTRL-L` [^2f]         | 12                            | Kontrol Karakteri | ␌        |
| `\n`   | New line ya da Line feed, imleç aşağıdaki satırın başına geçirilir | 10                            | Kontrol Karakteri | ␊        |
| `\r`   | Carriage return, imleç bulunduğu satırın başına geçer              | 13                            | Kontrol Karakteri | ␍        |
| `\t`   | Horizontal tab, imleç yataydaki ilk tab stop'a atar.               | 9                             | Kontrol Karakteri | ␉        |
| `\v`   | Vertical tab, imleç düşey olarak bir tab atar                      | 11                            | Kontrol Karakteri | ␋        |

Bu sekanslar kullanıldığı zaman aslında stringlerin içerisine tek bir karakter
yazmış oluruz.

Örnek:

```python
x = "alper\nyazar"
y = "alper\byazar"
z = "alper\b"

print(x)
print(y)
print(z)
```

Çıktı:

```text
alper
yazar
alpeyazar
alper
```

### `'` içinde `'`, `"` içinde `"`

Yazı sabiti oluşturmak için `''` kullanıyorsak ve yazının içerisinde `'`
karakteri geçiyorsa sorun yaşamaya başlayabiliriz. Aynısı `""` ve `"` için de
geçerlidir.

```text
>>> a = 'Türkiye'nin başkenti Ankara'dır'
  File "<stdin>", line 1
    a = 'Türkiye'nin başkenti Ankara'dır'
                 ^^^
SyntaxError: invalid syntax
```

Burada sentaks hatası vardır. Bunu çözmek için tercih edebileceğimiz birkaç
yol vardır. İlki, escape sequence konusunda kullandığımız `\` karakterinin
kullanımıdır. Eğer `'` yerine `\'` yazarsak bir sorun oluşmamaktadır.

```text
>>> a = 'Türkiye\'nin başkenti Ankara\'dır'
>>> a
"Türkiye'nin başkenti Ankara'dır"
```

Diğer bir yöntem ise yazıyı `""` içerisine almak ve `'` karakterlerini de yazı
içerisinde doğrudan kullanmaktır.

```text
>>> a = "Türkiye'nin başkenti Ankara'dır"
>>> a
"Türkiye'nin başkenti Ankara'dır"
```

Bu durumda `""` kullanırken yine istersek `'` yerine `\'` yazabiliriz.

```text
>>> a = "Türkiye\'nin başkenti Ankara\'dır"
>>> a
"Türkiye'nin başkenti Ankara'dır"
```

Aynı durum, `""` içerisinde `"` kullanırken de çıkmaktadır. Benzer çözümler
burada da uygulanabilir.

```text
>>> a = "Kesinlikle "hemen" gelmelisin!"
  File "<stdin>", line 1
    a = "Kesinlikle "hemen" gelmelisin!"
                     ^^^^^
SyntaxError: invalid syntax

>>> a = 'Kesinlikle "hemen" gelmelisin!'
>>> a
'Kesinlikle "hemen" gelmelisin!'

>>> a = "Kesinlikle \"hemen\" gelmelisin!"
>>> a
'Kesinlikle "hemen" gelmelisin!'

>>> a = 'Kesinlikle \"hemen\" gelmelisin!'
>>> a
'Kesinlikle "hemen" gelmelisin!'
```

### Regular String, `r` ve `R`

Bir string sabiti içerisinde ters bölü, `\`, karakterinin kendisini yazmak
istiyoruz diyelim. Eğer bu karakterin sağındaki karakter, yukarıdaki tabloda
belirttiğimiz bir karakterle birleşip *escape sequence* oluşturuyorsa, bu
durumda istediğimizi yazamamış olacağız. Örnek:

```text
>>> x = 'C:\temp\a.txt'
>>> print(x)
C:  emp.txt
```

Örneğin `'C:\temp\a.txt'` içerisindeki `\t` ve `\a` birer escape sequence
oluşturmaktadır. Fakat

```text
>>> x = 'C:\dizin\c.txt'
>>> print(x)
C:\dizin\c.txt
```

şeklinde yapsaydık `'C:\dizin\c.txt'` içerisinde `\d` ve `\c` bir escape
sequence oluşturmadığı için tek bir karaktere çevrilmeyecek ve beklediğimiz
çıktıyı alacaktık.

Programcı olarak *Acaba burada `\` bir escape sequence oluşturur mu?* diye
sürekli diken üstünde olmak çok iyi değildir. `\` karakterinin bir sağındaki
karakter ile bir escape sequence oluşturmadığından emin olmak için `\`
karakterinin önüne bir `\` yazarak yani `\\` ile değiştirerek kendimizi
güvenceye alabiliriz.

```text
>>> x = 'C:\\temp\\a.txt'
>>> print(x)
C:\temp\a.txt

>>> x = 'C:\\dizin\\c.txt'
>>> print(x)
C:\dizin\c.txt
```

Eğer `\` ile zaten bir escape sequence oluşmuyorsa bile `\\` kullanmanın
bir zararı yoktur. **O yüzden her zaman `\\` kullanmamız faydalı olacaktır.**

Son bir not olarak şu da sentaks hatasıdır:

```text
>>> s = '\'
  File "<stdin>", line 1
    s = '\'
        ^
SyntaxError: unterminated string literal (detected at line 1)

>>> s = "\"
  File "<stdin>", line 1
    s = "\"
        ^
SyntaxError: unterminated string literal (detected at line 1)
```

Tek başına `\` olması hatadır.

---

Burada Python C, C++, Java ve C#'tan farklılık göstermektedir. Örneğin C'de
`\x` gibi bir sekans oluştuğu zaman eğer bu bir escape sequence oluşturmuyorsa
C derleyicisinde bir uyarı alabiliriz.

```c
#include <stdio.h>

int main(void)
{
    const char *x = "C:\temp\a.txt";
    const char *y = "C:\dizin\c.txt"; //derleyici uyarı veriyor.

    puts(x); puts(y);
}
```

Çıktı:

```text
C:  emp.txt
C:dizinc.txt
```

---

Python'da stringler ile interaktif terminalde uğraşırken içeriği `x` veya
`print(x)` ile yazdırabiliriz. Fakat bazı durumlarda iki çıktı farklılık
gösterebilir. En basitinden:

```text
>>> s = "\g"
>>> s
'\\g'
>>> print(s)
\g
```

Biz interaktif terminalde değişkenin adını yazıp ENTER tuşuna bastığımızda
Python shell'i aslında arka planda `repr()` fonksiyonunu çağırmaktadır.
Bu da ileride konuşacağımız (muhtemelen) *dunder* yani *double underscore*
method'ları ile ilgilidir, `__repr__()` vs.

```text
>>> s = "\g"
>>> s
'\\g'
>>> print(s)
\g
>>> print(repr(s))
'\\g'
```

`print(repr(s))` dediğimiz zaman `s` ile aynı çıktıyı aldık. Interaktif
terminalde `print()` kullanmadan yazdırdığımızda programcı içeriği daha rahat
anlasın diye daha *verbose* bir gösterim tercih edilmektedir.

---

Gelelim **regular string** konusuna, lafı biraz uzattık.

Eğer bir string sabitinin başına, `''` ve `""` fark etmez, `r` veya `R` koyarsak
bu string regular string olmaktadır. Bu noktada artık string içerisindeki `\`
karakterleri escape sequence durumunda olduğu gibi özel bir anlamla yorumlanmaz.
İçerisinde hiç `\` olmayan stringleri de regular string haline getirmenin bir
zararı da yoktur.

```text
>>> x = r"C:\temp\a.txt"
>>> print(x)
C:\temp\a.txt

>>> x = R"alper"
>>> print(x)
alper
```

### String Concatenation

Python'daki yazıların tek satıra yazılması zorunludur:

```text
s = 'hebele hubele
hoho'
```

Yukarıdaki yazım sentaks hatasıdır. Ama satır sonuna `\` koyarak alt satıra da
geçebiliriz.

```python
s = 'hebele hubele\
hoho'

print(s)
```

Çıktı

```text
hebele hubelehoho
```

Dikkat ederseniz aynı satıra, boşluksuz yazmış gibi olduk.

Fakat aynı satıra birden fazla yazı yazabiliriz. Eğer aralarında başka bir operatör
yoksa bu iki string birleştirilir ve tek string gibi ele alınır.

```text
>>> x = 'alper' "yazar"
>>> x
'alperyazar'
```

Arada bir boşluk olmadığına dikkat ediniz.

### `"""` ve `'''` Kullanımı

Buradayım


[^1f]: <https://c-for-dummies.com/blog/?p=6173>
[^2f]: <https://en.wikipedia.org/wiki/Page_break#Form_feed>
