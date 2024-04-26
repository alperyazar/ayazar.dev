---
# License: CC-BY-SA-4.0.
giscus: 8f1b0c05-2e5b-450b-8d44-8ba0dd314520
og:description: "Buildroot ile ilk derlememizi yapıyoruz. Elbette tahmin ettiğim gibi ilk seferde olmuyor, uğraşıyoruz.."
---

# Buildroot ile ilk derleme!

```{note}
İçerik, bu sayfadaki yazıların üzerine anlatım yapılarak video olarak
sunulmuştur. Her ne kadar yazı ile video içerik benzese de vaktiniz var ise
videoyu izlemenizi tavsiye ederim, çünkü bazı noktalarda yazıda olmayan
yorumlar yapıyorum.
```

```{youtube} sO_Sdf09DiY
:align: center
:width: 100%
```

---

```{todo}
asciinema kayıtlarını ekle
```

Buildroot yolculuğumuza, *Buildroot Öğreniyoruz* serisinin 4. bölümü ile devam
ediyoruz. Bu bölümde, Buildroot ile ilk derlememizi yapacağız. Bir [önceki
bölümde]({% post_url 2024-02-04-buildroot-ogreniyoruz-03 %}), Buildroot ile
tanışmış, tasarım felsefesine, kimler tarafından kullanıldığına ve nasıl
kullanıldığına bakmıştık. Bu bölümde ise, bir önceki bölümde öğrendiklerimizin
adeta pratiğini yapacağız. Eğer bir önceki bölümü izlemediyseniz konu bütünlüğü
açısından önceki bölüme bakmanızı öneririm. 👇

[](tanisma.md)

## Geliştirme Ortamının Oluşturulması 💻

Önceki bölümde, Buildroot'un bir Linux dağıtımı üzerinde çalıştığından
bahsetmiştik.

**Buildroot bir Linux dağıtımı oluşturma aracı fakat kendisi de Linux üzerinde
çalışıyor.** 🐧

Günlük yaşantısında zaten Linux ile çalışan arkadaşlar, kendi işletim
sistemlerinde çalışmaya devam edebilirler. Birazdan değineceğiz ama Buildroot'un
çalışmak için talep ettiği bileşenler (paketler) oldukça genel, herhangi bir
dağıtıma bağımlılığı bulmuyor. O yüzden zaten bir Linux dağıtımı (Ubuntu, Linux
Mint, Pardus, Fedora, Arch (BTW)) üzerinde çalışıyorsanız devam edebilirsiniz.

### Windows 🪟

**Windows** üzerinde çalışan arkadaşlar için ise durum biraz farklı. Önceki
bölümde, [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) yani
Windows Subsystem for Linux ile tek bir deneme yaptığımdan ve bu denememde
`/dev/pts` kaynaklı çeşitli uyarı mesajları aldığımdan bahsetmiştim. Windows
üzerinde çalışacak arkadaşlara (ben de kullanıyorum),
[Virtualbox](https://www.virtualbox.org/) yazılımını önermiştim.

Buildroot'un, WSL üzerinde çalıştırılması ile ilgili çeşitli
[tartışmalar](https://www.reddit.com/r/embedded/comments/fgnw1u/is_buildroot_or_yocto_or_alternatives_available/)
ve
[blog](https://blog.mjjames.co.uk/2019/06/can-you-use-buildroot-with-windows.html)
yazıları internette mevcut. Son sürümlerinin WSL ile çalıştığını okusam da ben
WSL üzerinden devam etmeyeceğim. Bu seri boyunca duruma göre ya bir Linux
dağıtımı ya da Windows üzerinde Virtualbox üzerinde çalışacağım. Sizlere de
Virtualbox kullanmanızı öneririm.

```{figure} assets/ilk-derleme-reddit.png
:align: center

Bağlantısı verdiğim
[Reddit](https://www.reddit.com/r/embedded/comments/fgnw1u/is_buildroot_or_yocto_or_alternatives_available/)
tartışmasından bir yorum. Ben de aynı fikirdeyim ama size karışamam. 😝
```

### Virtualbox

```{figure} assets/ilk-derleme-virtualbox.png
:align: center

Virtualbox logosu
```

[VirtualBox](https://www.virtualbox.org/), bilgisayarınızda sanal bilgisayarlar
oluşturmanızı sağlayan bir yazılım. Windows ve Linux üzerinde çalışabiliyor.
Buildroot serisi özelinde, zaten Linux bir makineniz varsa üzerine tekrar
Virtualbox ile bir sanal makine daha oluşturmanıza gerek yok.

Önceki bölümde, Virtualbox kurulumunu göstereceğimi söylemiştim. Sonra tekrar
düşündüm de, her yerde bulabileceğiniz bu bilgiyi (içeriği kısa tutmak adına da
)benim tekrar anlatmama gerek yok. Buildroot için herhangi bir Linux dağıtımı
kullanabilirsiniz. Tipik olarak [Ubuntu 22.04
LTS](https://ubuntu.com/download/desktop) veya en güncel sürüm olan [Ubuntu
23.10](https://ubuntu.com/download/desktop) tercih edebilirsiniz. **Ben Ubuntu
22.04 kullanacağım.**

Virtualbox üzerinde Ubuntu 22.04 kurulumu ile ilgili YouTube üzerinde de birçok
[anlatım
mevcut.](https://www.youtube.com/results?search_query=virtualbox+ubuntu+22.04)
Hangi dağıtımı kurarsanız kurun, zaten süreç benzer olacaktır.

Bilgisayarınızın gücüne bağlı olarak istediğiniz kaynakları verebilirsiniz ama
ben 50-100 GB arası bir disk tahsis etmenizi öneriyorum.

Ben ise 8 çekirdek, 6 GB RAM ve 100 GB disk verdim. Virtualbox'ta `preallocate`
demediğiniz sürece disk 100 GB (ya da ne seçtiyseniz) gözükse de diskinizde
fiziksel olarak bu kadar yer kaplamayacak, kurduğunuz sanal makine diski
kullandıkça diskinizdeki sanal disk dosyası büyüyecektir. Tahmin ediyorum ki
Buildroot derlenirken birden fazla çekirdek kullanabiliyordur. Bu yüzden CPU ve
RAM'i ne kadar fazla verirseniz derleme süreleri muhtemelen kısalır.

```{figure} assets/ilk-derleme-ubuntu-kurulum.png
:align: center

Ubuntu'yu `Minimal Installation` ve güncellemeleri kurulum
sırasında yükleyecek şekilde kurdum. Siz diğer seçenekleri de tercih edebilirsiniz.
```

Bilgisayarınıza (temelde SSD vs HDD) göre değişkenlik gösterecek olmasına rağmen
kurulum yaklaşık 10-20 dakika sürmektedir. Kurduktan sonra,

```shell
sudo apt update
sudo apt upgrade
```

ile sisteminizi güncelleştirmenizi öneririm.

Sanal makine deneyiminizi iyileştirmek için (ekran çözünürlüğünü dinamik olarak
büyütme, dosya ve pano (clipboard) paylaşımı gibi) **VirtualBox Guest
Additions** kurmanızı öneriyorum. Yine YouTube üzerinden
[izleyebilirsiniz.](https://www.youtube.com/results?search_query=virtualbox+ubuntu+guest+additions)

```{attention}
Bu noktadan sonra sanal veya gerçek bir Linux makine üzerinde
çalışabildiğinizi varsayıyorum.
```

## Buildroot'un Edinilmesi ⬇️

Ben de yeni kurulmuş bir Ubuntu 22.04 üzerinden anlatımıma devam edeceğim.

```{note}
ℹ️ Yazının devamında bulacağını ekran kayıtları ve görüntüler farklı farklı
olabilir. İçeriği uygunluk durumuma göre başka bilgisayarlar üzerinde
hazırlıyorum. Sizin açınızdan değişen bir şey olmayacaktır, sadece görsel
değişiklikler (terminal teması gibi) var gibi düşünebilirsiniz.
```

```{hint}
💡 İlerleyen kısımlarda [asciinema](https://asciinema.org/) ile alınmış
kayıtlar görecekseniz. Video gibi dursa da aslında bu kayıtlar metin yani text
tabanlıdır. İzlerken durdurup, izleme ekranından metinleri seçebilir,
kopyalayabilirsiniz. Bu kayıtları alırken bir şey olmadığı zaman (kullanıcı
girdisi ya da ekrana yazı basılması) kayıt uzamasın diye `asciinema` ya
otomatik "jump cut" yaptırtıyorum. O yüzden bazı işlemler olduğundan biraz
kısa gözüküyor olabilir. Bundan bağımsız olarak bilgisayarınızın özelliklerine
göre (ve internet hızınız) sizde farklı süreler çıkabilir.
```

İlk olarak kendimize bir çalışma dizini seçelim ve altında `git clone
https://git.buildroot.net/buildroot` komutunu çalıştıralım. Eğer minimal bir
kurulum yaptıysanız `git` kurulmamış olabilir, bu durumda hata alıyorsanız
öncesinde `sudo apt install git` ile `git` kurulumu yapınız.

```{asciinema} assets/ilk-derleme-636835.cast
```

clone işleminin süresi bağlantı hızınıza ve bir miktar bilgisayarınızın gücüne
göre değişecektir. 20-25 Mbps bir internet bağlantısı ve görece zayıf bir
bilgisayarda benim işlemim yaklaşık 1 dakika sürdü. Görebileceğiniz üzere daha
sonra `git tag -l --sort=-v:refname` komutu ile git'te verilmiş etiketlere
sıralı bir şekilde bakabiliyoruz. Önceki bölümde her bir sürüm için bir etiket
var demiştik, hatırlıyor musunuz? İşte onlar bunlar.

`git clone` ile projenin tüm geçmişini çeksek bile benim diskimde 180 MB yer
kaplıyor ve bu boyut günümüz disk kapasiteleri ve diğer projeler düşünülünce
oldukça düşük kalıyor.

```text
$ du -sh buildroot
180M    buildroot
```

O yüzden `git clone` yapabiliyorsanız `tar.xz` ile hiç uğraşmayın, `git` ile
çekin gitsin. Bundan önceki bölümde de bahsetmiştik.

## Paketlerin Kurulması 📦

Buildroot'un çalışabilmesi için derleme yapacağımız sistemde olması gereken
**zorunlu** ve **opsyionel** yazılımlar vardır. [^1f]

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
vardır, isimlerini tek tek yazmıyorum burada, Buildroot'un sitesinde varlar.
[^1f]

Bootlin firması aşağıdaki komut ile Debian tabanlı sistemlerde doğru geliştirme
ortamını sağlayacağımız söylüyor:

```shell
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

```shell
sudo apt install sed make binutils gcc g++ bash patch \
gzip bzip2 perl tar cpio python3 unzip rsync wget libncurses-dev
```

```{asciinema} assets/ilk-derleme-636604.cast
```

Son olarak yukarıda belirtilen versiyon ve `file` programının
konum koşullarını sağlayıp sağlamadığımıza bakalım:

```{asciinema} assets/ilk-derleme-636605.cast
```

**Evet görüldüğü üzere artık hazırız!** 🥳

## Buildroot'u Kullanmaya Başlama 🚀

Serinin önceki bölümünde, Buildroot'un kullandığı `make`, `Kconfig`, `Kbuild` gibi
araçlardan bahsetmiştim. Bu konulara tekrar girmeyeceğim.

Konfigürasyon tarafında Buildroot tarafından `menuconfig`, `nconfig`, `xconfig`,
`gconfig` araçları destekliyor. Bu 4 aracın da ortak özelliği bizlerin görsel
yani kolay ve doğru şekilde bir derleme konfigürasyonu oluşturmamızı sağlamak.
İşte Buildroot'u bu araçlar ile konfigüre edeceğiz. Bu araçlardan `menuconfig`
ve `nconfig` terminal tabanlı araçlar. Yani konsol içerisinde çalışıyorlar.
Bunlara **Text-based User Interface (TUI)** tarzı araçlar diyebiliriz. [^5f]
`xconfig` QT kütüphanesi, `gconfig` ise GTK kütüphanesini kullanan **Graphical
User Interface (GUI)** araçlardır. [^6f] Terminal tabanlı olması sebebiyle
pratikliğinden, GUI kütüphaneleri gerektirmemesinden (`libncurses-dev`
yeterlidir) dolayı SSH gibi bağlantılar üzerinden de sorunsuz çalışabilmesinden
(uzak bir geliştirme bilgisayarına SSH ile bağlısınız ve Buildroot orada
çalışıyor diyelim) dolayı `menuconfig` ve `nconfig` araçları gözlemlerime göre
daha sık kullanılmaktadır.

```{asciinema} assets/ilk-derleme-636607.cast
```

Burada ilk olarak `git checkout -b bootlin 2022.02` komutu ile `2022.02`
versiyonundan (tag) `bootlin` isimli bir branch oluşturuyoruz. `make help` ile
Buildroot'un desteklediği işlemlere bakıyoruz. `make clean` eğer varsa kalmış
ara dosyaların temizlenmesini sağlıyor. Biz zaten ilk defa çalışmaya
başladığımız için bu işlem aslında gerekli değil bu aşamada. `make menuconfig`
ile, `menuconfig` aracını çalıştırıp Buildroot ile beraber gelen `Kconfig`
dosyalarına göre konfigürasyonu görüyoruz. Burada ok, `Enter`, `ESC` ve `TAB`
tuşları ile gezinebiliyoruz. Benzer şekilde `make nconfig` ile `nconfig` aracını
gösteriyorum. Dikkat ederseniz ikinci `make menuconfig` komutu hemen çalışıyor
ama `make clean` dersek, `make menuconfig` tarafından kullanılan dosyalar da
silineceği için tekrar `make menuconfig` dediğim zaman menünün açılması zaman
alıyor.

Şimdi gelin, `gconfig` ve `xconfig` araçlarına bakalım.

```{asciinema} assets/ilk-derleme-636726.cast
```

Kayıttan da görebileceğiniz üzere `gconfig` ve `xconfig` araçlarını hemen
kullanamadık. Önceki bölümde de belirttiğim gibi, `gconfig` aracı GTK kütüphanelerine,
`xconfig` aracı ise QT kütüphanelerine bağımlı.

`gconfig` i çalıştırabilmek için:

```shell
sudo apt install libgtk2.0-dev libglib2.0-dev libglade2-dev
```

`xconfig` için:

```shell
sudo apt install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools
```

paketlerini kurmak gerekti. Bu kurulumlardan sonra `make gconfig` ve
`make xconfig` komutlarını çalıştırabildim. `menuconfig` ve `nconfig` komutlarının
aksine bu iki konfigürasyon aracının görüntülerini yukarıdaki terminal
kaydında göremiyorsunuz çünkü bu araçlar ayrı bir pencerede açılıyor. Belirttiğim
gibi, GUI araçları. Örnek olması açısından, birer adet görüntüyü ekliyorum.

**İlerleyen bölümlerde sadece `menuconfig` veya `nconfig` kullanacağız.**

```{figure} assets/ilk-derleme-gconfig.png
:align: center

gconfig
```

```{figure} assets/ilk-derleme-xconfig.png
:align: center

xconfig
```

## Derleyelim 🛠️

Geliştirme ortamımız hazır, ilk derlememizi yapalım.

Burada Bootlin'in, Beaglebone için hazırladığı [lab
materyallerini](https://bootlin.com/doc/training/buildroot/buildroot-labs.pdf)
takip edeceğim (Sayfa 5, `Configuring Buildroot` kısmı). Amacımız her
aşamayı anlamak değil, kurduğumuz araçları test etmek olacak. Aşamaları tek tek
buraya yazmıyorum, Bootlin'in dokümanlarından bakarak yapacağım. Aşağıdaki
kayıta ve lab dokümanlarına bakarak siz de kendinizde deneyebilirsiniz.

Bakalım karta yüklenmeye hazır bir şeyler çıkartabilecek miyiz?

```{asciinema} assets/ilk-derleme-636728.cast
```

Belirttiğim gibi şimdilik sadece "Derleyebiliyor muyuz?" diye baktığımız için
seçenekleri Bootlin'in tariflediği gibi yapıp, geçiyorum. İlerleyen bölümlerde
detaylara gireceğiz (muhtemelen).

### OpenSSL? 🔒

Burada bana ilginç olan, kernel seçeneklerinde OpenSSL ile ilgili bir ayar
yapmamız oldu. İlk başta "Acaba Secure Boot gibi bir mekanizma için bir şeylerin
imzalanması mı gerekiyor?" diye düşündüm, sonra bu düşünceden uzaklaştım.

Bootlin'in dokümanlarında şöyle bir ifade geçiyor:

> The kernel configuration for this platform requires having OpenSSL available on
> the host machine. To avoid depending on the OpenSSL development files installed
> by your host machine Linux distribution, Buildroot can build its own version:
> just enable the Needs host OpenSSL option.

Bunun tam neden olduğunu henüz anlayamasam da platformun kablosuz özelliğinden
dolayı olabileceğini düşünüyorum [^7f]. Karşılaştırma yapmak adına, Bootlin'in
eğitim için önerdiği ikinci platformun, [STM32MP1 Discovery Kit
1](https://www.st.com/en/evaluation-tools/stm32mp157a-dk1.html), [lab
dokümanlarına](https://bootlin.com/doc/training/buildroot-stm32/buildroot-stm32-labs.pdf)
da baktım. Burada da aynı ifade geçiyor fakat bu platfomun da Bluetooth ve Wi-Fi
özellikleri var. O yüzden hala bununla ilgili olabileceğini düşünüyorum, ilerleyen
zamanlarda burayı kurcalarız.

---

Bootlin'in dokümanlarında önerdiği şekilde,

```shell
make 2>&1 | tee build.log
```

derlemeyi başlatalım. Burada sadece `make` deseniz de yeterli. Önceki bölümde
anlattığım gibi burada `tee` komutu, `make` in oluşturduğu yazıların, yani logların,
hem ekrana gösterilmesini hem de `build.log` isimli bir dosyaya kaydedilmesini
sağlıyor. `2>&1` ifadesi ise `make` in `stderr` çıkışının da `stdout` çıkışına
yönlendirilmesini sağlıyor, ama şu aşamada konumuzun dışında bu kavram.

İlk derleme girişimimizin kaydına bir bakalım:

```{asciinema} assets/ilk-derleme-636729.cast
```

Loglar akarken şunlar dikkatimi çekti:

- Burada Buildroot'un arka planda birçok işlem yaptığını görebiliyoruz. İşte
  böyle bir araç kullanmasaydık, her şeyi elle yapsaydık, buralarda muhtemelen
  hatalar yapacaktık ve saatler sürecekti. Bu kavrama serinin
  [ikinci bölümünde]({% post_url 2024-01-20-buildroot-ogreniyoruz-02 %})
  detaylıca değinmiştik.
- Beklendiği üzere internetten bir şeyler çekiyor. İleriye soru: Offline ortamda
  derleme yapabilir miyiz eğer geliştirme ortamımızın internet bağlantısı yoksa?
- Toolchain de (derleyici vs) internetten hazır olarak çekildi, bunun ayarını
  yapmıştık.
- Busybox çekildi.

**Fakat patladık!** 🤦

İlk girişimimiz hata ile sonuçlandı, ben dedim demek istemiyorum ama bir
önceki bölümde muhtemelen problemsiz olmayacak demiştim. Dikkat ederseniz
`openssl/evp.h` dosyasının bulunamadığı bize söyleniyor. OpenSSL dedim dedim,
başımıza dert açtı. 😅

Normalde bu tarz header dosyaları, ilgili bileşenin "geliştirme paketleri"
kurulu değilse sistemde bulunmuyor. Fakat Bootlin'in dokümanlarında şöyle
bir açıklama vardı, yukarıda vermiştim:

> ...
> To avoid depending on the OpenSSL development files installed
> by your host machine Linux distribution, Buildroot can build its own version:
> ...

Benim beklentim, benim sistemimde OpenSSL'in geliştirme dosyaları olmasa da
bir problem yaşamamamdı. Yanlış anlamış olabilirim, ama `Needs host OpenSSL`
seçeneğini açtığımız için benim sistemimde OpenSSL'in geliştirme dosyaları
olmasa da Buildroot'un temin etmesini bekliyordum.

İnternette de tahmin ettiğim şekilde bir çözüm sunulmuş [^8f]: Derleme yaptığımız
sisteme OpenSSL'in geliştirme paketini kuralım ve derlemeyi tekrar deneyelim.

```{asciinema} assets/ilk-derleme-636770.cast
```

Bu sayede hatayı düzeltmiş olduk. Tekrar `make` dediğim zaman derleme işlemi
kaldığı yerden devam etti. **Bu da `make` gibi sistemlerin bizlere sunduğu en
büyük avantajlardan biri:** Sadece değişen veya yarım kalan kısımlar derleniyor,
bu da büyük bir zaman avantajı oluşturuyor. Gerçi bizim durumda kernel derlendiği
için zaman avantajını görememiş gibi olduk ama tüm işler bittikten sonra tekrar
`make` derseniz aslında hiçbir işlem yapılmadığını görebilirsiniz. Çünkü hiç
bir ayar değiştirmedik, o yüzden var olan bir çıktıyı tekrar oluşturmaya gerek
yok diye düşünüyor `make`.

Bu sırada bir hatamı daha düzeltmiş oldum. Bootlin dokümanlarına göre, Kernel
ayarlarına `defconfig` olarak `omap2plus_defconfig` yazmamız gerekiyordu, ben de
o şekilde yazdım. Fakat loglardan anladığım kadarıyla "birileri" bunun sonuna
otomatik olarak `_defconfig` ekliyor ve `omap2plus_defconfig_defconfig` oluyor,
bu da hataya sebep oluyor. O yüzden tekrar ayarlara girip, bu sefer
değişiklik olsun diye `menu nconfig` kullandım, `omap2plus_defconfig` yerine
`omap2plus` yazdım ve devam edebildim.

> Yukarıdaki paragraftaki hatamı videoyu çekerken fark ettim. Bootlin dokümanları
> aslında doğruymuş, ben yanlış yazmışım en başta.

Gözlemler:

- Kernel kaynak kodudan baştan derleniyor ve derleme sırasında çoklu çekirdek
  kullanımı oluyor. Çok fazla RAM tüketimi yok, fakat çekirdek sayınız ne kadar
  çok olursa belli oranda derleme süreniz azalacaktır.
- Her ne kadar bir önceki aşamada OpenSSL ile ilgili bir şeyler kurmamız gerekse
  de yine OpenSSL ile ilgili bir şeylerin indirildiğini gördüm. Yani seçtiğimiz
  `Needs host OpenSSL` ayarı bir etki gösteriyor bence ama niye header dosyalarını
  kurmamız gerekti tam çözemedim. Onu niye temin etmiyor?
- Loglar arasında `TI` ve `Wireless` kelimeleri geçiyor. BeagleBone Black, bir
  Texas Instruments üretimi SoC barındırdığı ve Wi-Fi bağlantısı olduğunu düşününce
  bunlar sürpriz değil.

Derleme sonrasında çıktılar `output/images` altında oluşuyor:

- `am335x-boneblack-wireless.dtb`: Bizim devicetree'miz.
- `MLO`: U-Boot SPL (Secondary Program Loader)'in adı, config ile biz seçmiştik.
- `rootfs.tar`: RootFS dosya sistemimiz. Yani oluşturduğumuz Linux dağıtımı asılnda
  Karta koyacağımız Linux'ta buradaki dosyalar olacak.
- `u-boot.bin`: U-Boot yani bootloader
- `zImage`: Sıkıştırılmış Linux yani kernel dosyası. Kart ayağa kalkarken
  Bootloader tarafından açılıp, RAM'e konulacak.

Hatırlarsanız önceki bölümde Buildroot'un derleme süresi ve RootFS dosya boyutu
açısından iddalı olduğunu görmüştük. 2 MB'a kadar düşebildiğini söylüyordu, biz
şu an 31 MB'tayız (`rootfs.tar`). Belki ilerleyen bölümlerde bunu küçültmeye
yönelik lablarımız da olur, bilemiyorum. Derleme süresi olarak baktığımızda da
RootFS kısmının (bu durumda Busybox) görece hızlı olduğunu düşünüyorum. En
çok süreyi kernelin derlenmesi aldı.

## Kapanış

Bir sonraki bölümde oluşturduğumuz imajı (RootFS + Bootloader + Kernel) karta
atıp, deneyeceğiz. Fakat şöyle bir sorun var, ilk bölümde bahsetmiştim:

**Bende BeagleBone Black yok, diğer STM32 kiti de yok!**

BeagleBone Black temin etmeye çalıştım ama bulamadım. Bende ilk BeagleBone var,
beyaz olan ve birkaç farklı model RaspberryPi var. Artık bir sonraki bölüme
kadar birini seçip devam edeceğim. Bootlin'in eğitiminde olmayan bir kartı
kullanmak daha da öğretici olabilir belki 😇.

Kendinize iyi bakın 🤒 🙋.

[^1f]: <https://buildroot.org/downloads/manual/manual.html#requirement>
[^4f]: <https://www.python.org/doc/sunset-python-2/>
[^5f]: <https://en.wikipedia.org/wiki/Text-based_user_interface>
[^6f]: <https://en.wikipedia.org/wiki/Graphical_user_interface>
[^7f]: <https://buildroot.uclibc.narkive.com/BX6jn0vO/patch-04-23-configs-qemu-x86-64-defconfig-remove-kernel-options-that-need-openssl-libelf#post9>
[^8f]: <https://elinux.org/Building_BBB_Kernel>
