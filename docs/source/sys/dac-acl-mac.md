# DAC, ACL, MAC

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

Linux'un klasik izin mimarisi bazı durumlarda yetersiz gelebilir. Örneğin bir
dosyaya farklı kullanıcılar için farklı erişim hakkı veremiyorsunuz. Kullanıcı
veya grup bazlı bir yetki veriyoruz ama bir kullanıcı listesi verip tek tek
izin belirtemiyoruz. İşte ACL bu tarz konularda yardımımıza yetişiyor.

Bunun çalışabilmesi için dosya sistemimizin bu yapıyı desteklemesi ve o şekilde
mount edilmesi gerekiyor, sonuçta disk üzerine bu verilerin kaydedilmesi lazım.
`mount` işlemi sırasında `acl` seçeneğinin verilmiş olması gerekiyor. ACL, uzun
yıllardır kernelde ve ext4 gibi *Linux native* dosya sistemlerinde olan bir
özellik. Muhtemelen günümüzdeki tüm Linux sistemlerinde kullanılabilir durumdadır.

```shell
alper@brs23-2204:~$ cat /etc/mke2fs.conf | grep acl
  default_mntopts = acl,user_xattr
```

Örneğin default olarak benim sistemim mount ederken `acl` seçeneğini açıyor.
Bildiğim kadarıyla ACL'nin çalışması için *extended user attributes* seçeneğinin
de, `user_xattr`, açık olması gerekiyor.

`getfacl` komutu ile o dosyanın ACL ayarlarını görebiliyoruz. Sistemde `acl` yoksa
bile bu hata vermeyebilir, DAC ayarlarını gösterecektir.

```shell
alper@brs23-2204:~/sys$ touch dosya

alper@brs23-2204:~/sys$ getfacl dosya
# file: dosya
# owner: alper
# group: alper
user::rw-
group::rw-
other::r--
```

Şimdi bu dosya üzerinde bir ACL kuralı ekleyelim:

```shell
alper@brs23-2204:~/sys$ setfacl -m "u:user1:rwx" dosya

alper@brs23-2204:~/sys$ ls -l dosya
-rw-rwxr--+ 1 alper alper 0 Jul 15 12:02 dosya
```

ACL kuralı eklenmiş dizin ve dosyalar `ls` çıktısında `+` ile işaretlenir.
Ayarlara bakalım:

```shell
alper@brs23-2204:~/sys$ getfacl dosya
# file: dosya
# owner: alper
# group: alper
user::rw-
user:user1:rwx
group::rw-
mask::rwx
other::r--
```

Burada `user1` in dosya üzerinde `rwx` hakkı oldu, test edelim.

```shell
user1@brs23-2204:/opt/sys$ echo "Ben user1 im" > dosya
user1@brs23-2204:/opt/sys$ cat dosya
Ben user1 im

user1@brs23-2204:/opt/sys$ ls -l dosya
-rw-rwxr--+ 1 alper alper 13 Jul 15 12:06 dosya
```

Normalde `user1` bu dosya için others kategorisindedir ve yazma hakkı yoktur,
`r--`. Fakat ACL ile `user1` e açıkça yazma hakkı verdiğimiz için bu kural
sayesinde dosyaya yazabildi.

Burada amacım sadece ACL'den bahsetmek olduğu için detaylandırmayacağım,
internette bir çok kaynak mevcut. [^1f] Sadece varlığından bahsetmek istedim.

---

Bir de [RBAC](https://en.wikipedia.org/wiki/Role-based_access_control) diye bir
şey var, Role Based Access Control. Şu aşamada detaylandırmaya gerek yok.

## Kaynaklar

- <https://wiki.archlinux.org/title/Security#Mandatory_access_control>
- <https://wiki.archlinux.org/title/SELinux>
- <https://wiki.archlinux.org/title/Access_Control_Lists>

[^1f]: <https://wiki.archlinux.org/title/Access_Control_Lists>
