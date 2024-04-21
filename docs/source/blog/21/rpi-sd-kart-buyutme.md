---
og:description: "Kullandığınız SD kartı aynı boy ya da daha büyük bir karta nasıl taşıyabileceğinizi anlatıyorum."
og:image: assets/social/blog/21/rpi.jpg
giscus: 35598bae-d784-4a38-aa32-3564bb7dd994
---

# Raspberry Pi SD kart taşıma ve büyütme

```{figure} /extra/assets/social/blog/21/rpi.jpg
:align: center
:figclass: thmbnl
```

---

Raspberry Pi 400'de kullandığım SD kartın boyutu biraz küçük kalmaya başlayınca
daha büyük bir SD karta (performansı da biraz daha iyi olabilir) geçmem gerekti.
Bu yazıyı küçük bir not yazısı olarak düşünebilirsiniz. İnternette farklı
yöntemlerle bu işi tarifleyen birçok yazı bulabilirsiniz. Yapılan işlemin çoğu
RPi 400'e özel olmadığından diğer RPi'ler ya da başka kartlar için de bu yöntem
uygulanabilir.

```{warning}
**Uyarı** Eğer hedef SD kart, ilk SD karttan daha küçük ise bu yöntem olduğu
gibi kullanılamaz. Öncesinde dosya sistemlerini küçültmek ve kopyalamayı dosya
sistemlerini göz önüne alarak (bu yazıda *ham* kopyalama anlatılıyor) yapmak
gerekecektir.
```

Ben işlemleri üzerinde Linux koşan ve SD kart takabildiğim başka bir
bilgisayarda yaptım. Windows için
[burada](https://peppe8o.com/raspberry-pi-migrating-to-larger-sd-card-with-windows-step-by-step-guide/)
anlatıldığı gibi `Win32DiskImager` isimli bir yazılım da kullanılabilir duruyor
(denemedim).

İşlemleri yapacağımızın bilgisayarın hangi Linux dağıtımını çalıştırdığının
önemi yok. Aşağıda verdiğim komutları `BASH` üzerinde çalıştırdım. Root hakkımızın
olması yani `sudo` ile komutları çalıştırabilmemiz gerekiyor.

## SD kartı bilgisayara kopyalama

```{attention}
⚠️ **Dikkat!** Sonraki adımlarda hata yapmamak adına bilgisayarınıza takılı ve
ihtiyaç duymadığınız USB bellek, harici disk, telefon gibi başka depolama
birimleri var ise onları şu aşamada çıkartmanızı öneririm.
```

İlk olarak RPi'de kullandığımız SD kartı çalışacağımız bilgisayara takıyoruz.
Aşağıdaki komutla SD kartımızın hangi isimde göründüğüne bakıyoruz.

```console
$ sudo fdisk -l
```

Benim durumumda SD kart `/dev/sdb` altında gözüküyordu. **Sizin durumunuzda
başka bir isimde çıkabilir.** İleride yazdığım komutlardaki `/dev/sdX` kısımlarını
sizde çıkan isim ile değiştirmeyi unutmayın. Örneğin ben, `/dev/sdX` yerine
`/dev/sdb` yazdım.

Eğer SD kartı bulmakta zorlanıyorsanız şunları yapabilirsiniz: 1) SD kartı
çıkarın ve `sudo fdisk -l` komutunu çalıştırın ve daha sonra geri takın tekrar
çalıştırın, yeni eklenen isim SD kart olmalıdır. 2) Yüksek ihtimalle
bilgisayarınızda kaç disk varsa `a` dan başlayarak o kadar harf zaten disklerinize
atanmış olacaktır. Örneğin 3 diskiniz varsa `a,b,c` harfleri yüksek ihtimalle
bu disklere atanmış olacağından başka bir USB bellek gibi cihaz da takılı değilse
SD kart `d` harfini alacaktır. 3) Standart Raspberry Pi OS (eski adıyla Raspbian)
kullanıyorsanız SD kart ile beraber iki bölüm de gözükecektir, `/dev/sdX0`
ve `/dev/sdX1`. Bu da bir doğrulama yöntemi olabilir.

Birçok Linux dağıtımı SD kartı takınca otomatik olarak üzerindeki 2 bölümü
otomatik *mount* edecektir. Bu bölümler üzerinde işlem yapmadığımız sürece
bir problem olmayacaktır ama emin olmak adına *mount* edilmiş kısımları *umount*
edelim. Böylece kopyalama yaparken dosya sistemlerin tutarsızlaşma riskini de
ortadan kaldırmış olacağız.

İlk olarak şu komutla *mount* edilmiş kısımlar var mı diye bakalım. Sonuç boş
dönerse bir sonraki komutu çalıştırmaya gerek yok ama çalıştırsanız da bir
zararı olmayacaktır.

```console
$ mount | grep /dev/sdX
```

Aşağıdaki komutla *umount* edelim.

```console
$ sudo umount /dev/sdX+([0-9])
```

Emin olmak adına iki üstteki komutla *mount* edilmiş bölüm var mı diye bakabiliriz.
Bu noktadan sonra *mount* edilmiş bir yer kalmaması gerekiyor.

Aşağıdaki komutla da SD kartı bilgisayarımıza kopyalamış oluyoruz.

```console
$ sudo dd if=/dev/sdX of=rpi.img bs=1M status=progress
```

Bu noktadan sonra komutu çalıştırdığımız dizinde oluşan `rpi.img` aslında SD karta
kurulum yapılacak bir işletim sistemi imajı olarak düşünülebilir. Bu noktadan
sonra SD kartı çıkartabiliriz.

ℹ️ `dd` komutu SD kartın tüm içeriğini kopyalayacaktır. Örneğin kartınız 32 GB
diyelim. 10 GB dolu olsa bile `rpi.img` 32 GB olacaktır. Çünkü `dd`, dosya
sistemini tanımaz ve *ham* haliyle tüm içeriği kopyalar. Eğer kartınızın çoğu
dolu ise zaten gereksiz yere kopyalanacak kısım az olacağından ekstra
kopyalayacağınız kısım zaman ve boyut açısından çok problem olmayacaktır. Ama
kartınızın çok azını kullanıyorsanız ve kullanılmayan kısmın kopyalanması ile
uğraşmak istemiyorsanız
[buradaki](https://serverfault.com/questions/439128/dd-on-entire-disk-but-do-not-want-empty-portion)
(🇬🇧) gibi çözümlere bakabilirsiniz. Yine de bu işlemi bir kere yapacağınızdan
alternatif aramak yerine kartı olduğu gibi kopyalamak iyi bir çözüm olabilir.

## Bilgisayardan yeni SD karta kopyalama

Şimdi `rpi.img` dosyasını geçiş yapacağımız (boyutu eskisinden küçük olmayan)
SD karta yazacağız. Bunun için üstteki adımlarda olduğu gibi yeni SD kartımızın
harfini, `/dev/sdX`, bulmamız gerekiyor. Yine yukarıdaki komutları kullanarak
*mount* edilmiş bölüm varsa onları *umount* etmemiz gerekiyor.

```{attention}
❗ ⚠️ İlk SD kartı söküp, ikincisini bilgisayar taktığımızda aynı `/dev/sdX` değerini
alması beklenir ama bu garanti değildir. Bu yüzden SD kartı değiştirince
tekrar kontrol etmekte fayda var.
```

SD kartın harfini bulduktan sonra imaj dosyasını yazacağız.

Aşağıdaki komut dikkat etmezseniz tehlikeli olabilir. `of` parametresine verilen
`/dev/sdX`in SD kartı gösterdiğinden emin olun. **Aksi taktirde sistemde bulunan
bir diskinizin üzerine dönüşü neredeyse olmayacak şekilde yazabilirsiniz.**
{: .notice--danger}

```console
$ sudo dd of=/dev/sdX if=rpi.img bs=1M status=progress
$ sync
```

SD kartımızı çıkartıp Raspberry Pi'ı açıp kalan işlemlere devam edebiliriz. Artık
`rpi.img` dosyasının olduğu bilgisayar ile de işimiz kalmadı.

## Raspberry Pi üzerinde alanların genişletilmesi

**⚠️ Bundan sonraki komutları Raspberry Pi üzerinde çalıştıracağız.**

```{note}
ℹ️ Raspberry Pi'ı yeni kart ile ilk açışımızda konsolda disklerin kontrol edildiğine
dair, `fsck` gibi, bir mesaj görebiliriz. Burada panik olmamıza gerek yok.
```

Yeni SD kartımız eskisinden büyükse bile RPi üzerinde alanın genişlediğini
hemen görmüyoruz çünkü SD kart üzerindeki dosya sistemlerinin de genişletilmesi
gerekiyor. Denemek için

```console
$ df -h
```

komutu ile ne kadar alanın olduğunu görebilirsiniz. SD kartınız büyüdüyse bile
buradaki değerler eski SD kartınızın değerlerini gösterecektir. Dosya sistemini
genişletmek için Raspberry Pi OS ile gelen `raspi-config` aracını kullanabiliriz.

```console
$ sudo raspi-config
```

komutunu çalıştırdıktan sonra açılan ekrandan `6 Advanced Options` ve ardından
`A1 Expand Filesystem` seçeneğini seçelim. RPi'yi yeniden başlattığımızda
kartımızın tüm alanının gözüküyor olması gerekiyor. Yine `df -h` ile kontrol
edebilirsiniz.

## Sonuç

Temelde eski SD kartımızın olduğu gibi yeni SD kartımıza kopyalamış ve ardından
da dosya sistemini yeni boyuta göre genişletmiş olduk. Eğer Windows üzerinde
bu işi yapmak istiyorsanız, daha küçük bir SD karta geçiyorsanız, kopyalama
işlemlerini kısaltmak için kart içeriğini *ham* olarak taşımak değil de dosya
sistemlerinden haberdar yöntemlerle taşımak istiyorsanız internetteki diğer
çözümlere bakabilirsiniz.

*İlk yayın: 2021-03-28*
