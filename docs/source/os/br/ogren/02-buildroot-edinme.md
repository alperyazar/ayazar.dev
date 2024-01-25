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

Buildroot'un çeşitli sürümleri mevcut. Ben, Bootlin'in eğitim dokümanları ile
paralel gitmek adına onların kullandığı **2022.02** sürümü ile devam edeceğim.
Bir tık eski bir sürüm fakat konunun temellerini anlamak için en güncel sürümü
kullanmamıza da gerek yok.

Buildroot'un web sitesi: [buildroot.org](https://buildroot.org/)

## Buildroot'un tasarım felsefesi

İşte Buildroot'un özellikleri aslında arkasındaki tasarım felsefesini de
yansıtıyor. Buildroot'un hedefleri arasında:

- kolay kullanılabilirlik
- kolay değiştirilebilirlik (customize)
- kolay tekrarlanabilirlik (reproducible builds)
- küçük ve hızlı açılan Linux dağıtımları oluşturabilme
- kolay öğrenilebilme

yer alıyor.

## Kimler Buildroot kullanıyor?

Bootlin'in dokümanlarına göre **SpaceX** ve **Tesla** gibi firmalar bu aracı
kullanıyor örneğin. Ayrıca bulabileceğimiz tüm Single Board Computer, SBC, ve
System on Chip, SoC, gibi ürünlerin Buildroot tarafından desteklendiğini
söylesek yanılmış olmayız.

## Buildroot'u edinme

<https://buildroot.org/downloads> adresinden indirebiliyoruz. Her 3 ayda bir,
Şubat (02), Mayıs (05), Ağustos (08) ve Kasım (11) aylarında bir sürüm
yayınlanıyor. Sürüm isimleri ise `Yıl.Ay` şeklinde. Örneğin an itibariyle en
güncel sürüm `2023.11`. Ayrıca her yıl bir adet **Long Term Support** yani
**LTS** sürümü yayınlanıyor. LTS sürüm yayınlandıktan sonra 1 yıl boyunca
güvenlik yamaları, hata yani bug düzeltmeleri ve derleme sistemi ile ilgili olan
düzeltmeler ile destekleniyor. An itibariyle güncel LTS sürümü `2023.02` ve
gidişata göre bir sonraki de `2024.02` olacak. Bootlin firmasının eğitim için
seçtiği ve benim de kullanacağım `2022.02` sürümünün de bir LTS sürümü olduğu
dikkatimi çekti.

<https://buildroot.org/downloads> adresine gittiğimiz zaman `.tar.xz` uzantılı
dosyalar görüyoruz, `buildroot-2023.11.tar.xz` gibi. Buildroot'u bu şekilde
indirebiliriz. Bu dosyaların boyutunun 10 MB'tan küçük olması da hoşuma gitti.
Windows'ta açmak isterseniz [7-Zip](https://www.7-zip.org) yazılımını
kullanmanızı öneririm. Linux'ta çalışanlar bu dosyayı nasıl açacağını zaten
bilir 🐧.

Fakat böyle indirdirdiğimiz zaman projenin `git` geçmişi gelmiyor ve `git`
komutlarını (`git diff` gibi) kullanamıyoruz. Bu yüzden, bu şekilde indirmek yerine
`git clone` yapmanızı **hem Bootlin öneriyor hem de ben öneriyorum.**

```text
git clone https://git.buildroot.net/buildroot
```

komutu ile projeyi git geçmişi ile kendimize *clone* layabiliriz. Her sürüm
için de `git` te verilmiş bir adet *tag* bulunuyor.

```{figure} assets/02-git-clone-sort.png
:align: center

`git tag -l --sort=-v:refname` ile etiketleri sıralatabilirsiniz
```

`git clone` ile projenin tüm geçmişini çeksek bile benim diskimde 180 MB
yer kaplıyor ve bu boyut günümüz disk kapasiteleri ve diğer projeler düşünülünce
oldukça düşük kalıyor.

```text
$ du -sh buildroot
180M    buildroot
```

O yüzden `git clone` yapabiliyorsanız `tar.xz` ile hiç uğraşmayın, `git` ile
çekin gitsin.

