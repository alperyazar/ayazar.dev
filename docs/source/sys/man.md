# man Sayfalarında Yolumuzu Bulma

```{note}
Okumadıysanız [](posix.md) ve [](kernel-arayuz.md) sayfalarına önce bakmanızı
öneririm.
```

Linux projesi kapsamında yürütülen **man-pages** projesinin amacı programcılara
sunulan C API'ını dokümante etmektir [^1f]:

> The Linux man-pages project documents the Linux kernel and C library
> interfaces that are employed by user-space programs. With respect to the C
> library, the primary focus is the GNU C library (glibc), although, where
> known, documentation of variations in other C libraries available for Linux is
> also included.

Linux sistem programlama yapacaksak man sayfaları hep önümüzde durmalı.
*man-pages* ayrı bir proje ve bu proje 2004 yılından beri *The Linux Programming
Interface* kitabının yazarı [Michael Kerrisk](https://man7.org/mtk/) tarafından
yürütülmektedir. man sayfası kavramı Linux'a özgü değil, Unix zamanından beri
hayatımızda [^2f]. *man*, *manual* kelimesinin kısaltılması, yani *kullanım
kılvauzu* olarak düşünebiliriz. Bu sayfalar hem programcılara hem de
kullanıcılara doküman sağlıyorlar. Hadi gelin bakalım!

## Yerel man sayfaları

Ubuntu gibi birçok Linux dağıtımı man sayfaları yüklü olarak gelmektedir. Eğer
BASH gibi bir shell'i açıp, `man` yadığınız zaman bir hata almıyor ve önünüze
çeşitli seçenekler dokülüyorsa sizde `man` programı ve muhtemelen ilgili
dokümanlar yüklü demektir. Eğer hata alıyorsanız kullandığınız dağıtım ile
ilgili internette bir arama yapın. `man` programı ile *man-pages* içerisinde
kolayca gezinip, arama yapabileceğiz.

`man ls` yazdığınız zaman `ls` komutunun dokümantasyonunu görüyorsunuz örneğin.
Doküman açıldıktan sonra `h` tuşuna basarak `man` programının içerisinde yani
dokümanların içerisinde gezinme ile ilgili yardım alabilirsiniz. `/` ile de
doküman içerisinde arama yapabilirsiniz. `man man` yazarak da `man` programı
hakkında bilgi alabilirsiniz (manception ?).

## Section(s)

Man sayfaları *section* denen bölümlere ayrılmıştır. Bir kelime birden fazla
section'da geçebilir. Eğer `man` programı, aynı kelimeyi birden fazla yerde
bulursa tek bir sonuç döner ve nereden sonuç döneceği ise (yani hangi sırada
arama yapacağı) `/etc/manpath.config` içerisinde belirtilmiştir (en azından
Ubuntu'da bu dosya belirtiliyor.)

```{attention}
`man` sayfasının ilk sonucu dönmesi yanıltıcı olabilir, diğer dokümanları
göremeyebilirsiniz, o yüzden okumaya devam edin...
```

Her section'nun bir numarası vardır. Ad ve açıklamalar şu şekildedir:

```text
1   Executable programs or shell commands
2   System calls (functions provided by the kernel)
3   Library calls (functions within program libraries)
4   Special files (usually found in /dev)
5   File formats and conventions, e.g. /etc/passwd
6   Games
7   Miscellaneous (including  macro  packages  and  conventions),  e.g.
    man(7), groff(7), man-pages(7)
8   System administration commands (usually only for root)
9   Kernel routines [Non standard]
```

```{note}
Bunlar temel section isimleridir. `3perl` gibi başka section isimleri olabilir ama
biz genelde section 1, 2, 3 dokümanları kullanacağız. 2 numaralı section kernele
yapabileceğimiz sistem çağrılarını anlatmaktadır.
```

Örneğin `man 1 chmod` bizlere `chmod` isimli kabuk komutunu anlatırken
`man 2 chmod` ise C API tarafından sunulan `chmod()` fonksiyonunu anlatmaktadır.

`man 2 chmod`:

```text
CHMOD(2)                   Linux Programmer's Manual                  CHMOD(2)

NAME
       chmod, fchmod, fchmodat - change permissions of a file

SYNOPSIS
       #include <sys/stat.h>

       int chmod(const char *pathname, mode_t mode);
       int fchmod(int fd, mode_t mode);
...
```

`CHMOD(2)` içerisindeki `2`, bize section numarasını gösteriyor.

`man 1 chmod`:

```text
CHMOD(1)                         User Commands                        CHMOD(1)

NAME
       chmod - change file mode bits

SYNOPSIS
       chmod [OPTION]... MODE[,MODE]... FILE...
       chmod [OPTION]... OCTAL-MODE FILE...
       chmod [OPTION]... --reference=RFILE FILE...

DESCRIPTION
       This manual page documents the GNU version of chmod.  chmod changes the
       file mode bits of each given file according to mode, which can  be  ei‐
```

Bir kelime ile ilgili tüm section'ları farklı biçimlerde bulabiliriz:

```text
$ man -f chmod
chmod (2)            - change permissions of a file
chmod (1)            - change file mode bits

$ whatis chmod
chmod (2)            - change permissions of a file
chmod (1)            - change file mode bits

$ apropos chmod
chmod (1)            - change file mode bits
chmod (2)            - change permissions of a file
fchmod (2)           - change permissions of a file
fchmodat (2)         - change permissions of a file
```

`man -f` ile `whatis` ve `man -k` ile `aprops` aynı anlamdadır. `man -a chmod`
derseniz `chmod` ile ilgili tüm dokümanları arka arkaya okuyabilirsiniz.

## GNU Info System

man sayfaları kadar yaygın olmasa da **GNU Info System** bir başka dokümantasyon
aracıdır. man'a göre sunduğu çeşitli avantajlar da vardır. [^3f] HTML'in
icadından önce, 1986 yılında ortaya çıkmasına rağmen buradaki dokümanlar
birbirleri ile linkler üzerinden bağlıdır. `info ls` yazarak neye benzediğini
görebilirsiniz. Özellikle `make` gibi GNU araçlarında `info make` yazmak daha
iyi bir dokümantasyon sunabilir.

`x` in dokümanında `man x` yeterli gelmiyorsa, `info x` ile bakmakta fayda var.
Daha iyisi bazen çıkıyor. GNU Info en kötü `man` sayfasını gösteriyor.

## GUI Yardım Araçları

GNOME üzerindeyseniz `yelp man:chmod.2` veya `yelp info:cpio` (GNU Info)
yazabilirsiniz. Plasma (KDE) üzerindeyseniz `khelpcenter` kullanabilirsiniz.
Şahsen GUI yardım araçlarını pek kullanmıyorum. Klasik man pages
kullanmayacaksam online olaranlar daha çok hoşuma gidiyor.

## Online

man sayfalarına online olarak da (hem de güzel formatlanmış şekilde) erişmek
mümkün. Örneğin [man7.org](https://man7.org/linux/man-pages/index.html) sayfası
*resmi* online Linux man sayfasıdır. Kişisel olarak
[mankier.com](https://www.mankier.com/), [tldr](https://tldr.inbrowser.app/),
and [the Arch Linux online man pages](https://man.archlinux.org/) sitelerini de
beğeniyorum. [](kaynak.md) kısmında daha geniş ve güncel bir liste tutmaya
çalışıyorum.

## Kaynaklar

- [](kaynak.md)
- [List available man page sections for an application
  (SO)](https://unix.stackexchange.com/questions/256205/list-available-man-page-sections-for-an-application)
- [STOP Using 'man' Pages Incorrectly!
  (YT)](https://www.youtube.com/watch?v=cnmtKv2kUXs)
- [Introduction to Linux
  (LFS101x)](https://training.linuxfoundation.org/training/introduction-to-linux/)
- [Linux Experts Read 'info' Pages (NOT 'man' pages)
  (YT)](https://www.youtube.com/watch?v=vnBCnd2L0dY)

[^1f]: <https://www.kernel.org/doc/man-pages/>
[^2f]: <https://en.wikipedia.org/wiki/Man_page>
[^3f]: <https://unix.stackexchange.com/a/77561>

```{disqus}
:disqus_identifier: 05503364-0731-4523-928d-c62906c29e86
```
