---
giscus: cf2437e7-7642-4e66-8455-aff7981b4b0b
---

# "Merhaba Dunya!"

Adettendir bir Hello World diyelim. Bir önceki bölümdeki `Makefile` dosyasını
kullanalım.

```{code-block} makefile
:caption: Makefile
:lineno-start: 1

obj-m += ${file}.o
PWD := $(CURDIR)

all:
  make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
  make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

Bu da kodumuz:

```{code-block} c
:caption: merhaba.c
:lineno-start: 1

#include <linux/module.h>
#include <linux/kernel.h>

int init_module(void){
  printk(KERN_INFO "Merhaba Dunya...\n");
  return 0;
}

void cleanup_module(void) {
  printk(KERN_INFO "Gule gule Dunya...\n");
}
```

Daha sonra `make file=merhaba` dediğimizde hata alıyoruz.

```shell
ay@ubuntu2204:~/ws/sys/driver$ make file=merhaba
make -C /lib/modules/6.5.0-27-generic/build M=/home/ay/ws/sys/driver modules
make[1]: Entering directory '/usr/src/linux-headers-6.5.0-27-generic'
warning: the compiler differs from the one used to build the kernel
  The kernel was built by: x86_64-linux-gnu-gcc-12 (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0
  You are using:
  CC [M]  /home/ay/ws/sys/driver/merhaba.o
/bin/sh: 1: gcc-12: not found
make[3]: *** [scripts/Makefile.build:251: /home/ay/ws/sys/driver/merhaba.o] Error 127
make[2]: *** [/usr/src/linux-headers-6.5.0-27-generic/Makefile:2039: /home/ay/ws/sys/driver] Error 2
make[1]: *** [Makefile:234: __sub-make] Error 2
make[1]: Leaving directory '/usr/src/linux-headers-6.5.0-27-generic'
make: *** [Makefile:6: all] Error 2
```

Diyor ki şu an kullanılan kernelin derlendiği C derleyicisi ile senin kullandığın
farklı ve `gcc-12` yi bulamadım diyor. Hemen bendekine bakıyoruz.

```shell
ay@ubuntu2204:~/ws/sys/driver$ gcc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

Bende versiyon 11 varmış, o 12 arıyor. `sudo apt install gcc-12` ile kuralım.

```shell
ay@ubuntu2204:~/ws/sys/driver$ gcc-12 --version
gcc-12 (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0
Copyright (C) 2022 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

ay@ubuntu2204:~/ws/sys/driver$ gcc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

Her ne kadar `gcc` hala eski olanı gösterse de `gcc-12` nin olması yeterli oluyor.

```shell
ay@ubuntu2204:~/ws/sys/driver$ which gcc
/usr/bin/gcc

ay@ubuntu2204:~/ws/sys/driver$ which gcc-12
/usr/bin/gcc-12

ay@ubuntu2204:~/ws/sys/driver$ ls -lah /usr/bin/gcc
lrwxrwxrwx 1 root root 6 Ağu  5  2021 /usr/bin/gcc -> gcc-11
```

ve

```shell
ay@ubuntu2204:~/ws/sys/driver$ make file=merhaba
make -C /lib/modules/6.5.0-27-generic/build M=/home/ay/ws/sys/driver modules
make[1]: Entering directory '/usr/src/linux-headers-6.5.0-27-generic'
warning: the compiler differs from the one used to build the kernel
  The kernel was built by: x86_64-linux-gnu-gcc-12 (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0
  You are using:           gcc-12 (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0
  CC [M]  /home/ay/ws/sys/driver/merhaba.o
  MODPOST /home/ay/ws/sys/driver/Module.symvers
ERROR: modpost: missing MODULE_LICENSE() in /home/ay/ws/sys/driver/merhaba.o
make[3]: *** [scripts/Makefile.modpost:144: /home/ay/ws/sys/driver/Module.symvers] Error 1
make[2]: *** [/usr/src/linux-headers-6.5.0-27-generic/Makefile:1991: modpost] Error 2
make[1]: *** [Makefile:234: __sub-make] Error 2
make[1]: Leaving directory '/usr/src/linux-headers-6.5.0-27-generic'
make: *** [Makefile:6: all] Error 2
```

Yukarıda hala derleyici uyarısı veriyor ama sadece isimler farklı gibi, sonuçta
ikisi de `12.3.0`.

`ERROR: modpost: missing MODULE_LICENSE()` şeklinde bir hata aldık, patladık.

Yüklenebilir kernel modüllerinde lisansın belirtilmesi güncel kernellerde
zorunludur. Bu, yasal problemler gibi çeşitli çok teknik olmayan problemlerin
önüne geçmek için ya da hata durumlarında kernel'i **tainted** olarak işaretlemek
için alınmış bir tedbirdir [^1f] [^2f] [^3f]. Eskiden derleniyormuş ama yüklerken
bu durum ortaya çıkıyormuş artık derlenmiyor.

`MODULE_LICENSE` makrosunun çalışması için `#include` larının altına yazmamız
gerekiyor. Şimdilik derlemeye devam etmek için `GPL` lisansını seçebiliriz.
Elbette normalde modülümüze uygun bir lisans seçmemiz gerekiyor, buna ileride
değinebilirim.

```{code-block} c
:caption: merhaba.c
:lineno-start: 1

#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");

int init_module(void){
  printk(KERN_INFO "Merhaba Dunya...\n");
  return 0;
}

void cleanup_module(void) {
  printk(KERN_INFO "Gule gule Dunya...\n");
}
```

bundan sonra

```shell
ay@ubuntu2204:~/ws/sys/driver$ make file=merhaba
make -C /lib/modules/6.5.0-27-generic/build M=/home/ay/ws/sys/driver modules
make[1]: Entering directory '/usr/src/linux-headers-6.5.0-27-generic'
warning: the compiler differs from the one used to build the kernel
  The kernel was built by: x86_64-linux-gnu-gcc-12 (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0
  You are using:           gcc-12 (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0
  CC [M]  /home/ay/ws/sys/driver/merhaba.o
  MODPOST /home/ay/ws/sys/driver/Module.symvers
  CC [M]  /home/ay/ws/sys/driver/merhaba.mod.o
  LD [M]  /home/ay/ws/sys/driver/merhaba.ko
  BTF [M] /home/ay/ws/sys/driver/merhaba.ko
Skipping BTF generation for /home/ay/ws/sys/driver/merhaba.ko due to unavailability of vmlinux
make[1]: Leaving directory '/usr/src/linux-headers-6.5.0-27-generic'
```

Bu sefer başarılı olduk. Bir sürü de dosya çıkıyor.

```shell
ay@ubuntu2204:~/ws/sys/driver$ ll
total 352
drwxrwxr-x 2 ay ay   4096 May  5 15:47 ./
drwxrwxr-x 3 ay ay   4096 May  4 18:40 ../
-rw-rw-r-- 1 ay ay    174 May  4 18:46 Makefile
-rw-rw-r-- 1 ay ay    232 May  4 19:09 merhaba.c
-rw-rw-r-- 1 ay ay 111424 May  5 15:47 merhaba.ko
-rw-rw-r-- 1 ay ay    300 May  5 15:47 .merhaba.ko.cmd
-rw-rw-r-- 1 ay ay     33 May  5 15:47 merhaba.mod
-rw-rw-r-- 1 ay ay    968 May  5 15:47 merhaba.mod.c
-rw-rw-r-- 1 ay ay    168 May  5 15:47 .merhaba.mod.cmd
-rw-rw-r-- 1 ay ay  96320 May  5 15:47 merhaba.mod.o
-rw-rw-r-- 1 ay ay  38560 May  5 15:47 .merhaba.mod.o.cmd
-rw-rw-r-- 1 ay ay  16536 May  5 15:47 merhaba.o
-rw-rw-r-- 1 ay ay  37410 May  5 15:47 .merhaba.o.cmd
-rw-rw-r-- 1 ay ay     33 May  5 15:47 modules.order
-rw-rw-r-- 1 ay ay    136 May  5 15:47 .modules.order.cmd
-rw-rw-r-- 1 ay ay      0 May  5 15:47 Module.symvers
-rw-rw-r-- 1 ay ay    185 May  5 15:47 .Module.symvers.cmd
```

Bizim yükleyeceğimiz dosya **kernel object** dosyası yani `.ko` oluyor.

## Kernel'e Modülün Yüklenmesi ve Çıkartılması

Bunun için `insmod` aracını kullanacağız. Bunun için root yetkisi gerekiyor.

```shell
ay@ubuntu2204:~/ws/sys/driver$ sudo insmod merhaba.ko
[sudo] password for ay:
```

Bu işlem ile modülümüz kernel'e yüklendi. Yani modül kernelin bir parçası haline
geldi.

Kaldırmak için de `rmmod` programını kullanacağız.

```shell
ay@ubuntu2204:~/ws/sys/driver$ sudo rmmod merhaba.ko
```

gibi

Peki bu mesajlar nereye gitti? Bunları da `dmesg` üzerinden görebiliriz:

```text
...
[ 1305.004460] merhaba: loading out-of-tree module taints kernel.
[ 1305.004502] merhaba: module verification failed: signature and/or required key missing - tainting kernel
[ 1305.148552] Merhaba Dunya...
[ 1453.721631] Gule gule Dunya...
```

Bir modül yüklendiği zaman `init_module()` çağrılıyor kernel tarafından. Bu
modülün constructor'ı gibi, `main()` gibi özel bir fonksiyonmuş gibi
düşünebiliriz. Başarı durumunda 0, hata durumunda negatif değer dönmelidir. Hata
dönerse kernel bu modülü yüklemekten vazgeçer. Herhangi bir parametre almaz.
`cleanup_module()` de modül kernelden çıkartılırken çağrılıyor, destructor gibi.
Bir parametre almaz ve bir geri dönüş değeri yoktur, `void`.

Burada bu fonksiyonların ismini değiştirme şansımız var ama onu bir macro ile
söylememiz gerekiyor kodda. Bir şey yapmak istemiyorsak bu isimleri kullanmalıyız.

`printk()` kernel tarafından sağlanan ve standart C'de olmayan bir fonksiyondur.
Benzer şekilde `KERN_INFO` da kernel tarafından tanımlanan bir makrodur. Bunları
göreceğiz.

```{note}
C kodunda include ettiğimiz `linux/module.h` ve `linux/kernel.h`,
`/lib/modules/$(uname -r)/build/include` dizini içerisinde yer almaktadır. Yani
bildiğimiz libc ve POSIX kütüphanelerinin başlık dosyalarının bulunduğu
`/usr/include` içerisinde değildir.
```

## Kaynaklar

- [Genel Kaynaklar](index.md)
- `127-13847`

[^1f]: <https://docs.kernel.org/admin-guide/tainted-kernels.html>
[^2f]: <https://docs.kernel.org/process/license-rules.html#id1>
[^3f]: <https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/include/linux/module.h#n187>
