# Podman'i Self Hosted Registry İle Kullanma

Podman varsayılan olarak Docker Hub'ı kullanmaktadır.

**Senaryo:** Podman kurduğumuz makine Docker Hub'a veya internete
çıkamamaktadır. Self-hosted bir registry'i ya da Docker Hub'ı proxy'leyen bir
registry'i Podman'e nasıl gösterebiliriz?

---

Podman içerisinde popüler image'ların adları aliased yapılmış şekilde duruyor.
Örneğin `podman pull ubuntu` yazarsanız `ubuntu` doğrudan
`docker.io/library/ubuntu` altında aranıyor. Gözlemlediğim kadarıyla biraz sonra
yapacağımız ayarların geçerli olması için bu alias'ları kaldırmamız gerekiyor.
Aksi taktirde Podman hep burada arıyor.  Elbette başka yöntemler de olabilir,
ben denediğimi yazıyorum. Bunun için:

```shell
cd /etc/containers/registries.conf.d
sudo mv shortnames.conf shortnames.conf.bak
```

diyerek bunu devre dışı bırakıyoruz.

Sonra `/etc/containers/registries.conf` dosyasını editliyoruz. Alttakileri
en sona ekleyebilirsiniz.

```toml
unqualified-search-registries = ["<registry>:<port>"]

[[registry]]
location = "<registry>:<port>"
insecure = true
```

`insecure=true` eğer HTTPS ile problem yaşıyorsanız veya Proxy zaten HTTP ise
anlamlı olacaktır. Problem yaşamıyorsanız koymanıza gerek yok. Bilmediğiniz
networklerde image registry'lerinden bir şeyler çekerken `true` yapmanızı
önermem.

Bu noktadan sonra problem yaşamamanız lazım.
