---
og:description: "Gözden kaçabilen, masum görünen fakat canınızı sıkabilecek bir C hatası"
giscus: 5c1e250a-1d99-4ec7-971f-bd0ca428aaa8
---

# C programlamada gördüğüm en sık yapılan hata

Gömülü sistemlerle uğraşan biri olarak C dili ile ilgileniyorum. Bu yazıda
oldukça masum duran fakat başımızı derde sokabilecek bir kodlama hatasından
bahsetmek istiyorum. **Yeni öğrenen kişilerin kodlarında (dikkatsizlik
durumunda görece tecrübeli kişilerinkilerde bile) karşıma en sık çıkan C
programlama hatası bu.**

İlk olarak hatalı olmayan bir duruma bakalım. Bir fonksiyonun içerisinde
x isminde bir tam sayı (integer) nesnesi yaratıp, buna daha sonra bir değer
atayalım.

```c
foo()
{
    int x;
    /*...*/
    x = 20;
}
```

Burada hiç bir problem yok. Şimdi de diyelim ki integer tipinde bir gösterici
(pointer) tanımlayalım ve benzer şekilde kodumuzun içerisinde daha sonra değer
atıyor olalım.

```c
foo()
{
    int *y;
    /*...*/
    *y = 10;
}
```

> ⚠️ `x`i nasıl kullandıysak aynı şekilde `y`yi kullandık değil mi?
> **Değil**, geçmiş olsun.

## Bu neden hatalı?

Çünkü, buradaki `x` ve `y` fonksiyon faaliyet alanında (*function scope*)
bulunan otomatik ömürlü (*automatic storage duration*) nesnelerdir. Otomatik
ömürlü nesnelerin ilk değerleri belirsizdir. İnanmazsanız mesela C99
standardının `6.2.4.5` nolu maddesine göz atabilirsiniz (*Storage durations of
objects* başlığı altında). **`x` ve `y`nin içinde başlangıçta ne var
bilmiyoruz! Çöp bir değer var.** Yani `*y=10` ifadesi ile nereyi gösterdiği
belli olmayan bir pointer'ın gösterdiği yere gidip 10 yazmış olduk. `x`
durumunda problem olmamasının sebebi zaten bizim için ayrılmış olan bir yere
bir değer atamamız. Eğer `y`yi güncelliyor olsaydık (`*y` değil, `y`) yine
problem yoktu, derleyici bizim için `y` isminde bir int tipinden pointer
ayırdı, istediğimizi yapabiliriz. AMA gidip *kullanım hakkı* bizim elimizde
olmayan, değeri `y`nin içerisinde olan rastgele bir adrese `*y` ile erişirsek
işte o zaman haddimizi aşmış oluyoruz.

## Bu hatayı neden yapıyoruz?

Dediğim gibi bu hata karşılaştığım en sık hata. Çünkü sanıyorum `x` ile `y`
aynıymış gibi düşünülüyor ve bu hatalı durum oluşuyor. Bunun bir sebebi de
belki şudur: `int *y` ile `*y`yi tanımladık ve `*y`yi kullandık değil mi? Öyle
olmuyor maalesef çünkü buradaki `*`ın iki yerdeki görevi farklı. `y`yi
tanımlarken `int* y` de diyebilirdik, belki o zaman kafalar karışmazdı. Fakat
genelde `int *y` olarak yazılır yani `*` karakteri `y`ye bitişik, `ìnt`e değil.
Kod içerisinde `*y` ile `y` nin gösterdiği yerdeki int değere erişme işlemi de
*dereferencing* olarak adlandırılır. Tanımlama kısmında ise gösterici
(*pointer*) tanımladığımızı söylüyor derleyiciye `*` karakteri. Yani *görsel*
olarak tanımlamada ve kullanım sırasında`*y`yi görsek de `*`ların görevleri
farklı. İşte burası sanıyorum bu hatanın ve yanılgının temel sebebi. Şekilsel
olarak tanımladığımız bir şeye erişiyoruz gibi oluyor, ama öyle değil.

## Örnek

```c
int main(void)
{
    int x, *y, *w, z;

    x = 20; /* Problem yok */

    /* YAPMAYIN! y'de "çöp" bir değer var, nereyi gösteriyor? */
    /* Programımız çökebilir, saçmalayabilir, her şey mümkün */
    *y = 10;

    x = z; /* z'de de çöp değer var ama program zarar görmez */

    /* w'yu okumak da programımızı çökertebilir */
    /* Sorun yazma ile sınırlı değil, okuma da sıkıntı */
    x = *w;

    return 0;
}
```

Burada örneği biraz daha genişlettim. İlk olarak `*y=10` satırının probleminden
zaten konuştuk, ne olduğu belli olmayan bir adrese bir şey yazıyoruz. Hemen
altında `x = z` var. Burada da aslında `z`de çöp değer var ve `x`e bunu
atıyoruz ama bu programımıza herhangi bir zarar vermez (işletim sisteminin
programı sonlandırması gibi), sadece `z`nin ilk değerinin 0 olduğunu düşünerek
bir şey yaptıysak hata ayıklama sırasında saç baş yoldurtabilir. Son olarak da
`y` ile benzer şekilde oluşturulmuş `w`nun okunduğu `x = *w` satırı var. **Bu
da problem!** Yani sadece yazma değil okuma da problem çünkü sonuçta
bilmediğiniz bir adrese erişiyorsunuz. İşletim sistemi üzerinde çalışıyorsanız
işletim sisteminin programınızı sonlandırması çok olası, erişim hakkınızın
olmadığı bir bellek alanına erişiyor olacaksınız muhtemelen (yazma ya da
okuma).

Bir de işletim sistemsiz bir ortamda, MCU üzerinde vs çalışıyorsanız bu hata
yüzünden şu cümleyi kurabilirsiniz:

> "Ya abi çok ilginç bir şey oluyor, seri kanaldan mesaj işleyen fonksiyona girince
> kart reset atıyor/LED yanıyor."

Kart reset atsa biraz şüphelenirsiniz de LED yanarsa iyice garip değil mi? Tamam,
bir LED'in yanması çok olası değil ama *yeteri kadar şanslı* iseniz `y`ye
alacağınız çöp değer GPIO biriminin çıkış yazmacını (*register*) gösteriyor olabilir.
Reset olayında da *unaligned memory access* yaşanıyor olabilir. Olaylar olaylar...

## Derleme sırasında yakalayalım

Bu tarz hataları derleme sırasında yakalamak oldukça kolay. Öncelikle kod
yazdığınız editör yüksek ihtimalle bunu fark edecektir. Mesela, yukarıdaki kodu
Visual Studio 2022 içerisine koyduğum zaman aşağıdaki gibi bir görüntü çıkıyor.

```{figure} assets/en-cok-hata-vs.png
:align: center

Visual Studio 2022 uyarılar
```

Burada fark ederseniz problemli olan kısımların altlarında işaretler var.
Mesela bize `C60001: Using uninitialized memory` uyarısını veriyor. Detaylı
bilgi
[şurada](https://docs.microsoft.com/tr-tr/cpp/code-quality/c6001?view=msvc-170)
var.

Bitti mi? Hayır. Derleyiciden de uyarı mesajları alabilirsiniz. Mesela
[GCC](https://gcc.gnu.org/) ve [Clang](https://clang.llvm.org/) ile kodu
derleyelim. Yukarıdaki örnek kodu `test.c` ismiyle kaydettim. Bu durumda
aşağıdaki gibi derleyebiliriz. Örnek olarak Ubuntu 20.04 kullanıyorum.

```shell
$ gcc test.c
$ clang test.c
```

İkisi de uslu uslu derledi. Çünkü kod geçerli bir C kodu, sadece çalışma sırasında
görebileceğiniz bir hata içeriyor. Fakat her iki derleyiciden size uyarı mesajlarını
basmasını isterseniz şu çıktılar gelecektir.

```shell
$ gcc -Wall test.c
```

dediğimizde

```text
test.c: In function ‘main’:
test.c:3:9: warning: variable ‘x’ set but not used [-Wunused-but-set-variable]
    3 |     int x, *y, *w, z;
      |         ^
test.c:9:8: warning: ‘y’ is used uninitialized in this function [-Wuninitialized]
    9 |     *y = 10;
      |     ~~~^~~~
test.c:11:7: warning: ‘z’ is used uninitialized in this function [-Wuninitialized]
   11 |     x = z; /* z'de de çöp değer var ama program zarar görmez */
      |     ~~^~~
test.c:14:7: warning: ‘w’ is used uninitialized in this function [-Wuninitialized]
   14 |     x = *w;
      |     ~~^~~~
```

`Wuninitialized` uyarısını görüyoruz.

ya da

```shell
$ clang -Wall test.c
```

dediğimizde de

```text
test.c:9:6: warning: variable 'y' is uninitialized when used here [-Wuninitialized]
    *y = 10;
     ^
test.c:3:14: note: initialize the variable 'y' to silence this warning
    int x, *y, *w, z;
             ^
              = 0
test.c:11:9: warning: variable 'z' is uninitialized when used here [-Wuninitialized]
    x = z; /* z'de de çöp değer var ama program zarar görmez */
        ^
test.c:3:21: note: initialize the variable 'z' to silence this warning
    int x, *y, *w, z;
                    ^
                     = 0
test.c:14:10: warning: variable 'w' is uninitialized when used here [-Wuninitialized]
    x = *w;
         ^
test.c:3:18: note: initialize the variable 'w' to silence this warning
    int x, *y, *w, z;
                 ^
                  = 0
3 warnings generated.
```

aynı uyarı çıkıyor.

Bir de [cppcheck](https://cppcheck.sourceforge.io/) isimli *Linter* aracından
geçirelim kodumuzu bakalım ne diyecek?

```shell
$ cppcheck test.c
```

dedik ve bize

```text
Checking test.c ...
test.c:9:6: error: Uninitialized variable: y [uninitvar]
    *y = 10;
     ^
test.c:14:10: error: Uninitialized variable: w [uninitvar]
    x = *w;
         ^
test.c:11:9: error: Uninitialized variable: z [uninitvar]
    x = z; /* z'de de çöp değer var ama program zarar görmez */
```

`uninitvar` dedi.

GCC ve Clang kodumuzu uyarı verse de derliyor, peki çalıştıralım bakalım.

```shell
$ ./a.out
Segmentation fault (core dumped)
```

Tüh, işletim sistemi harcadı güzel programımızı!

Eğer `*y = 10` ve `x = *w` satırlarını kaldırırsak program hatasız çalışacaktır
(Uyarı veren `x = z` kalsa bile, buna işletim sistemi laf etmez). Fakat bu iki
satırdan bir tanesinin olması bu hatayı *verdirebilir.* Her durumda hata
almayabilirsiniz. Mesela Clang ile derlediğim yazılım gayet güzel çalıştı ama
GCC ile derlediğim sürümde yukarıdaki hatayı aldım. Yani siz de deneyip bir
hata almazsanız çalışma sırasında "Bak bir şey olmuyor" demeyin.

## Özetle

- Pointer'ları sevin.
- Bilmediğiniz adreslere erişmeyin (en iyisi evdeki adreslere erişmek, dışarda
  nasıl yapıldığı belli değil).
- Editör ve IDE'nizin turuncu yaptığı, altını çizdiği şeylere dikkat edin.
  "Derleniyor ya!" demeyin. C derleyicileri bir Vivado değil, hunharca uyarı
  basmazlar, varsa da bir bakıverin.

```{figure} assets/en-cok-hata-meme.jpg
:align: center

[Vivado Meme](https://www.reddit.com/r/FPGA/comments/mdi4te/its_just_a_warning_right/)
```

- Kullandığınız derleyicinin *flag*lerini bir kurcalayın (`-Wall` falan).
- Bir C kodunun derleniyor olması, sizin sisteminizde sorunsuzca çalışıyor olması
  o kodun başka bir derleyicide düzgün derleneceğinin, çalıştırılabilir kodun
  başka bir sistemde **hatta başka bir zaman sizin sisteminizde de** düzgün
  çalışacağı anlamına gelmez (genel olarak, bu duruma özgü değil).
