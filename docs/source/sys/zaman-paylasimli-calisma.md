---
giscus: eb5525de-ad64-4ec1-89ac-5eee793790c3
---

# Zaman Paylaşımlı Çalışma (Time Sharing Execution)

`33-2.23.30`

İşletim sistemlerinin kodları zamanlı paylaşımlı çalıştırması 1950'li yılların
ortalarından başlıyor. Kaynak sınırlı olduğu için daha verimli kullanım
hedefleniyor. Artık işletim sistemleri konusunda bu artık standart oldu,
işlemciler de artık bunu donanımsal destekliyor.

Proses, çalışmakta olan tüm programı kapsayan bir terim. Thread ise akış demek.
Bir process tek bir thread ile başlıyor, `main()`. İstersek başka akışlar
oluşturabiliyoruz. Eskiden thread'ler yokmuş, 90'lı yıllarda thread kavramı
çıkmış. Öncesinde birden fazla process kullanılıyormuş.

Günümüzdeki OS'ların hemen hemen hepsi *multi process* ve *multi thread* olarak
geçmektedir, ikisini de desteklemektedir. **Modern işletim sistemleri process'leri
değil, thread'leri çizelgelemektedir.**

Bugünkü masaüstü işletim sistemleri "zaman paylaşımlı (time sharing)" bir
çalışma ortamı oluşturmaktadır. Zaman paylaşımlı çalışma fikri ilk kez 1957
yılında uygulanmış ve sonra aktif bir biçimde işletim sistemlerine sokulmuştur.
Dolayısıyla bugün kullandığımız UNIX/Linux, Windows ve macOS sistemleri zaman
paylaşımlı çalışma uygulamaktadır.

Proses terimi çalışmakta olan programın bütün bilgilerini içermektedir.
Programın bağımsız çizelgelenen akışlarına "thread" denilmektedir. Thread'ler 90
yılların ortalarına doğru işletim sistemlerine sokulmuştur. Bir proses tek bir
thread'le çalışmaya başlatılır. Buna prosesin "ana thread'i (main thread)"
denir. Diğer thread'ler sistem fonksiyonlarıyla ya da sistem fonksiyonlarını
çağıran kütüphane fonksiyonlarıyla programcı tarafından yaratılmaktadır.

Zaman paylaşımlı çalışmada proseslerin thread'leri işletim sistemi tarafından
CPU'ya atanır. O thread'in CPU'da belli bir süre çalışmasına izin verilir. O
süre dolduğunda thread'in çalışmasına ara verilip başka thread benzer biçimde
CPU'ya atanmaktadır. Tabii çalışmasına ara verilen thread'in bilgileri proses
kontrol bloğuna (PCB) kaydedilmekte ve çalışma sırası yeniden o thread'e
geldiğinde thread en son kesilen noktadan çalışmasına devam etmektedir.

## Quanta ve Context Switch Kavramları

Bir thread'in zaman paylaşımlı bir biçimde çalıştırıldığı parçalı çalışma
süresine **quanta süresi** ya da İngilizce **time quantum** denilmektedir.
Quanta süresinin ne kadar olacağı işletim sisteminin tasarımına bağlıdır. Bir
thread'in çalışmasına ara verilmesi ve sıradaki thread'in CPU'ya atanması
sürecine ise İngilizce **task switch** ya da **context switch** denilmektedir.
Tabii bu işlem de belli bir zaman çerçevesinde yapılabilmektedir. Eğer quanta
süresi uzun tutulursa interaktivite azalır. Quanta süresi tutulursa zamanın
önemli kısmı "context switch" için harcanır dolayısıyla "birim zamanda yapılan
iş miktarı (throughput)" düşer. Quanta süresi çeşitli faktörlere bağlı olarak
değişebilmektedir. **UNIX/Linux sistemleri ortalama 60 ms. civarında Windows
sistemleri ortalama 20 ms. civarında bir quanta süresi uygulamaktadır.**

Zaman paylaşımlı bir sistemde kullanıcı sanki tüm proseslerin aynı anda
çalıştığını sanmaktadır. **Halbuki bu bir illüzyondur.** Aslında programlar
sürekli ara verilip çalıştırılmaktadır. Bu işlem çok hızlı yapıldığı için sanki
programlar aynı anda çalışıyormuş gibi bir algı oluşmaktadır.

````{note}

Bu videoyu (ve kanalı) beğeniyorum.

```{youtube} M9HHWFp84f0
:align: center
:width: 100%
```
````

## Preemption Kavramı

**Pekiyi bir thread CPU'ya atanmışken onun quanta süresini doldurması ve CPU'dan
kopartılması nasıl sağlanmaktadır?** İşte bu işlem hemen her zaman donanım
kesmeleri (interrupt) yoluyla yapılmaktadır. Sistem donanımında periyodik kesme
oluşturan bir mekanizma vardır. Buna "timer kesmesi" ya da UNIX/Linux dünyasında
**jiffy** denilmektedir. Eski Linux sistemleri makineler yavaş olduğu için timer
kesme periyodunu 10 ms olarak ayarlamaktaydı. Ancak makineler hızlanınca artık
bu periyot uzun süredir 1 ms biçiminde ayarlanmaktadır. Yani her 1 milisaniyede
bir aslında donanım kesmesi yoluyla kernel kodu devreye girmektedir. Bu kesme
kodu da 60 ms gibi bir zaman dolduğunda threadler arası geçiş (context switch)
yapmaktadır. Thread akışının bu biçimde quanta süresi dolduğunda donanım kesmesi
yoluyla zorla ara verilmesine işletim sistemleri dünyasında **preemptive**
işletim sistemleri denilmektedir. UNIX/Linux, Windows ve macOS sistemleri
preemptive işletim sistemleridir. Artık pek çok işlemci ailesi bu biçimdeki
donanım kesmeleri oluşturan timer devrelerini CPU'nun içerisine de dahil
etmiştir. Ancak x86 ve x64 sistemlerinde timer sistemi için genel olarak eskiye
uyum bakımından Intel 8254 ve onun ileri versiyonları olan ve ismine **PIT
(Programmable Interval Timer)** denilen devreler aktif olarak kullanılmaktadır.
Preemptive sistemlere bir alternatif olarak **non-preemptive** ya da
**cooperative multitask** da denilen sistemler bulunmaktadır. Bu sistemlerde bir
thread çalıştığında kendi rızası ile CPU'yu bırakır. Eğer CPU bırakmazsa diğer
threadler çalışma fırsatı bulamazlar. Bu patolojik duruma **diğer thread'lerin
açlıktan ölmesi (starvation)** denilmektedir. Tabii bu sistemler artık çok
kısıtı kullanılmaktadır. PalmOS, eski Windows 3.X sistemleri böyleydi.

`33-FIN`
