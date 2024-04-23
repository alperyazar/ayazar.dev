---
giscus: 2ab55136-5c08-47f7-85e0-f26625687228
---

# User Space Programlamaya Giriş: `write()` ve `read()`

Yavaştan xv6 üzerinde çalışacak user space programlara bakalım. Bunun için
MIT 6.1810 tarafından sağlanan lab repository'sini kullanacağım.

[](merhaba-dunya.md) yazısında cross-compiler ve QEMU kurmuştum. Elimizde şu an
xv6-riscv çalıştırabilen bir sistemimiz var.

```shell
git clone git://g.csail.mit.edu/xv6-labs-2023
cd xv6-labs-2023
make qemu
```

Sorunsuzca boot edip çalışması lazım

```text
xv6 kernel is booting

hart 2 starting
hart 1 starting
init: starting sh
$
```

`Ctrl-A X` ile çıkabiliriz. Varsayılan olarak `util` branchinde olmamız lazım.
`git branch` ile kontrol edebiliriz.

Tekrar çalıştıralım `make qemu` ile. `ls` yazarsak emüle edilen makine
içerisindeki dosyaları görüyoruz. xv6 reposu, bir sanal disk oluşturuyor, `mkfs`
ile. Burada çalıştırabileceğimiz bir çok program var. `ls` de böyle bir program.

```shell
$ ls
.              1 1 1024
..             1 1 1024
README         2 2 2305
xargstest.sh   2 3 93
cat            2 4 32848
echo           2 5 31696
forktest       2 6 15824
grep           2 7 36224
init           2 8 32192
kill           2 9 31656
ln             2 10 31480
ls             2 11 34784
mkdir          2 12 31712
rm             2 13 31696
sh             2 14 54144
stressfs       2 15 32584
usertests      2 16 180624
grind          2 17 47536
wc             2 18 33800
zombie         2 19 31056
console        3 20 0
```

Normalde Linux'ta `ps` komutu ile çalışan programları görebiliyoruz. xv6'da bu yok
fakat `Ctrl-p` ile görebiliriz.

```shell
$
1 sleep  init
2 sleep  sh
```

2 adet program var. `init`, çalışan ilk program vs `sh` ile şu an çalışan shell
diye tahmin ediyorum. `1` ve `2` değerleri de PID diye tahmin ediyorum.

## `read()` ve `write()`

xv6 çekirdeğinin desteklediği iki adet syscall ile tanışalım: `read` ve `write`
Bunlar, Unix `read()` ve `write()` fonksiyonlarına benzer tasarlanmışlar.

`user/user.h` içerisinde syscall ve C kütüphanesi fonksiyon prototipleri mevcut

```c
struct stat;

// system calls
int fork(void);
int exit(int) __attribute__((noreturn));
int wait(int*);
int pipe(int*);
int write(int, const void*, int);
int read(int, void*, int);
int close(int);
int kill(int);
int exec(const char*, char**);
int open(const char*, int);
int mknod(const char*, short, short);
int unlink(const char*);
int fstat(int fd, struct stat*);
int link(const char*, const char*);
int mkdir(const char*);
int chdir(const char*);
int dup(int);
int getpid(void);
char* sbrk(int);
int sleep(int);
int uptime(void);

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

`write()` fonksiyonu 3 adet parametre alıyor. İlki file descriptor, `fd`, ikincisi
içeriği yazılacak bufferın adresi ve üçüncüsü de kaç byte yazılacağı. Fonksiyon
yazımı yapılan byte sayısını dönüyor. İstenenden daha az yazma yapılması bir hata
göstergesi. Hemen ekrana *Merhaba Dunya!* yazan bir örnek yapalım.

```c
#include "kernel/types.h" //uint vs için
#include "user/user.h"

int
main()
{
  int n = write(1, "Merhaba Dunya!\n", 15);
  if (15 == n)
    exit(0);
  else
    exit(1);
}
```

Yukarıdaki kodu `user/merhaba.c` olarak kaydedelim. Bir de `Makefile` içerisinde
değişiklik yapmamız gerekiyor ki kodumuz derlensin `UPROGS` kısmını bulup en
sona kendi kodumuzu ekleyelim.

```makefile
UPROGS=\
        $U/_cat\
        $U/_echo\
        $U/_forktest\
        $U/_grep\
        $U/_init\
        $U/_kill\
        $U/_ln\
        $U/_ls\
        $U/_mkdir\
        $U/_rm\
        $U/_sh\
        $U/_stressfs\
        $U/_usertests\
        $U/_grind\
        $U/_wc\
        $U/_zombie\
        $U/_merhaba\
```

En sona `$U/_merhaba\` ekledim. `Makefile` ın sentaksını henüz anlamadım ama
öncekilere benzeterek yapıyorum şimdilik, sonra bakarız. `make qemu` dediğimizde
vs `ls` çektiğimizde `merhaba` komutunu görmemiz lazım.

```shell
$ ls
.              1 1 1024
..             1 1 1024
README         2 2 2305
xargstest.sh   2 3 93
cat            2 4 32848
echo           2 5 31696
forktest       2 6 15824
grep           2 7 36224
init           2 8 32192
kill           2 9 31656
ln             2 10 31480
ls             2 11 34784
mkdir          2 12 31712
rm             2 13 31696
sh             2 14 54144
stressfs       2 15 32584
usertests      2 16 180624
grind          2 17 47536
wc             2 18 33800
zombie         2 19 31056
merhaba        2 20 31160
console        3 21 0
```

Burada dikkatimi çeken şey sıralamanın alfabetik olmaması oldu, `Makefile` daki
sıraya göre çıkıyor. i-node ? gibi bir şeye göre sıralıyor olabilir, ilerde
bakarız. `console` da bir *device file* muhtemelen.

```shell
$ merhaba
Merhaba Dunya!
```

Ne güzel oldu değil mi? `write(1, ..)` ile `stdout` a bastık.

```text
ay@dsklin:~/ws/xv6-labs-2023$ ll user/merhaba*
-rw-rw-r-- 1 ay ay 38743 Apr 23 14:36 user/merhaba.asm
-rw-rw-r-- 1 ay ay   173 Apr 23 14:35 user/merhaba.c
-rw-rw-r-- 1 ay ay    58 Apr 23 14:36 user/merhaba.d
-rw-rw-r-- 1 ay ay  6536 Apr 23 14:36 user/merhaba.o
-rw-rw-r-- 1 ay ay  1535 Apr 23 14:36 user/merhaba.sym
```

**Gözlemler:** `make qemu` deyince otomatik derlendi ve bunlar çıktı. `.o` obhe
dosyası olmalı. Tüm executableların önünde `_` karakteri var, neden bilmiyorum.
Her şey statik linkleniyor, basit bir OS için mantıklı. O yüzden `.asm` dosyasının
boyutu büyük diye anlıyorum, içeriği de karmaşık. Fakat `.asm` neden sadece bizim
programı içermiyor çözemedim, ayrıca bunu nasıl yapmışlar `Makefile` ile bakacağım.

```shell
ay@dsklin:~/ws/xv6-labs-2023$ file user/_merhaba
user/_merhaba: ELF 64-bit LSB executable, UCB RISC-V, RVC, double-float ABI, version 1 (SYSV), statically linked, with debug_info, not stripped
ay@dsklin:~/ws/xv6-labs-2023$ file user/merhaba.o
user/merhaba.o: ELF 64-bit LSB relocatable, UCB RISC-V, RVC, double-float ABI, version 1 (SYSV), with debug_info, not stripped
```

---

Şimdi `read()` e bakalım. Benzer mantık, bu okuma yapıyor. Okuduğu byte sayısını
döndürüyor.

stdin'den okuduğunu stdout'a yazan bir program yazalım.

```c
#include "kernel/types.h"
#include "user/user.h"

static char buf[16];
static const char msg1[] = "read yapildi\n";
static const char msg2[] = "write yapildi\n";
static const char msg3[] = "read cikti!!!\n";

int main()
{
  for (;;){
    int n = read(0 , buf, sizeof(buf));
    write(1, msg1, sizeof(msg1) - 1);
    if (n <= 0) {
      write(1, msg3, sizeof(msg3) - 1);
      break;
    }
   write(1, buf, n);
   write(1, msg2, sizeof(msg2) - 1);
  }

  exit(0);
}
```

Bunu `user/loop.c` olarak kaydedelim ve yine `Makefile`ı benzer şekilde
düzenleyelim.

```text
...
  $U/_zombie\
  $U/_merhaba\
  $U/_loop\
...
```

Benzer şekilde `make qemu` ile çalıştıralım.

Şimdi bu kod ne yapıyor? `read(0,..)` ile stdin'den okuyoruz, okunan byte
kadar yazma yapıyoruz aynı içeriği geri basıyoruz, yani loopback yapıyoruz.
`sizeof(x) - 1` deki `-1` in sebebi stringlerin sonundaki `\0` karakteri
basmamak.

```text
$ loop
```

ile çalıştırdığımızda program bekliyor.

```text
$ loop
asd
read yapildi
asd
write yapildi
```

`asd` yazdım **ama Enter diyene kadar bir şey olmadı.** `read()` bloklanan bir
ama Enter'a basana kadar yazdıklarımız nerde, birazdan bakarız.

Burada buffer boyutunu 16 gibi küçük bir sayı seçtim. Bunu aşarsak ne olacak?

```text
abcdefghijklmnoprst0123456789
read yapildi
abcdefghijklmnopwrite yapildi
read yapildi
rst0123456789
write yapildi
```

Burada Enter demeden önce `abcdefghijklmnoprst0123456789` yazdım, 29 karakterden
oluşuyor. Sonra Enter'a bastığım zaman `read yapildi` mesajını gördük ve
`abcdefghijklmnop` kısmı ekrana write ile basıldı, tam 16 karakter. Mesajın
sonunda `\n` olmadığı için `write yapildi` yazısı hemen arkasına geldi. Daha
sonra read tekrar donüş yaptı ve kalan `rst0123456789` ve `\n` ekrana basıldı.
Dikkat ederseniz Enter karakteri de programa iletiliyor, `asd` yazdığımda da
öyle olmuştu.

Peki ben Enter'a basana kadar bu karakterler nerede duruyor? Bunun cevabı için
belki erken ama biraz kayna koduna bakındım, cevaplar `kernel/console.c`
içerisinde. Aslında biz bir şeyler yazdıkça ekranda görmemizin sebebi de bu.
Yani QEMU ya da başka bir şey bize bastığımızı geriye basmıyor.
[Burası](https://github.com/mit-pdos/xv6-riscv/blob/f5b93ef12f7159f74f80f94729ee4faabe42c360/kernel/console.c#L162)
ekrana basıldığı yer.

```{code-block} c
:lineno-start: 162
:emphasize-lines: 2
:caption: kernel/console.c

// echo back to the user.
consputc(c);
```

Burada kerneldeki console sürücüsü ekrana basıyor.

Hemen altında da gelen mesajların circular buffer mantığı ile console bufferına
konulduğunu görüyoruz.

```{code-block} c
:lineno-start: 159
:emphasize-lines: 1, 5, 8
:caption: kernel/console.c

if(c != 0 && cons.e-cons.r < INPUT_BUF_SIZE){
  c = (c == '\r') ? '\n' : c;

  // echo back to the user.
  consputc(c);

  // store for consumption by consoleread().
  cons.buf[cons.e++ % INPUT_BUF_SIZE] = c;
```

Bu buffer ise 128'lik olarak tanımlanmış.

```{code-block} c
:lineno-start: 48
:caption: kernel/console.c

#define INPUT_BUF_SIZE 128
```

Eğer buffer dolana kadar Enter'a basılmazsa 128 karakter yazılınca sanki
Enter'a basılmış gibi read ile bloklanmış olan fonksiyona buffer iletiliyor.

```{code-block} c
:lineno-start: 168
:caption: kernel/console.c
:emphasize-lines: 1, 2

if(c == '\n' || c == C('D') || cons.e-cons.r == INPUT_BUF_SIZE){
  // wake up consoleread() if a whole line (or end-of-file)
  // has arrived.
  cons.w = cons.e;
  wakeup(&cons.r);
```

O zaman hemen deneyelim bakalım 128 den fazla bir şey verince ne oluyor.
Beklediğimiz gibi Enter'a basmasak bile 128 karakter gelince read devam ediyor,

```text
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000read yapildi
0000000000000000write yapildi
read yapildi
0000000000000000write yapildi
read yapildi
0000000000000000write yapildi
read yapildi
0000000000000000write yapildi
read yapildi
0000000000000000write yapildi
read yapildi
0000000000000000write yapildi
read yapildi
0000000000000000write yapildi
read yapildi
0000000000000000write yapildi
```

Diyelim ki `CTRL-D` ye bastık bu sefer de

```text
read yapildi
read cikti!!!
$
```

alıyoruz çünkü `CTRL-D` aslında bir nevi `EOT`/`EOF` sinyali veriyor yani bitti.
Bu durumda `read()` fonksiyonu pozitif bir sayı dönmüyor, bizim programımız da
çıkıyor.

Bu da yine yukarıdaki satır 168'de var, `c == C('D')` olarak kontrol ediliyor.
`C(x)` bir fonksiyonel macro, `#define C(x)  ((x)-'@')  // Control-x` olarak
verilmiş satır 26'da. `Ctrl-x` kombinasyonun kodları bu değerler sahip [^1f],
[^2f]. Yani Enter'a basmadan girdi vermek istiyorsak `CTRL-D` yapabiliriz
yazıyı yazıp. Yazmadan verirsek 0 uzunlukta bir girdi yapmış oluyoruz.

```text
$ loop
asd
read yapildi
asd
write yapildi
asdread yapildi
asdwrite yapildi
read yapildi
read cikti!!!
```

Yukarıdaki denemede `asd` yazıp Enter dedim daha sonra `asd` yazıp `Ctrl-d` yaptım.
Peki neden read ikinci çağrıda hemen dönüp, çıkışa sebep oldu? O da sanıyorum
şundan, sonra tekrar bakarız biraz yoruldum 😅

```{code-block} c
:lineno-start: 101
:caption: kernel/console.c
:emphasize-lines: 3, 4

if(c == C('D')){  // end-of-file
  if(n < target){
    // Save ^D for next time, to make sure
    // caller gets a 0-byte result.
    cons.r--;
  }
  break;
}
```

## Özet

Fena ilerlemedik, biraz *sistem programlama* yaptık, console driver'ına baktık.
`write()` ve `read()` i sanki anladık. Bir sonraki bölümde programımızı debug
etmeye çalışabiliriz gdb ile.

## Kaynaklar

- <https://pdos.csail.mit.edu/6.1810/2023/labs/util.html>
- <https://pdos.csail.mit.edu/6.1810/2023/lec/l-overview/>
- Ayrıca bknz: [genel kaynaklar](index.md)

[^1f]: <https://jkorpela.fi/chars/c0.html>
[^2f]: <https://stackoverflow.com/a/75030219/1766391>
