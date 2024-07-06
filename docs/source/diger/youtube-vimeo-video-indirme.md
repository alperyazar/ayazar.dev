# YouTube, Vimeo (Şifreli Videolar Dahil) Video İndirme

Çeşitli sebeplerden dolayı YouTube, Vimeo gibi platformlardaki videoları
indirmek ve saklamak isteyebilirsiniz. İndireceğiniz içeriğe sahip olmanız doğru
mu ve etik mi, buna siz karar vermelisiniz. Ben bu yazıda işin teknik kısmından
bahsedeceğim. Bahsedeceğim yöntemleri hem **Windows** hem de **Linux** üzerinde
kullanabilirsiniz.

## yt-dlp ve FFmpeg

Kullanımını ilk önereceğim yöntem [yt-dlp](https://github.com/yt-dlp/yt-dlp)
isimli komut satırı temelli aracın kullanımı olacaktır. yt-dlp, Python dilinde
yazılan, alanında çok yetenekli bir araç. Kendisi daha eski bir proje olan
youtube-dl isimli araçtan çatallanarak (fork) oluşturulmuş bir proje. youtube-dl,
zamanında DMCA yani Digital Millennium Copyright Act kapsamında bir ara Github'tan
kaldırılmış sonra geri gelmişti. [^1f] [^2f] [^3f]

Windows kullanıcıları yt-dlp'yi [kendi sitesinden](https://github.com/yt-dlp/yt-dlp/releases)
`yt-dlp.exe` olarak indirebilirler. Alternatif olarak Python pip ile `pip install`
diyerek de kurabilirsiniz: [yt-dlp, pypi.org](https://pypi.org/project/yt-dlp/)
Ben Github üzerinden `.exe` yi indirip kullanmayı tercih ediyorum.

Linux kullanıcıları da benzer şekilde Github üzerinden doğrudan binary indirebilir
ya da pip ile kurabilir.

yt-dlp, gerçekten çok yetenekli bir program. Neredeyse var olan tüm stream
platformlarını destekliyor ve birçok indirme seçeneği sunuyor. Örneğin beğendiğiniz
bir YouTube playlisti tek seferde indirebiliyorsunuz ya da bir videonun sadece
sesini indirip, `mp3` olarak kaydedebiliyorsunuz. yt-dlp'nin yetenekleri bu
yazının konusunun dışında olduğu için araştırma işini size bırakıyorum.

Günümüzdeki birçok stream platformu, video ve ses dosyalarını ayrı ayrı sunuyor.
Videoya göre değişse de yt-dlp de genelde bu şekilde indiriyor, yani bir ses
dosyası bir de video dosyası indiriyor. Fakat bunların birleştirilmesi gerekiyor.
İşte burada FFmpeg devreye giriyor. FFmpeg hem bu işte hem de bir dönüşüm istendiyse,
örneğin mp3'e dönüştürme gibi, yt-dlp tarafından kullanılıyor.
**yt-dlp indirildiği zaman FFmpeg gelmiyor, ayrıca temin etmemiz lazım.**

### FFmpeg

Linux kullanıcıları paket yöneticilerini, apt vs, kullanarak FFmpeg'i
kurabilirler.

Windows kullanıcıları, `ffmpeg.exe` yi internetten indirebilirler yani Windows
için derlenmiş sürümler de bulunuyor. Resmi FFmpeg sitesine Windows için iki
farklı "kişi" tarafından yapılmış derlemeler bulunuyor. [^4f] Ben
[buradan](https://github.com/BtbN/FFmpeg-Builds/releases) indirmeyi tercih
ediyorum. ` ffmpeg-master-latest-win64-gpl.zip ` isimli dosyayı indirin.
İçerisindeki `bin/ffmpeg.exe` dosyasını alın. Ben şu şekilde kullanıyorum:
`yt-dlp.exe` ve `ffmpeg.exe` dosyalarını bir klasör altına koyuyorum, yan yana.
Bir diğer alternatif çözüm de `ffmpeg.exe` nin bulunduğu yerin PATH'e eklenmesi
ama bana ilki daha pratik geliyor. Günün sonunda `yt-dlp`, `ffmpeg` i
çağırabiliyor olmalı.

## YouTube Video İndirme

`yt-dlp` yi ve `ffmpeg` i bir şekilde kurduk, şimdi test amaçlı bir video
indirelim. Ben bundan sonraki denemeleri Windows üzerinde yapacağım. Linux
üzerinde çalışan arkadaşlar komutları kendilerine göre modifiye edebilirler,
`\`, `/` konuları vs.

Belirttiğim gibi ben `yt.dlp.exe` ve `ffmpeg.exe` yi aynı klasörde tutuyorum,
PATH'e bir değişiklik yapmıyorum. Şimdi bu dizine gidip bir terminal açalım.

```text
.\yt-dlp.exe WO2b03Zdu4Q
```

Çıktılar da şu şekilde:

```text
[youtube] Extracting URL: WO2b03Zdu4Q
[youtube] WO2b03Zdu4Q: Downloading webpage
[youtube] WO2b03Zdu4Q: Downloading ios player API JSON
[youtube] WO2b03Zdu4Q: Downloading player 5352eb4f
[youtube] WO2b03Zdu4Q: Downloading m3u8 information
[info] WO2b03Zdu4Q: Downloading 1 format(s): 337+251
[download] Destination: 2021 LG OLED l  Ink Art 4K HDR 60fps [WO2b03Zdu4Q].f337.webm
[download] 100% of  149.01MiB in 00:00:32 at 4.53MiB/s
[download] Destination: 2021 LG OLED l  Ink Art 4K HDR 60fps [WO2b03Zdu4Q].f251.webm
[download] 100% of  773.64KiB in 00:00:00 at 2.07MiB/s
[Merger] Merging formats into "2021 LG OLED l  Ink Art 4K HDR 60fps [WO2b03Zdu4Q].webm"
Deleting original file 2021 LG OLED l  Ink Art 4K HDR 60fps [WO2b03Zdu4Q].f251.webm (pass -k to keep)
Deleting original file 2021 LG OLED l  Ink Art 4K HDR 60fps [WO2b03Zdu4Q].f337.webm (pass -k to keep)
```

Gördüğünüz üzere iki farklı dosya iniyor, biri video ve biri ses. Daha sonra
`[Merger]` kısmında bu iki dosya FFmpeg çağırılarak birleştiriliyor. Medya
dosyaları ile "oynamak" yt-dlp'nin işi değil, o noktada FFmpeg devreye giriyor.
yt-dlp, özünde bir Download manager.

Eğer yt-dlp, FFmpeg'i bulamıyorsa bu sefer şöyle bir mesaj alırsınız:

```text
[youtube] Extracting URL: WO2b03Zdu4Q
[youtube] WO2b03Zdu4Q: Downloading webpage
[youtube] WO2b03Zdu4Q: Downloading ios player API JSON
[youtube] WO2b03Zdu4Q: Downloading m3u8 information
WARNING: ffmpeg not found. The downloaded format may not be the best available. Installing ffmpeg is strongly recommended: https://github.com/yt-dlp/yt-dlp#dependencies
[info] WO2b03Zdu4Q: Downloading 1 format(s): 18
[download] Destination: 2021 LG OLED l  Ink Art 4K HDR 60fps [WO2b03Zdu4Q].mp4
[download] 100% of    2.32MiB in 00:00:00 at 2.68MiB/s
```

Bu durumda yine bir şekilde video indirdi fakat bu indirdiği video 4K değil 360p!
Bazen indirme yapması da mümkün olmuyor, o yüzden FFmpeg'in kullanılabilir olmasını
sağlayın.

---

YouTube kısmı bu kadar, playlist indirme ve ihtiyacı varsa dokümanlarını ve
interneti kurcalarsınız.

## Vimeo

yt-dlp, vimeo üzerinde de kullanılabiliyor.

```text
.\yt-dlp.exe https://vimeo.com/<ID>
```

şeklinde kullanabilirsiniz.

Örnek:

```text
.\yt-dlp.exe https://vimeo.com/226053498
[vimeo] Extracting URL: https://vimeo.com/226053498
[vimeo] 226053498: Downloading webpage
[vimeo] 226053498: Downloading JSON metadata
[vimeo] 226053498: Downloading JSON metadata
[vimeo] 226053498: Downloading jwt token
[vimeo] 226053498: Downloading JSON metadata
[vimeo] 226053498: Downloading akfire_interconnect_quic m3u8 information
[vimeo] 226053498: Downloading akfire_interconnect_quic m3u8 information
[vimeo] 226053498: Downloading fastly_skyfire m3u8 information
[vimeo] 226053498: Downloading fastly_skyfire m3u8 information
[vimeo] 226053498: Downloading akfire_interconnect_quic MPD information
[vimeo] 226053498: Downloading akfire_interconnect_quic MPD information
[vimeo] 226053498: Downloading fastly_skyfire MPD information
[vimeo] 226053498: Downloading fastly_skyfire MPD information
[info] 226053498: Downloading 1 format(s): http-720p
[download] Destination: Test Video [226053498].mp4
[download] 100% of   11.13MiB in 00:00:03 at 2.97MiB/s
```

### Şifreli Videoları İndirme

Vimeo, YouTube'tan farklı bir platform. Kişilerin ve kurumların şifreli video
sunmasına imkan sağlayabiliyor. yt-dlp, şifreli videoların indirilmesini de
destekliyor.

```text
.\yt-dlp.exe --video-password <SIFRE> https://vimeo.com/<ID>
```

şeklinde indirebiliyorsunuz. **Fakat bu iş o kadar kolay olmayabiliyor.**

---

yt-dlp gibi araçlar, aslında kullanıcıyı ve bir web tarayıcısını taklit ederek
videoları indirmeye çalışıyorlar. Stream platformları hem bu tarz girişimleri
engellemek hem de başka sebeplerden dolayı altyapılarında değişiklik
yapabiliyorlar. Bu durumda da `yt-dlp` gibi araçların çalışmadığı anlar
olabiliyor. Eğer bir problem yaşarsanız ilk olarak yt-dlp'yi en güncel sürümüne
yükseltmenizi öneririm. **Bunu yaparken dikkatli olun.** Öncesinde `yt-dlp
--version` diyerek elinizdeki sürümün ne olduğuna bakın, çünkü geri dönmek
gerekebilir. Bazen güncellemeler bir şeyleri bozabiliyor. En yeni sürüme
geçseniz de bazı şeyleri yapamıyor olabilirsiniz. Örneğin YouTube çok popüler
bir platform olduğu için yt-dlp geliştiricileri ve topluluğu YouTube'un aldığı
önlemlere ve altyapı değişikliklerine çok hızlı tepki gösterip programı
düzeltebiliyorlar fakat Vimeo o kadar popüler olmadığı için yt-dlp, her zaman
düzgün çalışmayabiliyor.

Örneğin:

```text
.\yt-dlp.exe --video-password <SIFRE> https://vimeo.com/<ID>

[vimeo] Extracting URL: https://vimeo.com/<ID>
[vimeo] <ID>: Downloading webpage
ERROR: [vimeo] <ID>: Unable to download webpage: HTTP Error 403: Forbidden (caused by <HTTPError 403: Forbidden>)
```

Gibi 403 hatası alırsanız bende durum `yt-dlp` yi güncelleyerek çözüldü, daha
doğrusu başka hataya geçti. Bu arada yt-dlp'yi `.\yt-dlp.exe -U` diyerek hiç
Github'a vs gitmeden güncelleyebiliyorsunuz.

```text
.\yt-dlp.exe -U

Current version: stable@2024.05.27 from yt-dlp/yt-dlp
Latest version: stable@2024.07.02 from yt-dlp/yt-dlp
Current Build Hash: e96f6348244306ac999501b1e8e2b096b8a57f098c3b2b9ffe64b2107039e0ae
Updating to stable@2024.07.02 from yt-dlp/yt-dlp ...
Updated yt-dlp to stable@2024.07.02 from yt-dlp/yt-dlp
```

gibi.

Bunu güncelledikten sonra Vimeo'dan şifreli bir video indirmek istediğimde
yine başarısız oldu fakat 403 değil, 400 hatası vermeye başladı:

```text
.\yt-dlp.exe --video-password <SIFRE> https://vimeo.com/<ID>

[vimeo] Extracting URL: https://vimeo.com/<ID>
[vimeo] <ID>: Downloading webpage
[vimeo] <ID>: Downloading JSON metadata
[vimeo] <ID>: Downloading JSON metadata
ERROR: [vimeo] <ID>: Unable to download JSON metadata: HTTP Error 400: Bad Request (caused by <HTTPError 400: Bad Request>)
```

### Protected ve Private Videolar

Vimeo'nun video yükleyen tarafında olmadım. Anladığım kadarıyla şifreyle korunan
iki tip video var: protected ve private. yt-dlp, private videoları indirebiliyor
fakat protected videolarda başarısız oluyor, en azından şimdilik. Belirttiğim
gibi siz bu yazıyı okuduğunuz zaman durum değişmiş olabilir çünkü hem Vimeo
tarafı hem de yt-dlp tarafı sürekli güncelleniyor.

yt-dlp'nin başarısız olduğu durumlarda tarayıcımızın geliştirici araçlarını
kullanarak indirme işlemi yapabiliriz.

### Chrome Üzerinden İndirme

Chrome'un geliştirici aracını bu iş için daha kullanışlı buldum, o yüzden anlatımı
Chrome üzerinden yapacağım ama siz diğer tarayıcılarda da benzer işler
yapabilirsiniz.

İndirmek istediğimiz videoyu açıyoruz, şifremizi girip izlemeye başlıyoruz.
Burada görüntü kalitesini elle ayarlamanızı öneririm aksi taktirde pencere
boyutunuza ve internet hızınıza göre Vimeo daha düşük kalitede bir video gönderiyor
olabilir. Diyelim ki Full HD, yani 1080p indirmek istiyoruz:

```{figure} assets/yt-dlp-vimeo-kalite.png
:align: center

Elle kaliteyi 1080p yaptım.
```

Videoyu başlatalım, bir 10 snye oynasın, videoyu durdurmayın oynamaya devam
etsin. Daha sonra **F12** tuşuna basarak, *Geliştirici Araçlarını* yani
*DevTools* u açalım ve *Ağ* Yani *Network* sekmesine giderek gelen giden şeyleri
yakalayalım. Bu arada videomuz oynuyor olmalı. Daha sonra *Boyut* a göre
azalacak şekilde sıralayalım. Bendeki gibi iki farklı isimde `.mp4` dosyaları
gördükten sonra paketlerin yakalanmasını durdurabilirsiniz.

```{figure} assets/yt-dlp-chrome-devtools.png
:align: center

`F12` ile açıyoruz.
```

Burada ismi farklı olan iki adet `.mp4` dosyası göreceksiniz. Ben yukarıdaki
görselde `1` ve `2` olarak işaretledim. Biz videoyu izledikçe bu dosyalar
Vimeo'dan tarayıcımıza gelmeye devam edecektir. Boyutu yaklaşık 2 MB olan dosya
parçaları yani `1.mp4`, video dosyasıdır fakat sessizdir. Boyutu 100 kB altında
parçaları olan `2.mp4` dosyası ise ses dosyasıdır onda da video yoktur. `1.mp4`
e ait satırlardan birine sağ tıklayalım, `Kopyala → URL'yi kopyala` diyelim.
Bunu doğrudan yeni bir sekme açarak adres çubuğuna veya bir not defterine
yapıştıralım. Şu formatta olacaktır:

```text
https://vod-adaptive-ak.vimeocdn.com/a/1.mp4?c&range=d-f
```

Ben birçok yeri kısalttım. Burada sonda bulunan `&range=...` kısmını **siliyoruz.**
Fakat onun dışındaki diğer parçaları bırakıyoruz. Yani:

```text
https://vod-adaptive-ak.vimeocdn.com/a/1.mp4?c
```

kalıyor. Kalan kısma tarayıcımızla gidiyoruz.

Burada videomuz doğrudan tarayıcı içerisinde oynayacaktır, fakat sesi yok.
Videonun sağ altında bulunan `⋮` sembolüne tıklıyor ve `İndir` diyoruz.
`1.mp4` dosyamız iniyor.

Aynı işlemi `2.mp4` için yani ses dosyası için de tekrarlıyoruz. Günün sonunda
elimizde `1.mp4` yani video dosyası ve `2.mp4` yani ses dosyası bulunuyor.

Son aşamada bunları birleşitiriyoruz. Bunun için FFmpeg kullanabiliriz. Zaten
yazının başında FFmpeg'i temin etmeyi anlatmıştım, yt-dlp için de temin etmemiz
gerekiyor. İndirdiğimiz FFmpeg'i kullanabiliriz. Şu yazımda FFmpeg ile
birleştirme işlemini anlatıyorum:

[](ffmpeg-birlestirme.md)

Birleştirdikten sonra videoyu bir kontrol edin, sesi düzgün mü? Bazen başları
düzgün olup sonda bozulmalar olabiliyor. Böyle bir durumda işlemleri tekrar
etmeyi deneyebilirsiniz. Nadir de olsa anlık ağ problemlerinden dosyalar bozuk
gelebiliyor. Videonun başını, ortasını ve sonunu atlayarak şöyle bir 2-3 saniye
bakarak test edin.

## Kapanış

An itibariyle durum bu şekilde. Ama dediğim gibi YouTube, Vimeo gibi stream
platformları sürekli değişiklik yapıyorlar. Bunların bir kısmı yt-dlp gibi
programların çalışmasını engellemeye yönelik oluyor. Buna karşı tedbirler de
yt-dlp tarafından alınıyor, yani sonu olmayan bir mücadele adeta. Sizin bu yazıyı
okuduğunuz tarihte yazdığım yöntemler çalışmıyor olabilir ya da işler kolaylaşmış
olabilir.

Tekrar hatırlatmak isterim ki ben burada yöntemi tarifliyorum. İndireceğiniz
içeriklerin sahiplik konusu, kullanım lisansı gibi konulara lütfen dikkat edin.

**Bir şeyi yapabiliyor olmanız onu yapmanızı her zaman haklı kılmaz.**

## Kaynaklar

- [r/youtubedl](https://www.reddit.com/r/youtubedl/)

[^1f]: <https://github.blog/2020-11-16-standing-up-for-developers-youtube-dl-is-back/>
[^2f]: <https://www.eff.org/deeplinks/2020/11/github-reinstates-youtube-dl-after-riaas-abuse-dmca>
[^3f]: <https://www.reddit.com/r/youtubedl/comments/jgttnc/youtubedl_github_repository_disabled_due_to_a>
[^4f]: <https://www.ffmpeg.org/download.html#build-windows>
