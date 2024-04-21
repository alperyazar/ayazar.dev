---
og:description: "Sumatra PDF, Windows için tasarlanmış, hafif, hızlı bir PDF okuyucusu."
og:image: assets/social/blog/21/sumatra.png
giscus: 280d2a03-2f2b-4f6c-8e96-224f342340a6
---

# Sumatra PDF

```{figure} /extra/assets/social/blog/21/sumatra.png
:align: center
:figclass: thmbnl
```

---

## Giriş

[Sumatra PDF](http://sumatrapdf.org/), Windows için geliştirilmiş küçük
boyutlu, hafif ve hızlı açılan bir PDF görüntüleme yazılımı. Sanılabileceğinin
aksine yazılım, adını Endonezya'nın Sumatra Adası'ndan almıyor [^1f]. GPLv3 ile
lisanslanmış olan yazılım,
[Github](https://github.com/sumatrapdfreader/sumatrapdf) üzerinden açık kaynak
ve ücretsiz olarak sunuluyor.

Bu yazılımı,
Windows üzerinde çalışırken günlük yaşantımda sıklıkla kullanıyorum.
Bu yazıda, yazılımı tercih etme sebeplerimi ve görüşlerimi sizlerle paylaşıyorum.

## Fare Desteği

Sumatra PDF'in en çok sevdiğim özelliği klavyeye hiç dokunmadan sadece fareyi
kullanarak kolay bir gezinme sağlaması. **Sağ tık + tekerlek hareketleri** ile
dokümanda yaklaşıp uzaklaşabilmek (zoom in/out) mümkün. Farenin tekerleğini
kullanırken bir yandan klavyede `CTRL` tuşuna basmaya ya da diğer PDF okuyucu
yazılımlarda da bulunan yaklaşma/uzaklaşma (`+` ve `-`) tuşlarına basmaya
gerek olmuyor.

**Sağ tık + fare hareketleri** ile dokümanı yukarı/aşağı veya sağa/sola kaydırmak
mümkün oluyor (*pan* hareketi). Bunlar sayesinde tek elimle dokümanda gezinirken
boştaki diğer elimle çaydır, kahvedir içebiliyorum.

## LaTeX ve SyncTeX Kolaylığı

[Sumatra PDF](http://sumatrapdf.org/), görüntülenen doküman açık iken o
dokümanın başka bir yazılım tarafından değiştirilmesine izin veriyor. Adobe
Acrobat Reader DC gibi diğer popüler yazılımlarda ise bunun mümkün olmadığını
gözlemliyorum. Bu, özellikle LaTeX gibi bir araçla bir formattan, kaynak
kodundan dönüşüm yaparak yani bir şeyleri derleyerek PDF üretiyorsanız faydalı
oluyor. Diğer yazılımlarda açtığınız dokümanın bir başka yazılım tarafından
değiştirilmesini sağlamak için PDF'i kapatmanız, değiştikten sonra ise tekrar
açmanız gerekiyor. Eğer LaTeX ile bir şeyler yazdıysanız bunu bir saatte
neredeyse 50-100 kere yapabileceğinizi hissetmişsinizdir. İşte bu gibi
durumlarda Sumatra PDF bir kurtarıcı oluyor.

LaTeX konusundan bahsetmişken Sumatra PDF'in
[SyncTeX](https://tex.stackexchange.com/questions/118489/what-exactly-is-synctex)
desteklediğini de belirteyim. Bu sayede LaTeX editörünüz ile Sumatra PDF arasında
çift taraflı geçişler yapabiliyorsunuz. Yani kaynak kodunda ilgilendiğiniz yerin
çıktısının nasıl olduğunu Sumatra PDF üzerinden görebiliyor ya da PDF'te gördüğünüz
bir yerin kaynak koduna hızlıca gidebiliyorsunuz. Bunun nasıl yapılacağı ile
ilgili
[yazımızı okuyabilirsiniz.]({% post_url
2021-10-30-sumatrapdf-texstudio-synctex-search-link %})

## Küçük Boyut, Hız, Taşınabilir Sürüm

[Sumatra PDF](http://sumatrapdf.org/) resmi olarak 32/64-bit bilgisayarlar için
hem kurulabilir hem de taşınabilir sürümler sunuyor. Bu dosyalar ise sadece 6-7
MByte yer kaplıyorlar. Kurulduktan sonra da yaklaşık 22 MByte yer harcıyor.
Bu arada kurulum ekranı 90'lardan kalma gibi, çok eski bir görünümü var ama
neyse ki bir kez görüyorsunuz ve kurulum da güncel bir bilgisayarda 5 saniyeyi
geçmiyor diyebilirim.

Günlük kullanımda hafif bir okuyucu olmasından dolayı hızlı açıldığını hissediyorum.
Daha nicel bir veri sunmak için 88 sayfalık, yazı ağırlıklı bir PDF dokümanı
bilgisayarımda bulunan 3 farklı yazılımda açtığımda aşağıdaki gibi ölçümler aldım.

| Yazılım | Açılış Süresi (sn) |
|---------|--------------------|
| [Sumatra PDF](http://sumatrapdf.org/) | 0.4 |
| [PDF-XChange Editor](https://www.tracker-software.com/product/pdf-xchange-editor) | 0.6 |
| [Adobe Acrobat Reader DC](https://www.adobe.com/tr/acrobat/pdf-reader.html) | 2.2 |

Bu denemelere Foxit PDF Reader'i dahil edemedim çünkü
**kendisini indirmeme antivirüs yazılımım izin vermedi.**

Yazılımlar çalışırken de en düşük miktarda hafıza kullanan yazılımın Sumatra PDF
olduğunu söyleyebilirim.

## Kişiselleştirme

[Sumatra PDF](http://sumatrapdf.org/)'i kişiselleştirmek kolay ve taşınabilir.
Çünkü `Settings → Advanced Options` denildiğinde yazılımın tüm ayarlarını
görüp değiştirebiliyoruz. Ayarlar metin formatında olduğu için bu ayarları
kopyalayarak çalıştığınız diğer bilgisayarlara taşımak ya da format öncesi
kaydetmek kolay oluyor.

Buradan değiştirebileceğiniz kullanışlı ayarlardan birkaçı metin ve arka plan rengi
olabilir. Özellikle gece çalışıyorsanız renklerle oynamak isteyebilirsiniz.

Yazılımla ilk defa tanışıyorsanız
ilk olarak öncellikle `Settings → Options` kısmından `Advanced` başlığı altındaki
`Use tabs` seçeneği seçiliyken ve değilken yazılımı denemenizi öneririm. Eğer
sekmeli kullanırsanız birden fazla PDF dokümanı açtığınızda tek bir programın
içerisinde tüm PDF'leri sekmeler halinde görüyorsunuz. Ben ise diğerini tercih
ediyorum çünkü sekmesiz kullanımda açık olan her bir doküman için Windows görev
çubuğunda ayrı bir ikon oluşuyor ve bunlara hızlıca ön izleme yapmayı tercih ediyorum
fare imlecini üzerlerinde gezdirerek. Kullanan arkadaşlarımdan sekmeliyi daha çok
sevenler çoğunlukta, tercihi deneyerek siz yapın.

## Eksiler

Yazılımı PDF **okuyucusu** olarak düşünürseniz ben bir eksiklik hissetmiyorum ama
PDF üzerine yorumlar eklemek için kullanacaksanız bu konuda çok bir seçenek
sunmadığını belirteyim. Yapmak mümkün ama beklentiniz düşük olmalı. Bu konuda,
[PDF-XChange Editor](https://www.tracker-software.com/product/pdf-xchange-editor),
[Adobe Acrobat Reader DC](https://www.adobe.com/tr/acrobat/pdf-reader.html) gibi
alternatifleri kullanmanızı öneririm.

Diğer bir konu ise, her ne kadar çözümsüz olmasa da, Linux için doğal bir
desteğinin olmaması. Ben denemedim ama sanırım [Wine](https://www.winehq.org/)
ile sorunsuz da çalışıyor. Linux dağıtımlarda aslında Sumatra PDF'in tüm
özelliklerini içermese de kullandığım masaüstü ortamının okuyucuları (GNOME:
[Evince](https://wiki.gnome.org/Apps/Evince), KDE:
[Okular](https://okular.kde.org/tr/), [Xpdf](https://www.xpdfreader.com/) gibi)
çoğu zaman işimi görüyor.

```{youtube} ysju2yE5l5Y
:align: center
:width: 100%
```

[^1f]: <https://web.archive.org/web/20120303132633/http://forums.fofou.org/sumatrapdf/topic?id=3392&comments=2>

*İlk yayın: 2021-10-29*

