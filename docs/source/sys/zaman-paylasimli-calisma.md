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

`34-12.10`

## Çok Çekirdekli Sistemler

**Pekiyi sistemimizde birden fazla CPU (ya da çekirdek) varsa zaman paylaşımlı
çalışma nasıl yürütülmektedir?** Aslında değişen bir şey yoktur. Bu durum tıpkı
yemek verilen bir kurumda yemeğin birden fazla koldan fazla verilmesi gibidir.
İşletim sisteminin zaman paylaşımlı çalışma için oluşturduğu kuyruğa işletim
sistemleri dünyasında **çalıştırma kuyruğu (run queue)** denilmektedir. Bu
çalıştırma kuyruğu çok CPU söz konusu olduğunda her CPU için oluşturulmaktadır.
Böylece her CPU yine zaman paylaşımlı bir biçimde çalıştırma kuyruğundaki
thread'leri çalıştırmaktadır. Yani yukarıda açıkladığımız temel prensip
değişmemektedir. Tabii burada işletim sisteminin bazı kararları da vermesi
gerekir. Örneğin yeni bir thread (ya da proses) yaratıldığında bunun hangi
CPU'ya atanacağı gibi. Bazen işletim sistemi thread'i bir CPU'nun çalıştırma
kuyruğuna atar. Ancak diğer kuyruklar daha boş hale gelirse (çünkü o sırada
çeşitli prosesler ve thread'ler sonlanmış olabilir) işletim sistemi başka bir
CPU'nun çalıştırma kuyruğundaki thread'i kuyruğu daha boş olan CPU'nun
çalıştırma kuyruğuna atayabilir. (Biz bir süper markette işin başında boş bir
kasanın kuyruğuna girmiş olabiliriz. Sonra başka bir kasadaki kuyruk çok azalmış
duruma gelebilir. Biz de o kuyruğa geçmeyi tercih ederiz. İşletim sistemi de
buna benzer davranmaktadır.) Linux işletim sistemi, Windows sistemleri ve macOS
sistemleri buna benzer bir çizelgeleme algoritması kullanmaktadır. Bir ara Linux
**O(1) çizelgelemesi** denilen bir yöntem denemiştir.[^1f] Bu yöntemde işletim sistemi
tek bir çalıştırma kuyruğu kullanıyordu. Hangi CPU'daki parçalı çalışma süresi
biterse bu kuyruktan seçme yapılıyordu.

Çok CPU'lu zaman paylaşımlı çalışmada CPU sayısı artırıldıkça total performans
artacaktır. Çünkü CPU'lar için düzenlenen çalıştırma kuyruklarında daha az
thread bulunacaktır.

```{note}
Üstteki argüman genel olarak doğrudur. Fakat [Amdahl's
law](https://en.wikipedia.org/wiki/Amdahl%27s_law) gibi kavramları da unutmamak
gerekir. Yani performans artışının artan çekirdek sayısı ile doğrusal bir
ilişkisi pratikte neredeyse hiçbir zaman olmayacaktır.
```

`34-43.30`

Burada aklımıza **kuyruk geçişleri nasıl oluyor** diye bir soru gelebilir. Yani
**hangi mekanizmalarla context switch tetikleniyor?** Çeşitli mekanizmalar
mevcut. Meseala `waitpid()` ile bloke oldun. Bir process bittiği zaman OS gidip
kuyruklara bakıyor, mesela `exit()` sistem çağrısı yapıldığı zaman. Sen eğer
sonlanan prosesi bekliyorsan unblock oluyorsun. Device driver'da ise driver
interrupt ile yapıyor benzer mekanizmayı. Socket'te `recv()` ile okuma yapmaya
çalıştığın zaman socket boşsa bloklanıyorsun. Network kartı interrupt
oluşturuyor, oradan yürüyor. `sleep(10)` derse mesela benzer şekilde
bloklanıyorsun, timer interrupt geldikçe sayıyor, dolunca thread'i salıyor.
Bunun detaylarına şu aşamada bakmıyoruz.

**Şunu da vurgulamak gerekir ki çekirdek sayısı ile çalıştırılabilir thread sayısı
arasında bir bağlantı yoktur.** İşin performans ve bellek kısımlarını bir kenara
bırakırsak tek çekirdekli bir bilgisayarda teorik olarak sonsuz adet thread
çalışabilir.

`34-50.30`

Bir de *processor affinity* diye bir kavram var. Burada bir thread'i istediğimiz
bir işlemci çekirdeğine kalıcı olarak bağlayabiliyoruz yani adeta işletim sisteminin
çizelgeleyecisini *tam otomatik* moddan *yarı otomatik* moda alıyoruz. Buna
ileride bakacağız.

## Bloke Olma, Blocking Kavramı

`34.52.00`

Zaman paylaşımlı çalışmada en önemli kavramlaran biri de **bloke olma (blocking)**
denilen kavramdır. İşletim sistemi bir thread'i CPU'ya atadığında o thread
**dışsal bir olaya ilişkin bir işlem başlattığı zaman** uzun süre bekleme
yapabileceğinden dolayı işletim sistemi o thread'i *çalıştırma kuyruğundan (run
queue)* çıkartır, *bekleme kuyruğu (wait queue)* denilen bir kuyruğa ekler.
Böylece zaten bekleyecek olan thread boşuna CPU zamanı harcamadan pasif bir
biçimde bekletilmiş olur.

Örneğin bir thread klavyeden bir şey okumak istesin. İşletim sistemi thread'i
bloke ederek çalıştırma kuyruğundan çıkartır ve onu bekleme kuyruğuna alır.
Artık o thread çalıştırma kuyruğunda olmadığından zaman paylaşımlı çalışmada
işletim sistemi tarafından ele alınmaz. Beklenen dışsal olay (örneğin klavye
okuması) gerçekleştiğinde thread yeniden çalıştırma kuyruğuna yerleştirilir.
Böylece çalışma aynı prensiple devam ettirilir.

**İşletim sistemi bekleme kuyruklarındaki thread'lere ilişkin olayların
gerçekleştiğini birkaç biçimde anlayabilmektedir.**

Örneğin bir soket okuması yapıldığında eğer sokete henüz bilgi gelmemişse
işletim sistemi thread'i bloke eder. Sonra network kartına paket geldiğinde
network kartı bir donanım kesmesi oluşturur. İşletim sistemi devreye girer ve
eğer gelen paket soketten okuma yapmak isteyen thread'e ilişkinse bu kesme
kodunda (interrupt handler) aynı zamanda o thread'i blokeden kurtarır. Ya da
örneğin `wait` gibi bir işlemde işletim sistemi wait işlemini yapan thread'i
bloke ederek wait kuyruğuna yerleştirir. Alt proses bittiğinde `_exit` sistem
fonksiyonunda bu wait kuyruklarına bu sistem fonksiyonu bakar ve ilgili
thread'in blokesini çözer. `sleep()` gibi bir fonksiyonda ise işletim sistemi
bekleme zamanını kendisi hesaplamaktadır. İşletim sistemi bekleme zamanı dolunca
thread'in blokesini çözer. Genel olarak işletim sistemleri her olay için ayrı
bir wait kuyruğu oluşturmaktadır. **Örneğin aygıt sürücüler kendi wait
kuyruklarını oluşturup bloke işlemlerini kendileri yapmaktadır. (ilginç)**

**Thread'in çalıştırma kuyruğundan çıkartılıp wait kuyruğuna alınması nasıl ve
kimin tarafından yapılmaktadır?** Böyle bir işlem user mode'da sıradan prosesler
tarafından yapılamaz. Hemen her zaman kernel mode'da işletim sisteminin sistem
fonksiyonları tarafından ya da aygıt sürücüler tarafından yapılmaktadır. Yani
thread'in bloke olması programın çalışması sırasında çağrılan bir sistem
fonksiyonu (ya da aygıt sürücü fonksiyonu) tarafından yapılmaktadır.

## I/O ve CPU Bound yani Yoğun Thread'ler

`34-1.07.30`

Thread'ler **IO yoğun (IO bound)** ve **CPU yoğun (CPU bound)** olmak üzere
ikiye ayrılmaktadır.

**IO yoğun thread'ler** kendisine verilen quanta süresini çok az kullanıp hemen
bloke olan thread'lerdir.

**CPU yoğun thread'ler** ise kendisine verilen quanta süresini büyük ölçüde
kullanan thread'lerdir. Örneğin bir döngü içerisinde sürekli hesap yapan bir
thread CPU yoğun bir thread'tir. Ancak aşağıdaki gibi bir thread IO yoğun
thread'tir:

```c
for (;;) {
  scanf("%d", &val);
  if (val == 0)
    break;
  printf("%d\n", val);
}
```

Burada bu thread aslında çok az CPU zamanı harcamaktadır. Zamanının büyük
kısmını uykuda geçirecektir. **IO yoğun ve CPU yoğun thread kavramı işletim
sistemi için değil durumun insanlar tarafından anlaşılması için uydurulmuş
kavramlardır.** Yani işletim sistemi bu biçimde thread'leri ayırmamaktadır. Bir
sistemde yüzlerde IO yoğun thread olsa bile bu durum sistemi çok fazla *yormaz.*
Ancak çok sayıda CPU yoğun thread sistemi yavaşlatacaktır.

## Örnek

`34-1.22.00`

Bir örnek yapıp, konuyu daha iyi anlamaya çalışalım. Aşağıdaki C koduna bakalım:

```{code-block} c
:lineno-start: 1
:emphasize-lines: 19-21
:caption: zaman.c

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

void exit_sys(const char *msg);

int main(int argc, char *argv[])
{
  struct timespec ts1, ts2;
  clock_t clk1, clk2;
  long long elapsed_time;

  if (clock_gettime(CLOCK_MONOTONIC, &ts1) == -1)
      exit_sys("clock_gettime");

  clk1 = clock();

  for (long i = 0; i < 1000000000; ++i)
      for (int k = 0; k < 10; ++k)
          ;

  clk2 = clock();

  if (clock_gettime(CLOCK_MONOTONIC, &ts2) == -1)
      exit_sys("clock_gettime");

  elapsed_time = (ts2.tv_sec * 1000000000LL + ts2.tv_nsec) - \
                 (ts1.tv_sec * 1000000000LL + ts1.tv_nsec);

  printf("\n[%d] clock_gettime(): %f saniye\n", (int)getpid(), elapsed_time / 1000000000.);
  printf("[%d] clock(): %f saniye\n", (int)getpid(), (double)(clk2 - clk1) / CLOCKS_PER_SEC);

  return 0;
}

void exit_sys(const char *msg)
{
  perror(msg);

  exit(EXIT_FAILURE);
}
```

Yukarıdaki kod parçası aslında iç içe boş yere dönen iki adet `for` döngüsünden
ibarettir, satır `19-21` arası. Döngünün ne kadar sürdüğü de
[clock_gettime()](https://man7.org/linux/man-pages/man3/clock_gettime.3.html)
sistem fonksiyonu ile ölçülmekte ve daha sonra yazdırılmaktadır. Bu fonksiyon,
Linux üzerinde bulunan bir sistem fonksiyonudur. Burada standard C
fonksiyonlarından olan [clock()](https://en.cppreference.com/w/c/chrono/clock)
fonksiyonunu da kullandım, farklarını göreceğiz.

Bunu `gcc zaman.c -o zaman` olarak derleyelim. Burada derleyiciye optimizasyon
yaptırmamak önemli, çünkü bu durumda boş yere dönen döngümüz derleyici
tarafından atılacaktır. BASH üzerinde çalıştıralım.

```shell
ay@2204:~/ws$ ./zaman

[3263] clock_gettime(): 10.081996 saniye
[3263] clock(): 10.074354 saniye
```

`3263` proses id değeri, ne olduğu önemli değil. Benim sistemimde kodun
çalışması yaklaşık 10 saniye sürdü. Siz kendi sisteminize göre döngülerin dönüş
sayısını ayarlayabilirsiniz. `clock_gettime()` ve `clock()` fonksiyonu yaklaşık
aynı süreyi ölçtü. Bu işlem sırasında `top`, `htop` veya eşdeğer bir araç ile
CPU kullanımı gözlemlerseniz, çekirdeklerden birinin 10 saniye boyunca (daha
doğrusu program sizde kaç saniye çalışıyorsa o süre boyunca) `%100` de durduğunu
görebilirsiniz.

Şimdi BASH'in *background process* özelliğini kullanarak aynı programı ark
arkaya çalıştıralım ve benzer gözlemleri yapalım. Alternatif olarak birden fazla
terminal açarak da bunu yapabilirsiniz ama daha zor olacaktır. `./zaman &`
komutlarını olabildiğince boşluk vermeden arka arkaya çalıştırmaya çalışın.

```shell
ay@2204:~/ws$ ./zaman &
[1] 3268
ay@2204:~/ws$ ./zaman &
[2] 3269
ay@2204:~/ws$
[3268] clock_gettime(): 9.954639 saniye
[3268] clock(): 9.747574 saniye

[3269] clock_gettime(): 10.033636 saniye
[3269] clock(): 9.725093 saniye

[1]-  Done                    ./zaman
[2]+  Done                    ./zaman
```

Gördüğünüz üzere iki proses de yaklaşık aynı sürede işlerini tamamladılar ve
her iki fonksiyon da yaklaşık aynı süreyi ölçtü. Eğer CPU kullanımını
gözlemlediyseniz bu sefer iki adet çekirdeğin `%100` olduğunu görebilirsiniz.

Şimdi aynı deneyi 3 proses oluşturarak yapalım:

```shell
ay@2204:~/ws$
[3272] clock_gettime(): 14.485561 saniye
[3272] clock(): 9.775364 saniye

[3273] clock_gettime(): 14.798592 saniye
[3273] clock(): 9.816638 saniye

[3274] clock_gettime(): 14.409517 saniye
[3274] clock(): 9.772058 saniye

[1]   Done                    ./zaman
[2]-  Done                    ./zaman
[3]+  Done                    ./zaman
```

Bu sefer farklı şeyler oldu gibi , acaba neden 🤔?

Bu testi yaptığım sanal makinamda 2 çekirdekli bir işlemci var. Aynı anda ve
*CPU bound* olan 3 adet işlem çalıştırdığım zaman bu prosesler arasında bir
"işlemci kavgası" çıkıyor. İşletim sisteminin çizelgeleyicisi 2 çekirdeği 3
proses arasında paylaştırıyor. Proseslerin yaklaşık aynı anda başlayıp aynı anda
bittiğini ve her iki çekirdeğin de tam dolu olduğunu düşünürsek yaklaşık 15
saniyeden, 2 çekirdek 30 saniyelik iş yaptı. Tek başına çalıştırdığımızda ise
bir proses 10 saniye sürüyordu. Yani `n` aynı anda çalıştırdığımız proses sayısı
ise bu deney için görmemiz gereken süre `10 * n / 2, n >= 2` iken olacaktır.

Bir diğer fark ise `clock()` ile `clock_gettime()` ile ölçtüğümüz sürelerde
çıktı. Ölçümleri neredeyse aynı noktadan alsak da (döngünün başı ve sonu), bu
iki fonksiyon bize farklı sonuçlar döndü. Çünkü,

> The clock() function returns an approximation of processor time used by the
> program.

şeklinde bir açıklama bulunmaktadır. [^2f] Yani `clock()` fonksiyonu o programın
**işlemciyi kullandığı zamanı** ölçmektedir. `clock_gettime()` ile *wall time*
yani programın toplam geçirdiği süreyi ölçtük. Her programımız yaklaşık 15
saniye çalıştı fakat sadece 10 saniye işlemciyi aktif olarak kullanabildi, 5
saniye ise bir işlemciyi kullanabilmeyi bekledi. **İşte işletim sisteminin
yaptığı context switch'in yansımasını bu şekilde gözlemeyebiliyoruz.**

Ben bütünlük olması açısından aynı anda çalıştırdığım program sayısını yani `n`
yi değiştirerek şöyle ölçümler aldım. Süreleri tam sayı olacak şekilde yuvarladım,
kabaca neye benziyor görmemiz yeterli zaten:

| `n` | `clock()` | `clock_gettime()` | `10 * n / 2` |
| --- | --------- | ----------------- | ------------ |
| 1 | 10 | 10 | N/A |
| 2 | 10 | 10 | 10 |
| 3 | 10 | 15 | 15 |
| 4 | 10 | 20 | 20 |
| 5 | 10 | 25 | 25 |
| 6 | 10 | 30 | 30 |
| 7 | 10 | 35 | 35 |
| 8 | 10 | 41 | 40 |

Gördüğünüz gibi aynı anda kaç program çalıştırırsak çalıştıralım yaptığımız iş
aslında 10 saniye sürüyor fakat işlemci çekirdeği için ortamdaki yarış kızıştıkça
programımızın tamamlanma süresi uzuyor. Bu sürenin de `10 * n / 2` şeklindeki
modelimizle de oldukça uyumlu olduğunu söyleyebiliriz.

## time Programı

Süre ölçmek için aslında `time` programını da `time ./zaman` şeklinde
kullanabilirdik.

```shell
ay@2204:~/ws$ time ./zaman &
[1] 3462
ay@2204:~/ws$ time ./zaman &
[2] 3464
ay@2204:~/ws$ time ./zaman &
[3] 3466
ay@2204:~/ws$
[3463] clock_gettime(): 15.282302 saniye
[3463] clock(): 9.940349 saniye

real 0m15.284s
user 0m9.931s
sys 0m0.011s

[3465] clock_gettime(): 15.263072 saniye
[3465] clock(): 9.950134 saniye

real 0m15.265s
user 0m9.937s
sys 0m0.015s

[3467] clock_gettime(): 15.366907 saniye
[3467] clock(): 9.959166 saniye

real 0m15.369s
user 0m9.949s
sys 0m0.012s

[1]   Done                    time ./zaman
[2]-  Done                    time ./zaman
[3]+  Done                    time ./zaman
```

Burada `real` kısmı aslında bizim `clock_gettime()` ile ölçtüğümüz, saatimizin
kronometresi ile ölçebileceğimiz zaman olmaktadır. `user`, programın CPU'yu
*user-mode* da iken kullandığı, `sys` ise *kernel-mode* da iken kullandığı zaman
olmaktadır. Bizim programımız kerneli zaman ölçümü ve ekrana yazıları basmak
dışında kullanmadığı için `sys` zamanımız 0'a yakındır. `clock()` ile ölçtüğümüz
zaman yaklaşık `user` zamanına denk gelmektedir. Genel olarak da bir programın
işlemciyi aktif olarak kullandığı tüm zamanı hesaplamak için eğer `time` dan
yardım alıyorsak `user + sys` zamanını kullanmamız uygun olacaktır. [^3f]

`34-2.02.45`

## Kaynaklar

[](kaynak.md) fakat ağırlıklı CSD notları.

[^1f]: <https://en.wikipedia.org/wiki/O(1)_scheduler>
[^2f]: <https://man7.org/linux/man-pages/man3/clock.3.html>
[^3f]: <https://stackoverflow.com/a/556411/1766391>
