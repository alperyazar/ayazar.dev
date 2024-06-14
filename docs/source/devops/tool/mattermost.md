# Mattermost

```{figure} assets/mm.jpg
:align: center
:figclass: thmbnl
```

---

[Mattermost](https://mattermost.com/), özünde bir chat uygulaması,
[Slack](https://slack.com/)'e benzetebiliriz. Ücreti karşılığında doğrudan kendi
altyapıları üzerinden de Mattermost'u kullanabiliyorsunuz. Fakat self-hosted
seçeneği de mevcut. Burada ise hem `Free` hem de `Professional` paket var. Free
paketin çeşitli limitleri mevcut fakat birçok kullanım senaryosu için yeterli
olacağını düşünüyorum.

Bakınız: [Mattermost Pricing](https://mattermost.com/pricing/)

Uygulamada temelde **takımlar** ve bu takımların altında **kanallar** yani chat
odaları oluşturuyorsunuz. Örneğin her proje için takımlar veya projeler için
kanallar oluşturabilirsiniz, bu sizin yoğurt yeme şeklinize bağlı.

Kanallardaki konuşmalar saklanıyor. Kanala daha sonra eklediğiniz kişi,
geçmişteki konuşmaları okuyabiliyor.

Bunun dışında benim pek tecrübe etmediğim
[Playbooks](https://mattermost.com/playbooks/) isminde bir otomasyon altyapısı
da bulunuyor.

DevOps, CI/CD alanında yer alan bir çok araçlar [entegre
edilebiliyor.](https://mattermost.com/marketplace/) Çeşitli araçların **bot**
hesaplarını da ekleyerek birçok işi Mattermost üzerinden
[ChatOps](https://docs.gitlab.com/ee/ci/chatops/) yaklaşımı ile
yapabiliyorsunuz. Eğer entegrasyon ile uğraşırsanız Mattermost'u tüm işlerinizi
yapabileceğiniz bir merkez olarak kullanabilirsiniz.

Aracı ister web üzerinden isterse bilgisayarınıza kuracağınız kendi istemci
yazılımı ile kullanabiliyorsunuz. Kapsamlı bir araç olduğu için tüm
özelliklerini anlatmam kolay olmayacak, o yüzden niyetiniz var ise denemenizi
veya videolarını izlemenizi tavsiye ederim.

**Bedava sürümünün çeşitli kısıtları** olduğundan bahsetmiştim. Önemli
kısıtlarından biri kanallardaki konuşmaların export edilememesi, yani HTML veya
PDF gibi bir formatta kanaldaki konuşmaları çıkartamıyorsunuz. Diğer bir limiti
ise Active Directory, LDAP gibi Single Sign-On (SSO) altyapılarının ücretsiz
sürümde olmaması. Fakat ücretsiz sürüm login tarafında Gitlab ile (self-hosted
olabilir) entegre olabiliyor ve zaten çalışan bir Gitlab var ise, ki kendisi
LDAP ile entegre edilmiş olabilir, kullanıcıları buradan login edebilirsiniz. Bu
durumda dolaylı yoldan Mattermost da LDAP ile entegre edilmiş olacaktır. Bunun
dışında tipik kullanımda ücretsiz sürüm size ciddi bir kısıt getirmeyecektir.

**Alternatif olarak** da [rocket.chat](https://www.rocket.chat/) ya da
[matrix.org](https://matrix.org/) araçlarına da bakabilirsiniz. Elbette her
aracın kendine has bir kullanım tarzı, artı ve eksileri oluyor. O yüzden sizin
veya ekbinizin ihtiyaçlarına ve tarzına uygun doğru aracı bulmak için denemeler
yapmak gerekiyor.

[Docker](https://docs.mattermost.com/install/install-docker.html) veya [diğer
yollar](https://docs.mattermost.com/guides/deployment.html) ile kurulum
yapabilirsiniz.
