---
og:description: "udisks komutu ile bağlanmayan disketlere çözüm"
---

# 🇹🇷 Ubuntu Üzerinde Disket Sürücüsünü Kullanma

"Bu çağda disket mi kaldı kardeşim, disketi ne yapalım?" demeniz çok normal.
Fakat bazı kişilerin hala disket sürücüsü olan masaüstü bilgisayarları olabilir.
Daha da ilginç bir şekilde bu kişilerin ellerinde çalışan disketler olabilir
benim gibi. 😄 Neyse, lafı çok uzatmayalım. Eğer bilgisayarınızda Ubuntu yüklü
ise zaten direkt olarak disket sürücünüzü görüyor olması lazım. Fakat disketi
takıp, çift tıkladığınız zaman `Konum Bağlanamadı – Sürücüde hiçbir ortam
bulunamadı` şeklinde bir hata vermektedir. Aynı durumu Linux Mint üzerinde de
yaşadım. Zaten Linux Mint'in LMDE olmayan sürümleri Ubuntu üzerine
geliştirildiği için olağan dışı bir durum değil. Elbette Linux dünyasındaki
birçok sorun gibi bunun da çözümü mevcut. Bu çözümü Ubuntu 10.04 üzerinde
denedim. Hem başkalarının işine yarayabilir hem de ileride tekrar lazım olursa
aramakla uğraşmayayım diye buraya da eklemek istedim.

Sürücümüze disketi taktıktan sonra, terminalimizi açıyoruz ve aşağıdaki komutu
veriyoruz:

```shell
$ udisks --mount /dev/fd0
```

Burada `/dev/fd0` bizim disket sürücümüz. Sizde de muhtemelen aynı yerde
olacaktır. Komutu verdikten 10-15 saniye sonra masaüstümüzde bir disket ikonu
çıkıyor. Bu ikona tıklayarak disketi açabiliyoruz. İşte bu kadar basit.

İşimiz bittikten sonra da

```shell
$ udisks --unmount /dev/fd0
```

komutu ile disketimizi güvenle kaldırıp, çıkarabiliyoruz.

Bol Linux'lu günler dileği ile..

*İlk yayın: 2012-07-28*

```{disqus}
:disqus_identifier: 5c7f0505-abe1-4510-87bd-2d579b36387a
```
