---
gicus: fcfdf3ee-92c3-45f5-ad75-4f6a79053c1e
---

# `open()` ve `close()`

Bir önceki bölümlerde kendi user space programlarımızı nasıl ekleyeceğimizi ve
`write()`, `read()` fonksiyonlarını görmüştük. Aldığını geri basan yani loopback
yapan (ya da echo) bir program yazmıştık. Bu bölümde `open()` fonksiyonu ile
tanışalım.

Artık `Makefile` a ekleme yapma konusundan bahsetmeyeceğim fakat yazdığımız
programların önceki `loop.c` gibi eklenmesi gerektiğini unutmayın.

---

I/O fonksiyonlarının en önemlilerinden biri de `open()` ve kardeşi `close()`
fonksiyonlarıdır. `open()`, `write()`, `read()`, `close()` adeta
[Voltran](https://tr.wikipedia.org/wiki/Voltran)'ı oluşturur.

```{note}
Tamam, Voltran için 5 bileşen lazım. [lseek()](https://man7.org/linux/man-pages/man2/lseek.2.html)
olsaydı bence bu da 5. olurdu. Fakat xv6'da, `lseek()` bulunmuyor. 🤖
```

Önceden de bahsettiğim gibi `read()` ve `write()` fonksiyonları birer
*file descriptor, fd* üzerinden çalışırlar. Bu fonksiyonlar dosya ismi bilmezler.
Önceki `loop.c` örneğinde process başladığı zaman shell tarafından açılmış
`stdout, 1` ve `stdin, 0` fd'lerini kullanmıştık. Peki kendimiz bir dosya yazmak
istersek, örneğin `not.txt`, bunu nasıl yapacağız?

## `open()`

İşte burada `open()` fonksiyonu devreye giriyor. `open()` fonksiyonu diskte var
olan bir dosyanın açılmasını ya da dosya yoksa istenirse önce dosyanın yaratılmasını
sağlıyor.

```{note}
İlerleyen kısımlarda [f5b93ef](https://github.com/mit-pdos/xv6-riscv/tree/f5b93ef12f7159f74f80f94729ee4faabe42c360)
nolu commit'i referans alacağım.
```

Fonksiyon prototipine bir bakalım.

```{code-block} c
:caption: user/user.h
:lineno-start: 11
:emphasize-lines: 3

//...
int exec(const char*, char**);
int open(const char*, int);
int mknod(const char*, short, short);
//...
```

`open` bizden iki parametre istiyor. İlki bir char pointer, buraya açmak
istediğimiz dosyanın adını vereceğiz, `"not.txt"` gibi. İkinci parametre ise
dosyanın açış modlarını belirliyor.

```{code-block} c
:caption: kernel/fcntl.h
:lineno-start: 1

#define O_RDONLY  0x000
#define O_WRONLY  0x001
#define O_RDWR    0x002
#define O_CREATE  0x200
#define O_TRUNC   0x400
```

```{attention}
Linux sistem programlama ile ilgileniyorsanız oradaki sembolik sabitin adı `O_CREAT`
olmaktadır, buradaki `O_CREATE`.
```

Bu sembolik sabitleri OR'layarak `open()` fonksiyonunun dosyayı nasıl açacağını
belirleyebiliyoruz. Sırası ile:

- read only
- write only
- read ve write
- eğer yoksa yarat
- dosyanın içeriğini sil

gibi seçenekler verebiliyoruz. Elbette bunların tüm kombinasyonları anlamlı değil.
`O_RDONLY | O_RDWR` mantıksız bir seçenek mesela, hem read only hem de okuma
yazma istiyoruz.

Bu fonksiyon günün sonunda kernel içerisinde bulunan `sys_open` fonksiyonunu
çağrıyor. Bunun mekanizmasına sonraki bölümlerde bakarız, şu an amacımı kernel'i
çok fazla kurcalamadan kullanıcı olarak nasıl kod yazabiliriz ona bakmak.

`open()` eğer bir hata ile karşılaşırsa `-1`, karşılaşmasa da o dosyaya karşılık
gelen file descriptor, fd, sayısını dönüyor. Biz de bu sayıyı daha sonra
`write()` ve `read()` fonksiyonları ile işlem yapmak için kullanabiliyoruz.

## `close()`

`close()` ise açılmış bir dosyanın kapatılmasını sağlıyor. Bir adet parametre
alıyor, kapatmak istediğimiz file descriptor ve eğer başarılı olursa 0, eğer
başarısız olursa (örneğin parametre hatası) -1 dönüyor.

Linux gibi sistemlerde dosya erişimleri için her zaman diske gidilmiyor. Bunun
sebebi performans. Bellek yani RAM ile bir tampon oluşturuluyor. Linux'taki
`close()` gibi fonksiyonlar bu belleğin *flush* edilmesini sağlıyor, yani RAM'de
duran değişiklikleri diske işliyor. Fakat görebildiğim kadarıyla xv6'da böyle
bir mekanizma yok, tam da emin değilim. O yüzden `close()` pek bir işlevi olan
fonksiyon olmayabilir.

Linux gibi sistemlerde bir process sonlandığı zaman açık olan tüm dosyalar
otomatik `close()` ediliyor, xv6'da böyle mi bilmiyorum, ilerleyen zamanlarda
umarım öğreniriz.

## Örnekler

Şimdi biraz örnek yapalım.

```{code-block} c
:caption: user/not.c
:lineno-start: 1

#include "kernel/types.h"
#include "user/user.h"
#include "kernel/fcntl.h" //O_WRONLY vs

static const char not[] = "Merhaba Dunya!\nBen bir notum.\n";

int main() {
  int fd, result;

  fd = open("not.txt", O_RDWR);

  if (fd < 0){
    fprintf(2, "fd = %d not.txt acilamadi!\n", fd);
    exit(1);
  }

  printf("fd = %d\n", fd);

  result = write(fd, not, sizeof(not) - 1);

  if (result != sizeof(not) - 1){
    fprintf(2, "result = %d yazma basarisiz\n", result);
    exit(2);
  }

  result = close(fd);

  if (result != 0) {
    fprintf(2, "result =%d kapama basarisiz\n", result);
    exit(3);
  }

  exit(0);
}
```

Yukarıdaki programda önceden kullanmadığımız iki adet fonksiyon var: `printf()`
ve `fprintf()`. Bunlar standart C fonksiyonları.
**Fakat bunlar xv6 ile geliyorlar.** Yani her ne kadar standart C fonksiyonları
olsalar da xv6 standart C fonksiyonları ile derlenmiyor.

```{code-block} makefile
:caption: Makefile
:lineno-start: 61
:emphasize-lines: 2

CFLAGS += -mcmodel=medany
CFLAGS += -ffreestanding -fno-common -nostdlib -mno-relax
CFLAGS += -I.
```

Burada `-nostdlib` flag'ine dikkat.

```{hint}
Standart C kütüphanesi olmadan Linux üzerinde program derlemeyle ilgili
yazdığım bir yazı: [](/sys/merhaba-dunya.md)
```

`fprintf()` ve `printf()` fonksiyonları `user/printf.c` içerisinde implement
edilmiş durumda. Bu ikisi neredeyse aynı, `fprintf(fd, printf kısmı)` ya da
`printf(...) ≡ fprintf(1, ...)`  gibi düşünülebilir yani fazladan bir file
descriptor alıyor. Her ikisi de ilgili dosya içerisindeki `vprintf()`
fonksiyonunu çağırıyor. `printf()` in farkı fd 1'e yani stdout'a basması.
Ben burada hata durumlarını fd 2'ye yani `stderr` ye bastırdım. Bunun çeşitli
avantajları var, ilerleyen zamanlarda görürüz. Yine de hem `stdout` hem `stderr`
default olarak shell ekranına basmaktadır.

xv6'da kısıtlı sayıda standart C fonksiyonları implement edilmiş durumda.
İlgili fonksiyonlar:

```{code-block} c
:caption: user/user.h
:lineno-start: 26

// ulib.c
int stat(const char*, struct stat*);
char* strcpy(char*, const char*);
void *memmove(void*, const void*, int);
char* strchr(const char*, char c);
int strcmp(const char*, const char*);
void fprintf(int, const char*, ...);
void printf(const char*, ...);
char* gets(char*, int max);
uint strlen(const char*);
void* memset(void*, int, uint);
void* malloc(uint);
void free(void*);
int atoi(const char*);
int memcmp(const void *, const void *, uint);
void *memcpy(void *, const void *, uint);
```

Bu programı `make qemu` ile derleyip QEMU'da çalıştırdığımızda bize bir hata
veriyor ne yazık ki:

```text
$ not
fd = -1 not.txt acilamadi!
```

**Peki neden?** Çünkü `not.txt` dosyası yok ve `open()` bunu açamadı.

---

İki seçeneğimiz var.

Seçeneklerden biri dosyayı önden oluşturmak diğer ise `open()` a `O_CREATE`
flagini vermek.

```c
//...
fd = open("not.txt", O_RDWR | O_CREATE);
//...
```

Bunu deyip derlersek işlem başarılı oluyor.

```shell
$ not
fd = 3
```

Gördüğünüz üzere `open()` 3 nolu file descriptor ile döndü. Neden 3? Çünkü
bir process hayatına başladığı zaman tipik olarak `0, stdin`, `1, stdout` ve
`2, stderr` file descriptor'ları açık oluyor. `open()` kullanılmayan en düşük
numaralı fd'yi verdiği için 3 numarasını aldık.

```shell
$ ls not.txt
not.txt        2 24 30

$ cat not.txt
Merhaba Dunya!
Ben bir notum.
```

Gördüğünüz üzere dosya sistemimizde `not.txt` oluştu ve içinde yazı var.

Şimdi tekrar `not` programını çalıştırıp `not.txt` nin içeriğine bakalım.

```shell
$ not
fd = 3

$ cat not.txt
Merhaba Dunya!
Ben bir notum.

$ not
fd = 3

$ cat not.txt
Merhaba Dunya!
Ben bir notum.
```

Neden hep aynı içerik oluyor? Çünkü her seferinde dosyayı programımız açıyor
ve en başından itibaren aynı yazıyı yazdığı için dosya içeriği hep aynı
oluyor. xv6'de `open()` fonksiyonunda Linux'ta olduğu gibi `O_APPEND` gibi bir
mod, `lseek()` biri bir sistem fonksiyonu da ya da implement edilmiş `fseek()`
fonksiyonu yok.

---

Peki önceden dosyaya bir şeyler yazsak ne olacak?

```shell
$ rm not.txt
$ echo 0123456789012345678901234567890123456789 > not.txt

$ cat not.txt
0123456789012345678901234567890123456789

$ not
fd = 3

$ cat not.txt
Merhaba Dunya!
Ben bir notum.
0123456789
```

İlk olarak xv6'da bulunan `echo` komutu ile `not.txt` ye bir şeyler yazdık. Daha
sonra bizim programımızı çalıştırınca başını doldurdu devamı kalan içeriklerden
oldu.

---

Fakat `O_TRUNC` ile açsaydık, bu sefer dosyanın içeriği `open()` fonksiyonu
tarafından silinecekti, adeta yeni yaratılmış gibi olacaktı.

```c
fd = open("not.txt", O_RDWR|O_CREATE|O_TRUNC);
```

ve sonuç:

```shell
$ echo 0123456789012345678901234567890123456789 > not.txt

$ cat not.txt
0123456789012345678901234567890123456789

$ not
fd = 3

$ cat not.txt
Merhaba Dunya!
Ben bir notum.
```

Gördüğünüz üzere dosyamız *truncate* oldu yani içeriği silindi.

Elbette, read only modda açarsak, `write()` sırasında hata alırız.

Örneğin:

```c
fd = open("not.txt", O_RDONLY|O_CREATE|O_TRUNC);
```

---

Tabii read only bir dosyaya `O_CREATE` ve `O_TRUNC` vermek biraz garip ama
göstermek istediğim şey, bir dosya read only açılırsa `write()` yapılamaz.
Aşağıda göreceğiniz gibi `open()` bize geçerli bir fd dönüyor fakat `write()`
bize hata dönüyor, çünkü dosyayı read only açtık.

```shell
$ not
fd = 3
result = -1 yazma basarisiz
```

## Kaynaklar

- [xv6 book](https://pdos.csail.mit.edu/6.828/2023/xv6/book-riscv-rev3.pdf)
- Ayrıca bknz: [genel kaynaklar](index.md)
