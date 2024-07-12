# Gitlab Private Container Registry, Runner Konfigürasyonu

Aşağıdaki senaryoyu düşünelim:

```text
- grup
  - container
  - a
  - b
  - ...
```

Burada `grup` isimli bir Gitlab proje grubu içerisinde `container`, `a`, `b`
gibi repolar vardır. `container` isimli repo içerisindeki *Container Registry*
altında ekip tarafından diğer repoların CI/CD akışları için kullanılacak, ekip
tarafından oluşturulmuş çeşitli container imajları bulunmaktadır. `grup` atına
eklenmiş docker üzerinde container çalıştıran çeşitli runner'lar bulunmaktadır.
Grup ve altındaki tüm repolar *private* tır.

**Sorun: `grup` altına eklenmiş olan runner'lar CI/CD işleri için `container`
altındaki docker imajlarını nasıl kullanacaklar?**

Eğer `container` reposu veya altındaki container registry *public* olursa,
runner'lar zaten buradaki imajları çekebilmektedir. Sorun, container
registry'nin private olduğu durumda çıkmaktadır.

---

Bununla ilgili gitlab üzerinde dokümanlar varsa da bana takip etmesi nedense
biraz zor geldi, bazı çözümlerin çalışmadığını düşünüyorum ya da ben
beceremedim. Örneklerin çoğu da `dind` yani, *Docker in Docker* içindi. Çalışan
bir konfigürasyonu paylaşıyorum:

Öncelikle private registry'ye runner'ların login olabilmesi için projelerin
`.gitlab-ci.yml` dosyalarında değişiklik yapmak istemiyorum. CI/CD yazan
geliştiricilerin, altta yatan altyapı hakkında bilgi sahibi olmaya çalışması
verimsiz bir senaryo oluşturmaktadır. Geliştiriciler, `.gitlab-ci.yml`
içerisinde nasıl `image: ubuntu:22.04` diyerek Docker Hub'ta bulunan imajları
patır kütür çekiyorlarsa private imajları da `image: private-ekip-imajı:latest`
gibi çekebilmelidir, ya da buna en yakın şekilde. Private imajları çekebilmek
için `.gitlab-ci.yml` dosyalarını `docker login` vs ile modifiye etmek bana
doğru gelmiyor, ölçeklenebilir değil. O yüzden runner'ları konfigüre edeceğim.

## Access Token Oluşturulması

İlk olarak `container` reposuna gidip `Settings → Access Tokens` sayfasına
geliyoruz. Burada `Add new token` diyerek yeni bir token oluşturuyoruz. `Token
name` kısmına `x` girdik diyelim, bir son tarih girmek zorundayız, uzun bir
tarih girebilirsiniz ama sonsuz ömürlü token oluşturamıyoruz. Gitlab
dokümanlarından anladığım kadarıyla role'ün en az `Reporter` olması gerekiyor
ama `Guest` ile olmuyor mu cidden diye kontrolü deney yapmadım, o yüzden role
kısmını `Reporter` seçelim, `scope` olarak da **sadece** `read_registry` rolünü
seçiyoruz. Bunu oluşturduktan sonra bir `token` ımızı alıyoruz, değerine `token`
diyelim. Sayfayı kapatmadan kaydetmeyi unutmayın, tekrar erişim şansı olmuyor.

```{figure} assets/gitlab-private-registry-runner-token.png
:align: center

Sonuç
```

Token name, `x` ve token'ı `token` kullanarak runner'ları konfigüre edeceğiz.
Runner'larımız bu bilgiyi kullanarak private registery'imize login
olabilecekler.

## Runner Konfigürasyonu

Burada kullanabileceğimiz birkaç yol var. `docker` komutlarını çalıştırdığımız
bir makineye gidip şöyle bir çalışma yapabiliriz:

```shell
ayazar@abc:~$ sudo docker login <gitlab registry URL>
Username: x
Password:
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credential-stores

Login Succeeded
```

Bu sayede `x` ve `token` kullanarak login olabildiğimizi gördük. Şimdi
`/root/.docker/config.json` dosyasına bakalım:

```json
{
    "auths": {
            "<gitlab registry URL>": {
                    "auth": "<base64-token>"
            }
    }
}
```

Bu formatta bir içerik görmemiz lazım. Bu json dosyasını aldıktan sonra istersek
ve içerisinde başka içerik yoksa `/root/.docker/config.json` dosyasını
silebiliriz.

Şimdi bu bilgileri runner konfigürasyonuna girmemiz gerekiyor.

```toml
# ...

[[runners]]
  environment = ["DOCKER_AUTH_CONFIG={\"auths\":{\"<gitlab registry URL>\":{\"auth\":\"<base64-token>\"}}}"]

# ...
```

şeklinde bir girdi yapmamız gerekiyor. Bu noktadan sonra runner'ımız private
repolara erişebiliyor olacaktır.

---

`<base64-token>`, `x:token` yazısının Base64 olarak kodlanmış halidir. Eğer bir
yerden `docker login` yapamıyorsanız `printf "x:token" | openssl base64 -A` ile
`<base64-token>` ı elde edebilirsiniz.

Runner'ı restart atalım.

## Test

Bu noktadan sonra `image: <gitlab registry URL>/imaj:tag` şeklindeki işleriniz
runner üzerinde çalışabilecektir.

Çalışan işlerinizin loglarında

```text
Using Docker executor with image <gitlab registry URL>/imaj:tag ...
Authenticating with credentials from $DOCKER_AUTH_CONFIG
```

gibi bir ifade görmelisiniz. `config.toml` dosyasına yazdığımız bilgiler,
`$DOCKER_AUTH_CONFIG` isimli bir environment variable'ın içerisine
yazılmaktadır.
