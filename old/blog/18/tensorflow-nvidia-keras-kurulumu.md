---
og:description: "GPU desteği ile Tensorflow ve Keras'ın Windows'a nasıl kurulabileceğini ve olası problem ve çözümleri anlatıyorum."
giscus: bb323257-54b5-4c9b-82f5-995182351d20
---

# Tensorflow (NVIDIA GPU Desteği ile) ve Keras Kurulumu

```{attention}
⚠️ **Dikkat! Eski içerik.** Bu yazı 2018'de yazılmış olup içerikte önemli bir
güncelleme yapılmamıştır. Bu yüzden bu yazıdaki içerikler yüksek ihtimalle
geçerliliğini yitirmiştir. Yazı, arşiv amaçlı tutulmaktadır ve daha güncel
kaynaklara bakmanızı öneririm.
```

ℹ️ Aşağıda yazdığım kısımlar konu ile ilgili kendime aldığım notlardır. Bir blog
yazısına kıyasla daha az özenle yazılmıştır. Faydalı olması için paylaşıyorum.

Doküman Kasım 2017 içinde hazırlandı. Sürümler şu şekilde:

- Tensorflow 1.4
- CUDA 8.0
- cuDNN v6.0 for CUDA 8.0
- Python 3.6.3 64 bit
- Keras 2.1.1

❗ 64-bit sistemlerde denendi yazılanlar.

## Windows 10 İçin

Win 7’ye kıyasla özel bir şey yok. Sadece bazı yerlerdeki Win 7 sürümleri yerine
Win 10 sürümleri kurulmalı. Win 7 kısmını okurken nerede Win 10 için ayrı
yazılım indirmeniz gerektiği anlaşılıyor olmalı.

## Windows 7 İçin

### Nvidia Araçlarının Kurulumu

#### CUDA 8.0

1. İlk olarak ekran kartımızın CUDA desteği olup olmadığına bakıyoruz şu
   listeden:
   [https://developer.nvidia.com/cuda-gpus](https://developer.nvidia.com/cuda-gpus)
   Tensorflow GPU desteği için CUDA Compute Capability en az 3.0 istiyor (Ref:
   `https://www.tensorflow.org/install/install_windows` `404 🔗`).
   Eğer ekran kartımız bunu desteklemiyorsa oturup ağlayabiliriz. Şaka şaka, GPU
   desteksiz kurulabilir Tensorflow. Bu dokümanda yazmadım ama daha basit
   olacaktır zaten, bodos Tensorflow kurulumu ile devam edilebilir bence.
2. Eğer ekran kartımızın desteği ile ilgili bir problem yoksa
   [https://developer.nvidia.com/cuda-80-ga2-download-archive](https://developer.nvidia.com/cuda-80-ga2-download-archive)
   adresinden işletim sistemimize uygun olan versiyonu indiriyoruz. Installer
   type olarak "exe(local)" olanı tavsiye ederim. Hem "Base Installer"ı hem de
   "Patch2" yi kuruyoruz. Başka patch'ler varsa bu doküman hazırlandıktan sonra
   çıkan onları da kurun bence. Tabii ilk önce “Base Installer” sonra sırası ile
   (varsa birden fazla) patch'ler kurulmalı. An itibariyle sürüm **CUDA
   8.0.61**. CUDA'nın kurulumu biraz uzun sürebiliyor ve restart etmek gerekiyor
   bilgisayarı.

### Python

1. Python sitesinden Tensorflow'un istediği Python sürümü indirilir (Ref:
   `https://www.tensorflow.org/install/install_windows` `404 🔗`). An itibariyle
   python-3.6.3-amd64 indirdim.
2. Yüklerken "Add Python 3.6 to PATH" seçeneği seçilmelidir. Yükleme lokasyonu
   olarak **C:/Python36_64** seçtim.
3. Eğer yükleme ve PATH'e ekleme başarılı ise, Windows'ta **cmd** ile komut
   satırı açılır ve **python** yazılır. Bu komut başarı ile çalışmalıdır.
   PATH'te sorun varsa python bulunamadı diye hata alınır. Python açılınca
   sürümünün doğru olduğu (3.6.3 gibi) açılan yazılımdan kontrol edilir.

### Tensorflow

1. Tensorflow kurlumu için `pip3 install --upgrade tensorflow-gpu` komutu
   **Window cmd**’ye yazılır (python çalıştırıp içine değil). Tabii CUDA desteği
   eklenemediyse önceki adımlarda ekran kartının eski olması gibi bu durumda
   GPU’suz seçenekle kurulur. Detaylı bilgi için:
   `https://www.tensorflow.org/install/install_windows` `404 🔗`.
2. Yükleme adımı bittikten sonra Tensorflow’un ekosisteminin uygun olup
   olmadığının kontrol edilmesini öneriyorum. Bunun için
   `tensorflow_self_check.py` isimli scripti kullanacağız.
   [Bunu](https://gist.github.com/mrry/ee5dbcfdd045fa48a27d56664411d41c )
   indiriyoruz ve dosyanın olduğu yerde windows CMD’yi açıp (Shift + Sağ click
   ve sonra Open Command Window Here veya cmd başlatıp cd ile o klasöre
   gidiyoruz) `pyton tensorflow_self_check.py` yazıyoruz.
3. Bu noktada muhtemelen cuDNN hatası alınacak. Onun için lütfen hata ayıklama
   kısmına bakın.

### Keras

1. Keras kurulumu için `pip3 install keras` yazıyoruz yine Windows CMD’ye
   (Python shell değil).
2. Test etmek için örnek bir kod çalıştıracağız. Kod, MNIST set kullanacak ve
   MLP networkü eğitecek. Şu
   (`https://github.com/fchollet/keras/blob/master/examples/mnist_mlp.py` `404
   🔗`) adresten ilgili dosyayı indiriyoruz. Diğer python scriptleri
   çalıştırdığımız gibi `python mnist_mlp.py` ile çalıştırıyoruz. Not: Bu script
   ilk olarak MNIST data setini indiriyor internetten. O yüzden ilk çalıştırmada
   biraz bekletebilir. Daha sonra lokal’deki datayı kullanacaktır.
3. Eğer tam data işlenmeye başlanınca bilgisayar "xxx (Nvidia GPU modeli)
   çıkartılamaz" gibi bir hata verip çakılıyorsa ve PC donuyorsa **Hata
   Ayıklama** kısmına bakın.

## Hata Ayıklama

### tensorflow_self_check.py ile CuDNN Hatası Alınması

#### Problem

`pyton tensorflow_self_check.py` zaman aşağıdaki hata alınıyor:

```text
- Could not load 'cudnn64_5.dll'. The GPU version of TensorFlow
  requires that this DLL be installed in a directory that is named in
  your %PATH% environment variable. Note that installing cuDNN is a
  separate step from installing CUDA, and it is often found in a
  different directory from the CUDA DLLs. You may install the
  necessary DLL by downloading cuDNN 5.1 from this URL:
  https://developer.nvidia.com/cudnn

- Could not find cuDNN.
```

#### Çözüm

1. Bu korkulacak bir şey değil. Sistemimize birkaç şey daha kurmamız gerekiyor.
   [Şu](https://developer.nvidia.com/cudnn) adrese gidelim.
2. Ne yazık ki bu noktada NVidia üyelik istiyor. Üye oluyoruz.
3. Lisans anlaşmasını kabul ediyoruz.
4. TensorFlow sürümümüz 1.3’ten büyük olduğu için cuDNN v6’yı indirmemiz
   gerekiyor. Script bize v5 kurun dese de v5’i kurunca bu sefer v6 kurmalıydın
   ama yanlış oldu diyor. O yüzden an itibariyle şunu indirmeliyiz: **Download
   cuDNN v6.0 (April 27, 2017), for CUDA 8.0**.
5. Buradan işletim sistemimize uygun olanı seçiyoruz: **cuDNN v6.0 Library for
   Windows 7, cuDNN v6.0 Library for Windows 10** gibi…
6. İndirdiğimiz zip dosyasını güzel bir yere extract ediyoruz. Mesela
   `C:\cuDNN60_CUDA80` gibi. Bu klasörün altında 3 adet klasörümüz oluyor:
   `bin`, `include` ve `lib`.
7. Daha sonra yüklediğimiz yerin bin dosyası sistemin PATH’ine eklenir:
   `C:\cuDNN60_CUDA80\bin` gibi.
8. PATH ekleme işleminden sonra PC’ye restart atmamız gerekiyor.
9. Restart sonrası `tensorflow_self_check.py` tekrar çalıştırılarak kontrol
   edilir. Hatanın gitmiş olması gerekir.

### Çalışırken Windows'un Ekran Kartının Çıkarılamayacağını Söylemesi ve Takılması

#### Problem

Ekran kartı kullanılmaya başlandığı anda PC takılıyor ve "hard reset" yapmadan
çalışmıyor. Bu bende Nvidia 650M’de görüldü. Optimus teknolojisi ile de alakalı
olabilir.

#### Çözüm

Bence problemin kaynağı CUDA'nın kurulduğu anda ekran kartı sürücüleri ile
oynaması. Benim durumumda son sürüm sürücüleri Nvidia sitesinden indirmek
problemi çözdü. Fakat internette başka yazılımlarda (Adobe Premier gibi) sorun
yaşayanlar olmuş. Onların bir kısmı BIOS'tan optimus'u kapatmış, kimisi Nvidia
ayarlarından kendi yazılımları için sürekli Nvidia GPU’yu kullan diye ayar
yapmış (bizim durumda bu python.exe oluyor). Net bir çözümü yok, biraz doğaçlama
yapmak gerekecek böyle bir sorunda.

*İlk yayın: 2018-02-10*
