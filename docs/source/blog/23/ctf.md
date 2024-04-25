---
og:description: "Çalıştığım kurumda düzenlenen CTF (Capture the Flag) yarışmasına katılıp ikinci oldum. Bu bahaneyle kısaca CTF'ten bahsediyorum."
giscus: 084882d4-cb61-4009-b9ac-e303a14e8fae
---

# İlk CTF Deneyimim

```{figure} assets/ctf.jpg
:align: center
:figclass: thmbnl
```

Bu yazım oldukça kişisel. Katıldığım ve ikinci olduğum CTF yarışması
hakkında tarihe not düşmek için bu yazıyı hazırladım. Yarışma sonrasında
çevremdeki arkadaşlardan sorular gelmişti, benzer soruları yanıtlamak ve süreci
de anlatmak istedim.

Bahsettiğim yarışma 2022 yılında, çalıştığım şirkette, sadece şirket
çalışanlarının katılımına açık olacak şekilde düzenlenmişti. Yarışmanın amacının
çalışanların bilgi güvenliği konusundaki farkındalığının hem kullanıcı hem de
tasarımcı olarak arttırılması olduğu iletilmişti. Yarışmanın üzerinden aylar
geçtikten sonra bu yazıyı yeni hazırlayabildim.

Yarışmanın benim için önemli bir tarafı da **CTF** yani **Capture the Flag**
konseptini bana tanıtmış olmasıdır. Yarışma sayesinde bu kavram ile tanıştım ve
yarışmada yer almaktan da çok keyif aldım.

O zaman ilk olarak bu kavrama bir bakalım.

## CTF (Capture the Flag)

Capture the Flag (CTF) aslında fiziksel bir aktivite olarak oynan bir
[oyun](https://en.wikipedia.org/wiki/Capture_the_flag). Ama burada bahsi geçen
oyun daha farklı. CTF, bilişim dünyasında güvenlik temalı bir oyun olarak
biliniyor. **Aslında "hacker"lık oyunu olarak özetleyebilirim.** Çeşitli sorular
bulunuyor. Burada, oyunda kurgulanan sistemlerdeki açıkları bularak ulaşmamanız
gereken bir yere erişmeye çalışıyor, görmemeniz gereken bir bilgiyi görmeye
çalışıyorsunuz. Eriştiğiniz bilgi de "kaptığınız" *flag* oluyor. Buradaki flag
rastgele oluşturulmuş bir metin olabilir (UUID formatında bir metin gibi). Bu
metni gireceğiniz bir yarışma sistemi oluyor. Doğru bildikçe puan alıyorsunuz.
Bu şekilde farklı alanlardaki becerilerinizi tartan birçok oyun bulunuyor.

```{note}
ℹ️ Belirttiğim gibi ben de bu kavramla yeni tanıştığım için yazdıklarımı işin
uzmanı yazıyormuş gibi algılamayın. Sadece öğrendiklerimi ve tecrübe ettiklerimi
paylaşıyorum.
```

Buradaki oyunlar ise çeşitli konular üzerine olabiliyor. Örneğin, web temelli
sistemlerdeki açıklar (veritabanı açıkları gibi), Linux güvenliği ile ilgili
açıklar, binary exploit, kriptografi ya da tersine mühendislik gibi konular yer
alabiliyor. Benim katıldığım yarışmada hatırladığım kadarıyla 20-25 arası soru
vardı. Elbette tüm sorular aynı zorluk seviyesinde değil. Soruyu bilen sayısı ne
kadar az olursa o sorudan kazanılan puan da o kadar yüksek oluyor. Eşitlik
durumu olursa da ilk cevaplayan kişi önde oluyor(muş). Bizdeki konu başlıkları
da yine hatırladığım kadarıyla temelde PHP, MySQL, Python Flask ve Django, GIT,
temel kriptoloji, Linux sistem güvenliği gibi konular üzerineydi, unuttuklarım
olabilir.

CTF yarışmaları sektörde gördüğüm kadarıyla yaygın. Firmaların iyi eleman
bulması için de güzel bir yol. Bu yarışmalara bireysel ya da takım olarak da
katılabiliyorsunuz. Bir kısmı da iki aşamalı olabiliyor, ikinci aşaması da
fiziksel olarak düzenlenen hackathon tarzı etkinlikleri kapsıyor. Konu ilginizi
çektiyse aşağıdaki bağlantılara bakabilirsiniz. Kısa bir arama ile birçok sonuç
bulmak mümkün:

- <https://ctf.hacker101.com/>
- <https://capturetheflag.withgoogle.com/>
- <https://ctf101.org/>

## "Ee, peki sen nasıl ikinci oldun?"

İlk CTF deneyimim olduğundan bahsetmiştim. Bu durumda ikincilik kazanmam ilk
bakışta biraz ilginç geliyor elbette. Kurum içi bir etkinlik olduğu için,
katılımcı sayısının dışarıya açık bir yarışmaya göre düşük olmasının muhakkak
buna faydası olmuştur. Ama bu konularla "resmi" olarak ilgilenmesem de en
azından kavramsal olarak duymamış olduğum konular da değillerdi. Bir elektronik
mühendisiyim ama ilk öğrendiğim programlama dillerinden biri de (en azından
uğraştığım) PHP olmuştu. O yıllarda kendime bir web sitesi yapmaya çalışıyordum
ve o zamanlar Wordpress gibi sistemler pek yaygın değildi, belki de yoktu, belki
sadece Drupal vardır? ya da haberim yoktu, neyse. Kendi kendime Apache + PHP +
MySQL kurup, *dinamik* bir web sitesi oluşturmaya çalışıyordum. Yani önce
altyapıyı kodlayıp, sonra içeriği oluşturmaktan bahsediyorum. E hali ile SQL
injection gibi kavramlara aşina olmuştum (`mysql_real_escape_string` 😎 ).
Ayrıca sağdaki soldaki sitelere başarılı/başarısız injection denemlerim de
olmuştu 🙄. Yani konulara o kadar uzak değildim. Yarışmada çok ciddi zaman
harcadım konu hoşuma gidince, biraz da "vura kıra" ilerledim diyebilirim 😄 .
Daha sonradan bu vesileyle tanıştığım arkadaşlardan öğrendim ki soruların bir
kısmını çözen ya da kolaylaştıran çeşitli araçlar varmış. Benim bunlardan
haberim olmadığı için çoğu soruyu daha fazla çaba ile daha uğraştırıcı bir
şekilde çözmüşüm. Belki de bu daha çok keyif almamı sağlamıştır. Günün sonunda
soruların hepsini yapabildim ama tamamlama süremden dolayı ikinciliği elde
edebildim.

Özetle, bilgi birikiminiz az olsa bile yeteri kadar arama motoru kullanıp zaman
harcayarak ilerlemek mümkün olabiliyor bence, yeter ki keyif alın ve merak
duyun (her işte olduğu gibi)…

## Son Sözler

Bu yarışma aracılığı ile CTF kavramından haberdar olduğum için çok mutluyum.
Yarışma süreci de çok keyifli geçti benim için. Bu sayede yeni kişilerle de
tanışma fırsatı buldum. Bu yüzden emeği geçen herkese teşekkürlerimi sunmak
isterim.

Her ne kadar bu yarışmadan sonra tekrar bu konuda bir çalışma yapmamış olsam da
kesinlikle boş bir zamanımda geriye dönüp bakmak isteyeceğim bir alan oldu,
müthiş keyif aldım. Sizin de biraz ilginiz varsa internette herkese açık olan
çeşitli yarışmaları en azından "tadımlık" denemenizi şiddetle tavsiye ederim.
YouTube üzerinde de arama yaparsanız neye benzediğini çok daha iyi görebilirsiniz.
Bu konuda birçok kanal mevcut.

Bir ürün tasarlarken de tavsiye edilen akış, bilgi güvenliği ile ilgili
kaygıların tasarım sürecinin en başından beri yer almasıdır. Tasarım bitmeye
yaklaştıktan sonra "hadi şimdi bunu güvenli yapalım" demek verimli bir yöntem
olarak önerilmiyor. Benim gibi elektronik mühendislerinin de uğraştığı gömülü
sistemler de gittikçe en az bir ağ bağlantısı bulunduran ya da gömülü Linux
çalıştıran sistemler haline dönüşüyorlar. Bu yüzden, gömülü sistemler ile
uğraşan kişilerin de en azından temel seviyede bu kavramlar ile ilgilenmesinin
yararlı olacağını düşünüyorum.

```{note}
Yazıdaki kurum ve kişi isimleri bir nebze de olsa gizliliği kourmak için
gizlenmiştir.
```

Tarihe bir not daha:

```{note}
🔥 Bu yazı Ankara'nın muhtemelen 2023'teki en sıcak gününde,
[RaspberryPi 400](https://www.raspberrypi.com/products/raspberry-pi-400/)
üzerinde hazırlanmıştır. Sadece 2W tükettiği için odadaki sıcaklığa artışı
minimal oluyor kendilerinin, sıcaklara birebir…
```

*İlk yayın: 2023-08-15*
