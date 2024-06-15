# Hata Durumları, `errno`

Çağırdığımız sistem ya da POSIX fonksiyonları çeşitli durumlarda bize hata
dönebilirler, isteklerimizi yerine getiremeyebilirler. Birçok sistem fonksiyonun
dokümanında hata durumları için bir kısım bulunmaktadır. `write()` fonksiyonundan
devam edelim: [^1f]

```text
ERRORS

       EAGAIN The file descriptor fd refers to a file other than a
              socket and has been marked nonblocking (O_NONBLOCK), and
              the write would block.  See open(2) for further details on
              the O_NONBLOCK flag.

       EAGAIN or EWOULDBLOCK
              The file descriptor fd refers to a socket and has been
              marked nonblocking (O_NONBLOCK), and the write would
              block.  POSIX.1-2001 allows either error to be returned
              for this case, and does not require these constants to
              have the same value, so a portable application should
              check for both possibilities.

       EBADF  fd is not a valid file descriptor or is not open for
              writing.
...
```

`write()` fonksiyonu birçok hata oluşturabiliyor, ben bir kısmını aldım.
Bazı fonksiyonlar ise çok az sayıda hata koşulu var iken bazı fonksiyonlar için
bu sayı fazla oluyor fakat hepsi için hataları yakalama yöntemi aynı: `errno`

## `errno`

`errno`, C dili ile uğraştıysanız duymuş olabileceğiniz bir kelime. `errno`, C
standartlarında bulunuyor. Yani ister POSIX uyumlu bir yerde çalışın, ister uyumsuz
olsun, ister Windows üzerinde olsun `errno` C dilinde olan bir kavram, POSIX veya
Linux ile sınırlı değil. POSIX standartları da C dilinde var olan `errno` *hata
bildirim yöntemini* tercih etmiştir. [^2f] O zaman önce C dilindeki `errno`
kullanımına bakalım.

C89'dan yani ilk C standartından itibaren `errno` ve `errno.h` standartlar içerisinde
yer alıyor. Standart C kütüphane fonksiyonları, hata bildirimleri için bu yöntemi
kullanabiliyorlar. [^3f]

`errno` yu, `int` türden bir değişken gibi düşünebiliriz. Fakat aslında teknik
olarak bu tam doğru değil. C11 standartlarına kadar `errno` hakkında şöyle bir
ifade bulunuyordu:

> It is unspecified whether errno is a macro or an identifier declared with
> external linkage.

C11 ile burada bir değişiklik yapıldı ve bu ifade kaldırıldı, `errno` nun
aslında bir önişlemci macro'su olması sağlandı. [^4f] Ama biz kullanıcılar
açısından bu fark çok önemli değil, sonuçta derleyici yazmıyoruz. `errno.h`
içerisinde `extern int errno;` şeklinde bildirimi yapılmış global bir değişken
gibi düşünebiliriz.

`errno` ya erişmek için kodumuza `errno.h` ı `#include` etmemiz gerekiyor. Bu
noktadan sonra `errno` yu rezerve edilmiş gibi global değişken gibi düşünebiliriz,
ama arka planda macro olabilir. Problem yaşamamız için `errno` yu `#undef` etmeye
çalışmamalıyız. Ayrıca POSIX standartları `errno` isminde bir şey tanımlamamamız
gerektiğini belirtiyor. [^5f]

> It is unspecified whether errno is a macro or an identifier declared with
> external linkage. If a macro definition is suppressed in order to access an
> actual object, or a program defines an identifier with the name errno, the
> behavior is undefined.

Benzer ifade C standartlarında da var:

> If a macro definition is suppressed in order to access an actual object, or a
> program defines an identifier with the name errno, the behavior is undefined.

**Yani özetle `errno.h` ı include edin ya da etmeyin `errno` isminde kendiniz
bir şeyler tanımlamayın, başka bir isim bulun.** (Yani aslında `errno.h` ı
kullanmıyorsanız `errno` tanımlamak problem de olmayabiliyor bazı durumlarda ama
başka isim mi bulamadınız kardeşim, bela aramayın!)

---

C'de bir kütüphane fonksiyonu başarısız olduğu zaman, 0 olmayan bir tam sayı ya
da NULL pointer dönebiliyor. İşte bu durumda bu fonksiyon tarafından `errno`,
daha detaylı bir hata bilgisi vermek için set edilebiliyor. Biz de bu değere
bakarak hata hakkında detaylı bilgi edinebiliyoruz. Aşağıdaki koda bakalım:

```c
#include <stdio.h>
#include <errno.h>

int main(void)
{
  printf("%d\n", errno); //0

  FILE* f = fopen("olmayan-dosya.txt","r");
  if (!f)
    printf("%d\n", errno);
  errno = 0; //bizim sorumluluğumuzda
}
```

Bu kodun çıktısı:

```text
0
2
```

olmaktadır.

Program başlangıcındaki thread'te `errno` nun değerinin `0` olacağı C
standartları tarafından garanti edilmiştir. Çok thread'li programlarda her
thread için ayrı bir `errno` vardır. Standartlar, başlangıç thread'i hariç diğer
thread'lerdeki `errno` değerinin belirsiz olacağını belirtmektedir. Standart C
fonksiyonları, `errno` yu hata olsun olmasın bir pozitif sayıya set edebilirler.
Fakat C kütüphanesi fonksiyonları `errno` yu 0'a set etmezler. Dilersek biz elle
`0` yazabiliriz.

Yukarıdaki kodda var olmayan bir dosya `fopen()` standart C fonksiyonu ile
açılmaya çalışılmış. Dosya olmadığı için `fopen()` bize `NULL` pointer dönmüş ve
`errno` yu set etmiştir.

Aslında bu örnek iyi bir örnek değildir. Çünkü C standartları gereğince
`fopen()` fonksiyonunun hata durumunda `errno` yu set etme gibi bir zorunluluğu
yoktur. Hata durumunda `errno` nun set edilmesi POSIX standartlarında zorunlu
kılınmıştır. [^6f] Fakat Microsoft C derleyicisi de uyumluluk adına `errno` yu
bu durumda set etmektedir. C standartlarında `fgetpos()` gibi fonksiyonların
`errno` yu set etmesi zorunlu kılınmıştır. Yine de basitlik açısından yukarıdaki
örneğin vermeyi tercih ettim. Ama yine de bu şekilde kullanım C standartları
açısından doğru değildir çünkü `errno`, `fopen()` tarafından set edilmeyebilir.

---

**Peki 2 nolu hata ne demektir?** Bunu anlamak için `errno.h` içerisindeki
sembolik sabitlere bakmamız gerekir. `errno` yu anlamlandırmak için standart C'de
bulunan bazı yardımcı fonksiyonları kullanabiliriz.

```c
#include <stdio.h>
void perror(const char *s);
```

`stdio.h` içerisinde prototipi bildirilen `perror()` fonksiyonu standart hata
akımına, stderr, istediğimiz bir mesaj ile beraber hata bilgisi yazdırmaktadır.
[^7f] Kodumuzu değiştirelim:

```c
#include <stdio.h>
#include <errno.h>

int main(void)
{
  printf("%d\n", errno); //0

  FILE* f = fopen("olmayan-dosya.txt","r");
  if (!f){
    printf("%d\n", errno);
    perror("Patladık!");
  }
  errno = 0; //bizim sorumluluğumuzda
}
```

Çıktı:

```text
0
2
Patladık!: No such file or directory
```

Gördüğünüz üzere bizim mesajımız ile beraber hatayı yazdırdı. Demek ki benim
sistemimde 2, bu demekmiş. Dikkat ederseniz `perror()` a ayrıca `errno` geçmiyoruz
çünkü `errno` adeta bir global değişken olduğu için `perror()` tarafından
okunabiliyor.

Bir diğer fonksiyon da `string.h` içerisindeki `strerror()` fonksiyonudur. Bu
fonksiyon da ilgili hata kodunu, string bir mesaja çevirmeye yarar.

```c
for (int i = 0; i < 30; ++i)
  printf("error code %2d: %s\n", i, strerror(i));
```

Dilersek bu şekilde hata kodlarının anlamlarını öğrenebiliriz. Dikkat ederseniz
bu fonksiyon global değişken gibi düşündüğümüz `errno` yu okumuyor, argüman olarak
bir hata kodu alıyor. Elbette bunu çağırırken `strerror(errno)` dersek, `perror()`
benzeri bir etki alırız. `strerror()`, standart bir C fonksiyonudur.

## POSIX ve Sistem Fonksiyonları

Gelelim POSIX ve sistem fonksiyonları ile `errno` nun kullanımına. POSIX, kendi
fonksiyonları için sembolik sabit şeklinde hatalar tanımlamıştır. Formatları,
`EXXX` şeklindedir. `EACCES`, `EAGAIN`, `EBADF` gibi. Bu sembolik sabitlerin
değerleri ise POSIX standartlarında uspecified olarak bırakılmıştır. [^8f]
Standart C fonksiyonları gibi POSIX fonksiyonları da `errno` yu 0 değerine set
etmezler:

> No function in this volume of POSIX.1-2017 shall set errno to zero.

`errno` ile ilgili yapılabilecek hatalardan biri de bir fonksiyon hata dönmemiş
olsa bile `errno` yu anlamlandırmaya çalışmaktır. `errno`, fonksiyon hata
döndüyse anlamlı olacaktır. Elbette her fonksiyonun dokümanına bakmalıyız.

## `errno` Değerleri

Ubuntu üzerinde `sudo apt install moreutils` ile `moreutils` paketini yükleyerek
komut satırı üzerinden `errno` programını çalıştırıp hata kodlarını
öğrenebiliriz. `errno -l` diyerek tüm kodları listeleyebilir, `errno 2` diyerek
ise `2` nolu hata hakkında bilgi alabiliriz.

Örnek olarak `open()` POSIX fonksiyonu ile aşağıdaki gibi bir kullanım düşünebiliriz:

```c
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <stdlib.h>
#include <errno.h>

int main(void)
{
  int fd;

  if ((fd = open("olmayandosya", O_RDONLY)) == -1) {
    fprintf(stderr, "open failed: %s\n", strerror(errno));
    exit(EXIT_FAILURE);
  }

  printf("success\n");

  return 0;
}
```

Çıktı:

```text
open failed: No such file or directory
```

Ya da istersek kendimize boilerplate bir kod hazırlayabiliriz:

```c
void exit_sys(const char* msg)
{
  perror(msg);
  exit(EXIT_FAILURE);
}

//...

exit_sys("Elveda zalim dünya");
```

## Bakınız

- <https://man7.org/linux/man-pages/man3/strerror.3.html>

[^1f]: <https://man7.org/linux/man-pages/man2/write.2.html>
[^2f]: <https://pubs.opengroup.org/onlinepubs/9699919799/functions/errno.html>
[^3f]: <https://en.cppreference.com/w/c/error/errno>
[^4f]: <https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1338.htm>
[^5f]: <https://pubs.opengroup.org/onlinepubs/9699919799/functions/errno.html>
[^6f]: <https://pubs.opengroup.org/onlinepubs/9699919799/functions/fopen.html>
[^7f]: <http://port70.net/%7Ensz/c/c99/n1256.html#7.19.10.4>
[^8f]: <https://pubs.opengroup.org/onlinepubs/9699919799/functions/V2_chap02.html#tag_15_03>
