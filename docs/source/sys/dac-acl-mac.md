# DAC, ACL, MAC

```{todo}
Yazı yarımdır.
```

İzinlerle ilgili sanıyorum şimdilik son yazım bu olacak. Son olarak birkaç
kavrama daha bakalım.

## DAC, Discretionary Access Controls

Discretionary, isteğe bağlı demektir. Şimdiye kadar gördüğümüz klasik owner:group
ve `rwx` bazlı izin modeli böyle bir modeldir. Peki neden buna isteğe bağlı
diyoruz?

Bir açıklama şöyle: Kullanıcı kendi dosyasını isteğe bağlı olarak başkalarına
açabiliyor, kapatabiliyor. Kendi kaynağını kendi yönetiyor. Sistem yöneticinin
buna engel olması bu modelde daha zor. Bu modelde ayrıca `root` kullanıcısının
sınırsız olarak her yere erişmesi de potansiyel bir güvenlik problemi. Çünkü bir
kişi veya proses root yetkisi kazanırsa veya root yetkisinde çalışan proseste
güvenlik açığı olursa işler karışabiliyor.

## MAC, Mandatory Access Controls

MAC türü izinler ise DAC'tan daha *yüksek çözünürlüğe* sahip ve daha *katı*
engellemeler içerebiliyor. Örneğin bir sunucu çalıştırıyorsunuz, içinde DNS
sunucusu var, BIND mesela, bu arkadaş `root` yetkileri ile çalışıyor. BIND'ta
bir hata olsa ve bir hacker ele geçirse `root` yetkisini kullanarak her yere
erişebilir. Fakat MAC sistemlerinde BIND'in erişeceği dosyaları
limitleyebiliyorsunuz, `root` olsa bile. Diyorsunuz ki BIND kendi konfigürasyon
dosyası olan, atıyorum `/etc/bind.conf` dışında bir dosyaya erişemesin. Bu
sayede birisi BIND'ı ele geçirse bile başka dosyalara erişemiyor.

Bu elbette kernelde olması gereken bir özellik. Uzun yıllardır var olan NSA
tarafından geliştirilen 🤔
[SELinux](https://en.wikipedia.org/wiki/Security-Enhanced_Linux) ve
[AppArmor](https://en.wikipedia.org/wiki/AppArmor) gibi sistemler birer MAC
örneğidir. Örneğin bilgisayarınıza Fedora kurduğunuzda SELinux açık gelmektedir.
Ben burada detaya girmeyeceğim çünkü bunları konfigüre etmek ve kullanmak ayrı
bir iş, sadece varlıklarından bahsetmek istedim.

**Bu not serisi boyunca sadece DAC'ı düşüneceğiz.**

## ACL, Access Control List

ACL, DAC'ın genişletilmiş hali gibi düşünebilir. Her ne kadar Arch Linux Wiki'de
MAC'ın altında anlatılmış olsa da standart Linux izinlerinin genişletilmiş hali
olarak düşünebiliriz.

```{todo}
Buradayım
```

---

Bir de [RBAC](https://en.wikipedia.org/wiki/Role-based_access_control) diye bir
şey var, Role Based Access Control

## Kaynaklar

- <https://wiki.archlinux.org/title/Security#Mandatory_access_control>
- <https://wiki.archlinux.org/title/SELinux>
- <https://wiki.archlinux.org/title/Access_Control_Lists>
