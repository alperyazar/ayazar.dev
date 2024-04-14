# Merhaba Dünya!

```{todo}
Bu yazı henüz tamamlanmamıştır.
```

Önceki kısımlarda Linux çekirdeğinin bizlere sunduğu 300'den fazla sistem
çağrısı olduğundan bahsetmiştim. Bunların hepsini öğrenecek miyiz? Belki,
bilemiyorum. Hepsini olmasa da çoğuna bakarız. Fonksiyonların kendisini öğrenmek
zaten çok önemli değil, önemli olan mantığını öğrenmek ve faydalı bir şeyler
çıkartabilmek.

Şimdi adettendir bir Merhaba Dünya yani Hello World projesi yapalım. Standart C
fonksiyonu olan `printf()` ekrana bu yazıyı yazan programımızı bir yazalım.

```c
#include <stdio.h>

int main(void)
{
  printf("Merhaba Dunya!\n");
  return 0;
}
```

Bunu örneğin `gcc merhaba.c` olarak derlediğimiz zaman bir `a.out` dosyası
çıkıyor, derlenmiş hali. `./a.out` dediğimiz zaman da bu program çalışıyor
çıktıyı ekranda görüyoruz. Peki sistem programlama bunun neresinde? Bu zaten
standart C fonksiyonu değil mi? Evet ama geliyoruz şimdi.

Peki, önceki bölümlerde aslında tüm programların işletim sisteminin çekirdeğine
yani Linux kerneline çeşitli syscall'lar yaparak bir şeyler yaptırabildiğinden
bahsetmiştim. Programın çalıştığı ekrana bu yazıyı yazması da işletim sistemi
desteği olmadan yapabileceği bir şey değil. O zaman bizim programımız da bir
noktada işletim sistemine çağrı yapıyor olmalı değil mi? Peki bunu
gözlemleyebilir miyiz? Elbette!

Linux üzerinde bu işler için kullanacağımız `strace` isimli bir yazılım
bulunuyor. `man strace` diyerek dokümanına bakabilirsiniz, açılımı *trace system
calls and signals*. Bu program sayesinde herhangi çalışan bir programın yaptığı
syscall'ları görebiliyoruz. Ubuntu 22.04 Desktop üzerinde bende yüklü durumda,
yoksa `apt install strace` ile kurabilirsiniz diye düşünüyorum.

`strace ./a.out` diyerek bu sefer programımızın yaptığı syscalları görebiliyoruz
ama ekran bir hayli kalabalık:

```text
alper@b:~/tmp$ strace ./a.out
execve("./a.out", ["./a.out"], 0x7ffc10249a00 /* 56 vars */) = 0
brk(NULL)                               = 0x649061d1d000
arch_prctl(0x3001 /* ARCH_??? */, 0x7ffdea160530) = -1 EINVAL (Invalid argument)
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x78c20b001000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=87923, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 87923, PROT_READ, MAP_PRIVATE, 3, 0) = 0x78c20afeb000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0P\237\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
pread64(3, "\4\0\0\0 \0\0\0\5\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0\0\0\0\0"..., 48, 848) = 48
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0\302\211\332Pq\2439\235\350\223\322\257\201\326\243\f"..., 68, 896) = 68
newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=2220400, ...}, AT_EMPTY_PATH) = 0
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
mmap(NULL, 2264656, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x78c20ac00000
mprotect(0x78c20ac28000, 2023424, PROT_NONE) = 0
mmap(0x78c20ac28000, 1658880, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x28000) = 0x78c20ac28000
mmap(0x78c20adbd000, 360448, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1bd000) = 0x78c20adbd000
mmap(0x78c20ae16000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x215000) = 0x78c20ae16000
mmap(0x78c20ae1c000, 52816, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x78c20ae1c000
close(3)                                = 0
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x78c20afe8000
arch_prctl(ARCH_SET_FS, 0x78c20afe8740) = 0
set_tid_address(0x78c20afe8a10)         = 30555
set_robust_list(0x78c20afe8a20, 24)     = 0
rseq(0x78c20afe90e0, 0x20, 0, 0x53053053) = 0
mprotect(0x78c20ae16000, 16384, PROT_READ) = 0
mprotect(0x64906036f000, 4096, PROT_READ) = 0
mprotect(0x78c20b03b000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0x78c20afeb000, 87923)           = 0
newfstatat(1, "", {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0x3), ...}, AT_EMPTY_PATH) = 0
getrandom("\x3f\x0c\xd0\x7f\x43\xca\xde\x43", 8, GRND_NONBLOCK) = 8
brk(NULL)                               = 0x649061d1d000
brk(0x649061d3e000)                     = 0x649061d3e000
write(1, "Merhaba Dunya!\n", 15Merhaba Dunya!
)        = 15
exit_group(0)                           = ?
+++ exited with 0 +++
```

Akıllarda iki soru? **Bunlar ne?** ve **Bizim basit programdan niye bu kadar
çıktı oluştu?** Bu gördüklerimiz aslında sistem çağrıları. `brk()`, `mmap()` vs
bunlar hepsi birer sistem çağrısı. İnanmazsanız `man x` diyerek (ya da doğrudan
çoğu için `man 2 x` çünkü man sayfalarında section 2 sistem çağrılarını anlatıyor)
bakabilirsiniz. Peki neden bu kadar çoklar? Hepi topu `printf()` çağırdık?
Bizim C programımız oldukça basit olsa bile bir programın çalışması sırasında
henüz konuşmadığımız *dinamik linker* gibi araçlar çalışıyor. Yani bir C
programının `main(){` sonrası ilk satırına gelene kadar otomatik olarak işletim
sistemi ya da standart C kütüphanesi tarafından yapılan işler var, burada onların
izini görüyoruz.

Şimdi bir şey deneyelim. Benim durumumda `a.out` dosyası yaklaşık 16 KB. Şimdi
`gcc -static merhaba.c` ile derliyorum. `-static` switch'i, derleyicinin
standart C kütüphanesi (libc) gibi tüm kütüphaneleri çıkan çalıştırılabilir
dosyayın içine gömmesini söylüyor. Bu durumda `a.out` un boyutu tam 880 KB.
Neden? Çünkü normalde `out` dosyası içerisinde olmayan, çalışma sırasında
dinamik olarak yüklenen glibc, yani GNU libc artıkbu dosyasının içerisinde.

```text
alper@b:~/tmp$ strace ./a.out
execve("./a.out", ["./a.out"], 0x7ffcd8092410 /* 56 vars */) = 0
arch_prctl(0x3001 /* ARCH_??? */, 0x7fff74ec9930) = -1 EINVAL (Invalid argument)
brk(NULL)                               = 0x1940000
brk(0x1940dc0)                          = 0x1940dc0
arch_prctl(ARCH_SET_FS, 0x19403c0)      = 0
set_tid_address(0x1940690)              = 31366
set_robust_list(0x19406a0, 24)          = 0
rseq(0x1940d60, 0x20, 0, 0x53053053)    = 0
uname({sysname="Linux", nodename="brs23-2204", ...}) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
readlink("/proc/self/exe", "/home/alper/tmp/a.out", 4096) = 21
getrandom("\x8e\x66\xcf\x02\x5f\x36\xb6\x55", 8, GRND_NONBLOCK) = 8
brk(0x1961dc0)                          = 0x1961dc0
brk(0x1962000)                          = 0x1962000
mprotect(0x4c1000, 16384, PROT_READ)    = 0
newfstatat(1, "", {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0x3), ...}, AT_EMPTY_PATH) = 0
write(1, "Merhaba Dunya!\n", 15Merhaba Dunya!
)        = 15
exit_group(0)                           = ?
+++ exited with 0 +++
```

**Peki şimdi kaç syscall?** [^2f] dersek bu sefer programımızın çok daha az syscall
ile çalıştığını görebiliriz. Yine bizim kodlamadığımız kısımlar var gibi ama
neyse şimdilik onlara takılmayalım. Ama statik linkediğimiz zaman syscall
sayımız azaldı, bunu gözlemledik.

```{todo}
Assembly ile sadece ret yapan program yaz. Bu syscall, strace overheadi olabilir mi?
```

Konumuza geri dönecek olursak trace çıktısının en son kısımlarında

```text
...
write(1, "Merhaba Dunya!\n", 15Merhaba Dunya!
)        = 15
...
```

Diye bir kısım görüyoruz. İşte programımız yazıyı ekrana burada basıyor. Biraz
karışık, 15 sayısı geçiyor ne alaka? Alakası şu, `Merhaba Dunya!\n` tam 15
karakter yer tutuyor, `\n` tek karakter. `write()` diye bir fonksiyondan bahsediyor
trace çıktısı? Peki neymiş bu `write()`?

```text
alper@b:~/tmp$ whatis write
write (2)            - write to a file descriptor
write (1)            - send a message to another user
```

`whatis write` dediğimiz zaman iki adet sonuç görüyoruz. `1` olan bir shell
komutu, `man 1 write` ile bakabilirsiniz. 2 olan ise bizim aradığımız. `man 2
write` ile ya da [buradan](https://man7.org/linux/man-pages/man2/write.2.html)
online dokümantasyonuna bakalım.

`write()` en temel fonksiyonlardan biri. Bir dosyaya yazmayı sağlıyor. Bakın:

```text
WRITE(2)                    Linux Programmer's Manual                   WRITE(2)

NAME
  write - write to a file descriptor

SYNOPSIS
  #include <unistd.h>

  ssize_t write(int fd, const void *buf, size_t count);

DESCRIPTION
  write()  writes up to count bytes from the buffer starting at buf to the file re‐
  ferred to by the file descriptor fd.
```

**Pardon dosya mı? Ne alaka? Biz dosyaya yazmadık ki?** Eeee, evet. Yazmadık
doğru. Biz ekrana yazdık, dosya ne alaka değil mi? Dosyaya yazacak olsam
`fprintf()` kullanırdım, ben gittim `printf()` kullandım. Doğru. Fakat Linux'ta
işler biraz karışık, ya da alışırsanız çok basit!

---

**Everything is a file** [^1f]

---

İşte Linux hatta Unix ile ilgili duyabileceğiniz en sık ifadelerden de biri
budur: **Her şey bir dosyadır.** Bunu, hemen anlamak kolay değil. Fakat kısaca
şunu söyleyebilirim. 70'lı yıllarda tasarımı yapılmış Unix sisteminin tasarımı
sırasında alınmış bir karar var. Unix üzerinde bulunan birçok donanım, sabit
disk, yazıcı, klavye gibi neredeyse tüm giriş/çıkış, I/O, cihazların kernel
dışına sanki bir dosya sisteminde bulunan, *byte stream* okunup yazılabilen bir
dosyalarmış gibi gösterilir. Yani programcı normal bir dosyaya nasıl yazma okuma
yapıyorsa bir cihaza da okuma yazma yapabilir. Cihaza yapılan okuma yazma
istekleri genelde o cihazın sürücüsüne yönlendirilir. Bunun getirdiği çeşitli
kolaylıklar var fakat yazıyı dağıtmamak adına geçiyorum. Şu an bilmemiz gerek
şey, `Merhaba Dunya!\n` yazısının gözüktüğü terminal ekranının çıkışının da
bizim programımız için bir dosya gibi davrandığıdır.

Linux üzerinde çalışan programlar, ki bunlara process yani proses diyoruz,
çalışmaları boyunca çeşitli dosyaları açıp kapatabilirler, yazma ya da okuma
amaçlı mesela. Açılmış olan dosyalar tipik olarak bir tamsayı ile ifade
edilirler. Linux dünyasında bu tam sayılara **file descriptor** adı
verilmektedir. Genelde `fd` olarak kısaltılırlar. Dikkat ederseniz `write()`
fonksiyonunun açıklaması da `...by the file descriptor fd` ile bitiyor. Fakat
Linux çekirdeği, bir program çalışmaya başladığı zaman tipik olarak 3 adet
dosyayı önden açar ve bunu programın en başında programın kullanabileceği hazır
hale getirir. Bunlara **standard stream** yani **standart akışlar** denir.
Bunlar:

- **standard input** yani **standart giriş**, `stdin`
- **standard output** yani **standart çıkış**, `stdout`
- **standard error** yani **standart hata**, `stderr`

bağlantılardır. Açık olan her bir dosyanın bir numarası olduğundan bahsetmiştim.
İşte `stdin` in numarası `0`, `stdout` un numarası `1`, `strderr` nin ise `2`
olmaktadır. **Peki bu dosyalar ne demek? Bir program buraya yazarsa bu yazdıkları
nereye gidiyor?**

İşte bu da Linux sistemlerinin güzelliklerinden biri. *Onu bilemiyoruz
maalesef!* [^3f] Nasıl bilemiyoruz? Öyle şey mi olur? Programlar bilemiyor.
Bunlar diskte yer kaplayan gerçek dosyalar değiller, adeta *sanal dosyalar.*
İşte her şeyin dosya olması biraz da bu demek. Yavaş yavaş geliyoruz, ha? Yani
bizim programımız kendi `stdout` dosyasına daha da doğrusu `1` nolu dosyasına
yazıyı basıyor, `stdout`, `stdin` gibi şeyler bizim koyduğumuz isimler kolay
anlaşalım diye, program sadece numaraları biliyor. Bu dosyaya gelen byte'ların
nereye gittiğini ise bizim programımız bilemez. O, bizim programı nasıl
çağırdığımıza bağlı. Normal şartlarda, `stdout` ve `stderr` ye yapılan yazmalar
önümüzdeki terminal ekranına düşüyor. Dışarıdan bir şey okumaya değinmedik ama
bunu sağlayan `stdin` girişi de yine aynı yere bağlı.

Şunu koy: `https://commons.wikimedia.org/wiki/File:Stdstreams-notitle.svg`

```{disqus}
:disqus_identifier: c6945529-ff36-4f4e-a4e6-eccfc09e0734
```

[^1f]: <https://en.wikipedia.org/wiki/Everything_is_a_file>
[^2f]: <https://www.youtube.com/watch?v=0yUYYohSXpc>
[^3f]: <https://www.youtube.com/watch?v=KLLt3izCIo4>
