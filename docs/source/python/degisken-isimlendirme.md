---
giscus: 20417d4b-bc0a-4fc8-82ba-a878190d30c8
---

# Değişken İsimlendirme Kuralları

Diğer programlama dillerinde olduğu gibi Python'da da değişken isimlendirme
ile ilgili uyulması gereken çeşitli kurallar vardır.

1️⃣ Değişken isimleri rakamla başlayamaz, alfabetik karakterlerle başlatılmalıdır.
İlk karakter dışında diğer karakterler rakam olabilir. Alt tire, `_`, karakteri
alfabetik karakter olarak sayılmaktadır.

```text
1x = 4 # Hata, 1 ile başlayamaz
x1 = 4 # Uygun
(x = 4 # Hata, ( ile başlayamaz
_x = 4 # Uygun
```

2️⃣ Değişken isimleri anahtar sözcük olamaz. (Bknz:
[](token-keyword-expression-white-space.md))

```text
while = 4 # Hata, while bir anahtar sözcüktür.
```

3️⃣ Değişken isimleri boşluk karakterlerini içeremez.

```text
my variable = 4 # Hata
```

4️⃣ Değişken isimleri operatör karakterlerini içeremez.

```text
my+variable = 4      # Hata
benim-degiskenim = 4 # Hata
```

5️⃣ Python **case-sensitive** bir dildir, küçük/büyük harf duyarlılığı vardır.
C, C++, Java, C# da böyledir fakat Pascal, Basic, Fortran böyle değildir, onlara
*case-insensitive* diyoruz.

```text
>>> x = 4
>>> X
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'X' is not defined. Did you mean: 'x'?
```

*Did you mean? de diyor!*

6️⃣ Python 3 ile UNICODE desteği değişken isimlerine de gelmiştir. Türkçe
karakter içeren değişkenler yaratabiliriz. Buradan böyle yapmalıyız anlamı
çıkmasın elbette.. Ayrıca değişken isimlendirmede tüm UNICODE karakterler
kullanılabilir anlamı da çıkmasın. [^1f]

```text
benim_değişkenim = 4 # Uygun
😊 = "gülen yüz"     # 😊 değişken adı olamıyor, UNICODE full desteklenmiyor
değişken = "😊"      # Uygun
```

7️⃣ Python, Python Language Reference, değişkenlerin maksimum uzunluğu konusunda
bir şey söylememektedir. Burada genelde ilgili Python implementasyonunu yazan
kişilerin, CPython, PyPy gibi belirlediği içsel bir limit olacaktır. Örneğin
değişken isimlerin ilk N karakteri dikkate alınıyor olabilir. Ama pratikte
buralara takılmamamız lazım. Bu kadar uzun karakterli değişken isimleri
kullanmıyor olmalıyız. Tipik olarak 256 karakter uzunluğa kadar isimler
sorunsuzca desteklenecektir ama böyle uzun isimler kullanmamalıyız.

## Naming Conventions, Coding Conventions, İsimlendirme/Kodlama Stilleri

Değişken isimlendirmede boşluk karakterlerini kullanamıyoruz. Kod
okunabilirliğini aynı projelerde çalışan geliştiriciler arasında da arttırmak
için programlama dünyasında süregelen çeşitli isimlendirme kuralları vardır. Bu
kurallar dilin doğru çalışması için gerekli değildir. Daha çok kodların rahat
okunması için vardır. Her dilin sahiplendiği ve genel geçer doğru kabul ettiği
tarzlar, dilden dile değişebilir.

### Snake Case 🐍

Klasik C tarzı da denmektedir. C, Python, Rust, SQL gibi dillerde kullanımı
yaygındır. Sözcüklerin arasında `_` konur.

```python
benim_degiskenim
file_name
user_intput_data
MAX_CONNECTIONS
```

gibi..

### Kebab Case 🌯

Snake Case'e benzer. İsimler arasında `_` yerine `-` kullanılır. **Python'da
değişken isimlerinde `-` bulunamadığı için kullanılamaz.** Fakat programlama
dünyasında CSS ve JavaScript framework'lerinde tercih edilebilmektedir.

### Camel Case 🐫

Burada ilk sözcüğün tamamı küçük harf yazılır. Sonraki sözcüklerin ilk harfi
büyük, devamı küçük yazılır. Sözcükler arasında boşluk bırakılmaz. Bu tarza
*lowerCamelCase* de denmektedir.

```python
benimDeğişkenim
fileName
userInputData
```

gibi. Java'da sık tercih edilir.

### Pascal Case

Camel Case'e benzer. Farkı, ilk harfin de büyük harf olmasıdır. Bazen
*UpperCamelCase* de denmektedir.

```python
BenimDeğişkenim
FileName
UserInputData
```

gibi.

## Hangisini kullanalım?

Python'da C tarzı isimlendirme yani snake case sıklıkla tercih edilir. Python
case sensitive bir dil olsa da genelde küçük harf kullanılır. Sembolik sabit
görevindeki değişkenler, yani C'deki `#define` ile tanımlanan makrolarla aynı
amacı taşıyanlar, genelde BÜYÜK HARF ile yazılır. Sınıf isimlendirmelerinde
PascalTarzı da tercih edilebilmektedir.

Google Python Style Guide, snake_case önermektedir. [^2f] [^3f] Ama örneğin
Python'da QT ile çalışıyorsak o kütüphane Camel Casting tercih ettiği için
kendi kodumuzu da ona uydurmamız mantıklı olabilir.

Değişken isimlendirmelerinde Türkçe karakter kullanabilsek de genelde önerilen,
diğer dillerde de, değişken isimlerinin İngilizce isimlendirilmesidir.

[^1f]: <https://stackoverflow.com/a/21867836/1766391>
[^2f]: <https://google.github.io/styleguide/pyguide.html#316-naming>
[^3f]: <https://stackoverflow.com/a/8423697/1766391>
