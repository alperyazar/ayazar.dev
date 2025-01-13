# Asciinema

```{figure} assets/asciinema.png
:align: center
:figclass: thmbnl
```

---

Asciinema, sloganı **terminal session recorder** olarak geçen bir araç. Linux
üzerinde terminalde bir şeyler yapan ve bunları paylaşmak isteyen kişilere hitap
ediyor. OBS gibi ekranı video olarak kaydeden bir yazılımla arasındaki temel
fark kaydı bir metin dosyası olarak alıyor olması. Oynatıcısında da bir video
gibi izlesek de aslında arkada metin oynatılıyor. **İzlerken durdurup, faremizle
o metni kopyalayıp yapıştırabiliyoruz.** Diyelim ki bir tutorial hazırladınız,
bunu takip eden kişiler sizin yazdığınız komutları doğrudan kopyalayıp
kendilerine yapıştırabiliyorlar. Kayıtlar da metin tabanlı tutulduğu için bir
video kaydına göre çok az yer kaplıyor.

Bu servisi dilerseniz [asciinema.org](https://asciinema.org/) adresinde de
kullanabilir ya deneyebilirsiniz. Burada gördüğünüz servisin aynısını kendi
makinelerinizde de çalıştırabiliyorsunuz. SMTP entegrasyonu yapmanız biraz şart
gibi çünkü login sistemi mail üzerinden gönderilen tek kullanımlık linkler ile
çalışıyor.

Eğer ZSH gibi terminallerde, Unicode karakterler ile çalışıyorsanız kaydettiğiniz
terminal kayıtları web üzerinden oynatılırken düzgün gözükmeyebilir. Burada bir
deneme yapmanızı veya kayıt sırasında daha basit bir terminal düzenine geçmenizi
öneririm.

Kayıt sırasında **otomatik jump cut** yaptırabiliyorsunuz. Belirlediğiniz süre
boyunca terminalde bir işlem yapmazsanız o boşluklar kaydedilmiyor. Böylece
daha kısa süren kayıtlar elde edebiliyorsunuz. İzleyen kişiler de "Vay be
hiç düşünmeden takır tukur yazıyor" diyorlar. 😉

Aşağıdaki yazımda kaydettiğim birkaç örneği de görebilirsiniz:

[](../../buildroot/ilk-derleme.md)

## Kurulum ve Kullanım

Kurulum oldukça basit, web sitesine
[bakabilirsiniz.](https://docs.asciinema.org/manual/cli/installation/)

Önerilen yöntem `pipx` ve `pip` ile kurmak, `pipx install asciinema`. Birçok
dağıtımın da resmi repolarında bu yazılım bulunuyor. `sudo apt install asciinema`
şeklinde kurabilirsiniz. Özellikle Debian gibi dağıtımlarında repolarındaki
versiyon bir miktar eski olabilir. Örneğin an itibariyle `pypi.org` taki version
yani `pip/pipx` ile kurulan versiyon `2.4.0` olmasına rağmen Debian 12 repolarında
`2.2.0` bulunuyor. Bu sizin için bir sorunsa en güncelini kurabilirsiniz ama
çoğu durumda ihtiyacınız olmayacaktır.

### Kayıt Alma ve Oynatma

`asciinema rec` ile kayıt alabilirsiniz. Böyle kullanırsanız `/tmp` altında
rastgele isimle bir kayıt oluşturacaktır. Kayıt dosyasını düzgün isimlendirmek
istiyorsanız en baştan `asciinema rec kayit.cast` diyebilirsiniz. Daha sonra
`asciinema play kayit.cast` ile dosyayı oynatabilirsiniz. `.cast` dosyaları
metin formatındadır, metin editörü (`vim` gibi) ile içeriğine bakabilirsiniz.

### Otomatik Jump-Cut

`rec` derken `-i` argümanı geçirirseniz asciinema kayıt sırasında boşlukları
otomatik olarka atacaktır. Bunun kayıt dosyasını küçülteceğini söylemek doğru
olmaz ama kayıt alırken klavyeye basışlarınız arasında boşluklar varsa ve
bunları otomatik kırpmak istiyorsanız bu seçeneği kullanabilirsiniz. Bence
1 saniye gayet yeterli: `asciinema rec -i 1 kayit.cast` Aynı argümanı oynatırken
de geçirebilirsiniz kaydı böyle almadıysanız da `asciinema play -i 1 kayit.cast`
gibi ama kaydederken yapmak bence daha doğru.

### Yükleme

`rec` ile kayıt aldıktan sonra `asciinema` otomatik olarak dilerseniz
<https://asciinema.org/> adresine yükleme yapabilmektedir. Dilerseniz
birazdan anlatacağım self-hosted sunucuya da yükleme yapabilir. Elinizdeki
bir `.cast` dosyasını `asciinema upload` ile yükleyebilirsiniz.

### Yardım Alma

`asciinema --help` ile genel bir yardım görüntüleyebilir ya da her bir komutun
yardım ekranına `asciinema <komut> --help` şeklinde erişebilirsiniz,
`asciinema rec --help` gibi.

## Online ve Self-Hosted Kullanım

<https://asciinema.org/> adresine kayıtlarınızı yükleyebilir ve paylaşabilirsiniz.
Dilerseniz bu sistenin aynısını Docker gibi bir teknoloji ile self-hosted
olarak da barındırabilirsiniz.

Ben burada self-hosted kullanımı anlatmaya çalışacağım.

### Sunucu Kurulumu

İlk olarak [buraya](https://docs.asciinema.org/manual/server/self-hosting/quick-start)
bir bakalım.

```{todo}
Henüz bitmedei buradayım.
```
