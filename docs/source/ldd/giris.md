---
giscus: 11abc6dd-d8e8-44f1-9ad4-c18530c13372
---

# Aygıt Sürücüleri ve Çekirdek Modülleri

**Çekirdek modülleri** yani **kernel modules**, kernel içerisinde ve kernel
space içerisinde çalışan kodlardır. Eğer bir modül bir cihaz için yazılıyorsa o
**device driver** yani **aygıt sürücüsü** olur. Yani aygıt sürücüleri, çekirdek
modüllerinin bir alt kümesidir.

Aygıt sürücüler donanımın interrupt kontrolcülerine erişmek isteyecektir tipik
olarak ya da donanım register'larına erişmek isteyecektir. Bu tarz *özel*
erişimler user space tarafından mümkün olmamaktadır.

Kernel'in bilgisayarın donanımları ile konuşabilmesi için bir sürücüye ihtiyacı
vardır. Aksi taktirde kernel, donanıma istediğini yaptıramaz.

Doğal olarak her işletim sisteminin aygıt sürücüsü farklıdır: Windows vs Linux
Genel bir aygıt sürücüsü yazmak diye bir şey yoktur. Hatta Linux özelinde
konuşacak olursak kernel versiyonu değiştikçe sürücülerin de değişmesi
gerekebilmektedir çünkü kernelin kendi kodu da değişmektedir.

```{note}
Yine de versiyon 2.6'dan sonra çok büyük köklü değişikliklerin olmadığını
söylemek yanlış olmaz. O yüzden klasik kitaplardan LDD3'ün hala geçerli olduğunu
düşünebiliriz.
```

Aygıt sürücüler gibi kernel modüllerde tüm C fonksiyonları kullanılamaz çünkü
standart C kütüphanesi, kernel içerisinde kullanılmamaktadır. Kernel tarafından
sağlanan başka fonksiyonlar ve header yani başlık dosyaları vardır. Bizler
öncelikle gerekli dosyaları kurmalıyız.

## Gerekli Dosyaların Elde Edilmesi

Kernel modülü yazmak için kaynak kodlara ihtiyacımız yok fakat istersek Ubuntu
gibi sistemlerde `linux-source` paketini `apt` ile kurabiliriz. Bu paket ile
Canonical'ın patch'lerinin uygulanmış olduğu kernel kodu sistemimize gelecektir.

```shell
$ apt search linux-source

...

linux-source/jammy-updates,jammy-updates,jammy-security,jammy-security 5.15.0.102.99 all

  Linux kernel source with Ubuntu patches

...
```

Bu paketi kurarsak kaynak kodu `/usr/src` altına gelmektedir.

---

Kernelin sunduğu çeşitli fonksiyon ve macroları kullanabilmek için başlık
dosyalarına ihtiyacımız vardır. Bunlar `/usr/src/linux-headers-...` içinde
bulunur. Bunun için `linux-source` kurmamıza gerek yoktur.

```shell
ay@ubuntu2204:~$ ls -d /usr/src/linux-headers-$(uname -r)
/usr/src/linux-headers-6.5.0-27-generic
```

gibi.

---

Yüklenebilir kernel modülleri tipik olarak `/lib/modules/$(uname -r)` altında
bulunur. Bizim modülleri derlememiz için gerekli olan çeşitli dosyalar da
burada yer alır.

```shell
ay@ubuntu2204:~$ ls -d /lib/modules/$(uname -r)
/lib/modules/6.5.0-27-generic
```

---

## Kernel Fonksiyonları

Kernel modülünde user space kütüphaneleri kullanılamaz, örn `malloc(), free(),
printf()` kullanılamaz. Burada kernel içerisindeki bazı fonksiyonları
kullanabiliriz, bunlar **kernel tarafından export edilir.** Kernel içerisindeki
her fonksiyon, driver içerisinden kullanılamaz. Bu fonksiyonlar doğal olarak
user tarafından da çağrılamaz. Sistem programlama yani sistem fonksiyonlarının
bu export edilen fonksiyonlarla bir ilgisi yoktur.

Bir kernel modülü içerisindeki belli fonksiyonlar da programcı tarafından export
edilebilir. Böyle bir durumda bu fonksiyonlar da başka modüller tarafından
kullanılabilir. Günün sonunda eklenen bir modül kernelin bir parçası haline
geliyor ve o da bir şeyler export edebiliyor.

> Monolitik ve C'de yazılmış bir kernelin böyle bir "plug-in" mekanizması içermesi
> şaşırtıcı değil mi?

## Kernel Modüllerinin Derlenmesi ve Link Edilmesi

Normalde statik ve dinamik link şeklinde iki tip link biliyoruz user space
programlar için. Kernel modüllerinin derlenmesi ve link edilmesi, user space
programlardan daha karmaşık olabilir. Kernel geliştiricileri bizler için bu
işleri kolay yapabilmemiz için `Makefile` lar veriyorlar.

Derlenmiş kernel modülleri birer **ELF object file** formatındadır ama
kendilerine özel çeşitli **section** lar içerirler. Böyle bir formatın
çıkabilmesi için GCC'nin özel switch'ler ile çağırılması gerekir.

### Örnek

Aşağıdaki `Makefile` örnek olarak verilmiştir.

```makefile
obj-m += helloworld.o

all:
  make -C /lib/modules/$(shell uname -r)/build M=${PWD} modules
clean:
  make -C /lib/modules/$(shell uname -r)/build M=${PWD} clean
```

veya (alttakini tercih edin [^1f])

```makefile
obj-m += helloworld.o

PWD := $(CURDIR)

all:
  make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
clean:
  make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```

Yukarıdaki Makefile bir *boilerplate code* olarak kullanılabilir.

`obj-m`, kernel tarafından sağlanan Makefile'ların kullandığı bir değişkendir:

> A makefile symbol used by the kernel build system to determine which modules
> should be built in the current directory

Aslı işi yapan yer `-C` ile belirtilen yerdeki Makefile dosyalarıdır. Bunlar,
kernel geliştiricileri tarafından sağlanır.

```shell
$ cat /lib/modules/$(uname -r)/build/Makefile

...
```

Yukarıdaki Makefile, `helloword.c` dosyasının derlenmesini sağlamaktadır.

Eğer birden fazla dosya varsa:

```makefile
obj-m += a.o b.o c.o
```

veya

```makefile
obj-m += a.o
obj-m += b.o
obj-m += c.o
```

yapabiliriz.

Bu dosyayı parametrik de yapabiliriz:

```makefile
obj-m += ${file}.o
#...
```

sonra

```text
make file=helloworld
```

diyebiliriz.

## Kaynaklar

- [Genel Kaynaklar](index.md)
- `127-2625`

[^1f]: <https://stackoverflow.com/q/52437728/1766391>
