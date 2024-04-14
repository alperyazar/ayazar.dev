---
og:description: "Dual boot çalışan bilgisayarın Windows güncellemesi ile bozulan disk düzenini tamir ediyoruz."
---

# Windows 10 1803->1903 Yükseltmesi Sırasında GRUB'un Bozulması

## Sorun

Windows 10 1803 ve Debian 9 dual boot çalışan (fiziksel olarak aynı diskte
kurulu) dizüstü bilgisayarımın Windows'unu 1903'e "Update Assistant" (bknz:
[Link](https://www.microsoft.com/tr-tr/software-download/windows10) ve
[Link](https://go.microsoft.com/fwlink/?LinkID=799445) ) kullanarak yükselttim.
Windows'un kendi update kısmında 1903 çıkmadığı için (çok benzer sürüm
çalıştıran masaüstü bilgisayarımda çıkmıştı) bu asistanı kullandım ama bu sorun
ile ilgisi olduğunu sanmıyorum. Güncelleme sırasında bilgisayar birkaç kez
reboot ediyor. Benim default GRUB ayarım Debian açılacak şekilde. Bu reboot
yapma sırasında bir kez GRUB ekranını kaçırarak Debian'ın açılmasına sebep
oldum. Buradan da tekrar reboot edip, Windows'u açarak güncellemenin devam
etmesini sağladım. Masaüstü bilgisayarımda böyle bir an yaşanmadı ama yine
sorunun bundan kaynaklanacağını zannetmiyorum. Daha sonra olan bir reboot
sırasında GRUB menüsü gelemeden BIOS mesajından sonra şu yazı beni karşıladı:

```text
error: unknown filesystem.
Entering rescue mode...
grub rescue>
```

Windows update'e devam etmek için BIOS'a girerek boot device'ımı "debian"dan
"Windows Boot Manager"a geçirdim. Bu isimler EFI bölümleri olmalı. GRUB,
"debian" isimli yerde kurulu. "Windows Boot Manager" ile açınca GRUB ekranı
gelmeden Windows açılıyor. Bu sayede güncelleme işlemini tamamlayabildim.

## Çözüm

### 1. Deneme (Başarısız)

[Boot-Repair-Disk](https://sourceforge.net/p/boot-repair-cd/home/Home/) imajını
USB belleğe yazıp, bilgisayarı boot ettim. Doğrudan "Recommended repair" dediğim
zaman bir şeyler yaptı ama hata devam etti. Kendisi Lubuntu 17.xx (04 ya da 10,
an itibariyle) temelli Openbox çalıştıran minimal bir dağıtım.

Live bir dağıtım ile konsoldan GRUB kurmayı deneyeceğim. Sistemde "LVM over
LUKS" var, ona dikkat etmem gerekir mi?

Ref:

- `https://askubuntu.com/questions/1098221/windows-10-update-grub-rescue` `404`
- <https://help.ubuntu.com/community/RecoveringUbuntuAfterInstallingWindows>
- <https://help.ubuntu.com/community/Boot-Repair>

### 2. Deneme (Başarılı)

Boot-Repair-Disk işi hemen olmayınca elimde olan Ubuntu 18.04 imajı ile
bilgisayarı boot ettim. Takip ettiğim kısım temel olarak şurası:
<https://help.ubuntu.com/community/Grub2/Installing#via_ChRoot>
"via ChRoot" kısmı. Benim sistemde root kısmı LVM üzerinde bulunuyor. Bu da
şifreli bir partition üzerinde. Buna göre adımları biraz modifiye ettim. Bende
RAID yok.

Ubuntu imajında Gparted dahili bulunuyor. Bu disk ile ilgili bilgilere hızlıca
bakmak için iyi oldu. Kendi yazdığım komutlar şu şekilde. Siz yapıyorsanız
harflere, numaralara dikkat edin.

İlk olarak şifreli diski açalım. Ubuntu imajında LVM ve dm-crypt ile ilgili
şeyler kurulu olduğu için bir şey yüklemeye gerek yok.

```shell
$ sudo cryptsetup open /dev/sdaX lv
```

Yukarıdaki `lv` rastgele bir isim, önemi yok. Burada diskin şifresini girmek
gerekiyor. Disk otomatik bir şekilde boot esnasında açılıyor ve şifre
bilinmiyorsa ne yapılır araştırmak lazım. Bu işlem için burayı da mount etmek
gerekiyor mu onu da bilmiyorum aslında.

Şifreyi girdikten sonra LVM vs otomatik çalıştı ve partitionlarım gözüktü.
Listelemek için:

```shell
$ sudo lvdisplay
```

Burada `LV Path`e bakarak root dizinini mount edelim.

```shell
$ sudo mount /dev/vg/root /mnt
```

Bu noktada `/mnt` altında dosyalarımızı görmemiz lazım. Ben burada
`/etc/fstab`'tan kopya çektim. Ek olarak mount ettiğim iki partition daha var:
`/boot` ve `/boot/efi`.

Örnek:

```shell
$ sudo mount /dev/sdaY /mnt/boot
$ sudo mount /dev/sdaZ /mnt/boot/efi
```

Birazdan `chroot` yapacağız, onun için hazırlık yapıyoruz şimdi. Eğer bunları
yapmazsak olmuyor mu denemedim.

```shell
$ for i in /dev /dev/pts /proc /sys /run; do sudo mount -B $i /mnt$i; done
```

Sonra

```shell
$ sudo chroot /mnt
# grub-install /dev/sda
# update-grub
```

`CTRL-D` ile `chroot` içinden çıkıyoruz ve bilgisayarımızı yeniden başlatıyoruz.
Bu noktada benim problemim çözüldü.

## Sebebi neydi ki?

Şu an bulamadığım (tekrar çok da aramadım) bir linkte bunun Windows 10 ile
ilgili bir bug olduğu yazıyor. Benzer işlemi masaüstü bilgisayarımda yaptım
fakat onda Windows ile Linux veya hatta GRUB, tam konfigürasyon aklımda yok,
fiziksel olarak ayrı disklerde olduğu için belki de bu problem olmadı. Her iki
bilgisayar da EFI, fark burdan değil.

Dikkatimi çeken bir nokta da problem yaşadığım dizüstü bilgisyarın /etc/fstab
girdisi oldu. Burada zamanında kurulum sırasında otomatik olarak UUID'lerle
girdiler oluşturulurken bırakılmış yorumlar var. Diyor ki UUID bilmem ne
zamanında /dev/sdaX'teydi. İlginç olan /boot/efi ile ilgili yorumda belirtilen
paritition numarası hala doğruyken /boot ile ilgili yorumda yazan partition
numarası, diskteki numaradan 1 fazla. Tabii bu farklılık önceden var mıydı
bilmiyorum. Bu son işlem sırasında olmamış da olabilir. Fakat Windows update
sırasında (aslında upgrade demek daha doğru buna) disk layout'u ile oynamış ve
dual boot olma ihtimalini düşünmemiş olabilir.

[Lanet olsun sebebi neydi ki?](https://www.youtube.com/watch?v=cEsocsQPVmw)

*İlk yayın: 2019-08-17*

```{disqus}
:disqus_identifier: a751a9a1-d774-48e1-a7aa-3e7659dc10f8
```
