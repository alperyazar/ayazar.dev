---
og:description: Karta yapılan JTAG bağlantısına ağ üzerinden başka bilgisayardan erişip, kod atma, hata ayıklama gibi tüm işleri karta bağlıymış gibi yapabilirsiniz.
giscus: a993e68b-6e51-4dab-8c05-cffe1b3ea138
---

# Xilinx (AMD) Remote Debugging Neden Kullanışlı ve Nasıl Yapılır?

```{figure} assets/xilinx-remote-debugging.png
:align: center
:figclass: thmbnl
```

---

*Karta yapılan JTAG bağlantısına ağ üzerinden başka bilgisayardan erişip, kod
atma, hata ayıklama gibi tüm işleri karta bağlıymış gibi yapabilirsiniz.*

Xilinx ürünleri (FPGA ve SoC) ile çalışırken tipik olarak karta fiziksel bir
JTAG bağlantımız oluyor. [Platform
Cable](https://www.xilinx.com/products/boards-and-kits/hw-usb-ii-g.html)
("kırmızı şey") veya benzeri bir ürünü, çalıştığımız bilgisayara USB veya
Ethernet gibi bir arayüzden bağlıyoruz. Genelde de geliştirme ve hata ayıklama
yaptığımız bir adet bilgisayar bulunuyor ve kartın JTAG arayüzünü de bu
bilgisayara bağlamış oluyoruz. Bu çoğu durumda kullanışlı olsa da **böyle yapmak
zorunda değiliz.**

Xilinx'in *Remote Debugging* başlığı altında sunduğu iki adet çözüm var:
Bunlardan ilki (bu yazıda üzerine konuşacağımız), karta fiziksel bir JTAG
bağlantısı içeriyor. Fakat bu çözümde alışkın olduğumuz kurgunun aksine **bir
değil, iki adet bilgisayar var** ve bu bilgisayarlar ağ üzerinden bağlı,
detaylara geleceğiz. Diğer çözüm ise, karta fiziksel bir JTAG bağlantısı
istemeyen, adeta karta doğrudan yapılan bir Ethernet bağlantısı üzerinden "sanal
bir JTAG" bağlantısı oluşturulan Xilinx Virtual Cable (XVC) çözümü. **Bu yazıda
XVC'ye değinmeyeceğim.**

Gelin aşağıdaki duruma bir bakalım:

```{figure} assets/remote-debugging-1.png
:align: center
```

Yukarıdaki yapıda ağ üzerinden "bir şekilde" bağlı iki adet bilgisayar
görüyoruz. Bu bilgisayarların bir tanesine Platform Cable (demo kartlar
üzerindeki dahili JTAG gibi benzer bir donanım olabilir) ile kartın JTAG arayüzü
bağlı. Bu bağlantıda kartın bağlı olduğu bilgisayara **lab bilgisayarı**,
diğerine ise **geliştirme bilgisayarı** diyeceğiz.

## Peki Ama Neden?

```{figure} https://c.tenor.com/ou8FHfIO7EAAAAAd/tenor.gif
:align: center

[GIF](https://tenor.com/view/nacho-libre-why-but-gif-23595404)
```

İlk bakışta bu bağlantı çok da mantıklı gelmiyor değil mi?

**Tek bir bilgisayar üzerinden bunu yapabilirken niye iki adet bilgisayar
kullanalım?**

Evet, haklısınız. Çoğu durum için tek bilgisayar yeterli. Ama
iki bilgisayarlı setup'ın da kullanışlı olduğu durumlar var, gelin bir bakalım.

### Taşınabilirlik (Gerçek Anlamda)

```{figure} assets/remote-debugging-2.png
:align: center
```

Vivado ve Vitis'in yeni sürümleri çıktıkça ve entegreler de büyüdükçe bu
yazılımların talep ettiği disk ve RAM boyutları hızla artıyor. **Örneğin AMD
Vitis 2023.2, 64 GB RAM öneriyor.** Elbette tüm Vitis projeleri için bu kadar
belleğe ihtiyaç yok ama basit projelerde bile 8-16 GB belleğin yetersiz
kalabildiğini hemen görebiliyorsunuz. Bazı mühendisler, çalıştıkları kartı
bilgisayarlarının yanında tutabilecek kadar şanslı ama birçok mühendis de bir
sistem üzerindeki bir kartta çalışmak durumunda kalıyor. Örneğin bir sisteme
entegre edilmiş bir kart, masanızdan veya labınızdan uzak bir yerde oluyor ve o
sistemin yanına bir laptop ile gitmek gerekiyor. Görece güçlü laptoplar,
masaüstü sistemler kadar yaygın değil. Bir seçenek Vitis'i doğrudan
çalıştırabilecek güçlü laptoplar almak (maliyet açısından uygun olmayabilir,
ağır olabilir, başkasının bilgisayarında çalışmanız gerekiyor olabilir). **Diğer
bir seçenek de basit bir laptop alıp, bunu hedef karta sadece JTAG bağlantısını
almak için takmak ve ağ üzerinden daha güçlü bir bilgisayara bu JTAG
bağlantısını Xilinx'in sağladığı Remote Debugging altyapısı ile açmak.** Bu
sayede uzaktaki güçlü masaüstü bilgisayar **sanki USB'den Platform Cable
takılıymış gibi** kart üzerindeki entegreye erişebilecektir.

### Güçlü Uzak Bilgisayarlar

Senaryomuzu biraz değiştirelim ve aşağıdaki duruma bakalım. Bu çizim üzerinden
birden fazla olası durumu anlatacağım.

```{figure} assets/remote-debugging-3.png
:align: center
```

Diyelim ki sağda solda duran kartlarla uğraşmamıza gerek yok, masamızda
çalışabiliyoruz. Eğer 10 kişilik bir takımsak herkese güçlü masaüstü
bilgisayarlar almamız gerekecektir. Bunun yerine, uzaktan bağlantı ile (Windows
Remote Desktop, VNC, X2Go vs.) geliştirme yapacağımız güçlü, workstation veya
sunucu sınıfında bilgisayarlar kullanabilir, 10 adet giriş seviyesi masaüstü
veya laptop bilgisayarı takıma dağıtabiliriz. Herkese güçlü bilgisayarlar
verseydik, 10 x 64 GB = 640 GB'lık bir hafıza maliyetimiz olacaktı. Elbette
uzaktaki ortak geliştirme bilgisayarının biraz güçlü olması gerekiyor, özellikle
aynı anda birden fazla kişi çalışacaksa. Ama burada tepe kullanıma göre değil de
ortalamaya göre bir kaynak ataması yapacak olursak, örneğin 256 GB'lık bir
makina muhtemelen iş görecektir ve takıma da 16 GB'lık makinalar dağıtırsak
256 + 10 x 16 = 416 GB ile işi hallettik, takımdaki bilgisayarlar adeta bir *thin
client* oldu.

```{note}
*💲 Fun fact:* Tepe kullanıma göre değil, istatistiksel bir kullanıma göre yatırım
yaptığımız için adeta bulut bilişim sağlayıcıları (cloud provider) ve Internet
servis sağlayıcıları (ISP) gibi "para kazandık."
```

### Windows ve Linux Beraber Çalışma (Cross-Platform) 🐧 🥳 🪟

Vitis'in yanında PetaLinux ve Yocto gibi araçlar kullanıyor olabilirsiniz. Bu
araçlar zaten Linux dağıtımları üzerinde çalışmaktadır. Üstteki senaryodan devam
edecek olursak, takımın masasındaki bilgisayarlar Windows olabilir. Linux bir
ortamda Windows üzerinde çalışmak için WSL ya da sanallaştırma gibi çözümler
var. Fakat PetaLinux ve Yocto'nun görece güçlü geliştirme ve derleme ortamları
istediğini düşünürsek yine uzaktan erişilebilen güçlü bir Linux bilgisayar
mantıklı duruyor. Remote Debugging, farklı işletim sistemleri arasında da
yapılabiliyor. Yani lab bilgisayarı ve geliştirme bilgisayarı dediğimiz
bilgisayar Windows veya Linux olabilir biraz üstteki çizimde gösterdiğim gibi, 4
kombinasyon da mümkün.

### Birden Fazla Vitis/Vivado

Çalışılan proje sayısı arttıkça bilgisayarda birden fazla Vitis veya Vivado
bulundurmak gerekiyor. Fakat ne yazık ki bu yazılımların istediği disk alanları
az değil. **Örneğin Vitis 2023.2, en az 200 GB'lık bir disk alanı istiyor.**
Sadece kurduğumuz programların kapladığı alanın, yaptığımız proje sayısı
arttıkça terabyte mertebesine ulaşması çok zor değil. Onun yerine yine uzaktan
erişilebilen ve kullanılan tüm araçların kurulu olduğu güçlü geliştirme
bilgisayarları kullanılabilir. Bu durumda kendi bilgisayarımıza sadece **Vivado
Lab Solutions** kurmamız yeterli oluyor. Bunun Vivado'nun sadece Hardware
Manager'i içeren bir hali olarak düşünebiliriz. **Örneğin Vivado Lab Solutions
2022.1'in kurulmuş hali diskte sadece 6.1 GB yer kaplıyor.** Böyle kısıtlı iş
yapan bir yazılım için bence hala büyük ama Vivado'nun kendisine kıyasla oldukça
az. Eğer uzaktan erişebileceğimiz güçlü bir bilgisayarımız var ise buna
Vivado'ları kurabilir, kartı takacağımız bilgisayarlara ise sadece Lab
Solutions'ları kurup ciddi bir disk tasarrufu elde edebiliriz.

```{hint}
Eğer birden fazla Vivado/Vitis versiyonu ile çalışıyorsanız her birinin ayrı Lab
Solutions uygulamasını kurmanızı öneririm. Görece az yer kaplayan bu uygulamalar
için disk cimriliği yapıp, tasarruf yapmaya bence çalışmayın. Yakın sürümde
olanlar çalışabilse de (örn. lab bilgisayarında Vivado Lab Solutions 2022.1,
geliştirme bilgisayarında ise Vivado 2022.2 durumu iş görebilir) risk almamak
adına geliştirme ve lab bilgisayarındaki yazılım sürümlerinin aynı olmasını
sağlayın. Çoğu durumda zaten çeşitli hata ve uyarılar alacaksınız.
```

## Nasıl yapılır? 🤓

Bu sistemin çalışması için iki bilgisayarın ağ üzerinden birbirini (bir şekilde)
görebilmesi gerekiyor. Önemli olan bu imkanın ne işe yarayabileceğini
kavrayabilmek. Nasıl yapılacağı ile ilgili AMD'nin dokümanlarında veya başka
internet sitelerinde bilgiler mevcut. Ben yine de tipik bir sistemi anlatacağım,
ihtiyaçlarınıza göre değişiklikler yaparsınız.

Lab bilgisayarında Hardware Server, `hw_server`, çalışıyor olması gerekiyor. Bu
yazılımın yaptığı temel iş, bir TCP portunu (varsayılan 3121) dinlemek
(server'lar bunu yapar, client'lar bağlantıyı başlatır) ve buraya bağlanan
client'ların yaptırmak istediği işleri JTAG üzerinden yapmak. Bu yazılımı *JTAG
↔ TCP converter* gibi hayal edebiliriz. **Laf aramızda, tek bir
bilgisayarda çalışırken de aslında olan şey bu.** Yani arka planda `hw_server`
ayağa kalkıyor, 3121 nolu portu dinliyor. Vivado, Vitis, SDK, XSCT gibi
client'lar bu sunucuya 3121 portundan bağlanıyor. Tek bilgisayar durumunda bu
bağlantı ağ üzerinden değil, doğrudan o bilgisayar üzerinde yapılıyor
(`localhost`). Remote Debugging'te ise client ve server farklı bilgisayarlarda
oluyor ve bağlantı `localhost` üzerinden değil de gerçekten de ağ üzerinden
yapılıyor, işin özü bu. Eğer iki bilgisayar aynı LAN üzerinde ise ve firewall
kaynaklı bir port kısıtlaması yok ise işimiz daha kolay olacak.

### Lab Bilgisayarı

İlk olarak lab bilgisayarında Hardware Server çalıştırmamız gerekiyor. Masaüstü
ortamında yapmanın en kolay yolu o bilgisayardaki Vivado'yu (Lab Solutions veya
full Vivado olabilir) açmak ve Hardware Manager ile "bildiğimiz yoldan" JTAG
bağlantısını yapmak (`Open Target` ➔ `Auto Connect`). Ama elbette doğrudan komut
satırından da `hw_server` çalıştırabilirsiniz.

```{figure} assets/remote-debugging-4.png
:align: center
```

Burada `Tcl Console`'a bastırılan logları okursanız zaten arka planda otomatik
olarak 3121 nolu TCP portunu dinleyen bir `hw_server` başlatıldığını
görebilirsiniz.

```{figure} assets/remote-debugging-5.png
:align: center
```

Dilerseniz Windows'un görev yöneticisinden `hw_server`'ın çalıştığını
doğrulayabilirsiniz. Linux üzerinde çalışıyorsanız `ps -aux | grep hw_server`
gibi bir komutla kontrol edebilirsiniz.

```{figure} assets/remote-debugging-6.png
:align: center
```

"Yok kardeşim benim içim rahat etmedi" diyorsanız 3121 nolu portu dinleyen bu
programı PowerShell üzerinden de bulabilirsiniz (Linux'çu aslanlar da bir yolunu
bulup listeleyebilirler).

```powershell
Get-NetTCPConnection -LocalPort 3121 -State Listen | Select-Object OwningProcess, LocalAddress, LocalPort, @{n='ProcessName';e={(Get-Process -Id $_.OwningProcess).ProcessName}}
```

```{figure} assets/remote-debugging-7.png
:align: center
```

Yani artık lab bilgisayarı üzerinde `hw_server`'ın çalıştığından eminiz. Şimdi
yapmamız gereken şey, geliştirme bilgisayarından buradaki sunucu yazılıma
(`hw_server`) bağlantı yapmak.

## Geliştirme Bilgisayarı

Geliştirme bilgisayarında ise donanıma Remote Debugging ile bağlanmak
istediğimiz zaman `Open Target` ➔ `Open New Target` diyoruz, `Auto Connect`
**demiyoruz:**

```{figure} assets/remote-debugging-8.png
:align: center
```

Daha sonra `Remote server` seçeneğini seçiyoruz:

```{figure} assets/remote-debugging-9.png
:align: center
```

Sonraki pencere `Hostname` kısmına lab bilgisayarının IP'sini ya da tam adını,
`Port` kısmına da lab bilgisayarında koşan `hw_server` ın dinlediği port
numarasını yazıyoruz. Varsayılan olarak `hw_server` 3121 nolu portu dinlediği
için lab bilgisayarında `hw_server`'ı ayağa kaldırırken başka bir port numarası
vermediyseniz bu değeri bu şekilde bırakın. Eğer bu noktada hata alıyorsanız
yazının sonundaki **Hata Ayıklama** kısmına bakabilirsiniz.

```{figure} assets/remote-debugging-10.png
:align: center
```

```{note}
Ben denemek için burada aynı bilgisayarda koşan `hw_server` a bağlandım
(`localhost`). Eğer ilerleyen ekran görüntülerinde bir yerlerde
`localhost`görürseniz kafanız karışmasın lütfen. Sizde lab bilgisayarının adı
veya IP adresi yazacaktır.
```

Sonraki pencerede lab bilgisayarında takılı olan JTAG cihazını ve konuştuğu
FPGA'i görmemiz gerekiyor. `Hardware server` kısmında lab bilgisayarının
bilgileri olmalı.

```{figure} assets/remote-debugging-11.png
:align: center
```

Sonraki pencerede özet bilgileri gördükten sonra bağlantıyı kurulacaktır. Bundan
sonra Vivado'da kart sanki o bilgisayara bağlıymış gibi çalışabiliriz:

```{figure} assets/remote-debugging-12.png
:align: center
```

```{figure} assets/remote-debugging-13.png
:align: center
```

## SSH Tünel 🚇

```{figure} https://c.tenor.com/zPTX9b_cfD0AAAAC/tenor.gif
:align: center

[GIF](https://tenor.com/view/cat-cute-fat-chonky-lawd-he-coming-gif-16205308)
```

İki bilgisayar arasında port kısıtlamaları olabilir, 3121 nolu (veya benzer)
portu açamıyor, fakat [SSH](https://tr.wikipedia.org/wiki/G%C3%BCvenli_kabuk)
gibi çeşitli amaçlar ile iki bilgisayar arasında çeşitli portlardan (22 gibi)
bağlantı kurabiliyor olabilirsiniz. **Diyelim ki SSH bağlantısı kurabiliyorsunuz
fakat 3121 gibi portları açamıyorsunuz. İşte bu durumda SSH Tünel kullanarak**
`hw_server` **bağlantısını SSH üzerinden yapabiliriz.** Bu durumu kısaca
anlatayım.

```{figure} assets/remote-debugging-14.png
:align: center
```

Yukarıdaki çizimde lab bilgisayarından, geliştirme bilgisayarına SSH bağlantısı
yapıyoruz. Fakat SSH bağlantısını açarken, geliştirme bilgisayarının 3122 nolu
portuna gelecek istekleri lab bilgisayarının 3121 nolu portuna "tünelleyecek"
şekilde açıyoruz. Bunun için **SSH Reverse Tunneling** yapmalıyız. Elbette bu
senaryoda geliştirme bilgisayarında bir SSH server çalıştığını varsaydık. Bu
bilgisayar bir Linux bilgisayar ise SSH server kurmak zaten zor olmayacaktır. Bu
arada 3122 değerinin özel bir değer olmadığını de belirtmekte fayda var, başka
sayılar seçebilirsiniz. SSH bağlantısını, geliştirme bilgisayarından lab
bilgisayarına doğru yapacaksanız "klasik" **SSH Forward Tunneling**
yapmalısınız.

Lab bilgisayarınız Windows ise [Putty](https://www.putty.org/) ile tünel işlemi
yapabilirsiniz. Putty'de bunu yapmak için `Connection` ➔ `SSH` ➔ `Tunnels`
kısmına girip aşağıdaki ekran görüntüsündeki gibi ayarları yapıyoruz. SSH
bağlantısı kurulduktan sonra artık **geliştirme bilgisayarından 3122 nolu
porta yapılacak bir bağlantı, lab bilgisayarının 3121 portuna
yönlendirilecektir.**

```{figure} assets/remote-debugging-15.png
:align: center
```

Bağlantıyı yaptıktan sonra geliştirme bilgisayarında `telnet localhost 3122`
yazarak bağlantıyı doğrulayabiliriz. Eğer her şey yolunda ise geliştirme
bilgisayarında çalıştırdığımız bu komut ile, SSH tünel üzerinden lab
bilgisayarında 3121 portunda çalışan `hw_server` a bağlanabilmemiz gerekir.
Örnek bir çıktı:

```text
alper@gelistirme-bilgisayari:~$ telnet localhost 3122
Trying ::1...
Connected to localhost.
Escape character is '^]'.
ELocatorHello["ZeroCopy","MicroPython","JtagFpga","DebugCore","XicomEverest",...
```

Gelen cevap, `hw_server` ile iletişim kurabildiğimizi göstermektedir. Geliştirme
bilgisayarınız Linux ise ve Türkçe klavye kullanıyorsanız `telnet` ten `CTRL-ü`
yaparak çıkabilirsiniz. Daha sonra `telnet>` e düştüğünüz zaman `quit` yazıp
Enter'a basabilirsiniz.

Bu noktadan sonra her şey aynı aslında aynı. Sadece geliştirme bilgisayarında
`Remote server` bağlantısı yaparken, `Host name` yerine `localhost`, `Port`
yerine de `3122` yazacaksınız. SSH bağlantısı kopmadığı sürece bir problem
yaşamamanız gerekir.

Lab bilgisayarı olarak Linux kullanan *Linux'çu aslanlar* SSH bağlantısı
yaparken `ssh -R` kullanabilirler, Linux'çulara komutu söyleyecek değilim, onlar
bulurlar... 😉

## Vivado, Vitis, SDK, XSCT, `program_flash`

Xilinx'in bildiğim kadarıyla tüm araçları, ister SSH tünel ile olsun ister
doğrudan olsun, remote JTAG yani remote debugging bağlantısını destekliyor.

Örneğin `program_flash` komutu ile kalıcı kod atarken `-url tcp:<lab bilgisayarı
IP>:<port>` (normal bağlantıda `-url tcp:1.2.3.4:3121` SSH tünelde `-url
tcp:localhost:3122` gibi) parametresini geçirebilirsiniz diğer parametrelerin
yanına.

```text
program_flash -f BOOT.bin -fsbl fsbl.elf -url tcp:1.2.3.4:3121
```

gibi

Benzer şekilde Vitis ile hata ayıklama yaparken `New Target Connection` diyerek
ilgili IP ve port bilgilerini girerek uzaktaki JTAG cihazına bağlanabilirsiniz:

```{figure} assets/remote-debugging-16.png
:align: center
```

Detaylar için Vitis dokümantasyonuna bakabilirsiniz.

Benzer şekilde `xsct` ile çalışıyorsanız `connect` komutuna ilgili parametreleri
geçerek de uzak bağlantı yapabilirsiniz. Aşağıdaki örnekte SSH tünel üzerinden
bağlanıyorum:

```text
xsct% connect -host localhost -port 3122
tcfchan#0
xsct% targets
  1  xc7s25
     2  MicroBlaze Debug Module at USER2
        3  MicroBlaze #0 (Running)
xsct%
```

Diğer Xilinx araçları için de kendi dokümantasyonlarına bakabilirsiniz.

## Hata Ayıklama 🐛

Karşılaşabileceğiniz hataların bir kısmından bahsetmeye çalışacağım. Yapmaya
çalıştığımız iş temel olarak iki bilgisayar arasında ağ üzerinden bir TCP
bağlantısı oluşturmak. Bu yüzden ağ erişim problemlerinde nasıl hata ayıklamalar
yapıyorsanız o taktikleri burada da kullanabilirsiniz, burada hepsini listelemem
zor. Benim tecrübeme göre çıkan hataların tamamına yakını Xilinx araçları
kaynaklı değil, ağ kaynaklı oluyor. Ağ kaynaklı erişim problemlerinin çoğu
portları kapatan güvenlik duvarlarından veya bilgisayardaki güvenlik
yazılımlarından (Windows Firewall, Antivirüs gibi) kaynaklanıyor.

- İlk olarak geliştirme bilgisayarından, lab bilgisayarına `ping` atmayı
  deneyin. Ağ erişimini kısıtlayan çoğu donanım/yazılım genelde `ping` e izin
  verecek şekilde konfigüre edilmektedir. `ping` atabiliyor olmanız iki
  bilgisayar arasında bir iletişim kurulabildiğini göstermektedir. Eğer lab
  bilgisayarının IP adresini değil de domaindeki adını yazıyorsanız, `ping`
  işleminin başarılı olması DNS çözümlemesinin de çalıştığını gösterecektir.
- ping atabiliyorsanız ama 3121 portuna uzaktan bağlantı yapamıyorsanız lab
  bilgisayarına koşan bir güvenlik yazılımı bunu engelliyor olabilir. Kurumsal
  bir şirkette iseniz bilgi işlem, ağ üzerindeki trafiği port tabanlı engelliyor
  olabilir, kendileri ile durumu konuşun.
- SSH bağlantısı var fakat 3121 gibi "garip" portlara bağlantı yapamıyorsanız
  anlattığım SSH Tünel yöntemini deneyebilirsiniz.
- Günün sonunda temelde bu bir soket haberleşmesi olduğu için işin içinden
  çıkamıyorsanız kullandığınız işletim sisteminin ağ bağlantıları için sunduğu
  hata ayıklama araçlarını (çeşitli komutlar gibi) veya
  [Wireshark](https://www.wireshark.org/) gibi yazılımları kullanabilirsiniz.

## Arkadaşlarınıza Şaka Yapın! 😜

Ben bu özelliği zamanında çalışma arkadaşlarıma "tatlı" şakalar yapmak için
kullanıyordum. Labta çalıştığını bildiğim bir arkadaşın bilgisayarının
`hw_server` ına kendi bilgisayarımdaki Vivado'dan bağlanıp FPGA'e zamansız
resetler atarak labtan gelen *Ya kart durup duruken reset atıyor, ne alaka
ya???* serzenişlerini dinliyordum. 😈 Yine de siz kararını kaçırmayın. 😇
