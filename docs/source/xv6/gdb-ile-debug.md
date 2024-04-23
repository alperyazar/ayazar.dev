---
giscus: be46d181-0399-4aaa-af9e-7ff85ff34934
---

# GDB ile Hata Ayıklama (Debug 🐛)

Şimdi, GDB ile kendi programımız debug etmeye çalışalım, olacak mı bilmiyorum.

## Çekirdek, Hardware Thread, hart Sayısı Ayarlama

Öncesinde bir konuya değinmek istiyorum. `make qemu` dediğimiz zaman aslında
çok çekirdekli bir sanal bilgisayar oluşuyor, elbette RISC-V. Default olarak
QEMU `-smp 3` diye bir argümanla çağrılıyor, 3 çekirdekli bir makine sayı
biraz ilginç. QEMU çalışırken `top -c` dersek QEMU'nun %300 CPU kullandığını
gördüm. Yani muhtemelen her bir sanal RISC-V çekirdeği için bilgisayarımdaki
bir core'u harcıyor. Normalde QEMU %100 CPU kullanan bir uygulama değil. Fakat
emule ettiği sistem hiç *uyumuyorsa* mesela infinite loopta dönüyorsa her core
böyle olabilir belki. Her ne kadar bu kadar CPU kullanımı garip gelse de
ileriye dönük bu konuyu bırakıyorum.

```text
xv6 kernel is booting

hart 2 starting
hart 1 starting
init: starting sh
```

Buradaki `hart x` core sayısı ile ilgili. Koda bir bakalım [^1f]:

```{code-block} c
:caption: kernel/main.c
:lineno-start: 13
:emphasize-lines: 26

if(cpuid() == 0){
  consoleinit();
  printfinit();
  printf("\n");
  printf("xv6 kernel is booting\n");
  printf("\n");
  kinit();         // physical page allocator
  kvminit();       // create kernel page table
  kvminithart();   // turn on paging
  procinit();      // process table
  trapinit();      // trap vectors
  trapinithart();  // install kernel trap vector
  plicinit();      // set up interrupt controller
  plicinithart();  // ask PLIC for device interrupts
  binit();         // buffer cache
  iinit();         // inode table
  fileinit();      // file table
  virtio_disk_init(); // emulated hard disk
  userinit();      // first user process
  __sync_synchronize();
  started = 1;
} else {
  while(started == 0)
    ;
  __sync_synchronize();
  printf("hart %d starting\n", cpuid());
  kvminithart();    // turn on paging
  trapinithart();   // install kernel trap vector
  plicinithart();   // ask PLIC for device interrupts
}
```

Kodu takip ederseniz `cpuid()` nin ilgili çekirdeğin `hart` yani `hardware thread`
ID'si olduğunu görebiliyoruz [^2f]. RISC-V mimarisi detaylarına şimdilik bakmıyoruz
ama hart'ları birer core gibi düşünebiliriz diye anlıyorum [^3f]

Burada ID 0 olanı niye bastırmamışlar bilmiyorum,
çünkü 1 ve 2 görünce 2 çekirdek düşünebiliriz aslında 3 çalışıyor.

İstersek çekirdek sayısını değiştirebiliriz. `Makefile` içerisinde `CPUS` diye
bir çevresel değişken, environment variable, okunuyor, default 3. Bunu geçersek
core sayısını değiştirebiliriz.

```text
ay@dsklin:~/ws/xv6-riscv$ CPUS=1 make qemu

xv6 kernel is booting

init: starting sh
$ QEMU: Terminated

ay@dsklin:~/ws/xv6-riscv$ CPUS=8 make qemu

xv6 kernel is booting

hart 6 starting
hart 7 starting
hart 3 starting
hart 2 starting
hart 1 starting
hart 4 starting
hart 5 starting
init: starting sh
```

Tek core ya da 8 core açabiliriz. Benim sistemde her core %100 CPU kullanıyor,
onu tekrar belirteyim. `make CPUS=4 qemu` diyebiliriz alternatif olarak,
`CPUS` u ortaya alma şeklinde.

## GDB

Şimdi gelelim esas konuya. QEMU üzerinde çalıştırdığı uygulamayı, sanal makinede
çalışan uygulamayı sanki JTAG gibi doğrudan donanıma bağlıymışız gibi GDB ile
debug etmeye imkan sağlıyor [^4f]:

> QEMU supports working with gdb via gdb’s remote-connection facility (the
> "gdbstub"). This allows you to debug guest code in the same way that you might
> with a low-level debug facility like JTAG on real hardware. You can stop and
> start the virtual machine, examine state like registers and memory, and set
> breakpoints and watchpoints.

Eğer xv6'yı `make qemu-gdb` ile çalıştırırsak QEMU bu modda çalışıyor.

```text
ay@dsklin:~/ws/xv6-riscv$ make qemu-gdb
sed "s/:1234/:26000/" < .gdbinit.tmpl-riscv > .gdbinit
*** Now run 'gdb' in another window.
qemu-system-riscv64 ... -S -gdb tcp::26000
```

Burada bizler için `.gdbinit` dosyası oluşuyor ve QEMU çalışırken
`S -gdb tcp::26000` parametresi geçiliyor. Şimdi başka bir pence açıp aynı
dizine gidip `gdb` diyoruz. `gdb`, buradaki `.gdbinit` dosyasını okuyacak.

Şöyle bir hata aldık:

```text
warning: File "/home/ay/ws/xv6-riscv/.gdbinit" auto-loading has been declined by
your `auto-load safe-path' set to "$debugdir:$datadir/auto-load".
```

Önce bunu düzeltelim [^5f].

`$HOME/.config/gdb/gdbinit` i açıp
`add-auto-load-safe-path /home/ay/ws/xv6-riscv/.gdbinit` ekliyoruz.
Bende bu dosya yoktu, yarattım.

Daha sonra `gdb` dediğimiz zaman bu sefer bu hata geliyor fakat

```text
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word".
.gdbinit:2: Error in sourced command file:
Undefined item: "riscv:rv64".
```

gibi bir hata aldık. Ben `gdb` yazdığım için RISC-V destekleyen *cross GDB ?*
değil, *klasik* gdb çalıştı. `riscv64-linux-gnu-gdb` çalıştıracaktım ama
böyle bir dosya sanırım yok [^6f]. `gdb-multiarch` ile yapalım, bu sefer oldu.
Şöyle bir uyarı aldık:

```text
warning: No executable has been specified and target does not support
determining executable automatically.  Try using the "file" command.
0x0000000000001000 in ?? ()
```

Şimdilik göz ardı ediyorum. `gdb` de `c` yani continue dediğimizde xv6 çalışmaya
başlıyor. `Ctrl-C` ile durdurabiliyoruz. Bunu durdurunca CPU kullanımı da 0'a
düşüyor, durduğu nokta bende schedular oldu. Daha sonra `c` ile devam edebiliriz.

### `loop.c` Debug

Şimdi bir önceki yazıda yazdığımız `loop.c` kodunu debug etmeye çalışalım.
Mesela `Ctrl-d` ile programdan çıkabiliyorduk. Bizim kodun çıkması için `read()`
geri dönüş değerinin 0 veya daha küçük olması gerekiyor. Bakalım hangi değeri
dönüyormuş.

`make qemu-gdb` ile bir pencerede başlatalım xv6'yı, diğer pencerede
`gdb-multiarch` çalıştıralım. `c` diyelim ve xv6'yı salalım çalışsın.

xv6'da `loop` diyerek yazılımı çalıştırıyoruz. Beklediğimiz gibi çalışıyor.
Şimdi `gdb` de `Ctrl-C` diyelim ve target'ı durduralım. `gdb` de
`file user/_loop` diyerek `gdb` ye çalışan komutu tanıtalım. Sonra `list main`
diyerek kaynak kodunu listeleyelim:

```text
(gdb) file user/_loop
Reading symbols from user/_loop...
(gdb) list main
5 static const char msg1[] = "read yapildi\n";
6 static const char msg2[] = "write yapildi\n";
7 static const char msg3[] = "read cikti!!!\n";
8
9 int main()
10 {
11   for (;;){
12     int n = read(0 , buf, sizeof(buf));
13     write(1, msg1, sizeof(msg1) - 1);
14     if (n <= 0) {
(gdb)
```

`n` nin değerini görmek için mesela satır 13'e breakpoint koyalım, `b 13` diyerek.

```text
(gdb) b 13
Breakpoint 1 at 0x56: file user/loop.c, line 13.
```

Şimdi `c` diyerek programımızı devam ettirelim. Mesela `test` yazıp Enter diyelim.
Programımız breakpoint'te duracaktır. Şimdi `p n` yazıp gdb'de `n` nin değerine
bakalım. `5` miş. Neden? Çünkü `test` + Enter 5 karakter. `c` deyip devam edelim.
Şimdi loop programına `Ctrl-d` verelim. Yine breakpointte durduk. `p n` diyoruz
ve 0 değerini gördük. Demek ki `read()` bize 0 dönüyormuş bu durumda. `c`
dersek programımızın çıkığını göreceğiz. QEMU'dan yine `Ctrl-a` `x` ,le çıkabiliriz.
`gdb` den de `quit` deyip çıkabiliriz. Böylece programımız debug edebildik, ne hoş

Bu altyapı kernelin kendsinin de debug işlemi için kullanılabilir. Onun için
`file kernel/kernel` dememiz gerekecek gdb'ye. Demesek olur mu tam emin değilim,
ileride bakarız.

[^1f]: <https://github.com/mit-pdos/xv6-riscv/blob/f5b93ef12f7159f74f80f94729ee4faabe42c360/kernel/main.c>
[^2f]: <https://stackoverflow.com/a/42698655/1766391>
[^3f]: <https://electronics.stackexchange.com/a/580661/15484>
[^4f]: <https://qemu-project.gitlab.io/qemu/system/gdb.html>
[^5f]: <https://pdos.csail.mit.edu/6.1810/2023/labs/guidance.html>
[^6f]: <https://stackoverflow.com/a/67403143/1766391>
