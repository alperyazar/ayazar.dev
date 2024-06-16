# Dosya Yaratma ve Açma: `open()`

Genel kavramları gördük, biraz ısındık diye düşünüyorum. Şimdi temel I/O
fonksiyonlarından devam edelim.

Bir programın yaptığı temel işlemlerden biri I/O işlemleridir, yani giriş ve
çıkış işlemleri. E bu da beklenen bir şey değil mi? Bilgisayar programları
günün sonunda veri alıp, ki bu veri kullanıcı girdisi olabilir, bir dosyadaki
kayıtlı veriyi okumak olabilir, bu veriyi işleyip dışarıya aktaran akışlardır.
Durum böyle olunca I/O işlemleri programlamanın önemli bir kısmını
oluşturmaktadır.

Linux gibi Unix türevi sistemlerde ise dosyalar daha da anlamlıdır. Çünkü bu
sistemlerde **"(Neredeyse) Her şey dosyadır."** şeklinde bir tabir vardır,
duymuş olabilirsiniz. Bu betimlemeyi farklı perspektiflerden
değerlendirebiliriz. Linux sistemlerde kernel'e ait çeşitli parametreler bile
dosya sistemi üzerinde adeta diskte var olan dosyalardan bir değer okunuyormuş
gibi okunabilir ya da yazılıyormuş gibi değiştirilebilir, `/sys` ve `/proc`
gibi. Linux sistemlerde diskte var olmayan ancak çeşitli işlemleri yapmak için
kullanılan *sanal* dosyalar vardır. Kullanıcı açısından bakıldığında böyledir.

Yazılımcı açısından bakıldığında ise Linux sistemlerdeki birçok bileşen bir
dosyaymış gibi gözükmektedir. Aslında bunun örneklerini önceki yazılarda biraz
gördük. Dosyalara yazmak için bulunan `write()` fonksiyonu ile `1` nolu dosyaya,
file descriptor, bir veri yazdığımız zaman bu veriler terminal ekranımıza düştü.
İlerleyen kısımlarda göreceğiz ki başka bir numaraya yazdığımızda bu yazdıklarımız
gerçek bir dosyaya gidecek. Yani `write()` fonksiyonunu bir dosya API'si olarak
düşünürsek aynı API fonksiyonu ile farklı işlemler yapabildik. Linux üzerinde
temel dosya işlemleri için `open()`, `close()`, `read()`, `write()` fonksiyonları
vardır. İşte biz bu fonksiyonları kullanarak gerçek dosyalara erişebilir, aygıt
sürücüler üzerinden donanıma da erişebiliriz. Programcı açısından Linux üzerinde
birçok bileşen temel dosya fonksiyonları ile kullanılabilir. Bu yüzden Linux
üzerinde I/O fonksiyonları ekstra kıymetlidir.

---

Sistem fonksiyonlarını düşündüğümüzde bildiğimiz türden (regular) dosyaları
yaratıp açmak için kullanabileceğimiz **tek bir fonksiyon vardır**, o da
`open()` fonksiyonudur. Bunun dışında `openat()` ve `creat()` fonksiyonları olsa
da bunlar aslında `open()` ile benzerdir, `open()` çağırılıyor gibi
düşünebiliriz.

`fopen()` gibi fonksiyonlar sistem fonksiyonu değildir. Bunlar, standart C
kütüphanesinde bulunan kütüphane fonksiyonlarıdır. Linux üzerinde `fopen()`
çağrısı yapan bir program C kütüphanesi aracılığı ile yine `open()` sistem
fonksiyonunu çağıracaktır.

`open()` sistem fonksiyonu da çoğu zaman doğrudan `sys_open` isimli sistem
çağrısını, syscall, yapmaktadır. Günün sonunda bir dosyanın yaratılması veya
var olan bir dosyanın açılması kernel tarafından yapılır.

```c
#include <fcnlt.h>

int open(const char* path, int flags, ...);
```

Prototip'i `fcnlt.h` içerisinde olan `open()` fonksiyonu aslında variadic bir
fonksiyondur, `printf()` gibi. Fakat aslında iki kullanımı vardır: 2 argümanlı
veya 3 argümanlı. 3 argümanlı kullanılacaksa bu 3. argüman `mode_t` türünden
olmalıdır. Yani

```c
#include <fcnlt.h>

int open(const char* path, int flags);
//VEYA
int open(const char* path, int flags, mode_t mode);
```

olmalıdır. Diğer kullanımlar tanımsız davranış, UB, sebebidir.

İlk parametre açılacak dosya adıdır.

İkinci parametre ise dosyanın açış modunu ve çeşitli ayarları iletmek için
kullanılır. Bu parametre için tanımlanmış birçok sembolik sabit vardır. `O_xxx`
formatında olan bu sembolik sabitler de `fcntl.h` başlık dosyası içerisindedir.
İkinci `flags` isimli parametre bu sembolik sabitlerin OR'lanması, `|` ile
oluşturulur. Burada uyulması gerekilen çeşitli kurallar vardır.

`flags` parametresi, `O_RDONLY`, `O_WRONLY` veya `O_RDWR` sembolik sabitlerinden
sadece bir tanesini içermek zorundadır. 0 adet veya 2, 3 adet içeremez, yalnızca
1 tanesi olmalıdır.

- `O_RDONLY`: Read-only açış
- `O_WRONLY`: Write-only açış
- `O_RDWR`: Read ve Write açış

Bunun dışında *file creation flags* ve *file status flags* sembolik sabitleri
vardır. Bunlar `|` operatörü ile OR'lanabilir. Burada bulunan bazı sembolik
sabitler Linux'a özgüdür, POSIX standartında yoktur, `O_DIRECT` gibi. Yani Linux,
POSIX standartını bazı noktalarda genişletmektedir.

`open()` fonksiyonun ismi var olan dosyaların açılmasını çağrıştırsa da dosya
yaratmak için de bu fonksiyon kullanılmaktadır. İşte `mode_t` türündeki 3 nolu
parametre bu noktada işe yaramaktadır. Eğer `flags` ile `O_CREAT` veya
`O_TMPFILE` geçilirse bu durumda 3 nolu parametre olan `mode` parametresinin
sağlanması **zorunludur.** Aksi taktirde `open()` fonksiyonu stack'ten rastgele
değerleri çekip, `mode` yerine bunları kullanacaktır. Bu da tanımsız
davranışlara yol açabilir. Eğer bu iki *flag* ten herhangi biri yoksa, `mode`
kullanılmaz ve `0` geçilebilir ya da `open()` fonksiyonu 2 argümanla
çağrılabilir.

---

Burada bir parantez açmak istiyorum, C ve variadic fonksiyonlar ile ilgili.
Gördüğünüz ve belirttiğim üzere `open()` variadic bir fonksiyon çünkü bazen
2 bazen ise 3 argüman alıyor. Burada bana ilk başta garip gelen şey, dokümanda
geçen bir ifade oldu. Yukarıda da belirttiğim gibi `O_CREAT` ve `O_TMPFILE`
geçmesek bile 3 nolu argümanı dilersek geçebiliriz. Yani bu durumda `open()`
fonksiyonu 2 argüman okusa bile 3 argümanın geçilmesi problem yaratmıyor.
**Peki C ve özellikle stack organizasyonu açısıdan bu nasıl olabilir?**
İlk olarak gelin, **musl** kütüphanesindeki implementasyona bakalım. [^1f]

```c
int open(const char *filename, int flags, ...)
{
  mode_t mode = 0;

  if ((flags & O_CREAT) || (flags & O_TMPFILE) == O_TMPFILE) {
    va_list ap;
    va_start(ap, flags);
    mode = va_arg(ap, mode_t);
    va_end(ap);
  }

  int fd = __sys_open_cp(filename, flags, mode);
  if (fd>=0 && (flags & O_CLOEXEC))
    __syscall(SYS_fcntl, fd, F_SETFD, FD_CLOEXEC);

  return __syscall_ret(fd);
}
```

Gördüğünüz üzere `O_CREAT` ve `O_TMPFILE` flag'larinin en az birinin olduğu
durumda `va_` macroları ile 3 nolu argümanın stack'ten alınması işlemi
yapılıyor. Diyelim ki bu flagleri geçmedik ama 3 adet argüman geçtik. Bu problem
değil mi? Aslında değil (en azından anladığım kadarıyla). Çünkü bir `open()` ı
çağırırken 3 adet argümanı stack'e soktuk, `open()` geldi 2 adedini çıkardı 1
adedi stack'te kaldı. Burada fonksiyon argümanlarının stack'e ters sırada
sokulduğunu varsayıyoruz. Yani stack'e ilk 3 nolu argüman, sonra 2 sonra 1
giriyor. Bu böyle olmak zorunda çünkü `printf()` stack'ten kaç argüman çekmesi
gerektiğini ilk argümanı çekerek anlayabiliyor. Yani variadic fonksiyonların ilk
argümanı çağrılan fonksiyonda stack'ten çekilecek ilk argüman olmalı yani
stack'e en son push edilen argüman olmalı. Kalan 1 argümanın üzerinin otomatik
ömürlü yerel değişkenlerle vs yazılması veya kullanılmaması problem değil. Esas
problem, stack'ten fazla sayıda argüman çekmek. [Şu SO
cevabı](https://stackoverflow.com/a/23104629/1766391) konuyu daha güzel
açıklıyor.

---

`open()` fonksiyonu bize bir `int` değer döndürmektedir. Eğer her şey yolunda
giderse bize negatif olmayan bir tam sayı dönecektir. İşte bu döndürdüğü şey
**file descriptor, fd** olarak adlandırılmaktadır. Fonksiyonun döndürdüğü fd
değeri 0 olabilir, detaylara geleceğiz. Eğer `open()` başarısız olursa bize `-1`
döner ve `errno` set olur. `errno` ya bakarak hatayı anlayabiliriz.

Bknz: [](errno.md)

---

`open()` a ikinci argüman olarak geçilecek `flags` kısmında birçok seçenek
vardır. Hepsini şimdi görmek çok anlamlı olmayacak fakat en sık kullanılanlardan
başlayalım. Bir kısmı *Advanced I/O* konularına gireceği için ilerleyen
kısımlarda değiniriz.

`O_CREAT` seçeneği eğer dosya yoksa `open()` fonksiyonun önce bu dosyayı
yaratıp, açmasını sağlar. `CREAT`, `CREATE` demektir (evet 1 harfin hesabını
yapmışlar). `O_CREAT` verdiğimiz zaman, üçüncü argüman olan `mode` argümanını
vermemiz gerekir. `mode` argümanları `S_xxx` formatındadır: `S_IRWXU`, `S_IROTH`
gibi. Bu `mode` değerleri dokümante edilmiştir. [^2f] Bunlar dosya izinleri ile
ilgilidir, sonra daha detaylı göreceğiz.

Hemen bir örnek yapalım.

```c
#include <fcntl.h>
#include <stdio.h>

int main(void)
{
  int fd = open("olmayandosya.txt", O_RDWR | O_CREAT, S_IRWXU | S_IRGRP | S_IROTH );
  if (-1 == fd) {
    perror("dosya acilamadi");
    return 1;
  }
  printf("Dosya Acildi, fd = %d\n", fd);
}
```

Yukarıdaki kodu derleyip çalıştırdığımız zaman aşağıdaki çıktıyı alıyoruz:

```text
Dosya Acildi, fd = 3
```

Programımızı çalıştırdığımız dizinde de `olmayandosya.txt` oluşuyor:

```text
-rwxr--r-- 1 alper alper 0 Jun 16 12:57 olmayandosya.txt*
```

Normalde bu dosya yoktu fakat `O_CREAT` bayrağını verdiğimiz için `open()`
fonksiyonu bu dosyayı oluşturdu. Şimdi dosyamızı silelim ve `O_CREAT` bayrağını
da kaldıralım, yani:

```c
int fd = open("olmayandosya.txt", O_RDWR , S_IRWXU | S_IRGRP | S_IROTH );
```

şekline getirelim. Konuştuğumuz gibi bu durumda üçüncü argümanların bir önemi
yok, bırakabiliriz fakat kafa karışıklığı yaratmamak adına silmek daha doğru
olacaktır.

`rm olmayandosya.txt` diyerek oluşmuş dosyayı silelim ve yeni programımızı
çalıştıralım.

```text
dosya acilamadi: No such file or directory
```

Bu sefer `open()` bize `-1` yani hata döndü, biz de `perror` ile hata mesajını
gördük. `O_CREAT` bayrağı olmadığı için dosya yoksa dosya yaratılmıyor ve
olmayan dosya açılamadığı için hata alıyoruz.

Son olarak programımızı tekrar ilk haline getirelim, yani `O_CREAT` bayrağı
olsun ve çalıştıralım. Sonra dosyamızı elle modifiye edelim, tekrar çalıştıralım
ve dosyanın bozulmadığını görelim:

```shell
alper@brs23-2204:~/temp$ ll olmayandosya.txt
ls: cannot access 'olmayandosya.txt': No such file or directory

alper@brs23-2204:~/temp$ ./a.out
Dosya Acildi, fd = 3

alper@brs23-2204:~/temp$ ll olmayandosya.txt
-rwxr--r-- 1 alper alper 0 Jun 16 13:15 olmayandosya.txt*

alper@brs23-2204:~/temp$ cat olmayandosya.txt

alper@brs23-2204:~/temp$ echo "deneme" > olmayandosya.txt

alper@brs23-2204:~/temp$ cat olmayandosya.txt
deneme

alper@brs23-2204:~/temp$ ./a.out
Dosya Acildi, fd = 3

alper@brs23-2204:~/temp$ cat olmayandosya.txt
deneme
```

Gördüğünüz üzere programımız çalıştığı zaman eğer o dosya varsa o dosyayı silmiyor,
var olanı açıyor. Yani `O_CREAT` bayrağı dosya varsa etkili olmuyor.

---

Şimdi gelin `O_EXCL` yani *exclusive mode* flag'ine bakalım. Bu flag `O_CREAT`
ile beraber kullanılmaktadır. Burada `open()` fonksiyonu eğer dosyayı sıfırdan
yaratmıyorsa ve var olan dosyayı açıyorsa başarısızlıkla dönecektir. Yani
`O_EXCL` ile `open()` ın var olan dosyayı açmadığından, dosyayı yeni yarattığından
emin olabiliyoruz.

```c
int fd = open("olmayandosya.txt", O_RDWR | O_CREAT | O_EXCL, S_IRWXU | S_IRGRP | S_IROTH );
```

şeklinde kodu değiştirip denemeler yapalım.

```shell
alper@brs23-2204:~/temp$ rm olmayandosya.txt

alper@brs23-2204:~/temp$ ./a.out
Dosya Acildi, fd = 3

alper@brs23-2204:~/temp$ ./a.out
dosya acilamadi: File exists
```

İlk olarak dosyamızı sildik, sonra programımızı çalıştırdık. Dosya `open()`
tarafından yaratıldı ve program sonlandı. Fakat daha sonra programı tekrar
çalıştırdığımızda *File exists* hatası aldık. Çünkü dosya zaten vardı ve
`O_CREAT` ile dosya oluşturmadığımız için `O_EXCL` bayrağından dolayı bu
`open()` bize bu sefer hata döndü.

---

Şimdilik `open()` fonksiyonuna ara verelim. Çünkü `open()` ile ilgili bazı
kavramları anlamak için dosya izinleri, user, group id, process gibi kavramları
anlamamız gerekiyor. Biraz onlara bakarız. Ama genel olarak fonksiyonun yapısını
görmüş olduk. Detaylı kullanım bilgileri, kullanabileceğimiz mod ve bayraklar
her zaman olduğu gibi dokümantasyonda yer alıyor. [^2f] Konularda ilerledikçe
`open()` a tekrar tekrar dönüp, diğer kullanım senaryolarına bakacağız.

[^1f]: <https://elixir.bootlin.com/musl/latest/source/src/fcntl/open.c#L5>
[^2f]: <https://man7.org/linux/man-pages/man2/open.2.html>
