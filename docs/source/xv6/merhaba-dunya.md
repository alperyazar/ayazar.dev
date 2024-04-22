---
giscus: 0736237c-2071-4fef-973c-692cc59d87ca
---

# Merhaba Dünya!

xv6, daha doğrusu xv6-riscv, RISC-V işlemcisi için tasarlanmış bir OS. Çoğumuzun
kullandığı x86-64 işlemcilerde RISC-V için kod derlememiz **cross-compiler**
kullanarak mümkün olmaktadır. Bir de RISC-V işlemcinin emulasyonunu yapmak için
QEMU'ya ihtiyacımız olacak. Şimdi bunları kurup, xv6'yı çalıştırmayı deneyelim.

Ben çalışmalarımı Ubuntu temelli bir bilgisayarda yapacağım. Bunun için çeşitli
araçlar kurmam gerekiyor [^1f]. Ama xv6'nın github sayfasında [^2f] daha elle
bir kurulum tariflenmiş. Elbette daha zor olanı deneyeceğim, çünkü neden
olmasın?

## riscv-gnu-toolchain

<https://github.com/riscv-collab/riscv-gnu-toolchain>

```shell
$ sudo apt-get install autoconf automake autotools-dev curl python3 python3-pip libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev ninja-build git cmake libglib2.0-dev libslirp-dev
```

sonra

```shell
git clone https://github.com/riscv/riscv-gnu-toolchain
cd riscv-gnu-toolchain/
./configure --prefix=/opt/riscv
make
```

İlk `git clone` çok hızlı, çoğu bileşen git submodule çünkü fakat `make` deyince
ihtiyaç duyulanlar çekiliyor internetten. Benim durumumda yaklaşık **2.9 GB**
veri çekti. Şunu atlamışım, `/opt/riscv` yazılabilir değil. `sudo make` yapmak
istemiyorum, bu biraz riskli. Normal `make` ve sonra `sudo make install` da bu
`Makefile` ile desteklenmiyor, adamlar `make install` ı boş tasarlamışlar,
`Makefile` dan görebilirsiniz. Ben de uğraşmamak adına `$HOME` altına
oluşturdum.

```shell
mkdir -p ~/opt/riscv
./configure --prefix=/home/ay/opt/riscv
make
```

Bu sefer oldu. Submodule clone işlemlerini tekrar yapmadı, doğrudan yüklemeye
geçti. `make -j8` falan demediğime pişman oldum, neyse... 20 dk sonra, evet
cidden pişman oldum, işlemin ortasında `CTRL-C` verip `make -j16` dedim, bilgisayarımda
16 çekirdek var. Tüm CPU'ların %100 olduğu paralel bir derleme izliyorum 🍿.
Bu şekilde derlemem 15 dk civarı sürdü. Bakalım neler çıkmış.

```text
ay@dsklin:~/opt$ du -sh ~/opt/riscv/
1,4G  /home/ay/opt/riscv/
```

1.4G, fena değil.

```text
ay@dsklin:~/opt$ ls ~/opt/riscv/bin
riscv64-unknown-elf-addr2line   riscv64-unknown-elf-gdb
riscv64-unknown-elf-ar          riscv64-unknown-elf-gdb-add-index
riscv64-unknown-elf-as          riscv64-unknown-elf-gprof
riscv64-unknown-elf-c++         riscv64-unknown-elf-ld
riscv64-unknown-elf-c++filt     riscv64-unknown-elf-ld.bfd
riscv64-unknown-elf-cpp         riscv64-unknown-elf-lto-dump
riscv64-unknown-elf-elfedit     riscv64-unknown-elf-nm
riscv64-unknown-elf-g++         riscv64-unknown-elf-objcopy
riscv64-unknown-elf-gcc         riscv64-unknown-elf-objdump
riscv64-unknown-elf-gcc-13.2.0  riscv64-unknown-elf-ranlib
riscv64-unknown-elf-gcc-ar      riscv64-unknown-elf-readelf
riscv64-unknown-elf-gcc-nm      riscv64-unknown-elf-run
riscv64-unknown-elf-gcc-ranlib  riscv64-unknown-elf-size
riscv64-unknown-elf-gcov        riscv64-unknown-elf-strings
riscv64-unknown-elf-gcov-dump   riscv64-unknown-elf-strip
riscv64-unknown-elf-gcov-tool
```

çeşitli cross programları görüyoruz.

```text
ay@dsklin:~/opt$ ~/opt/riscv/bin/riscv64-unknown-elf-gcc --version
riscv64-unknown-elf-gcc (gc891d8dc23e) 13.2.0
Copyright (C) 2023 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

sanki oldu.

## QEMU

Şimdi de `riscv64-softmmu` destekleyen bir QEMU gerekiyor. Ruh hastası olduğumuz
için bunu da kaynak koddan derleyelim bakalım [^3f].

```shell
wget https://download.qemu.org/qemu-9.0.0-rc4.tar.xz
tar xvJf qemu-9.0.0-rc4.tar.xz
cd qemu-9.0.0-rc4
./configure
make -j16
```

`.tar.xz` nin boyutu 123 MB civarı. `-j16` yerine kendi bilgisayarınızın işlemci
çekirdeği sayısını yazın. Derleme sırasında yaklaşık 9500 dosya derleniyor. Bu
da bende bir 10-15 dk sürdü. Burada `./build` altında çeşitli executable dosyalar,
`qemu-system-riscv64` gibi ve `.h` dosyaları var, yaklaşık 470 adet.

```text
ay@dsklin:~/ws/qemu/qemu-9.0.0-rc4$ du -sh build/
5,3G  build/
```

5.3G az değil. Elbette ben make deyince QEMU hangi sistemi destekliyorsa
her şey için derledi. Sadece `make qemu-system-riscv64` deseydik yetecekti sanırım.

## xv6-riscv

Projeyi çekelim.

```shell
git clone git@github.com:mit-pdos/xv6-riscv.git
```

`Makefile` a hızlıca baktığımda `qemu-system-riscv64` ve `riscv64-unknown-elf-`
gibi dosyaların path'te olması gerektiğini anlıyorum. O zaman

```shell
cd xv6-riscv
export PATH=$PATH:$HOME/opt/riscv/bin:$HOME/ws/qemu/qemu-9.0.0-rc4/build
make qemu
```

**Vee 3-4 saniye sonra...**

```text
xv6 kernel is booting

hart 1 starting
hart 2 starting
init: starting sh
$
```

🥳 🥳 🥳

xv6'yı derledik ve QEMU'da emule edebildik. Derleyiciyi ve QEMU'yu sıfırdan
kaynak kodundan derledik.

QEMU'dan `CTRL-A` ve ardından `x` tuşuna basarak çıkabiliriz.

## Pre-built Binary

Şimdi kendimizin derlediği QEMU ve cross-compile derleyici yerine MIT'nin
sitesinde anlatıldığı gibi `apt` den önceden derlenmiş programları kuralım
sisteme [^1f].

```shell
sudo apt-get install git build-essential gdb-multiarch qemu-system-misc gcc-riscv64-linux-gnu binutils-riscv64-linux-gnu
```

Şimdi yeni bir terminal açalım, `$PATH` normale dönsün yani kendi derlememiz olan
QEMU ve cross-compiler PATH'te olmasın ve aynı şeyi deneyelim:

```shell
cd xv6-riscv
make clean
make qemu
```

Burada da yine aynı sonucu alıyoruz.

**Yani kaynak kodundan derlemeye gerek yok bu araçları** Ama bunu yapmak daha
zevkli.

## Sonuç

Merhaba Dünya! diyebildik. Bilgisayarımıza `xv6-riscv` nin kaynak kodunu çektik,
cross-compiler ile derledik ve QEMU emülasyonu ile çalıştırdık, daha ne olsun!

[^1f]: <https://pdos.csail.mit.edu/6.828/2023/tools.html>
[^2f]: <https://github.com/mit-pdos/xv6-riscv>
[^3f]: <https://www.qemu.org/download/#source>
