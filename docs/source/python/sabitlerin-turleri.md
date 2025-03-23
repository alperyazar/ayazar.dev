---
giscus: c7024e58-1a48-4bed-9607-16ca199c83d7
---

# Sabitlerin Türleri

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

## Escape Sequences - Ters Bölü, `\`, Karakterleri

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

## `'` içinde `'`, `"` içinde `"`

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

## Regular String, `r` ve `R`

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
Python shell'i aslında arka planda ilgili objenin `__repr__()` metodunu
çağırmaktadır. Bu da ileride konuşacağımız (muhtemelen) *dunder* yani *double
underscore* method'ları ile ilgilidir.

```text
>>> s = "\g"
>>> s
'\\g'
>>> s
'\\g'
>>> print(s.__repr__())
'\\g'
>>> repr(s)
"'\\\\g'"
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

## String Concatenation

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

## `"""` ve `'''` Kullanımı

Python'da 3 adet tek ve çift tırnak yani `""""` ve `'''` ile de string sabitler
oluşturulabilmektedir. Tek olanı gördük, 3 olanı var diyoruz fakat ikililer
yoktur. Yani `""x""` ve `''x''` geçersizdir. Yine tekli olanda olduğu gibi
3'lülerde de `"` ile `'` arasında fark yoktur.

```text
>>> x = """alper"""
>>> x
'alper'

>>> y = '''yazar'''
>>> y
'yazar'
>>>
```

Tekli ile üçlü tırnak(lar) arasında şu farklar vardır:

1️⃣ Tek tırnak içerisindeki yazılar tek satırda yazılmak zorundadır, bunu
yukarıda görmüştük. Üç tırnaklı yazılar ise farklı satırlara bölünebilir.

2️⃣ Üç (çift) tırnak içerisinde tek (çift) tırnak bir sorun yol açmaz.

Üçlü tırnaklarda ters bölü, `\`, karakterinin yorumlanması açısından teklilere
göre bir fark yoktur. Yine burada da `r` ve `R` ile regular string
oluşturabiliriz. Bunu yapmazsak yine `\` karakteri bir sekans oluşuyorsa
"yorumlanacaktır."

```text
>>> x = '''Merhaba,
... nasılsınız?'''

>>> x
'Merhaba,\nnasılsınız?'

>>> print(x)
Merhaba,
nasılsınız?
```

Aşağıda rahatça `'''` arasına `'` yazabildik.

```text
>>> x = '''Ben giderim Batum'a'''
>>> print(x)
Ben giderim Batum'a
```

---

Üç tek tırnağın ya da üç çift tırnağın içerisindeki tek tırnak ya da tek çift
tırnak yazının başında olabilir **ama yazının sonunda olamaz.** Bunun sebebi,
[](token-keyword-expression-white-space) başlıklı yazıda da bahsettiğim
*maximal munch* kuralıdır.

```text
>>> x = """"Bugün" günlerden pazar."""
>>> print(x)
"Bugün" günlerden pazar.
```

Burada problem yok çünkü maximal munch kuralına göre atomlar şöyle ayrışıyor:

```text
x
=
""""Bugün" günlerden pazar."""
```

Ama şu sentaks hatasıdır:

```text
>>> x = """Bugün günlerden "pazar.""""
  File "<stdin>", line 1
    x = """Bugün günlerden "pazar.""""
                                     ^
SyntaxError: unterminated string literal (detected at line 1)
```

Çünkü yine aynı kurala göre atomlara ayırma şöyle olur:

```text
x
=
"""Bugün günlerden "pazar."""
"
```

Tabi burada yine `\` imdadımıza yetişebilir.

```text
>>> x = """Bugün günlerden "pazar.\""""
>>> print(x)
Bugün günlerden "pazar."
```

Sonda bir boşluk karakteri olsaydı yine atomlar doğru ayrışacaktı. Çünkü `" """`
görüldüğü zaman atomlar hayal ettiğimiz gibi oluşacaktır. Ama yazının sonunda
ekrana basınca görmediğimiz bir boşluk karakteri vardır.

```text
>>> x = """Bugün günlerden "pazar." """
>>> print(x)
Bugün günlerden "pazar."
```

Bu durumların aynısı `'''x''''` içerisinde `'` kullanımı için de geçerlidir.

Yukarıda bahsettiğimiz string concatenation burada da yapılabilir.

```python
s = 'Bugün' """hava
güneşli."""

print(s)
```

Çıktı:

```text
Bugünhava
güneşli.
```

## Unicode Strings, `u` ve `U`

Python 2'de anlamlı olan fakat Python 3 ile anlamı kalmamış bir kavramdır.
Python 2'de karakter kodlaması için bir byte'lık ASCII kodlaması kullanılıyordu.
ASCII ile de tüm karakteleri düşündüğümüz zaman çok kısıtlı bir karakter kümesini
gösterebiliyoruz. Bu gibi durumlarda UNICODE string oluşturmak gerekebiliyordu.
Bu, yazı sabitlerinin başına, `''` veya `""` olabilir `u` veya `U` getirerek
oluşturulmaktadır.

```python
x = "çay"  # Python 3'te sorun değil
x = u"çay" # Artık gerekli değil
x = U"çay" # Artık gerekli değil
```

Unicode string'ler Python 3.0 - 3.2 arasında sentaks hatası verdiriyordu hatta
dilden komple kaldırılmıştı. Python 3.3 ile geriye dönük uyumluluk için geri
getirildi.

İlginizi çekebilir:

- <https://docs.python.org/2/tutorial/introduction.html#unicode-strings>
- [What's the u prefix in a Python
  string?](https://stackoverflow.com/q/2464959/1766391)

## Bytes, `b` ve `B`

Tek tırnakların (`'`, `"`) veya üç tırnakların (`'''`, `"""`) önüne `b` ve
`B` getirirsek bu sefer **bytes** türünden bir şey oluşturmuş oluruz. Bu, `str`
türü değildir. İleride buna değiniriz.

```text
>>> x = b'alper'
>>> x
b'alper'
>>> type(x)
<class 'bytes'>
```

## 5 - `complex` Türden Sabitler

Python'da `j` harfine bitişik bir `int` veya`float` sabit kullandığımız zaman
`complex` türden bir sabit oluşturmuş oluruz. Elbette `+` ya da `-` operatörleri
ile de sayının reel kısmını oluşturabiliriz. Eğer sadece `j` yazarsak buradaki
`j` değişken olarak yorumlanır ve bunu önlemek için `1j` yazmak gerekir.
Örneğin:

```text
>>> x = j
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'j' is not defined

>>> x = 1j
```

```python
j = 5
z = 3j + j
print(z)  # Çıktı (5+3j)
```

Bir `complex` sayı `int` ya da `float` ile toplanır ya da çıkartılırsa sonuç
`complex` türden olmaktadır.

## 6 - `NoneType` Türden Sabitler

Türü `NoneType` olan tek sabit `None`dır. `None` bir anahtar sözcüktür.
`None` değeri REPL ortamında yani interaktif çalışma ortamında bir şey
basmamaktadır.

````{todo}
🤔 Burada tam anlayamadığım bir şey var. Yukarıda bahsettiğim `repr()` ve
`__repr__()` burada farklı davranmaktadır.

```python
>>> x = None
>>> x
>>> print(repr(x))
None
>>> repr(x)
'None'
>>> print(x.__repr__())
None
>>> print(None)
None
>>> None
>>> type(None.__repr__())
<class 'str'>
```

`x` yazıp ENTER deyince ekrana hiç bir şey basılmıyor ama `repr()` ile `None`
kelimesini görebiliyoruz.
````

[^1f]: <https://c-for-dummies.com/blog/?p=6173>
[^2f]: <https://en.wikipedia.org/wiki/Page_break#Form_feed>
