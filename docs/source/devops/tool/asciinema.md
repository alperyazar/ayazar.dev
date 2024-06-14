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

👉 [Docker](https://docs.asciinema.org/manual/cli/installation/#container-image)
