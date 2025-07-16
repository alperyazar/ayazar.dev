---
giscus: 59ea4e1a-fe42-4f3e-a504-52e65c6f7690
---

# Neden FuseSoC? (YARIM)

```{todo}
Yazıyı tamamla
```

FuseSoC, açık kaynak, ücretsiz, Python dilinde geliştirilmiş, Windows ve Linux
üzerinde çalıştırılabilen **FPGA projeleri** için geliştirilmiş

- 1️ **paket yöneticisi** ve
- 2️ **build system (derleme,sentezleme sistemi)** dir.

Projenin ana geliştiricisi ve yürütücüsü [Olof
Kindgren](https://www.linkedin.com/in/olofkindgren) olup, projenin geçmişi 2012
yılına kadar gitmekte ve kaynak kodu [GitHub
üzerinde](https://github.com/olofk/fusesoc) bulunmaktadır. [^1f]

Bu yazıdaki temel amacım aslında FPGA projelerimizde böyle bir aracın
kullanımının bizlere sağlayacağı avantajlardan bahsetmektir. FuseSoC aracının
kullanımından ve temel çalışma biçiminden de bahsedecek olsam da bunları
istediğiniz zaman aracın kendi dokümantasyonundan veya başka kaynaklardan daha
detaylı öğrenebilirsiniz.

**Daha önemli olanın FuseSoC ya da benzeri bir aracın çalışma ortamınıza
katabileceği değerleri kavramak olduğuna inanıyorum.**

## FPGA Projeleri ve Git

2018 yılının başlarında [ACCLOUD](http://accloud.eee.metu.edu.tr/about.html),
Accelerated Cloud, isimli bir AR-GE projesini başlattık. Yaklaşık 3 yıl süren bu
projenin birçok aşamasında baştan sona görev aldım. Bu projede yoğun bir FPGA
kullanımı vardı ve bugüne kadar çalıştığım takım yapısından farklı olarak
fiziksel olarak bir arada olmayan, aynı FPGA tasarımına farklı lokasyonlardan
katkı sunan kişilerden oluşan bir takım oluştu. Bu durum, bana o güne kadar
biraz daha deneysel takıldığım *Acaba FPGA projelerini bir yazılım projesi gibi
düzgün bir şekilde Github/Gitlab gibi platformlarda nasıl tutabiliriz?* başlıklı
araştırmalarımı ve denemelerimi hayata geçirmek için bir fırsat oluşturdu. FPGA
projelerimizi, Gitlab üzerinde tutmaya başladık. Bu çalışmada Xilinx, şimdiki
AMD, firmasının ürünleri ve araçları kullanıldı. Fakat önemli bir engel vardı.
**Xilinx gibi FPGA firmalarının araçlarının çoğu, Vivado gibi, Git ile
konfigürasyon takibi yapmaya ve CI/CD süreçleri ile otomatik derleme yapmaya çok
da uygun değildi.**

---

Kağıt üstünde baktığınız zaman, Vivado'nun 2010'lu yılların ilk versiyonlarından
itibaren Git ile uyumlu olduğunu söylediğini görebilirsiniz. **Fakat bunun ayağı
ne kadar yere basıyor?** Bugün bir yazılım projesini, bir framework ya da araç
ile oluşturduğunuz zaman size birçoğu bir `.gitignore` dosyası sunuyor örneğin.
Örneğin bilgisayarınızdaki Word dosyalarını, `.docx`, alıp bodoslama `git init`,
`git add .` ve `git commit` ile Git versiyon kontrolü altına aldığınızda Word,
Git uyumlu bir program mı oluyor?

Vivado gibi EDA araçları, sentez/derleme sırasında birçok ara dosya üretmekte.
Günün sonunda sizin amacınız belki 5-6 adet VHDL/Verilog/Block Design
dosyasından bir bitstream'e gitmek. Ama araçlar bu hedef bitstream dosyasını
üretirken onlarca, belki yüzlerce ara dosyalar üretebiliyor.

Bir projenin sağlıklı bir şekilde versiyon kontrolünün yapılabilmesi için,
Git gibi bir sistemde hangi dosyaların gerçekten bir kaynak dosya olduğu
hangilerinin ise göz ardı edilebileceğini bilmek gerekiyor. Örneğin sentez
ya da derleme sırasında üretilen ara dosyaların prensip olarak versiyon kontrol
altında olmaması gerekiyor. Olmasının getireceği en önemli problemlerden biri
`git diff` gibi bir komut ile iki *commit* arası farka baktığınız zaman aslında
anlamlı olmayan dosyaların size bir **diff noise** yaratacak olmasıdır.
Bunun dışında başka durumlar da var elbette ama yazıyı çok uzatmak istemiyorum.

```{figure} assets/fusesoc-neden-vivado.png
:align: center

Vivado'dan örnek verecek olursak ara çıktı dosyaları ve bitstream dosyası da,
şaşırtıcı gelebilir belki, versiyon kontrol altında olmamalı. Proje dosyalarınız
ile beraber projenizin ayarları ise versiyon kontrolü altında olmalı.
```

---

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD013 MD033 -->
<center>
<iframe src="https://giphy.com/embed/9itja4ux9fpFTSu7le" width="480" height="360" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/NTEtrondelag-madeleine-nte-madde-9itja4ux9fpFTSu7le">via GIPHY</a></p>

Saçma git diff çıktıları arasında önemli farkları ararken ben...
</center>
<!-- markdownlint-restore -->

---

```{important}
Bir projenin çalışma dizinin en azından düzgün bir `.gitignore` ile konfigüre
edilmeden olduğu gibi Github/Gitlab gibi platformlara *push edilmesi* o projenin
Git ile sağlıklı bir şekilde takip edildiği anlamına gelmemektedir.
```

---

Vivado'dan bir örnek ver.

## Problem: Tekrarlanabilir Çıktılar Alma

Yazılacak...

- Script ile yapmanın önemi
- hem local hem CI

### ACCBuild

Yazılacak.

## FuseSoC ile Tanışma

Yazılacak...

## FuseSoC Nasıl Çalışıyor?

Yazılacak..

## FuseSoC'u Ben Nasıl Kullanıyorum?

Yazılacak...

- pipenv örnek
- hook
- BD

## FuseSoC (ve Benzerleri) vs "Ev Yapımı" Araçlar

Yazılacak...

## Alternatifler: Hog (HDL on git) ve Diğerleri

Yazılacak...

[^1f]: <https://github.com/olofk/fusesoc/graphs/code-frequency>
