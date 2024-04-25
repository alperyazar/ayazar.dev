---
og:description: "Full Stack Developer var. Peki Full Stack Elektronik Mühendisi neden olmasın? Belki siz de full stack'sinizdir?"
og:image: assets/social/blog/23/fse.png
giscus: 1058066d-67b6-4ccd-9635-f944a96d10e2
---

# Full Stack Elektronik Mühendisi?

```{figure} /extra/assets/social/blog/23/fse.png
:align: center
:figclass: thmbnl
```

---

Belki dikkatinizi çekmiştir. Bir süredir kendimi, sitemdeki [profil
sayfamda](about.md) ve [LinkedIn
profilimde](https://www.linkedin.com/in/alperyazar) **Full Stack Electronics
Engineer** olarak tanıtıyorum. Adı geçtiği zaman piyasada yaptığı iş anlaşılan
**Full Stack Developer** veya **Full Stack Engineer** adında bir iş tanımı var.
Fakat Full Stack Electronics Engineer şeklinde bir **iş tanımı yok.** Bunu
aslında **uydurdum.**

Bu yazımda Full Stack Elektronik Mühendisi derken neden bahsediyorum? Neden
böyle bir tanıma ihtiyaç duydum? gibi sorulara cevap vermeye çalışacağım.
**Sizin de görüşünüzü merak ediyorum.** Haydi başlayalım...

## Full Stack Developer kimdir?

Peki Full Stack Developer kimdir, ne iş yapar? "Full Stack" kavramı, ağırlıklı
olarak web teknolojileri ile özdeşleşmiş bir kavram. Bizler web sitelerini
tarayıcılarımız (Firefox, Chrome, Edge vs...) ile görüntülüyor ve kullanıyoruz.
Tarayıcı tarafında temel olarak 3 bileşen bulunuyor: HTML, CSS ve JavaScript.
Bunun yanında ek bileşenler olabilir ama bunlar nerdeyse hiç eksik olmayanlar.
Bir web sitesinin, kullanıcı ile etkileşimi olan kısmına **front end (ön yüz)**
deniyor ve bu kısımları geliştiren kişiler de **front end developer** olarak
adlandırılıyorlar.

Web sitelerinin bir de sunucu tarafı oluyor. Arka planda koşan kodlar, arkadaki
mimari çözümler gibi altyapı tarafı bulunuyor. Bu taraf da **back end (arka yüz)**
olarak adlandırılıyor ve burada çalışan kişilere de **back end developer** deniyor.

Hem front end hem de back end yapan (en azından yapması beklenen) kişiler ise
**full stack developer** oluyorlar.

```{figure} assets/fse-a.jpg
:align: center

hehe [and then another](https://www.youtube.com/watch?v=IzyTGeoYPLk) hehe
```

## Stack nedir?

Peki stack nedir? Stack, bu kapsamda Türkçe'ye "katman" olarak çevrilebilir.
Veri yapıları konusunda da "yığın" kelimesi daha sık kullanılıyor. Bir de
biliyorsunuz Stack Overflow var, buradaki anlam "yığın" a daha yakın. Ben "Full
Stack" dediğimizde ise "katman" karşılığının daha doğru olduğunu düşünüyorum ve
bunu kullanacağım.

Yine web tarafına geri dönecek olursak, sık kullanılan terimlerden biri de
**solution stack** tir, yani *çözüm katman(lar)ı*. Back end'ten başlayacak
olursak belki bir web sitesinin en alt kısmında bir bulut bilişim (cloud)
çözümü bulunuyor, bu bir katman oluşturuyor. Belki üzerinde bir veri tabanı
çözümü oluyor, bu bir katman oluşturuyor. Üzerinde bir programlama yapılıyor,
bu bir katman. Front end'e gittikçe ve web sitesi bittikçe günün sonunda
üst üste konmuş birden fazla çözüm ile ortaya çıkmış bir ürün ortaya çıkıyor.

```{figure} assets/fse-b.jpg
:align: center

Web için örnek bir *solution stack*
```

Aslında yazılım ile ilgilenen kişiler bu katman yapısına oldukça aşinalar.
Yazılım mimarilerinde bu şekilde katmanlı tasarımlar çok sık bulunuyor. Üstteki
katman, bir alt katmandan faydalanıyor API aracılığı ile ama alttaki katmanın
nasıl çalıştığını bilmiyor veya ilgilenmiyor. Ağ işleri ile uğraşan kişilerin
çok iyi bildiği kavramlardan biri de **TCP/IP Stack** tir örneğin.

```{figure} assets/fse-c.png
:align: center

[Network Stack](https://isaaccomputerscience.org/concepts/net_internet_tcp_ip_stack)
örneği
```

Bence burayı anladık, daha fazla uzatmaya gerek yok.

## Elektronik sistemlerdeki katmanlar

Peki tipik bir elektronik sistem de aslında katmanlardan oluşmuyor mu? Her biri
ayrı bir uzmanlık gerektiren ve birbirinin çözümlerini kullanan katmanlar
aslında elektronik sistemlerde yer alıyor. "Back end" tarafından, "front end" e
doğru şöyle bir bakalım.

- **PCB (Printed Circuit Board) (Baskı Devre)** En alt katmanı boş devre kartı
  olarak düşünebiliriz. Bu alan, kendi başına bir uzmanlık içeriyor. İlgili
  kart yüksek hızlı hatlar içeriyorsa farklı kurallar ve dikkat edilmesi gereken
  noktalar, bir ADC içeriyorsa başka kurallar, bir güç kartı içeriyorsa başka
  noktalar devreye girebiliyor. Bunun yanında kartın üretim teknolojisi de
  önemli olabiliyor. Örneğin hangi tür malzeme kullanılacak? Ne tip via bulunacak?
  Pad kaplamaları ne olacak? gibi bir çok sorunun cevaplanması gerekiyor.
- **Malzeme seçimi ve devre şeması** ise bir üstteki katman olarak düşünülebilir.
  Kart tasarımında aslında tasarım sürecinde PCB tasarımına bu aşamadan sonra
  geçilse de sıralamayı bitmiş ürün açısından yaptığım için bu aşamayı ikinci
  sıraya aldım. Yoksa tasarım sürecinde PCB'den önce yer alıyor. Bu katmanda
  ise ihtiyaca uygun malzeme (component) seçimi ve bunların devre şeması ile
  bağlanması yer alıyor. İhtiyaca göre hangi tip ADC kullanılacak? Güç katı
  lineer çeviricilerden mi oluşacak yoksa SMPS topolojileri mi kullanılacak?
  FPGA boot mode'u ne olacak? Power up/down sekansı nasıl olacak gibi? bir çok
  soru da bu katmanda cevaplanıyor.
- **Gömülü Yazılım / BSP** katmanı ise artık günümüzdeki neredeyse tüm kartlarda
  var. "Akıllı eleman" olarak adlandırabileceğimiz mikrokontrolcüler, işlemciler,
  FPGA'ler, SoC'ler kartların çoğunda yer alıyor. Basit işlemci içeren kartlara,
  herhangi bir işletim sistemi desteği olmadan *bare metal* bir şekilde kod
  yazılabiliyor. Eğer biraz daha güçlü bir işlemci varsa kart, gömülü Linux
  dağıtımı çalıştırabiliyor. FPGA ise bambaşka bir dünya. Buradaki tasarımların
  yapılması ve doğrulanması ayrı bir uzmanlık alanı oluyor. Bazen de bir üst
  katmanın kullanması için bir BSP (Board Support Package) tasarlamak gerekebiliyor.
  İşte bu da üçüncü katmanımız oldu.
- **Uygulama / Görev Yazılımı** katmanı ise son katman olarak düşünülebilir.
  Özellikle altta gömülü Linux gibi bir işletim sisteminin koştuğu durumlarda,
  kartta bu işletim sisteminin üzerinde koşan C, C++, Python, Java gibi
  dillerde yazılmış, kartın yapması gereken işi yapan, diğer sistemlerle veya
  bir ara yüz ile bir kullanıcı ile "konuşan" yazılımlar bulunuyor. Bu da
  ayrı bir bilgi birikimi isteyen başka bir uzmanlık alanı oluyor. Örneğin
  gömülü Linux üzerinde koşan bir C yazılımından bahsediyorsak bir alt katman
  gömülü Linux dağıtımının oluşturulması, o dağıtımın boot etmesi gibi konular
  ile uğraşırken burada C ile program yazan kişiler altta bir POSIX uyumlu ortam
  olduğunu düşünerek sistem programlama yapabiliyorlar.

Hepsini birleştirirsek şöyle bir resim elde ediyoruz:

```{figure} assets/fse-d.png
:align: center

Elektronik sistemlerde tipik katmanlar
```

Elbette bu katmanların sayısını arttırıp detaylandırmak mümkün, ben
olabildiğince basit tutmaya çalıştım. Örneğin FPGA ve gömülü yazılım bence
**tartışmasız bir şekilde** ayrı katmanlara ayrılmalı. Ama genel olarak neden
bahsettiğimi aktarabildiğime inanıyorum.

## Full Stack Elektronik Mühendisi

Kısaca kendi kariyer yolculuğumdan bahsedip, konuya bağlayacağım.

2023 itibariyle meslekteki 11. yılım, elektronik mühendisi diplomasına
sahibim. Bu süre zarfında bahsettiğim katmanların hepsinde görev aldım. İlk
yıllarda ağırlıklı "back end" e yakın çalıştım, son yıllarda ise "front end"
tarafına daha yakınım.

> Katmanın pozisyonu, onun önemini göstermiyor, böyle bir yanılgı olmasın. Yani
> yukarıdaki katmanlar alttakilere göre daha önemli, zor vs. gibi bir durum yok.
> Bir ürünün düzgün olması için tüm katmanlar düzgün olmalı.

Çalışılan ekipte uzun süreler geçip "yaşlandıkça" ister istemez biraz danışman
rolünüz de oluyor. Ekibe yeni giren arkadaşların soru sorduğu kişi oluyorsunuz
ya da başka ekiplere görüş bildiriyorsunuz. O yüzden az ya da çok bu katmanların
hepsi ile ilgileniyorum. Kaldı ki üstteki çizimde yer almayan, yazılım
geliştirme araçlarının DevOps yaklaşımı ile CI/CD akışları ile kullanılması ve
entegre edilmesi de ilgilendiğim konular arasında.

Durum böyle olunca, kendimi nasıl tanımlayacağımı bilememeye başladım. *Digital
Design Engineer* desem, gömülü yazılım da ilgi alanımda. *Embedded Software
Engineer* desem, sayısal tasarım tarafı eksik kalıyor diye hissettiğim için ben
de kendime **Full Stack Elektronik Mühendisi** ünvanını yakıştırdım ve bunu
kullanmaya başladım. Var olmayan ve kişilerin "Bu ne ola ki?" diyebileceği ve
hatta bulunabilirliğim açısından beni kötü etkileyecek (LinkedIn'de klasik görev
tanımları ile kişiler arama yapabiliyor ama bu kelimeleri kimse yan yana
yazmayacaktır) bu tanımı ben niye bunu seçtim? Çünkü gerçekte yaptığım iş ile
yazdığım görev tanımını daha çok bağdaştırdığım için kendimi daha iyi
hissediyorum ve kişilere yaptığım işi daha iyi aktarabiliyorum (ya da bir anlam
ifade etmediği için hiç aktaramıyorum muhtemelen). Ama yine de şimdilik bu
tanımdan memnunum.

## Full Stack Electronics kavramı

Bu, "uydurma" bir kavram olsa da aslında ilk benim aklıma gelmiş
değil. Kısa bir Google araması ile Reddit
([1](https://www.reddit.com/r/embedded/comments/smi1oz/fullstack_in_embedded/),
[2](https://www.reddit.com/r/ECE/comments/ry9r66/is_fullstack_hardware_development_the_norm/)),
Quora ve
[Medium](https://olayiwolaayinde.medium.com/7-ways-to-become-a-full-stack-embedded-software-engineer-9401b591a71c)
gibi ortamlarda bu kavrama denk gelmek mümkün. Kişiler "Ben Full Stack
elektronikçi mi olmalıyım?" gibi sorular sormuş veya Full Stack Embedded
Developer gibi kavramlar kullanmışlar. Yani birileri de benzer kavramları
sorgulamış ama kendini böyle betimleyen bir kişi (benim dışımda) veya böyle
betimlenen birini arayan bir iş veren henüz görmedim.

## Tartışma

Geldik en önemli ve **sizin de görüşlerinizi merak ettiğim** kısma.

Tekrar Web dünyasına geri dönelim. Bir Full Stack Developer, bir Back End
Developer kadar Back End ya da Front End Developer kadar Front End bilebilir mi?
İdealde cevabımız hayır olacaktır. Bir kişinin bilebileceği bilgilerin
toplamının sabit olduğunu (veya sabit hızla arttığını) düşünürsek, konu çeşidi
arttıkça derinliğin azalmasını bekleriz. Peki Full Stack Developer'lar
potansiyel olarak bu kadar derinleşemiyorlarsa neden varlar? Çünkü muhtemelen
birçok kurumun veya projenin bu kadar derinliğe ihtiyacı yok. Görece basit
projeleri veya küçük işletmeleri ele aldığımızda ve işi Front End/Back End diye
iki kısıma bölersek iki farklı kişiyi çalıştırmak yerine işlerin tek bir kişiden
çıkması daha ekonomik olacaktır. Full Stack Developer'lar iş görmeseydi hala bu
kadar iş ilanı olmazdı. Öte yandan büyük projelerde ise (Google'ı düşünün) Front
End ve Back End onlarca daha ara katmana bölünmüş ve her katmanda onlarca
mühendis çalışmaktadır. Yani yapılan işe göre ne kadar bir derinlik
gerektiği değişmektedir. Full Stack Developer rolünün, tüm alanda çözüm üretmeye
çalıştığı için derinliğin (potansiyel olarak) az olduğunu düşünerek anlamsız bir
rol olduğunu düşünmek doğru olmayacaktır özetle, her projenin ihtiyacı farklı
diye düşünmek lazım.

```{figure} assets/fse-e.jpg
:align: center

"Full Stack Developer" deyince bu çıkıyor, koymadan edemedim. Herhalde arkadaşın
back end tarafı daha güçlü...
```

**Gelelim elektronik tarafına.** Türkiye'deki şirketlerin büyük çoğunluğunun da
aslında *Full Stack Elektronik Mühendisi* aradığını ve çalışanların da bu tarz
çalıştığını gözlemliyorum. En azından birkaç katmanı kapsayabilecek kişiler
arıyorlar veya böyle kişiler çalıştırıyorlar. Örneğin gömülü yazılım yapan bir
kişiden en azından temel seviye bir devre şeması okuma becerisi beklenir,
doğrudan kart tasarlamasa bile. Yine anlayacağınız benzer bir ihtiyaç durumu
burada da geçerli. Web'in aksine, kendi alanım olduğu için burada daha net
konuşabilirim. Bahsettiğim 4 katmanın hepsi gerçekten kendi içlerinde birçok
uzmanlık problemi barındırıyor. Katman sayısını belki kolaylıkla iki katına
çıkarabiliriz. Örneğin bir kişi tüm gün sadece FPGA teknolojileri ile
uğraşabilir hiç gömülü yazılıma bulaşmadan, o kadar derinleşilebilecek bir konu.
Eğer hedef ürün karmaşık değil ise bir kişi tüm katmanları halledebilir ama
hedef büyüdükçe alan uzmanlarına ihtiyaç artacaktır.

Peki **"Full Stack" Elektronik Mühendisi mi olmaya çalışmalıyız?** İşte en zor
soru, çünkü bilmiyorum. Benim cevabını en çok merak ettiğim soru da **Yurt dışı
firmalar nasıl profiller arıyorlar?** Benim gözlemlediğim, Full Stack'ten ziyade
bir alanda uzmanlaşmış kişiler arandığı.

> 🗯️ Bu yazının LinkedIn paylaşımında bu kısım ile ilgili yorumlar
> [var.](https://www.linkedin.com/posts/alperyazar_full-stack-elektronik-m%C3%BChendisi-activity-7106390221604163584-u2yG)

Elbette tek bir konuyu çok derin bilen kişi de arayan firmalar olacaktır,
hepsinden "az az" bileni de. Ben geneli merak ediyorum. Full stack gitmekteki en
büyük tehlike **[Jack of all trades, master of
none](https://en.wikipedia.org/wiki/Jack_of_all_trades,_master_of_none)**
konumuna düşmek yani her şeyden az az anlayıp bir konunun uzmanı olmamak. Böyle
bir durum da kariyer açısından dezavantaj yaratabilir. Yine de en önemlisi
bunlara çok takılmadan en motive çalışacağınız konu veya konularda çalışmaya
çalışmak bence.

Diyelim ki öğrenebileceğiniz bilgilerin toplamı 4 birim, yani kapasitemiz gibi
de düşünebiliriz. Siz 4 katmana *uniform* ayrılırsanız her katmanda 1 birimlik
uzmanlığa sahip olursunuz. Eğer bir iş için katmanlardaki ihtiyaç 1'den az ise o
işi yapabilirsiniz ama fazla ise siz tek başınıza yeterli olamazsınız. Diyelim
ki ihtiyaç katman başına 4 birim. Bu durumda da sizin gibi 4 kişi gelse yine
olmuyor çünkü 4 farklı kişi de olsa, bir katmandaki bilgi birikiminin toplamı 4
olmayacak. Herkes konunun başlarını bileceği için bir katmanda bilgi birikimi 1
olan 4 adet full stack'i bir ekibe koysak bile, o katman için bilgi birikimi
atıyorum 1.5, 2'ye çıkacaktır. 4'e çıkması için hiç kimsenin ortak bilgi
birikiminin olmaması ve birbirlerinin eksiklerini mükemmel şekilde tamamlaması
gerekiyor, bu da pek olası değil. İşte bu durumda "iş verenin" tercihi her biri
ayrı katmanda 4 birimlik bilgiye sahip olan 4 alan uzmanını o ekibe toplamak
olacaktır. Tebrikler, "bizimle değilsin". Yani özetle işler karışık, cevap
vermek gerçekten zor. Doğru cevap verebilmek için arz ve talep dengesi ile
ilgili elimizde veri olması gerekiyor.

Öte yandan 4 birimlik enerjimiz ile 4 katmanda `0 4 0 0` gibi bir uzmanlığa
sahip olmamız da çok istenen bir şey olmayabilir. Bu durumda diğer kişilerle
iletişimde problem yaşabiliriz. `0.4 3 0.4 0.2` daha tercih edilen bir dağılım
olabilir. Yani etkileşimimiz olduğu katmanlar konusunda da biraz fikir sahibi
olup, bir konuda daha uzman olmak.

Günün sonunda çözümün hibrit ekipler çıkması da olası. Full stack olan kişiler
tek başlarına yeterli olabilir ama alan uzmanları çalışıyor ise full stack
kişiler burada uzman kişilerin yaptığı işleri anlamak, iletişimi sağlamak ve
kişileri yönlendirmek adına da kilit bir rol üsteleniyor olabilir.

Bu yazıda Full Stack Elektronik kavramından bahsetmeye çalıştım. Full Stack
Elektronik Mühendisi olmayı savunuyor değilim, savunmuyor da değilim. Kariyer
problemleri çok parametreli problemler, hap gibi bilgiler vermek doğru değil,
her bireyin beklentisi farklı, karşılaştıkları farklı. Kaldı ki bu yazının amacı
da kavramı tanıtmaktı. Başka yazılarda o konulardaki görüşlerimi de
aktarabilirim.

**Varsa sizlerin de bu konudaki görüşlerini duymak isterim, yorum olarak iletebilirsiniz.**
**Kendinizi "full stack" mi hissediyorsunuz? Memnun musunuz?**

```{note}
🔥 Bu yazıyı LinkedIn'de
[paylaşmıştım.](https://www.linkedin.com/posts/alperyazar_full-stack-elektronik-m%C3%BChendisi-activity-7106390221604163584-u2yG)
Paylaşımın altında da çok değerli yorumlar bulunuyor. Eğer LinkedIn üzerinden
gelmiyorsanız,
[oraya](https://www.linkedin.com/posts/alperyazar_full-stack-elektronik-m%C3%BChendisi-activity-7106390221604163584-u2yG)
da bakmanızı öneririm.
```

*İlk yayın: 2023-09-09*
