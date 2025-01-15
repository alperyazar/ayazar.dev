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

Docker ya da Podman (compose) kullanarak aşağıdaki
`docker-compose.yml` dosyasını çalıştıralım:

```yaml
services:
  asciinema:
    image: ghcr.io/asciinema/asciinema-server:latest
    ports:
      - '4000:4000'
    volumes:
      - asciinema_data:/var/opt/asciinema
    depends_on:
      postgres:
        condition: service_healthy

  postgres:
    image: docker.io/library/postgres:14
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_HOST_AUTH_METHOD=trust
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U postgres']
      interval: 2s
      timeout: 5s
      retries: 10

volumes:
  asciinema_data:
  postgres_data:
```

Güncel compose dosyası için lütfen resmi dokümana bakınız. Ben podman'de
çalıştırdım. YML dosyasının bulunduğu dizinde `podman-compose up` ya da
`podman compose up` ya da `docker compose up` yazın. Her şey yolunda ise
<http://localhost:4000> adresinde görebilmeniz lazım.

```{important}
asciinema sunucusu ve login sistemi mail üzerinden çalışacak şekilde tasarlanmış.
Kayıt ve giriş işlemleri hep mail üzerinden gelecek linklerle sağlanıyor,
kullanıcı adı-şifre ile girilmiyor. O yüzden sisteminizde SMTP sunucus ve mail
altyapısı yoksa asciinema'yı istediğiniz gibi kullanamayabilirsiniz.
```

### `asciinema` Aracının Self-Hosted Sunucu ile Kullanımı

`asciinema` aracı varsayılan olarak <https://asciinema.org> adresine upload
edecek şekilde çalışıyor. Self-hosted kullanmak için ilk olarak bir çevre
değişken ayarlamamız gerekiyor. Self-hosted adresimiz `x` olsun, yukarıda
`http://localhost:4000` idi örneğin. `asciinema` aracının buraya upload etmesi
için `ASCIINEMA_API_URL=x` şeklinde bir environment variable tanımlamak gerekiyor.

```shell
$ export ASCIINEMA_API_URL=x
$ asciinema
```

demek gerekiyor ya da BASH kullanıyorsanız `~/.bashrc` içerisine
`export ASCIINEMA_API_URL=x` eklemek gerekiyor.

`asciinema auth` ile de authentication yapabilirsiniz.

### Self-Hosted ve Self-Signed Sertifika ile Kullanımı

Self-hosted sunucunuz HTTPS üzerinden hizmet veriyorsa `asciinema` aracını
kullandığınız bilgisayara da bu sertifikaları kurmanız lazım. Dağıtımınıza göre
self-signed sertifika nasıl kurulur araştırabilirsiniz. Dağıtımınıza bunu
eklediğiniz zaman `asciinema` da bu ayarları kullanıyor ve ek bir şey yapmanız
gerekmiyor diye hatırlıyorum.
