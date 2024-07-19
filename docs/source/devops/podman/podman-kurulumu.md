# Podman Kurulumu

Ubuntu üzerinde kurulumu ele alacağım. Ubuntu 22.04 ve 24.04'te Podman Ubuntu
repolarında bulunuyor ve buradan kurulabilir. Fakat güncel durumda
Ubuntu 22.04'te **podman version 3.4.4** bulunurken Ubuntu 24.04'te
**podman version 4.9.3** bulunuyor. Bildiğim kadarıyla v3 ile v4 arasında
önemli farklılıklar bulunabiliyor. Elbette bu farklılıklar sizin için kritik
olmayabilir fakat tercih edebiliyorsanız v4'ü ve Ubuntu'da devam etmeyi
düşünüyorsanız bu yüzden Ubuntu 24.04'ü kurmanızı öneririm. Elbette Ubuntu 22.04
ya da başka bir distro üzerinde Podman'ın en güncel versiyonu da kurulabilir
fakat en az uğraşı ile bunu yapmak istiyorsanız bu yolu seçebilirsiniz.

---

Kurulum oldukça basit, `sudo apt install podman` ile kurabiliyoruz.

## `/etc/subuid` ve `/etc/subgid`

Podman'i rootless mode'da, yani `sudo` olmadan, kullanacaksanız dikkat etmeniz
gereken bir konu daha var, o da bu konfigürasyon dosyaları. Eğer Podman'i
kurduğunuz sistem *local* bir Ubuntu makine ise yani kullanıcılar makinenin
üzerinde ise, `/etc/passwd` dosyasında tanımlı ise, yani `useradd` veya `adduser`
ile kullanıcıları siz elle ekliyorsanız muhtemelen bu işlemi yapmanıza gerek
yok. Eğer makineniz LDAP authentication gibi bir yöntemle merkezi bir hesap
sunucusu üzerinden kullanıcıları authenticate ediyorsa bu dosyaları elle
modifiye etmek gerekebilir.

Bu dosyalarda eksiklik olduğu zaman ile *basit* `podman` işlemlerini yapmanız
sorunsuz olabilir ama çok süre geçmeden çeşitli UID/GID hataları alabilirsiniz.

```shell
$ cat /etc/subuid
ayazar:100000:65536

$ cat /etc/subgid
ayazar:100000:65536
```

Bu ayarları değiştirdikten sonra `podman system migrate` demeke gerekebilir,
gereksiz yere demenin de bir zararı olmamalı.

Örneğin benim durumumda bir aralık bana tanımlanmış. LDAP gibi durumlarda bu
dosyalar güncellenmeyebiliyor. Bu durumda makineyi kullanacak herkes için
overlap etmeyecek aralıklar vermek gerekiyor. Aşağıdaki dokümanlarda bu konu
anlatılmaktadır.

- <https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md>
- <https://opensource.com/article/19/2/how-does-rootless-podman-work>
- <https://www.redhat.com/sysadmin/rootless-podman-makes-sense>
