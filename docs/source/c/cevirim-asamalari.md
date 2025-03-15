---
giscus: 1c100800-9bf7-4b6b-9cce-5eedb05d6c13
---

# 🔨 Translation Phases - Çevirim Aşamaları

Bu yazıda bir C programı *çevirilirken* olanlara biraz daha detaylı bakacağız.
Okumadıysanız önce [](derleme.md) yazısını okumanızı öneririm.

Burada *çevirim* kelimesini İngilizce *translation* kelimesinin karşılığı olarak
kullandım. Bilgisayar dünyasında *translator* kelimesi kullanılmaktadır.
Translator, bir programlama dilini başka bir programlama diline çeviren araç
anlamındadır. Eğer bu süreçte hedef dil, düşük seviyeli dil ise o zaman bu işi
yapan translator'lara compiler adını vermekteyiz. C'de de C kodları, (en) düşük
seviyeli bir hedef olan saf makina diline dönüştürülmektedir. Bu yüzden bu işlem
*compilation* olarak adlandırılır fakat aynı zamanda bir *translation* işlemi de
yapılır.

Peki bu aşamada bir C dosyasının başına neler gelmektedir?

```{note}
Birazdan bahsedeceğimiz adımlar derleyici tarafından takip edilmelidir. Fakat
derleyiciler isterlerse bu adımların bazılarını birleştirip tek bir adım olarak
yapabilirler. Önemli olan aşağıdaki sıranın bozulmadığını garanti etmektir. Biz
programcılar olarak derleyicinin nasıl gerçekleştirildiğinden bağımsız olarak
aşağıdaki sıranın takip edildiğini varsayabiliriz.
```

## Faz 1

İlk olarak kaynak kodda bulunan byte'lar, ki bu kaynak kod bir metin dosyası
olmaktadır tipik olarak ve UTF-8 gibi multibyte karakter kodlaması içerebilir,
*source character set* te bulunan karakterlere "implementation-defined" olarak
eşlenmektedir. Yani daha anlaşılır anlatımla, kaynak kodun içerisindeki byte'lar
karakter kodları olarak anlamlandırılır. Bu eşleşme, mapping, kullanılan
karakter kodlama sisteminin bir sonucudur.

Bknz: [](character-set.md)

*Source character set* bir multibyte character set'tir ve 96 karakterden oluşan,
single-byte olarak oluşturulmuş *basic source character set* i içermelidir.

```text
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
a b c d e f g h i j k l m n o p q r s t u v w x y z
0 1 2 3 4 5 6 7 8 9
! " # % & ' ( ) * + , - . / : ; < = > ? [ \ ] ^ _ { | } ~
<Space> <TAB> <VT> <FF> <LF ?>
```

```{note}
Bu karakterlerin toplam sayısı 96 yapmaktadır. Ama C standardlarına göre `0x0A`
kodlu `LF` karakteri *basic source character set* içerisinde değildir. Ama
iyice suyunu çıkartmayalım artık...

> Unlike C++, the U+000A LINE FEED (LF) character is not included in basic
> character set. Instead, there shall be some way of indicating the end of each
> line of text in the source file and the document treats such an end-of-line
> indicator as if it were a single new-line character.
>
> Basic character set is also known as basic source character set.


[REF](https://en.cppreference.com/w/c/language/charset)
```

Burada bizim için önemli olan noktalardan biri de kaynak dosyadaki işletim sistemi
spesifik satır sonu belirteçlerinin, Windows'ta `CRLF` gibi, Linux'ta `LF` gibi
*newline karakterleri*ne dönüştürülmüş olmasıdır. Bildiğim kadarıyla C standartları
*newline karakterleri* konusunda net bir açıklama yapmıyor, bunu biraz soyut bir
kavram olarak bırakıyor. Ama `LF` olarak düşünmek de bence çok yanlış değil.
Özetle kodu yazdığımız platformdan, Windows/Linux/Mac, bağımsız olarak satır
sonları anlaşılıyor diyebiliriz.

Daha sonra *trigraph sequence* dediğimiz `??x` formundaki 3'lü karakter grupları,
tekli karakter gösterimlerine çevrilir. Bu olay C23 ile kaldırılmıştır. Zaten
kim artık buna ihtiyaç duyuyordur bilmiyorum. Bknz: [](character-set.md)

## Faz 2

Eğer bir satırın sonunda ters bölü karakteri `\` ve hemen arkasında
*newline character* varsa, yani satır sonunda `\` varsa ve hemen alt satıra
geçtiysek burada iki karakter birden silinir ve iki satır birleştirilmiş
olur. Bu işlem bir kere yapılır, iteratif olarak bitene kadar yapılmaz.

```c
#define PUTS p\
u\
t\
s

//alttakiyle eş değer
#define PUTS puts
```

```text
//Sentaks hatası, birden fazla tur dönülmüyor çünkü
x = 5;\\

y = 4;
```

C kurallarına göre boş olmayan bir kaynak kod dosyası, *newline character* ile
bitmelidir. Eğer bu işlemden sonra yani `\` işledik diyelim, dosya sonunda
*newline character* yoksa **bu tanımsız davranış, UB** oluşturmaktadır.

## Faz 3

Burada dosya artık işlenerek adeta "parçalanır". Dosya yorumlar, whitespace
karakterlere yani `SPACE`, `TAB`, `LF`, `VT`, `FF`, ve token yani atomlara
ayrılır. Atomlara ayrılırken başlık dosyaları, header file isimleri,
identifier'lar, sabitler vs belirlenir.

**Her bir yorum tek bir boşluk, `SPACE`, karakteri ile yer değiştirilir.**

*New line* karakteri tutulur. New line karakterinden oluşmayan whitespace
sekanslarının birleştirilip tek bir space karakterine düşürülüp düşürülmeyeceği
**implementation defined** bir durumdur.

```{note}
Buradaki ayrılan tokenların tam doğru adı aslında *preprocessing token* dır ve
*C token*lardan biraz farklıdır. Daha preprocessor yani ön işlemci çalışmadı
farkındaysak. Ama iki token kategorisi arasındaki farka girmeyelim.

[REF](https://www.gnu.org/software/c-intro-and-ref/manual/html_node/Preprocessing-Tokens.html)
```

---

Burada önemli bir kural olan **maximal munch** kuralından söz etmeden olmaz.
Derleyici, token oluştururken yani kaynak koddaki karakterleri anlamlandırırken
karakterlerden en uzun parçalardan bir token oluşturmaya çalışır, devamında
bu bir sentaks hatası yaratacak olsa bile. Örneğin:

```c
int main(void)
{
    int x = 1, y = 2, z;

    z = (x++)+(++y);
}
```

gibi bir kod yazdık diyelim. Burada `z` nin değeri `4` olacaktı. Eğer öncelik
parantezlerini kullanmasaydık yani `z = x+++++y;` yazsaydık bu bir sentaks
hatası oluşturacaktı. Çünkü bu kuralara göre bu ifade `z = x++ ++ +y;` olarak
atomlarına ayrılacaktı, bu da geçerli bir sentaks değildir. Derleyici burada
*ya bu sentaks hatası olur, başka türlü yapayım* demiyor işte... 🤷

```c
int x = 10/*Bu yorum tek bir boşluk karakteri olacak*/+ 5; //OK, 10 + 5;
int x = y+++z; //OK, y++ + z;
int x = y++-++z; //OK y++ - ++z. -+ diye operatör yok çünkü.
int x = y+++ ++z; //OK y++ + ++Z;
int x = y+++/*tek boşluk olacak, üstteki ile aynı*/++z; //OK
```

Buna tek istisna `#include` dışındaki yerlerde `<>` karakterlerinin *header name
preprocessing token* oluşturmamasıdır. Yani derleyici her herde `<>` görünce
"atlamaz"

```c
#define MACRO_1 1
#define MACRO_2 2
#define MACRO_3 3
#define MACRO_EXPR (MACRO_1 <MACRO_2> MACRO_3) // OK: <MACRO_2> is not a header-name
```

## Faz 4

Bu aşamada ilk olarak önişlemci yani **preprocessor** çalışır. Eğer `#include`
önişlemci komutu ile dahil ettiğimiz dosyalar varsa her bir dosya için recursive
olarak, `#include` edilen dosya başka dosyaları da `#include` ediyor olabilir,
Faz 1-4 arası çalıştırılır.

**Bu aşamanın sonunda kaynak kodda hiçbir önişlemci komutu yani `#` ile
başlayanlar kalmaz.**

## Faz 5

Bu aşamada *source character set* ten, *execution character set* e çevrim
yapılır.

Bknz: [](character-set.md)

Source charactet set, bizim kodu yazdığımız bilgisayarda kullanılan karakter
seti iken execution character set, derlenmiş programın çalışacağı bilgisayarın
karakter setidir. Günümüzde belki çok anlamlı olmasa da örneğin ASCII karakter
kodlaması kullanılan bir bilgisayarda kodumuzu geliştiriyor ve derlenen kod
[EBCDIC](https://en.wikipedia.org/wiki/EBCDIC) kodlamasını kullanan bir
bilgisayarda çalışıyor olabilirdi. Kaynak kodda gördüğümüz yazıların, örneğin
*string literal*ların, hedef bilgisayarda da kod çalışınca düzgün gözükmesi için
bu çevrimin yapılması gerekmektedir.

Bu çevrim karakter sabitlerinin, `'a'` gibi, ve string literallerin, `"alper"`
gibi, içerisindeki karakterlerin ve *escape seqeunce*ların, `\n` gibi, tümünü
kapsamaktadır.

Execution character seti'nde bahsettiğimiz temel 96 karakterden oluşan, `<LF>` ?,
*basic source character set* bulunmalı ve 1-byte ile ifade edilmelidir. Diğer
karakterler UTF-8 gibi multi-byte olabilirler.

Eğer *escape sequence* ile belirttiğimiz bir karakterin execution character
set'te bir karşılığı yoksa bu çevrimin nasıl yapacağı implementation-defined
bırakılmıştır. Fakat bu dönüşüm sonucunda *null character* elde edilmeyeceği
garanti edilmiştir (sanıyorum wide karakterlerde de böyle)

Bu çevrim, GCC ve Clang'in desteklediği `-finput-charset`, `-fexec-charset`,
`-fwide-exec-charset` flagleri ile kontrol edilebilmektedir.

## Faz 6

Ard arda gelen *string literal*ler birleştirilir ve tek bir *string literal*e
dönüştürülür.

```c
#include <stdio.h>

int main(void)
{
    puts("Alper" "Yazar"); // Tek bir string literal "AlperYazar"
    return 0;
}
```

Yukarıdaki kod bu sebebpten dolayı `puts("AlperYazar")` ile eşdeğerdir. Bu,
garip bir özellik gibi gelebilir ama C'de idiomatic kod yazarken kullanışlı
olduğu trickli yerler vardır.

## Faz 7

Derleme işlemi artık yapılır. Her bir kaynak kod, daha doğrusu *translation
unit*, bağımsız olarak derlenir. String literallerin sonuna *terminating null
character* konması ve string literallerin statik ömüre sahip isimsiz bir
array olarak tutulması işlemi de bu aşamada yapılır. [^1f]

## Faz 8

Derleme işlemi bitip, elimizde obje code'lar oluştuktan sonra linker tüm
bağımsız derlenmiş çıktıları birleştirir ve bir adet dosya oluşur.

Özellikle Faz 7 ve 8 adımları [](derleme.md) yazısında daha detaylı
anlatılmıştır.

## Kaynaklar

- <https://en.cppreference.com/w/c/language/translation_phases>
- <https://stackoverflow.com/q/18379848/1766391>

[^1f]: <https://en.cppreference.com/w/c/language/string_literal>
