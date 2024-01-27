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

`git clone` ile projenin çekilip, `git tag` ile sürümlerin bakılması şu şekilde
olmaktadır:

<!-- markdownlint-disable-next-line -->
<script async id="asciicast-633812" src="https://asciinema.org/a/633812.js"></script>

İnternet hızınıza ve bir miktar bilgisayarınızın gücüne (git objelerinin açılması)
bağlı olsa da tüm clone işlemi bende 1 dakika 16 saniye sürmüştür.

## Geliştirme Ortamının Oluşturulması

**Buildroot ile çalışmak için bir Linux dağıtımında olmanız gekmektedir.**

Buildroot, dağıtıma özel bir araç kullanmadığı ve genel Linux araçlarını kullandığı
için hangi dağıtımı tercih ettiğimiz önemli değil [^1f]. Ben muhtemelen bu seri
boyunca iki farklı bilgisayar kullanacağım, birinde **Ubuntu 22.04** diğerinde
ise **Linux Mint** kurulu (sürümünü şu an bilmiyorum, en güncel diye düşünelim,
bakabilince yazarım). Herhangi bir dağıtımında problem yaşayacağınızı zannetmiyorum.

**Windows kullanıcıları** ise dilerlerse bilgisayarlarında Virtualbox gibi
araçlarla sanal Linux makine çalıştırabilirler. **Windows Subsytem for Linux
(WSL)** ile kısa bir deneme yaptığımda Buildroot'un `make` dediği zaman çeşitli
uyarlılar verdiğini (`pts` vs gibi konularda) gördüm. Açıkçası WSL ile
çalışabilmesini beklerim, son zamanlarda oluyor gibi duruyor ama ben Linux
üzerinden devam edeceğim [^2f], [^3f]. **Sizlere de imkanınız varsa sanal
makinede Linux ya da doğrudan Linux üzerinde çalışmanızı öneririm.**

### Paketlerin Kurulması

Buildroot'un çalışabilmesi için derleme yapacağımız sistemde olması gereken
**zorunlu** ve **opsyionel** yazılımlar vardır [^1f].

Zorunlu paketler:

`which sed make bintuilt build-essential diffutils gcc g++ bash patch gzip bzip2
perl tar cpio unzip rsync file bc findutils wget`

araçlardır. Bunlardan

- `make` versiyonu 3.81'den büyük
- `build-essential` sadece Debian tabanlı sistemlerde (Ubuntu ve Linux Mint gibi)
- `gcc` versiyonu 4.8'den büyük
- `g++` versiyonu 4.8'den büyük
- `perl` versiyonu 5.8.7'den büyük
- `file` ise `/usr/bin/file` da olmalıdır (buna neden gerek duyuyor anlamadım).

Yine bunlar dışında çeşitli yardımcı araçların çalışması için önerilen araçlar
vardır, isimlerini tek tek yazmıyorum burada, Buildroot'un sitesinde varlar
[^1f].

Bootlin firması aşağıdaki komut ile Debian tabanlı sistemlerde doğru geliştirme
ortamını sağlayacağımız söylüyor:

```console
sudo apt install sed make binutils gcc g++ bash patch \
gzip bzip2 perl tar cpio python unzip rsync wget libncurses-dev
```

Burada şöyle bir problem var. Ubuntu'da `python` paketini kurmak istediğiniz
zaman bu başarısız oluyor, ya `python2` ya da `python3` seçmek gerekiyor.
Buildroot'un sayfasında opsiyonel olarak belirtilen Python yazılımının hangi
versiyonunun istendiği yazmıyor. Ama tahmin ediyorum ki Python 2 değildir çünkü
Python 2'ye, 1 Ocak 2020'de "çivi çakılmama" kararı alındı [^4f] ve yazılımlar
zaten çok daha önceden Python 2'den Python 3'e geçmeye başlamıştı. Bu yüzden
Buildroot'un Python 2'ye bağımlı bir bileşen içerdiğini düşünmüyorum. O yüzden
üstteki komuttaki `python` paketini `python3` paketi ile değiştirince bende
eksik bir paket olmadığını görüyorum.

`python3` düzeltilmiş komut:

```console
sudo apt install sed make binutils gcc g++ bash patch \
gzip bzip2 perl tar cpio python3 unzip rsync wget libncurses-dev
```

<!-- markdownlint-disable-next-line -->
<script async id="asciicast-633819" src="https://asciinema.org/a/633819.js"></script>

Son olarak yukarıda belirtilen versiyon ve `file` programının
konum koşullarını sağlayıp sağlamadığımıza bakalım:

<!-- markdownlint-disable-next-line -->
<script async id="asciicast-633822" src="https://asciinema.org/a/633822.js"></script>

Evet görüldüğü üzere artık hazırız!

## Buildroot'u Kullanmaya Başlama

Buildroot'un yaptığımız ayarları tutmak ve bunlara uygun derlemeler yapmak için
kullandığı temel bir iki araç var:

- `make`. İleride detaylı bakacağız ama çok eskiden beri (70'ler) olan bir yazılım.
  Temelde derleyiciler ya da çeşitli programları bir hedef dosyayı oluşturmak
  için doğru sırada, gerektiği kadar ve doğru şekilde çağırmaya yarıyor.
- Çeşitli scriptler. Birkaç yardımcı script (BASH scripti ?) işleri kolaylaştırmak
  için kullanılıyor
- `Kconfig`. Linux, U-boot, Busybox gibi çeşitli projeler tarafından kullanılmaktdır.
  İlk olarak `Kbuild` ile beraber Linux projesi için geliştirilmiş olup temelde
  metin tabanlı olan `Kconfig` dosyaları ile Buildroot'un birçok ayarını tutmaya
  yarar. `Kconfig` dosyalarının kendine özgü fakat basit bir sentaksı vardır.
  Buildroot'un birçok bileşen arasındaki bağımlılıkları yönetmesine yardımcı olur.
  İleride tekrar değineceğiz, o yüzden biraz yüzeysel geçiyorum şimdilik.
- Konfigurasyon Araçları. `Kconfig` dosyalarının bir metin görüntüleyici ile
  okunup, ondan elle düzgün konfigürasyonlar üretmek pek pratik değildir.
  Onun yerine elimizde bu konfigürasyon dosyalarındaki ayarlar ve seçenkleri
  okuyup, görsel ve doğru bir şekilde (bağımlılıklara dikkat ederek) ayar yapma
  ve nihai konfigürasyon ayarlarını (dosyalarını) üretmeyi sağlayan çeşitli
  araçlar vardı. Buildroot tarafından `menuconfig`, `nconfig`, `xconfig`, `gconfig`
  araçları destekliyor. Bu 4 aracın da ortak özelliği bizlerin görsel yani kolay
  ve doğru şekilde bir derleme konfigürasyonu oluşturmamızı sağlamak. İşte
  Buildroot'u bu araçlar ile konfigüre edeceğiz. Bu araçlardan `menuconfig` ve
  `nconfig` terminal tabanlı araçlar. Yani konsol içerisinde çalışıyorlar.
  Bunlara **Text-based User Interface (TUI)** tarzı araçlar diyebiliriz [^5f].
  `xconfig` QT kütüphanesi, `gconfig` ise GTK kütüphanesini kullanan
  **Graphical User Interface (GUI)** araçlardır [^6f]. Terminal tabanlı olması
  sebebiyle pratikliğinden, GUI kütüphaneleri gerektirmemesinden
  (`libncurses-dev` yeterlidir) dolayı SSH gibi bağlantılar üzerinden de
  sorunsuz çalışabilmesinden (uzak bir geliştirme bilgisayarına SSH ile
  bağlısınız ve Buildroot orada çalışıyor diyelim) dolayı `menuconfig` ve
  `nconfig` araçları gözlemlerime göre daha sık kullanılmaktadır.

Şimdi Buildroot'u biraz kurcalayalım, şu konfigürasyon araçlarına bakalım:

<!-- markdownlint-disable-next-line -->
<script async id="asciicast-633824" src="https://asciinema.org/a/633824.js"></script>

Burada ilk olarak `git checkout -b bootlin 2022.02` komutu ile `2022.02`
versiyonuna gidiyor ve bu geçtiğimiz noktada bir de `bootlin` isimli bir imaj
oluşturuyoruz. `make help` ile Buildroot'un desteklediği işlemlere
bakıyoruz. `make clean` eğer varsa kalmış ara dosyaların temizlenmesini sağlıyor.
Biz zaten ilk defa çalışmaya başladığımız için bu işlem aslında gerekli değil
bu aşamada. `make menuconfig` ile, `menuconfig` aracını çalıştırıp Buildroot
ile beraber gelen `Kconfig` dosyalarına göre konfigürasyonu görüyoruz. Burada
ok, `Enter`, `ESC` ve `TAB` tuşları ile gezinebiliyoruz. Benzer şekilde
`make nconfig` ile `nconfig` aracını gösteriyorum. Dikkat ederseniz ikinci
`make menuconfig` komutu hemen çalışıyor ama `make clean` dersek, `make menuconfig`
tarafından kullanılan dosyalar da silineceği için tekrar `make menuconfig` dediğim
zaman menünün açılması zaman alıyor.

**BURADA KALDIM**

```{figure} assets/02-xconfig.png
:align: center

xconfig
```

```{figure} assets/02-gconfig.png
:align: center

gconfig
```

<!-- markdownlint-disable-next-line -->
<script async id="asciicast-633840" src="https://asciinema.org/a/633840.js"></script>

```console
sudo apt install libgtk2.0-dev libglib2.0-dev libglade2-dev

sudo apt install libqt5-dev # çalışmadı
sudo apt install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools
```

```{disqus}
:disqus_identifier: 0e601187-a184-4ea5-9f8a-373c5dfa53e8
```

[^1f]: <https://buildroot.org/downloads/manual/manual.html#requirement>
[^2f]: <https://blog.mjjames.co.uk/2019/06/can-you-use-buildroot-with-windows.html>
[^3f]: <https://www.reddit.com/r/embedded/comments/fgnw1u/is_buildroot_or_yocto_or_alternatives_available/>
[^4f]: <https://www.python.org/doc/sunset-python-2/>
[^5f]: <https://en.wikipedia.org/wiki/Text-based_user_interface>
[^6f]: <https://en.wikipedia.org/wiki/Graphical_user_interface>
