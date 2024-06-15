# `size_t` ve `ssize_t` Sorunsalı

[Bir önceki yazıda](merhaba-dunya.md), `write()` fonksiyonunu görmüş ve bununla
beraber iki adet tür eş ismi yani *typedef* ile tanışmıştık:
`size_t` ve `ssize_t`. Tekrar hatırlayalım:

- `size_t`, C standartlarında olan bir tür eş ismidir. Implementation defined bir
  tür olup, `sizeof` operatörünün dönüş değeri bu türden olmaktadır. Tipik olarak
  array'deki eleman sayısı gibi nesne sayılarını göstermek için kullanılan bir
  türdür. `size_t` türü, array'ler dahil olmak üzere var olabilecek en büyük
  nesnenin boyutunu tutabilmelidir. **İşaretsiz bir tam sayı** yani **unsigned
  integer** olacağı standartlarda garanti edilmiştir. `unsigned int`,
  `unsigned long` ve `unsigned long long` gibi bir tür olabilir. [^1f]
- `ssize_t` ise C standartlarında olmayan fakat POSIX standartlarında olan bir
  tür eş ismidir. Byte sayısı saymak ya da hata bildirmek için kullanılır. [^2f]
  Özünde `size_t` türünün işaretli versiyonu olarak düşünülmüştür. [^3f]
  İlgili sistemde `size_t` hangi türden ise, örneğin `unsigned int`, `ssize_t`
  onun işaretli versiyonu olabilir, örneğin `signed int`, ama böyle olmak zorunda
  değildir.
- `size_t` türü `[0, SIZE_MAX]` arasındaki değerleri tutabilmelidir. `SIZE_MAX`,
  `limits.h` içerisinde tanımlanmaktadır. [^4f] C99'dan itibaren `size_t` türünün
  en az 16 bit genişliğinde olacağı yani 65535'e kadar olan tam sayı değerlerini
  tutabileceği garanti edilmiştir. [^1f]
- `ssize_t` türü `[-1, SSIZE_MAX]` arasındaki değerleri tutabilmelidir. [^5f]
  POSIX standartlarına göre `SSIZE_MAX` değeri en az `_POSIX_SSIZE_MAX` olmalıdır.
  `_POSIX_SSIZE_MAX` ise 32767 olarak tanımlanmıştır. [^6f] Yani `ssize_t`
  türünde tanımlanmış bir değişken, en kötü ihtimalle `[-1, 32767]` arasındaki
  değeleri tutabilmektedir.

`ssize_t` türü, `size_t` türünün işaretli versiyonu olarak düşünülmüş ve
standartları okuduğumuz zaman bu durumu bir miktar gözlemleyebiliyoruz.
Programımızı C99 standartlarına uygun yazdığımız zaman C99, `size_t` türünün en
az 16-bit genişliğinde olacağını garanti etmiştir. POSIX standartları da `ssize_t`
türünün en az `[-1, 32767]` aralığını tutabileceği belirtiyor, yani aslında
işaretli 16-bit türünden bahsediyor. Yani her iki standarta göre her iki tür de
en az 16-bit genişliğinde olmalıdır.

`size_t` türünden bir değişkende tutulan bir değerin, bir işaret hatası olmadan
`ssize_t` türünden bir değişkende tutulabileceğinin garantisi yok. Örneğin her
ikisi de 16-bit genişliğinde ise, 16-bit genişliğindeki tüm işaretsiz tam sayılar
aynı genişlikteki işaretli bir değişkende tutulamaz. Örneğin `40000 (decimal)`
değeri bir problem oluşturacaktır. **Peki bundan bize ne?**

---

`write()` POSIX fonksiyonunu tekrar hatırlayalım:

```c
#include <unistd.h>

ssize_t write(int fd, const void buf[.count], size_t count);
```

`size_t` türünden olan 3. parametre, kaç byte yazma yapacağımızı söylememizi
sağlıyor. `write()` ise bize kaç byte'lık veriyi başarılı bir şekilde yazdığını
dönüyor. Fakat dikkat ederseniz dönüş değerinin türü `size_t` değil, `ssize_t`.
Çünkü `write()`, hata durumunda bize `-1` dönüyor. `size_t` işaretsiz bir tür
olduğu için dönüş değerini göstermek için kullanılamaz, o yüzden `ssize_t` türünden
bir dönüşe sahip.

`size_t` ve `ssize_t` türlerinin genişliklerinin 16-bit olduğu örnekten devam
edelim. `write(..,..,40000)` gibi bir çağrı yaparsak ve `40000` byte yazılırsa
ne olacak? `write()`, `40000` değerini dönmek isteyecek fakat `ssize_t` bu değeri
tutacak kadar geniş değil. İşte POSIX standartları bu durum için böyle bir
açıklama yapıyor: [^7f]

> If the value of nbyte is greater than {SSIZE_MAX}, the result is implementation-defined.

Yani yazmak istediğimiz byte sayısı, `ssize_t` nin tutabileceği maksimum değeri
aşıyorsa, sonuç implementation defined olur diyorlar. **Bu da "Git, kodunun
çalışacağı işletim sisteminin dokümanına bak" demek.** E biz de gidip Linux
dokümanlarına bakalım.

Elbette POSIX standartları geniş donanım ve işletim sistemi çeşitliliğini
kapsamayı hedefliyor, C standartları gibi. Örneğin günümüzde pratikte görme
ihtimalimiz düşük olsa da 16 bitlik bir işlemcide POSIX uyumlu bir işletim
sistemi çalışıyor olabilir. Bu yüzden ilgili limitlerin minimum değerleri
oldukça küçük. Fakat pratikte gömülü taraf da dahil olmak üzere bir Linux
işletim sistemi çalışıtırıyorsak o işlemci en az 32 bit hatta büyük olasılıkla
artık 64 bit olacaktır. Yine de sistem programlama yapan kişiler olarak bu
limitleri ve durumları akılda tutmak iyi olacaktır.

---

Linux'ta implement edilmiş olan `write()` fonksiyonun detayı ise şöyle: [^8f]

> On Linux, write() (and similar system calls) will transfer at
> most 0x7ffff000 (2,147,479,552) bytes, returning the number of
> bytes actually transferred.  (This is true on both 32-bit and
> 64-bit systems.)

Aynı açıklama henüz değinmediğimiz `read()` fonksiyonu için de yapılmıştır: [^9f]

> On Linux, read() (and similar system calls) will transfer at most
> 0x7ffff000 (2,147,479,552) bytes, returning the number of bytes
> actually transferred.  (This is true on both 32-bit and 64-bit
> systems.)

32 ve 64 bit sistemlerin hepsinde maximum transfer boyutu `0x7ffff000` olarak
belirtilmiş. Yani `write()` fonksiyonu bu değerden büyük bir değer dönemez. Bu
değer ise 32-bit genişliğinde bir işaretli tam sayının tutabileceği değer aralığı
arasında. **Fakat hala problemlerimiz var: Linux üzerinde `SSIZE_MAX` ne?**

C ve POSIX standartlarını beraber okuduğumuz zaman `ssize_t` türünün aralığının
`size_t` türünün aralığını kapsadığına dair bir çıkarım yapamıyoruz. Odağımızı
Linux'la sınırlasak bile `ssize_t` türünün en az 32-bit genişliğinde olacağını
garanti eden bir durum yok. Fakat pratikte durum bu kadar kötü değil.

POSIX sistemlerden ayrılıp daha odaklı olarak Linux sistemlere bakacak olursak,
eğer `SSIZE_MAX` değeri `0x7ffff000` dan büyük ise bir problemimiz yok. Çünkü
zaten Linux üzerinde `write()` ve `read()` fonksiyonları maksimum bu değeri
dönebiliyorlar ve `ssize_t` bu değeri tutabilecek kadar geniş ise tamamız.

---

Hadi gelin sistemimizdeki `SSIZE_MAX` değerine bakalım:

```text
ay@dsklin:~$ getconf -a | grep SSIZE_MAX
SSIZE_MAX                          32767
_POSIX_SSIZE_MAX                   32767
```

32767 mi? Şaka mı? 64 bit sistem üzerinde bu komutu çalıştırıyorum ve böyle bir
değer dönüyor. `_POSIX_SSIZE_MAX` ın 32767 olması doğru, çünkü bu POSIX'in
belirlediği sabit bir sayı. Bu sayı `SSIZE_MAX` ın alabileceği en düşük değeri
belirtiyor. Benim sistem de ise gerçekten `SSIZE_MAX` en düşük değerde mi? Bir
de aynı değeri `limits.h` içerisinden yazdıralım:

```c
#include <stdio.h>
#include <limits.h>  // For SSIZE_MAX
#include <unistd.h>  // For sysconf

int main() {
    // Print the SSIZE_MAX from limits.h
    printf("SSIZE_MAX from limits.h: %zd\n", SSIZE_MAX);

    // Get and print the SSIZE_MAX from sysconf
    long sysconf_value = sysconf(_SC_SSIZE_MAX);
    if (sysconf_value == -1) {
        printf("Failed to get SSIZE_MAX from sysconf");
    } else {
        printf("SSIZE_MAX from sysconf: %ld\n", sysconf_value);
    }

    return 0;
}
```

Programı derleyip çalıştırdığımızda

```text
SSIZE_MAX from limits.h: 9223372036854775807
SSIZE_MAX from sysconf: 32767
```

çıktısını elde ediyoruz. O uzun sayının hexadecimal karşılığı
`0x7FFFFFFFFFFFFFFF` yani 64-bit genişliğindeki işaretli tam sayının alacağı en
yüksek değer. Bu 64 bir sistem için mantıklı ve Linux'un belirttiği `0x7ffff000`
limit değerin de çok çok üstünde.

Gelin aynı kodu 32-bit bir sistem için derleyelim. Bunun için `gcc -m32` şeklinde
bir derleme yapabiliriz fakat 64-bit bir sistemde bu şekilde derlerken hata
alıyorsanız `sudo apt install gcc-multilib` (Ubuntu için verdim) şeklinde
32-bit derlemek için gerekli paketleri kurmanız gerekiyor. Bu noktadan sonra
`-m32` ile derleme yapabilmeniz lazım. Bu şekilde aynı kodu derleyip
çalıştırdığımızda ise

```text
SSIZE_MAX from limits.h: 2147483647
SSIZE_MAX from sysconf: 32767
```

çıktısını alıyor. Bu da `0x7FFFFFFF` demek yani 32-bit genişliğindeki işaretli
tam sayısının alacağı en yüksek değer.

**Özetle** pratikte gözüken hem 32-bit hem de 64-bit sistemlerde `SSIZE_MAX`
değeri, Linux'un belirlediği `0x7ffff000` limit değerinin üzerinde olduğu.
Pratikte bu sistemler ile çalışacağımız düşünürsek aslında bir problem yok.

---

**Peki `getconf()` kabuk komutu veya `sysconf()` fonksiyonu bize niye farklı
bir sayı dönüyor?**

`sysconf()` bir POSIX fonksiyonu [^10f] ve runtime sırasında uygulamanın
üzerinde çalıştığı sistemle ilgili çeşitli limit değerleri sorgulamasını sağlıyor.
Linux üzerinde de bulunuyor.[^11f]

```c
#include <unistd.h>

long sysconf(int name);
```

Fakat yukarıdaki kodda bulunan `sysconf(_SC_SSIZE_MAX)` çağrısı, `glibc` ye
özgü bir çağrı çünkü `_SC_SSIZE_MAX` sembolik sabiti POSIX standartlarında
belirtilen bir sabit değil. GNU dokümanlarında ise şöyle bir açıklama
yapılmış: [^12f]

```text
...
_SC_SSIZE_MAX

   Inquire about the maximum value which can be stored in a variable of type ssize_t.
```

Bize gerçekten de `ssize_t` nin tutabileceği maksimum değeri vermesi gerekiyor.
Fakat işler tam da öyle değil. `glibc` nin 2.39 sürümünün kaynak koduna baktığımızda
aslında bu sembolik sabit ile yapılan `sysconf()` çağrısının bize `_POSIX_SSIZE_MAX`
değerini döndürdüğünü görüyoruz: [^13f]

```{code-block} c
:caption: posix/sysconf.c
:lineno-start: 115
:emphasize-lines: 5

case _SC_NZERO:
  return NZERO;

case _SC_SSIZE_MAX:
  return _POSIX_SSIZE_MAX;

case _SC_SCHAR_MAX:
  return SCHAR_MAX;
```

**Neden POSIX'in belirlediği en düşük limiti dönüyor, bilmiyorum!** Ama bizler
için doğru olmadığı kesin. `getconf` kabuk komutu da aslında `sysconf()`
fonksiyonunu çağırdığı için terminalde de aynı değeri gördük [^14f].

```{todo}
Bunu glibc gruplarına sorabilirsin.
```

Fakat GNU dokümanlarında `sysconf()` dokümantasyonunda şöyle bir ifade mevcut:
[^15f]

> We recommend that you first test for a macro definition for the parameter you
> are interested in, and call sysconf only if the macro is not defined

Yani diyorlar ki aradığınız parametreyi gösteren bir macro yok ise `sysconf()`
ile sorgulama yapın. Bizim durumumuzda aslında `limits.h` içerisinde `SSIZE_MAX`
değeri mevcut. Bunu net belirtmemişler ama acaba bu macro tanımlı olduğunda
`sysconf()` doğru değeri vermiyor (yani vermek zorunda değil) olabilir mi? Yani
`SSIZE_MAX` zaten tanımlı olduğu için `sysconf()` ile biz doğru olmayan bir
sonuç alıyor olabilir miyiz? Öyleyse bile mantığını anlamış değilim.

Ben bu konuyu SO'da sordum fakat pek tatmin edici bir cevap gelmedi ama bir
kişinin yorumuna göre `limits.h` içerisindeki `SSIZE_MAX` değerine güvenebiliriz.
[^16f] Yani hem 32-bit hem de 64-bit sistemlerde görünüşe göre güvendeyiz.

---

glibc'nin kaynak kodlarına baktığım zaman ise `SSIZE_MAX` ile ilgili iki yerde
tanımlama görüyorum:

Bu [^17f]

```{code-block} c
:caption: posix/bits/posix1_lim.h
:lineno-start: 164

#ifndef SSIZE_MAX
/* ssize_t is not formally required to be the signed type
   corresponding to size_t, but it is for all configurations supported
   by glibc.  */
# if __WORDSIZE == 64 || __WORDSIZE32_SIZE_ULONG
#  define SSIZE_MAX LONG_MAX
# else
#  define SSIZE_MAX INT_MAX
# endif
#endif
```

ve bu [^18f]

```{code-block} c
:caption: posix/regex_internal.h
:lineno-start: 153

#ifndef SSIZE_MAX
# define SSIZE_MAX ((ssize_t) (SIZE_MAX / 2))
#endif
```

Bunlardan iki adet çıkarım yapabiliriz:

1. `ssize_t` türü 32-bit sistemlerde 32-bit genişliğinde, 64-bit sistemlerde ise
  64-bit genişliğinde.
2. `ssize_t` gerçekten de `size_t` nin işaretli versiyonu olarak kullanılıyor.

## Uçtan Uca

`SSIZE_MAX` ın minimum `0x7fffffff` olacağını hem deneyimledik hem de kaynak
kodlardan gördük diyebiliriz. Linux'taki fonksiyonlar `0x7ffff000` dan büyük değer
dönmeyeceğiz için bir problem pratikte yok. Ama bu kadar dibine girmişken
kendi C programımızda `write()` veya `read()` fonksiyonlarını çağırdığımızda
neler oluyor, uçtan uca onu bir anlamaya çalışalım.

`write()` fonksiyonu glibc tarafından implement edilmiş durumda. Fakat glibc
gibi büyük kütüphanelerin kodlarını takip etmek oldukça zor. Örneğin `write()`
fonksiyonu için *stub* benzeri yapılar kullanılmış. [^19f] Onun yerine daha
basit bir implementasyon olan `musl` a bakalım: [^20f]

```c
#include <unistd.h>
#include "syscall.h"

ssize_t write(int fd, const void *buf, size_t count)
{
  return syscall_cp(SYS_write, fd, buf, count);
}
```

`write()` fonksiyonu aslında doğrudan syscall yapan bir fonksiyon, `sys_write`
isimli syscall çağırıyor. Bu syscall ise kernel içerisinde tanımlanmış durumda
[^21f]

```c
SYSCALL_DEFINE3(write, unsigned int, fd, const char __user *, buf,
    size_t, count)
{
  return ksys_write(fd, buf, count);
}
```

Sonra [^22f]:

```c
ssize_t ksys_write(unsigned int fd, const char __user *buf, size_t count)
{
  struct fd f = fdget_pos(fd);
  ssize_t ret = -EBADF;

  if (f.file) {
    loff_t pos, *ppos = file_ppos(f.file);
    if (ppos) {
      pos = *ppos;
      ppos = &pos;
    }
    ret = vfs_write(f.file, buf, count, ppos);
    if (ret >= 0 && ppos)
      f.file->f_pos = pos;
    fdput_pos(f);
  }

  return ret;
}
```

ve [^24f]:

```c
ssize_t vfs_write(struct file *file, const char __user *buf, size_t count, loff_t *pos)
{
  ssize_t ret;

  if (!(file->f_mode & FMODE_WRITE))
    return -EBADF;
  if (!(file->f_mode & FMODE_CAN_WRITE))
    return -EINVAL;
  if (unlikely(!access_ok(buf, count)))
    return -EFAULT;

  ret = rw_verify_area(WRITE, file, pos, count);
  if (ret)
    return ret;
  if (count > MAX_RW_COUNT)
    count =  MAX_RW_COUNT;
  file_start_write(file);
  if (file->f_op->write)
    ret = file->f_op->write(file, buf, count, pos);
  else if (file->f_op->write_iter)
    ret = new_sync_write(file, buf, count, pos);
  else
    ret = -EINVAL;
  if (ret > 0) {
    fsnotify_modify(file);
    add_wchar(current, ret);
  }
  inc_syscw(current);
  file_end_write(file);
  return ret;
}
```

Burada `MAX_RW_COUNT` dikkat çekici. İşte Linux'un koyduğu limit buradan geliyor.

Bakalım [^23f]:

```c
#define MAX_RW_COUNT (INT_MAX & PAGE_MASK)
```

Burada mimariye özgü tanımlamalar olabiliyor ama sayfa boyutunu 12 bit, `int` i de
32 bit olarak düşünürsek aslında `0x7ffff000 = 0x7fffffff - 0xfff` ilişkisinden
elde edilmektedir. `count` yani gerçekten yazım yapılan değer ise aslında `if`
ile bu değere kernel içerisinde limitlenmektedir.

## Özet

Özetle, Linux üzerinde `ssize_t` türü ve `write()`/`read()` fonksiyonları
düşünüldüğünde pratikte bir problem bulunmamaktadır.

[^1f]: <https://en.cppreference.com/w/c/types/size_t>
[^2f]: <https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_types.h.html>
[^3f]: <https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_xsh_chap02.html>
[^4f]: <https://en.cppreference.com/w/c/types/limits>
[^5f]: <https://man7.org/linux/man-pages/man3/size_t.3type.html>
[^6f]: <https://pubs.opengroup.org/onlinepubs/009695399/basedefs/limits.h.html>
[^7f]: <https://pubs.opengroup.org/onlinepubs/9699919799/functions/write.html>
[^8f]: <https://man7.org/linux/man-pages/man2/write.2.html>
[^9f]: <https://www.man7.org/linux/man-pages/man2/read.2.html>
[^10f]: <https://pubs.opengroup.org/onlinepubs/9699919799.2018edition/functions/sysconf.html>
[^11f]: <https://www.man7.org/linux/man-pages/man3/sysconf.3.html>
[^12f]: <https://www.gnu.org/software/libc/manual/html_node/Constants-for-Sysconf.html>
[^13f]: <https://elixir.bootlin.com/glibc/glibc-2.39/source/posix/sysconf.c#L119>
[^14f]: <https://codebrowser.dev/glibc/glibc/posix/getconf.c.html#443>
[^15f]: <https://www.gnu.org/software/libc/manual/html_node/Examples-of-Sysconf.html>
[^16f]: <https://stackoverflow.com/q/78364115/1766391>
[^17f]: <https://elixir.bootlin.com/glibc/glibc-2.39/source/posix/bits/posix1_lim.h#L169>
[^18f]: <https://elixir.bootlin.com/glibc/glibc-2.39/source/posix/regex_internal.h#L153>
[^19f]: <https://elixir.bootlin.com/glibc/glibc-2.39.9000/source/io/write.c>
[^20f]: <https://elixir.bootlin.com/musl/v1.2.5/source/src/unistd/write.c#L4>
[^21f]: <https://elixir.bootlin.com/linux/v6.9.4/source/fs/read_write.c#L652>
[^22f]: <https://elixir.bootlin.com/linux/v6.9.4/source/fs/read_write.c#L632>
[^23f]: <https://elixir.bootlin.com/linux/v6.9.4/source/include/linux/fs.h#L2605>
[^24f]: <https://elixir.bootlin.com/linux/v6.9.4/source/fs/read_write.c#L570>
