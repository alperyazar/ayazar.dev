---
giscus: 11abc6dd-d8e8-44f1-9ad4-c18530c13372
---

# Aygıt Sürücüler ve Çekirdek Modülleri

**Çekirdek modülleri** yani **kernel modules**, kernel içerisinde ve kernel
space içerisinde çalışan kodlardır. Eğer bir modül bir cihaz için yazılıyorsa o
**device driver** yani **aygıt sürücü** olur. Yani aygıt sürücüleri, çekirdek
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

```{todo}
Yazı henüz bitmemiştir. `127-5851`
```

## Kaynaklar

- [Genel Kaynaklar](index.md)
- `127-2625`
