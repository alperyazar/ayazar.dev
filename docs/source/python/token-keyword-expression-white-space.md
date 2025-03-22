---
giscus: 0ffbc8b2-4718-49bf-bb31-0ebf0d25a193
---

# Token, Keyword, White Space, Statement ve Expression Kavramları

Bir Python programı, diğer dillerde olduğu gibi, çalıştırılmadan önce
yorumlayıcı veya derleyici tarafından, artık hangi implementasyonu
kullanıyorsak, bir *elden geçmektedir.* [](temel-kavramlar.md) yazısında
bir dili oluşturan en yalın ögelere **token** yani `atom 🇹🇷` dendiğini
söylemiştik. Türkçe gibi doğal dillerdeki atomlar, sözcüklerdir. Peki Python
gibi bir programla dilinde atomlar nelerdir?

## Python'da Atomlar, Tokens

Aşağıdaki örnek ve yarım Python programına bir bakalım.

```python
if a > 10:
  print("evet")
```

Bu programın atomları şu şekildedir:
`if`, `a`, `>`, `10`, `:`, `print`, `(`, `"evet"`, `)`

Python'da atomlar **5 gruba** ayrılır.

### 1 - Anahtar Sözcükler, Keywords

Bu atomlar aynı zamanda *reserved words* olarak da geçmektedir. Dilin kuralları
tarafından özel amaçlar için ayrılmış sözcüklerdir. Bizler bu sözcükleri başka
amaçlar için, örneğin bir değişkene isim vermek için, kullanamayız. `if` bir
anahtar sözcüktür ve ona bir değişken muamelesi yapamayız:

```text
>>> if = 5
  File "<stdin>", line 1
    if = 5
       ^
SyntaxError: invalid syntax
```

Eğer bir değer atamaya çalışırsak bu durumda sentaks hatası alırız.

Python 3.13.2'de bulunan anahtar sözcükler şunlardır [^1f]:

```text
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

Bir de Python 3.10 ile gelen **soft keyword** konsepti vardır. Bunlar aslında
tam bir anahtar kelime değildir. Program atomlarına ayrılırken anahtar kelime
muamelesi görmezler ama sonraki aşamalarda parser seviyesinde bazı bağlamlarda
anahtar kelime gibi davranırlar. Python 3.13.2'de bulunanlar `match`, `case`
`type` ve `_` dir. [^2f]

### 2 - İsimler, Değişkenler, Identifiers

İsmini istediğimiz gibi verebildiğimiz atomlara değişken denilmektedir.

```python
a = 10
```

Burada `a` bir değişken atomdur.

```python
print(a)
```

ile değerini ekrana basabiliriz. Burada `print` de bir atomdur fakat Python'un
standart kütüphanesinde olan bir fonksiyonun adı olması onu anahtar kelime
yapmaz, aslında bir noktada `a` atomundan pek de farkı yoktur. `print` de bir
değişken atomdur. İstersek bir değer bile atayabiliriz (yapmalıyız demiyorum).

```python
print = 10 # Bu kod hata vermez, yapın demiyorum ama! Dilin kurallarına uygun
```

Ama artık `print` fonksiyonuna bu isimle erişemeyiz:

```text
>>> print = 10
>>> print(print)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
>>> print("Alper")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```

Ama onun da çözümü elbette var:

```text
>>> myprint = print
>>> print = 10
>>> myprint(print)
10
```

Unutmayalım ki, **Python'da fonksiyonlar değişken türden atomlardır.**
Python 2'de `print` bir anahtar kelime iken Python 3'te anahtar kelime değildir,
sıradan bir fonksiyon ile bu açıdan aynı kaderi paylaşır, hayat işte, ne oldum
değil ne olacağım demek lazım…

### 3 - Sabitler, Literals

Programlama terminolojisinde sabitler genelde *literals* olarak adlandırılır,
*constants* olarak değil.

```python
x = y + 10
```

Burada `x` ve `y` birer değişken atomdur fakat `10` bir sabit atomdur. Benzer
şekilde `"Alper"` şeklindeki yazılar da birer sabit atomdur. Sabitler de kendi
aralarında alt kategorilere ayrılırlar, tam sayı sabitleri, yazı sabitleri gibi.
Bunları da yeri geldikçe detaylandırırız.

### 4 - Ayraçlar, Delimiters ya da Punctuators

İfadeleri yani statement'leri birbirinden ayırmak için kullanılan atomlardır.
`;`, `:` gibi atomlar ayraç atomlardır.

Python 3.13.2 itibariyle tanımlı ayraçlar şunlardır: [^4f]

```text
(       )       [       ]       {       }
,       :       !       .       ;       @       =
->      +=      -=      *=      /=      //=     %=
@=      &=      |=      ^=      >>=     <<=     **=
```

### 5 - Operatörler, Operators

Bir işleme yol açan ve değer üretilmesini sağlayan atomlar operatör olmaktadır,
`+`, `-` gibi atomlar operatördür.

Python 3.13.2 itibariyle tanımlı operatörler şunlardır: [^3f]

```text
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
```

---

En baştaki programa dönecek olursak artık bir kategorilendirme yapabiliriz.

```python
if a > 10:
  print("evet")
```

| Atom     | Türü                   |
|  ------  |  --------------------  |
| `if`     | Anahtar Sözcük         |
| `a`      | Değişken               |
| `>`      | Operatör               |
| `10`     | Sabit, Tam sayı sabiti |
| `:`      | Ayraç                  |
| `print`  | Değişken ❗            |
| `(`      | Ayraç                  |
| `"evet"` | Sabit, Yazı sabiti     |
| `)`      | Ayraç                  |

## White Space, Boşluk Karakterleri

Python gibi programlama dillerinde *boşluk duygusu oluşturmak* için
kullandığımız ve bir kısmı klavyemizde de olan çeşitli karakterler vardır.
*Space* yani *boşluk* karakteri ASCII kodu ondalık sistemde `32` olan
karakterdir. Fakat **white space** ismi altında başka karakter de bulunur. Tipik
akla gelenler

| Karakter | ASCII Kod Numarası, Ondalık |
| -------- | ------------------ |
| Space | 32 |
| TAB, Horizontal TAB | 9 |
| VT, Vertical TAB | 11 |
| LF, Line Feed, NL, New Line | 10 |
| CR, Carriage Return | 13 |

karakterleridir.

Burada tarihsel açıdan da süregelmiş çeşitli gösterimler vardır. Windows'ta
ENTER tuşuna basıp, alt satıra geçtiğimizde bir üst satırın sonuna `CR` ve `LF`
karakterleri ardarda yarleştirilmiş olur. `CR`, aslında aynı satırın başına geç
demektir. `LF` ise satırdaki konumu koruyarak aynen alt satıra geç demektir. Bu
yüzden imleci alt satırın başına almak için Windows'ta başa geç + alt satıra geç
denir. Linux'ta ve artık macOS'te ise aynı işi `LF` karakteri tek başına
yapmaktadır. macOS eskiden bu iş için `CR` karakterini tek başına
kullanıyordu.[^5f]

Klavyeden TAB tuşuna bastığımızda ASCII ve UNICODE kodlamada 9 numaralı karakter
olan, yukarıdaki tabloda da belirtilen, TAB karakterini göndermiş oluruz. TAB'ın
etkileri editör yazılımlarında farklı olabilir. Bu karakter yatayda belli bir
zıplama yapar fakat zıplamanın ne kadar olacağı belirtilmemiştir. Bu, karakteri
ele alan, genelde de metin editörü ya da IDE editörü olmaktadır, programa
bağlıdır. TAB karakterinin görsel olarak ne kadar boşluk karakterine karşılık
geleceği ayarlanabilmektedir. Tipik kullanılan değerler 2, 4, 8 gibi
değerlerdir. Bazı editörler bağlamdan bağımsız olarak TAB'a basıldığında hep
sabit bir boşluk görüntüsü oluşturur. Bazı editörlerde ise daktilolarda bulunan
*tab stop* mantığı bulunur. [^6f] Bu mantıkta TAB karakterinin görsel olarak ne
kadar boşluk yaratacağı içeriğe bağımlıdır. Örneğin TAB boşluk ayarı 4 karakter
ise TAB'a bastığımızda imleç 4'ün katlarına gider: 4, 8, 12.
Örneğin bir sözcük 3. karakterde bitiyorsa biz TAB'a orada basarsak imleç 4.
karaktere zıplar, yani 1 karakter zıplar. Tekrar basarsak bu sefer 4 atlayarak
8'e gider.

Sık tercih edilen bir durum da TAB tuşuna basılınca editörün TAB karakteri
yerleştirmek yerine önden ayarlanmış bir sayıda otomatik olarak SPACE karakteri
yerleştirmesidir. Burada yine *tab stop* mantığı ile "akıllıca" çalışabilir.
Yani yine içeriğe göre kaç adet SPACE karakterinin otomatik olarak
yerleştireceği değişkenlik gösterebilir.

```{hint}
Burada girmek istemiyorum ama [TAB vs
SPACE](https://www.google.com/search?q=tab+vs+space) tartışmalarına
bakabilirsiniz.
```

---

TAB vs SPACE konusunda Python'da önerilen şey SPACE kullanımıdır. Python,
aslında her ikisini de destekler. İlerleyen bölümlerde Python'da bu
karakterlerle yapılan hizalamaların, indentation, önemli olduğunu göreceğiz.
Fakat bir programda ikisinin karıştırılmasına izin verilmez. Eğer eski bir kodu
idame ediyorsak ve TAB kullanıldıysa TAB ile devam edebiliriz. Ama yeni kodlarda
önerilen ve Python IDE'lerinin hemen hemen hepsinin seçtiği yöntem SPACE
kullanımıdır. Yani editörümüzü TAB tuşuna basınca otomatik olarak SPACE
basmasını ayarlamalıyız. [^7f] [^8f]

---

Python'da white space karakterleri birer atom kategorisi **değildir.**
Boşluklar, atomları birbirinden ayırmada anlamlı olmaktadır. Burada tabii `LF`
gibi *line terminator* karakterleri atom olarak da değerlendirilebilmektedir.
Ama bu detayı geçebiliriz fakat satır sonu belirteçlerinin C gibi bazı programlama
dillerinin aksine Python'da daha anlamlı olduğunu birazdan göreceğiz. [^9f]

## Statement, Deyim Kavramı

Programlama dillerinin hemen hemen hepsinde olan bir kavramdır. Programlama
dillerindeki çalıştırma birimlerine deyim yani statement denilmektedir. Dile iş
yaptırmaya yönelik cümleler gibi de düşünebiliriz. Bunların detaylarına daha
sonra değiniriz. Örneğin `if statement`, `expression statement` gibi alt
kategorileri vardır.

## Expression, İfade Kavramı

Sabitlerin (literals) tek başına ya da değişkenlerin tek başına ya da
operatörlerle beraber oluşturdukları birim bir ifade yani expression olmaktadır.
Bir diğer alternatif tanım da tek başına operatörler hariç değişkenlerin,
sabitlerin ve operatörlerin her türlü kombinasyonunun oluşturduğu birimdir.
Tek başına operatörler bir ifade oluşturmaz.

```python
a + 3 - 8  #ifadedir
print(a)   #ifadedir
a          #tek başına değişken de ifadedir
```

Bir ifade, deyim haline gelince ifadesel deyim yani **expression statement**
oluşur. Python'da bir ifadeyi bir satıra yazdığımızda onu deyim yapmış oluruz.
Yukarıdaki örnek kod parçasındaki her satır aslında bir deyimdir ve tam adıyla
ifadesel deyimdir.

Burada Python dili, C dilinden ayrılmaktadır. Aşağıdaki C koduna bir bakalım.

```c
x = 5;
y = 4 + x;
```

C dilinde `x = 5` ve `y = 4 + x` birer ifadedir. Fakat bunları deyimleştirmek
için yani expression statement haline getirmek için `;` atomu eklememiz gerekir.
Python'da ise alt satıra geçmek yeterlidir, `;` atomuna gerek yoktur. Aynı
kod

```python
x = 5
y = 4 + x
```

şeklinde Python'da yazılabilir. Alt satıra geçme adeta C'dek `;` etkisini
yaratmaktadır. Hatırlarsanız birkaç paragraf üstte alt satıra geçmemizi sağlayan
*line terminator* karakterlerinin diğer white space karakterlerden aynı bir
kategoride olduğunu belirtmiştim.

---

Mesela aşağıdaki kod, C dilinde geçerlidir:

```c
a =
  b
  +
  c
;
```

Burada sürekli alt satıra geçmemizin herhangi bir mahsuru yoktur. İfadenin
bittiği, `;` atomu ile anlaşılmaktadır.

> C dili için ilginizi çekebilir: [](../c/cevirim-asamalari.md)

Oysa aynı kod Python dilinde geçersizdir. Çünkü Python dilinde alt satıra
geçmenin bir anlamı vardır. Satır sonunda bastığımız ENTER karakteri platforma
göre `CRLF` ya da `LF` olarak dosyaya kaydedilir ve Python tarafından bu
yeni satıra geçme işlemi ifadenin bittiği anlamında kullanılır. C'de ise
bunu yapmak için `;` karakterini kullanmamız gerekir.

---

İşte bu yüzden Python'da `;` karakterini kullanmaya gerek yoktur. Ama aynı
satırda birden fazla ifade yazmak için kullanılabilir.

```python
a = 10; b = 20   # Geçerli
a = 10; b = 20;  # Geçerli ama yaygın değil
```

Python'da satırın sonuna `;` koymak kural ihlali oluşturmaz ama genel geçer
kullanımı olan bir şey de değildir.

````{note}
C, C++ gibi dillerde bulunan **en uzun atom kuralı** yani **maximal munch**
kuralı Python'da da geçerlidir. Ama Python'da `++` gibi operatörler olmadığı
için bu kural pek önümüze çıkmaz.

```python
a>=b  # a> anlamsız olduğu için a >= olarak tokenize ediliyor.
```

[Python
dokümantasyonu](https://docs.python.org/3/reference/lexical_analysis.html#other-tokens):
*Where ambiguity exists, a token comprises the longest possible string that
forms a legal token, when read from left to right.*

Maximal munch ile ilgili daha detaylı bilgi: [](../c/cevirim-asamalari.md)

SPACE gibi karakterler bu tarz durumlarda bizim beklentimiz ile tokenizer'ın
çalışma biçiminin aynı olmasında bize yardımcı olurlar 🙂
````

[^1f]: <https://docs.python.org/3/reference/lexical_analysis.html#keywords>
[^2f]: <https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords>
[^3f]: <https://docs.python.org/3/reference/lexical_analysis.html#operators>
[^4f]: <https://docs.python.org/3/reference/lexical_analysis.html#delimiters>
[^5f]: <https://discussions.apple.com/thread/255505463?sortBy=rank>
[^6f]: <https://www.quora.com/How-do-tab-stops-work-on-a-typewriter>
[^7f]: <https://peps.python.org/pep-0008/#tabs-or-spaces>
[^8f]: <https://stackoverflow.com/q/120926/1766391>
[^9f]: <https://docs.python.org/3/reference/lexical_analysis.html#other-tokens>
