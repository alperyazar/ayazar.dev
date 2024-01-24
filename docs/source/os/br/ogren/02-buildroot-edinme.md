# Buildroot'u Edinme

Artık elimizi kirletmenin vakti geldi ve **Buildroot'u kullanarak ilk defa
kendimize ait bir gömülü Linux dağıtımı oluşturuyoruz.** Önce biraz Buildroot
hakkında konuşacağız ve sonra hep beraber Buildroot'u indirip, ilk derlememizi
yapacağız. Vallahi şimdiden heyecanlandım, haydi hemen başlayalım! Buildroot
öğreniyoruz serisinin üçüncü içeriği ile yolculuğumuza devam ediyoruz.

```{note}
[Bir önceki bölümde](01-gomulu-linux-nedir.md), Buildroot'un ihtiyacımız
doğrultusunda bir gömülü Linux dağıtımı oluşturan bir araç olduğunu görmüştük.
Eğer bakmadıysanız, gömülü Linux gibi önemli ve aslında Buildroot'tan bağımsız
genel kavramları konuştuğumuz, [bir önceki bölüme](01-gomulu-linux-nedir.md), bu
bölümden hemen önce bakmanızı tavsiye ederim.
```

Buildroot, Yocto ile benzer bir şekilde isteklerimiz doğrultusunda bize temelde
4 farklı çıktı üretiyor:

- İsteğimiz doğrultusunda ayarlanmış ve derlenmiş bir **Linux kernel**
- U-boot gibi bir **bootloader**
- Bir dosya sistemi yani **RootFS**
- oluşturduğumuz işletim sistemi üzerinde çalışacak programları geliştirmekte
kullanabileceğimiz, cross compile yeteneği olan bir **tool chain** (bazen SDK da
deniyor).

Peki bu ayarları nasıl yapacağız? Yani isteklerimizi bu araca nasıl ileteceğiz?
Birazdan göreceğimiz gibi [menuconfig](https://en.wikipedia.org/wiki/Menuconfig)
ve xconfig gibi araçları kullanacağız.

**BURAYA YAN YANA FOTO KOY**

## Buildroot'un özellikleri

Buildroot **hızlıdır.** Temel ve basit bir RootFS'i birkaç dakikada
oluşturabilirim diyor (elbette bilgisayarınıza bağlı). Göreceğiz! Ayrıca 2 MB
kadar küçük RootFS çıktıları üretebiliyormuş.

Buildroot **iyi belgelenmiş** bir projedir. Buildroot'un hem bundan hem de
[Make](https://en.wikipedia.org/wiki/Make_(software)) tabanlı olmasından dolayı
kolay anlaşılır olduğu söyleniyor, bunu da göreceğiz! (Umarım Makefile ile çok
uğraşmayız 🤞)

[Önceki bölümde](01-gomulu-linux-nedir.md) **userspace** kavramından
bahsetmiştik, hatırlıyor musunuz? Burada temelde kütüphaneler ve uygulamalar
vardı. İşte Buildroot 2800'den fazla userspace bileşeni destekliyor,
oluşturduğumuz Linux dağıtıma koyabiliyor.

Buildroot, yonga, işlemci, ya da SoC üreticisinden bağımsız bir yapıda, herhangi
bir üreticiye bağlı değil (**vendor neutral**). Bu da biz geliştiricilerin aynı
aracı, yani Buildroot’u, farklı farklı kartlar için kullanabileceği anlamına
geliyor. Benzer şekilde ARM, RISC-V, MIPS, Microblaze gibi birçok işlemci
mimarisini de destekliyor.
