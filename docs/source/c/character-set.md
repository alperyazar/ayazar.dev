# 🔤 Character Set(s) - Karakter Set(leri)

C programı yazma dediğimiz şey, çoğu zaman klavyeden çeşitli tuşlara basarak
metin dosyaları oluşturma, bunları `.c` veya `.h` dosyaları olarak kaydetme ve
derleme işidir. Yazdığımız programların önemli bir kısmı da çalışma sırasında
yazılar ya da harfler üzerinde işlemler yapar. Hem kod yazma hem de yazılan
kodun çalışması sırasında *yazı* konusu birçok noktada işin içindedir. **İşte bu
yüzden, C standartları derleyici yazanlar için çeşitli yazılar, daha doğrusu
yazıları oluşturan karakterler üzerine çeşitli kurallar getirmiştir.**
Programcıların önemli bir çoğunluğu için bu detaylar önemli değildir. Özellikle
yeni başlayan kişilerin bu detaylarla boğulmasını şahsen tavsiye etmem. Ama konu
bütünlüğü olması açısından ben biraz değinmek istiyorum.

İki tür karakter seti tanımlanmıştır: **Source Character Set** ve **Execution
Character Set**. *Source* adından da anlaşılacağı gibi C programlarının kaynak
kodlarında yani programın metin halinin kendisinde bulunan yazılarla ilgilidir.
Kaynak kodların yazımı ile ilgili kuralları belirler. *Execution* yani çalışma
olan ise derlenmiş programın çalıştığı ortam hakkındaki kuralları belirler.

**Execution Character Set** in içerisindeki karakterlerin *değerlerinin* yani
nümerik karşılıklarının ne olacağı **implementation-defined** olarak
bırakılmıştır.

## Basic ve Extended Karakterler

Her iki karakter seti de iki ayrı bileşenden oluşur: **Basic Character Set** ve
bu karakter setinde olmayan (varsa) karakterleri içeren **Extended Characters**.
*Extended Characters* dediğimiz karakterler tipik olarak *yerel* karakterleri
içerir, örneğin Türkçe'de bulunan `ş`, `ğ`. `ö` harfleri gibi. Ya da Uzakdoğu
Dilleri'ni bu şekilde de düşünebiliriz. İki setin birleşimine de
**Extended Character Sets** adı verilir.

## Escape Sequence

C'de `'x'` şeklindeki sabitlere **karakter sabiti** yani **character constant**
ve `"XYZ"` şeklindeki yazılara da **string literal** demekteyiz. C
standartlarına göre execution character set'i içerisindeki karakterler,
character constant veya string literal içerisinde ya doğrudan source character
set'teki bir karakter tarafından ya da `\` karakteri ile başlayıp ardında bir
veya birden fazla karakter içeren **escape sequence** ler tarafından
gösterilebilmelidir. C programlarında sıklıkla gördüğümüz `\n` gibi yazılar
birer escape sequence örneğidir. Yani özetle, kaynak kodunda bir şekilde
execution character set'indeki karakterleri gösterebiliyor durumdayız.

## Null Character

Standartlara göre, tüm bitleri `0` olan bir byte **null character** i temsil
etmektedir. Null character'in *execution character set* içerisinde bulunması
zorunlu olup bir karakter string'inin bittiğini göstermek için kullanılır.

```{important}
Null Character ile Null pointer'ı karıştırmayın.
```

## Basic Source ve Execution Character Sets

Standartlara göre hem source hem de execution ortamında basic character set
şu karakterleri içermelidir:

```text
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
a b c d e f g h i j k l m n o p q r s t u v w x y z
0 1 2 3 4 5 6 7 8 9
! " # % & ' ( ) * + , - . / : ; < = > ? [ \ ] ^ _ { | } ~
```

Yukarıdakilerin sayısı: `26 + 26 + 10 + 29`

Bunların dışında space `ASCII: 0x20`, horizontal tab `ASCII: 0x09`, vertical tab
`ASCII: 0x0B` ve form feed `ASCII: 0x0C`.

Hem source hem execution basic character set'in içerisindeki karakterlerin hepsi
**1 byte'a sığmalıdır.** Ayrıca `0` ı temsil eden karakter kodunun değerini 1
arttırınca `1` karakterine, onu da 1 arttırınca `2` karakterine yani koduna
erişmeliyiz. Bu `0-9` arası sağlanmalıdır. Dikkat ederseniz standartlar hala
ASCII gibi karakter kodlama standartlarından bahsetmiyor.

---

Kaynak kodlarda yani source set içerisinde satır sonlarını belirten
*belirteçler* olması gerekmektedir. C standartları bunların hepsini tek bir
new-line karakteri , `ASCII: 0x0A`, olarak kabul etmektedir. Örneğin Windows
sistemlerde satır sonlarında `\r\n` bulunduğu için burada yazdığımız C kodları
içerisindeki bu satır sonu *belirteçleri* aslında derleyici tarafından `\n`
olarak ele alınır diyebiliriz.

---

**Basic Execution Set** içerisinde bunların dışında *alert* `ASCII: 0x07`,
*backspace* `ASCII: 0x08`, *carriage return* `ASCII: 0x0D` ve *new line*
`ASCII: 0x0A`gösteren **kontrol karakterleri** yani **control characters**
olmalıdır.

---

Kaynak kod içerisinde isimler (identifier), character constant, string literal,
header isimleri, yorum blokları, (C) token'a dönüşmeyen preprocessor'e ait
tokenlar dışında bu belirtilen karakterler dışında karakterlerin kayna kodda
olması derleyici açısından **undefined behavior** oluşturmaktadır.

```text
x = x @ 2; //gibi, UB. Derleyici sentaks hatası vermeyip saçmalayabilir.
           //          pratikte günümüz derleyicileri hata verip duracaktır.
```

---

C standartları yukarıda belirtilen ve İngilizce'de bulunan 26 adet küçük ve
26 adet büyük karakter dışında, diğer dillerde bulunabilen karakterleri
**harf yani letter olarak kabul etmemektedir.**

## Trigraph sequences `??x`

Eskilerden gelen böyle bir şey geriye dönük uyumluluk olarak var. C23 standartı
ile beraber bu destek kaldırıldı [^1f]. Zaten bunun günümüzde kullanılma
ihtimali bence sıfıra yakın. Yine de ne olduğuna bakalım.

[ISO/IEC 646](https://en.wikipedia.org/wiki/ISO/IEC_646) isminde tarihsel açıdan
anlamlı bir encoding standartı var. Bunun içerisinde de *invariant characters*
isminde bir set tanımlanmış durumda. Bu set, uluslararası anlamda birçok ülke
tarafından kabul görmüş ve paylaşılan bir set. Fakat C kodları yazarken
kullanmamız gereken fakat bu karakter setinde olmayan bazı karakterler var.
Günümüzde bunları doğrudan klavyemizden basabiliyoruz. Ama takdir edersiniz ki C
dilinin geçmişi 70'li yıllara dayanıyor ve o yıllarda bu *ekstra* karakterleri
yazabilen klavyeler, gösterebilen ekranlar ya da transfer edip depolayabilen
sistemler olmayabilir diye C standartlarında *trigraph sequences* diye bir şey
tanımlanmış. Bu sekanslar gerçekten de 3 karakter den oluşuyor, yani klavyede 3
karaktere basıyorsunuz, ama derleme sırasında tek bir başka karaktere denk
geliyorlar. Tablo olarak veriyorum:

| Trigraph Sequence | Karşılığı |
| ----------------- | --------- |
| `??=` | `#` |
| `??(` | `[` |
| `??/` | `\` |
| `??)` | `]` |
| `??'` | `^` |
| `??<` | `{` |
| `??!` | `\|` |
| `??>` | `}` |
| `??-` | `~` |

Bu 9 sekans dışında başka sekans tanımlı değildir. Bununla ilginç örnekler
yapılabilir:

```{code-block} c
:emphasize-lines: 1, 4
:lineno-start: 1
??=include <stdio.h>

int main(void) {
    puts("??(merhaba-dunya??)"); //"[merhaba-dunya]"
    return 0;
}
```

Yukarıdaki kodda 3 adet trigraph seqeunce vardır. Bunları sırası ile `#`, `[` ve
`]` ile değiştirilecektir. Dikkat ederseniz preprocessor öncesi yapıldığı için
`#include` çalışmaktadır. Fakat bu kodu GCC default ayarlarla derlememekte,
`-trigraphs` bayrağı geçmek gerekmektedir. Dediğim gibi, günlük yaşantıda
kullanacağınız bir özellik değil.

## Kaynaklar

- [](resources.md)
- <https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf> Section 5.2

```{todo}
Multi-byte ve wide character konusunda yazı yazabilirsin.
```

[^1f]: <https://en.wikipedia.org/wiki/C23_(C_standard_revision)>
