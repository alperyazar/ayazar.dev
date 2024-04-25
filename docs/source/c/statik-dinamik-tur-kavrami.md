---
og:description: "C ve Python örnekleri ile statik ve dinamik tür kavramına bakıyoruz"
giscus: c6e98e12-1592-4b76-b2c1-d108ab215cb9
---

# Programlama dillerinde Statik ve Dinamik Tür kavramı

Programlama dillerinin (neredeyse ?) tamamında bir tür kavramından
bahsedebiliriz. **Tür**, İngilizce **type** kelimesinin karşılığıdır. Genelde
tüm programlama dillerinde, yazılan kodda tanımlanan değişkenlerin, sabitlerin,
oluşturulan ifadelerin birer türleri vardır. Dillerdeki tür ile ilgili
kavramları kapsayan çatı terim ise **Tür Sistemi** yani [Type
System](https://en.wikipedia.org/wiki/Type_system)'dir.

Dilde türe sahip olan değişken (nesne), ifade gibi kavramların türleri, eğer
derleme sırasında belirleniyorsa o diller **statically typed** yani statik türlü
ya da statik türe sahip olan dil, eğer çalışma sırasında (run time)
belirleniyorsa da dil **dynamically typed** yani dinamik türlü ya da dinamik
türe sahip olan dil olarak adlandırılır. İlk paragrafta da belirttiğim gibi
*type* kelimesinin buradaki Türkçe karşılığı *yazmak* değil *tür* dür. Statik ve
dinamik kelimeleri de *değişmeyen/sabit* ve *değişen/sabit olmayan*
anlamlarından ziyade (yazının ilerleyen kısımlarında aslında bunu da ima
ettiklerini göreceğiz) *derleme zamanında* ve *çalışma zamanında* anlamındadır.
Nasıl derleme zamanında bağlanan kütüphanelere *statically linked library*,
çalışma zamanında bağlanan kütüphanelere de *dynamically linked library*
diyorsak buradaki kelimeler de bu anlamdadır.

---

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD013 MD033 -->
<center>
<iframe src="https://giphy.com/embed/ule4vhcY1xEKQ" width="360" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/reactionseditor-cat-typing-ule4vhcY1xEKQ">via GIPHY</a></p>

<mark>Type derken bunu kastetmiyoruz…</mark> catly typed languages 🐈
</center>
<!-- markdownlint-restore -->

---

Biraz daha **genelleştirelim...**

| Özellik | Statik | Dinamik |
| :-----: | :----: | :-----: |
| **Türlerin belirlenme zamanı** | derleme zamanı (compilation time) | çalışma zamanı (run time) |
| Tür ile ilgili kontroller | derleme zamanı (compilation time) | çalışma zamanı (run time) |
| Tür ihlali bildirimleri | derleme hataları ve uyarıları | istisna üretilmesi (exception throwing) |
| Derlenen / Yorumlanan | derlenen (compiled) diller | yorumlanan (interpreted) diller |
| Değişkenlerin tür bildirimleri | açıkça (explicit) | örtülü (implicit), çıkarımlı (inferred) |
| Değişken türleri | sabittir, değişmez | sabit değildir, değişebilir |

Bu konudaki temel tanım, türlerin ne zaman belirlendiğidir, yani tablodaki ilk
satır. Diğer satırlar ise ilgili dillerin sahip oldukları genel geçer, tipik
özellikleridir. Yüzlerce programlama dili olduğunu düşünürsek tüm satırların tüm
diller için geçerli olduğunu söylemem fazla iddialı olabilir ama pratikte bu
şekilde olduğunu düşünmek de sizi fazla yanıltmayacaktır.

**C, C++, Java** gibi diller **statik** tür kavramına sahip iken, **JavaScript,
Python, PHP** gibi diller ise **dinamik** tür kavramına sahiptir [^1f] [^2f].
Şimdi gelin, C ve Python dillerinden örneklerle konuyu biraz daha anlayalım.

## Python, Dinamik Tür Kavramına Örnek

Python dilinde `type()` isimli fonksiyon ile bir nesnenin türünü öğrenebilmek
mümkündür. Aşağıdaki koda bir bakalım:

```python
x = 3
print (type(x))
x = "alper"
y = x + " yazar"
print (type(x))
x = 3.5
print (type(x))
y = x + " yazar"
```

Çıktı da şu şekilde olmaktadır:

```text
<class 'int'>
<class 'str'>
<class 'float'>
Traceback (most recent call last):
  File "<string>", line 8, in <module>
TypeError: unsupported operand type(s) for +: 'float' and 'str'
```

Durumu bir değerlendirelim:

- `x` değişkenin türü farklı türden değerler atayarak örtülü olarak belirlenmiş
  ve değişmiştir. `x` değişkenini tanımlarken açıkça türünü belirtmedik, ona
  atanan değere göre türü otomatik olarak belirlendi.
- `y = x + " yazar"` ifadesi hem satır 4 hem de satır 8 de vardır. İlk ifadede
  bir problem yoktur çünkü ilgili satırda `x` in türü `str` dir ve dilin
  kuralları gereğince  iki string toplanabilir. Fakat, ikinci ifadede hata
  vardır çünkü o noktada `x` in türü `float` tır ve yine dil kuralları gereği
  `str` ile `float` toplanamamaktadır. Çalışma sırasında bir değişkenin türü
  değiştirilebilmiştir.
- Son satırdaki hata ise ancak çalışma sırasında `TypeError` olarak
  yakalanabilmiştir. Peki niye programın çalışmasının başında yakalanamamıştır?
  Çünkü Python dilinde kodlar tipik olarak satır satır çalıştırılır ve hata
  ilgili satır çalıştırıldığı zaman ortaya çıkmıştır.

## C, Statik Tür Kavramına Örnek

Benzer bir örneği C ile yapalım. C dilinde, Python'daki gibi dahili (built-in)
bir `type()` fonksiyonu yoktur. Fakat dile C11 ile gelen *generic selection
expression* [^5f] desteğini bir makro ile kullanarak benzer bir kod oluşturabiliriz
[^3f] [^4f].

```c
// See: https://stackoverflow.com/a/17290414/1766391
// Tested with x86-64 gcc 12.2 with default flags on https://godbolt.org/
#include <stdio.h>
#include <stddef.h>
#include <stdint.h>

#define typename(x) _Generic((x),        /* Get the name of a type */             \
                                                                                  \
        _Bool: "_Bool",                  unsigned char: "unsigned char",          \
         char: "char",                     signed char: "signed char",            \
    short int: "short int",         unsigned short int: "unsigned short int",     \
          int: "int",                     unsigned int: "unsigned int",           \
     long int: "long int",           unsigned long int: "unsigned long int",      \
long long int: "long long int", unsigned long long int: "unsigned long long int", \
        float: "float",                         double: "double",                 \
  long double: "long double",                   char *: "pointer to char",        \
       void *: "pointer to void",                int *: "pointer to int",         \
      default: "other")

int main(void){
    int x;
    double y = 3.4;
    printf("x bir %s\n",typename(x));
    printf("y bir %s\n",typename(y));
    x = y; //Neden hata değil?
    printf("x hala %s\n",typename(x));
    printf("x = %d\n",x);
}
```

Çıktı da şu şekilde olmaktadır:

```text
x bir int
y bir double
x hala int
x = 3
```

Duruma bir bakalım:

- Yukarıda iki farkı değişken tanımladık: `x` ve `y`. Tanımlama sırasında ise
  türleri açıkça belirttik, `x` bir `int` türünden nesne, `y` ise `float`
  türünden bir nesne oldu. Artık bu değişkenlerin türleri programın ömrü boyunca
  sabit kalacaktır.
- Akışın ortalarında bir yerde 3.4 değerini tutan ve `float` türünden olan `y`
  nin değerini bir `int` türden değişken olan `x` e atadık. Peki bu niye problem
  olmadı? Hani türler değişimiyordu? Aslında yine değişmedi, `x` hep `int`. C
  dilinin kuralları gereğince aslında 3.4 bir *implicit type conversion* a yani
  *örtülü tür dönüşümüne* maruz kaldı. Bu atamada sanki değeri 3 olan gizli ve
  geçici bir `int` nesne yaratıldı ve bu nesnenin değeri `x` e atandı. Bu
  otomatik çevrim, dilin statik/dinamik türe sahip olması ile ilgili değildir.
  Otomatik çevrim konusu dilin *weakly/strongly typed* bir dil olması ile
  ilgilidir.
- `x` e ne yaparsak yapalım türünü değiştiremedik.

Hadi bir örneğe daha bakalım:

```c
// Tested with x86-64 gcc 12.2 with default flags on https://godbolt.org/
int main(void){
    int *p1, *p2, *p3;
    p3 = p1 + p2;
}
```

Derleyici çıktısı

```text
<source>: In function 'main':
<source>:3:13: error: invalid operands to binary + (have 'int *' and 'int *')
    3 |     p3 = p1 + p2;
      |             ^
ASM generation compiler returned: 1
```

Peki buradaki sorun nedir? C kuralları gereği pointer türden iki değişken
toplanamaz. Bu davranış konumuz ile ilgili değil. Burada vurgulamak istedğim,
Python'dakinin aksine bir kural ihlalinin derleme sırasında yakalanması. Çünkü
türler derleme sırasında belirlenir ve kurallar hemen kontrol edilebilir. Dikkat
ederseniz derleyici hatasından dolayı daha çalıştırılabilir dosya bile
oluşturamadık. Yani çalışma zamanına dahi gelemedik.

## İlgili

- <https://www.baeldung.com/cs/statically-vs-dynamically-typed-languages>
- <https://medium.com/android-news/magic-lies-here-statically-typed-vs-dynamically-typed-languages-d151c7f95e2b>
- <https://towardsdatascience.com/the-type-system-every-programmer-should-know-c3134a1b9bde>

```{attention}
⚠️ Bu yazının konusu değil ama yukarıdaki kaynakların ikisinde, C++ dili C'den
daha *weakly typed* gösterilmiş. Buna çok emin değilim.
```

Aşağıdaki video JavaScript ile ilgili ama konsepti güzel açıklıyor.

```{youtube} C5fr0LZLMAs
:align: center
:width: 100%
```

## Kaynaklar

- [Necati Ergin](https://github.com/necatiergin/), C Kursu notlarım
- [Kaan Aslan](https://github.com/CSD-1993), C Kursu notlarım

[^1f]: <https://stackoverflow.com/a/1517670/1766391>
[^2f]: <https://developer.mozilla.org/en-US/docs/Glossary/Static_typing>
[^3f]: <http://www.robertgamble.net/2012/01/c11-generic-selections.html>
[^4f]: <https://stackoverflow.com/a/17290414/1766391>
[^5f]: <https://en.cppreference.com/w/c/language/generic>
