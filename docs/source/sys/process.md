# Process Kavramı

```{todo}
Yazı henüz tamamlanmamıştır.
```

> An operating system is only as good as the applications that run on it.

*Anonim ?*

İşletim sistemleri eğer üzerlerinde herhangi bir program çalıştırmazlarsa pek
de kullanışlı olmuyorlar. Sonuçta temel var oluş amaçları zaten kullanıcıların
problemlerini çözen programların sorunsuzca çalışmasını ve bu programları
geliştiren programcılara çeşitli kolalıklar sağlamak. O yüzden üzerinde bir
şey program çalıştırmayan bir işletim sistemi pek kullanışlı olmayacaktır.
Bilgisayarınızı açıp, giriş yaptıktan sonra sadece ekrana baktığınızı düşünün
herhalde pek keyif almazdınız.

İşletim sistemi üzerinde **çalışan programlara process** denilmektedir. Türkçe
karşılığı olarak *proses* (eh…) ya da *süreç* kelimelerini kullanabiliriz.
Bilgisayarımızda programlar çalıştırılabilir dosyalar olarak ikincil hafızada
yani diskimizde dururlar, birinci hafıza bellek yani RAM'dir. Biz bir programı
çift tıklayıp ya da terminalden adını yazıp çalıştırdığımızda diskte duran
çalıştırılabilir kodlar işletim sistemi tarafından diskten yüklenir ve belleğe
açılır ve daha sonra bellek üzerinde yürütülmeye başlanır. İşte bu işlem de
**process creation** yani *proses yaratma/oluşturma* olarak adlandırılır. İlgili
program artık işletim sistemi tarafından bir proses haline getirilmiştir ve
işlemci üzerinde yürütülür.

Diskte duran bir bilgisayar programı proses haline gelip yürütülmeye başlandığı
zaman kernel içerisinde birçok işlem yapılır. Kernel o anda sistem üzerinde
çalışan tüm prosesleri takip etmek zorundadır.

Eğer aynı programı tekrar çalıştırırsak yani o programdan aynı anda birden fazla
çalıştırırsak her biri ayrı proeses haline gelir. Örneğin Linux üzerinde birden
fazla terminal çalıştırdığımız zaman ve eğer BASH kullanıyorsak diskte duran BASH
programı terminal sayısı kadar çalıştırılır ve hepsi ayrı proses haline gelir.

**Prosesler bir olaylar silsilesidir.**

## Prosesler ile İlgili Komutlar

Sistem programlama açısından proses kavramına bakmadan önce Linux'u kullanan bir
kullanıcı olarak proses ile ilgili kullanabileceğimiz komutlara bir bakalım.

Bu komutların en meşhuru `ps` yani **p**rocess **s**tatus komutudur. Bu komut
birçok argüman alabilmektedir.

```shell
alper@brs23-2204:~$ ps u

USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
alper       1774  0.0  0.0 165144  5888 tty2     Ssl+ 08:56   0:00 /usr/libexec/gdm-wayland-session env GNOME_
alper       1778  0.0  0.1 225796 15616 tty2     Sl+  08:56   0:00 /usr/libexec/gnome-session-binary --session
alper       4762  0.0  0.0  14184  5504 pts/0    Ss+  09:06   0:00 /usr/bin/bash --init-file /usr/share/code/r
alper       4766  0.0  0.0  14184  5504 pts/1    Ss   09:06   0:00 /usr/bin/bash --init-file /usr/share/code/r
alper       5280  0.0  0.1  18172  8884 pts/1    S    09:10   0:00 zsh
alper       5326  0.0  0.0  16380  4436 pts/1    S    09:10   0:00 zsh
alper       5342  0.0  0.0  17784  5588 pts/1    S    09:10   0:00 zsh
alper       5343  0.0  0.0  17768  5204 pts/1    S    09:10   0:00 zsh
alper       5345  0.0  0.0  20304  3328 pts/1    Sl   09:10   0:00 /home/alper/.cache/gitstatus/gitstatusd-lin
alper       5371  3.5  0.3  42000 28192 pts/1    S+   09:10   0:31 /home/alper/.local/share/virtualenvs/ayazar
alper       7160  0.0  0.0  14156  5248 pts/2    Ss   09:24   0:00 bash
alper       7236  0.0  0.0  15424  3328 pts/2    R+   09:25   0:00 ps u
```

Örneğin `ps u` dediğimiz zaman o kullanıcıya ait çalışan prosesler hakkında
bilgi verir. Ya da `ps -e` diyerek sistemde çalışan tüm prosesleri görebiliriz.

```shell
alper@brs23-2204:~$ ps -e --no-headers | wc -l

269
```

Örneğin benim sistemimde 269 adet proses çalışıyormuş. Masaüstü ortamı kurulu,
kullanıcının interaktif olarak bilgisayarı kullandığı bir Linux sisteminde,
örneğin Ubuntu üzerinde çalışıyorsunuz diyelim, birkaç yüz adet proses görmek
şaşırtıcı değildir.

---

Bazı işletim sistemlerinde process yerine **task** da denmektedir. Bu biraz
işletim sisteminin jargonuna da bağlıdır. Örneğin FreeRTOS işletim sisteminde
*task* kelimesi kullanılmaktadır ama Linux'ta proses diyoruz.

## `task_struct`

Çalışan her proses için kernel çeşitli bilgiler tutmak zorundadır. İşte bu
bilgilerin tutulduğu yere **Process Control Block (PCB)** diyebiliriz. Yine
burada işletim sisteminden işletim sistemine isimler değişebilir ama mantık
aynıdır. *PCB ismi de bana Baskı Devre Kartı'nı çağrıştırıyor.*

Linux kernel'i C dilinde yazılmış bir programdır ve PCB veri yapısı için bir
`struct` oluşturulmuştur. Bu struct'ın adı `task_struct` oldup `sched.h` içerisinde
tanımlanmıştır. [^1f]

```c
struct task_struct {
#ifdef CONFIG_THREAD_INFO_IN_TASK
  /*
   * For reasons of header soup (see current_thread_info()), this
   * must be the first element of task_struct.
   */
  struct thread_info  thread_info;
#endif
  unsigned int      __state;

  /* saved state for "spinlock sleepers" */
  unsigned int      saved_state;
//******//
}
```

Yukarıda çok kısa bir parçasını gösterdim. `task_struct`, büyük bir veri
yapısıdır. Örneğin kernel `6.9.5` sürümünde yorumlar ve önişlemci makroları ile
beraber 820 satır yer kaplamaktadır. Ayrıca buradaki elemanların bir kısmı
sadece pointer elemanlardır yani aslında daha başka veri yapılarını da gösterici
yolu ile içermektedir. Yıllar içerisinde kernel geliştikçe `task_struct` da
büyümüştür.

---

Özellikle ilk aşamada prosesler ile ilgilendiğimiz kavramlar daha temel kavramlar
olacaktır. Bu yüzden `task_struct` içerisindeki birkaç elemana bakacağız.

## PID

*PID* dendiği zaman aklınıza *PID kontrolcü* gelebilir ama Linux dünyasında
*PID*, **P**rocess **ID** demektir. Linux üzerinde koşan her bir prosesin bir
ID değeri olmaktadır, buna PID diyoruz. PID, bir tam sayıdır. Bir PID değeri
sadece bir prosese ait olabilir. Bir başka deyişle herhangi bir t anında sistem
üzerinde bir PID'nin gösterdiği proses yalnızca bir tanedir. Bir PID birden
fazla prosesi gösteremez, bir prosesin de birden fazla PID'si olamaz. Yani uzun
lafın kısası, prosesler ile PID değerleri arasında bire bir eşleme vardır.

PID değerleri kernel tarafından **handle** olarak kullanılır. Bir veri
yapısında, değerlere erişmek için kullanılan anahtarlara handle denmektedir.
Kernel, PID değerleri ile proseslerin `task_struct` elemanlarından oluşan bir
tablo tutmaktadır. Bir PID değeri ile işlem yapılmak istendiği zaman o prosese
ait `task_struct` elemanı kernel tarafından bulunur ve ilgili işlem yapılır.
Benzer handle yapısını daha henüz pek detaylarını görmediğimiz dosya işlemlerinde
de görmüştük. Orada gördüğümüz *file descriptor* değerleri de birer handle'dır.
Yine benzer şekilde C dilinde olan `FILE` nesneleri de birer handle olarak
kullanılmaktdır.

PID değerleri ile ilgili Linux üzerinde çeşitli limitler vardır. Herhangi bir
anda PID'ler ile prosesler arasında bire bir eşleşme olacağı garanti edilmiştir.
Özellikle sunucu gibi günlerce hatta yıllarca kapanmadan çalışan sistemlerde
prosesler yaratılıp sonlanmaktadır. Bellirli bir noktadan sonra daha önceden
kullanılmış bir PID değerinin tekrar başka bir proses için kullanılması
gerekecektir. Bire bir eşleme bozulmadığı sürece bir PID değerinin birden fazla
kez kullanılması problem değildir.

```{hint}
Örneğin TC kimlik numarası da aslında bir ID değeridir fakat bir kişi ölürse
onun TC kimlik numarası yeni doğan birine verilmez, yani *universal unique* bir
değerdir. PID değerleri ise böyle değildir, tekrar tekrar kullanılabilir. Örneğin
bir bankaya gidip numeratörden numara aldığımız zaman o numaranın başka birisinde
olmaması önemlidir ve aynı zamanda yeterlidir. Ertesi gün aynı numaralar başka
kişilere de verilir, yeter ki herhangi bir anda çakışma olmasın. İşte PID de
bu açıdan TC kimlik numarasına değil banka sıra numarasına benzemektedir.
```

Linux üzerinde kernel tarafından başlatılan ilk process, **init process** olarak
adlandırılır. Kernel adeta açıldıktan yani boot ettikten sonra sistemi bu process'e
emanet eder. Geri kalan tüm işlemler bu process tarafından yapılır. Bu yüzden
init process'ler özeldir ve bunlar için sistemlerimizde *systemd*, *openrc* gibi
init sistemleri kullanırız. İşte init process'in PID değeri 1 olmaktadır. Bazen
bu processler **PID 1 process** olarak da adlandırılır. Detaylarını ileride
göreceğiz, bu init process yeni prosesler yarattıkça kernel bu oluşturulan yeni
proseslere PID numaraları atar, 2, 3, 4 gibi. Elbette bu sayının da bir sınırı
vardır. Kernel tipik olarak belli bir limit değere kadar bu sayıyı arttır ve
o limit değere ulaşınca başa döner. İşte bu limit değeri
`/proc/sys/kernel/pid_max` dosyasını okuyarak öğrenebiliriz. Örneğin benim
sistemimde

```shell
alper@brs23-2204:~$ cat /proc/sys/kernel/pid_max

4194304
```

böyle bir değer çıktı. Tipik olarak `32767` değerini de görebilirsiniz. Yine
bu dosyaya yazarak ya da başka yollardan bu limiti değiştirebilirsiniz ama
şu an konumuz değil.

````{note}
Burada Linux üzerinde **her şey dosyadır** yaklaşımını tekrar vurgulamak istiyorum.
`/proc` altında bulunan dosyaların hiçbiri diskte bulunan dosyalar değildir.
Bilgisayarımızı kapattığımız zaman sabit diskimizde böyle bir klasör yer almaz.
`/proc`, *sanal dosya sistemidir*. Bunu dilerseniz `mount` komut ile kontrol
edebilirsiniz:

```shell
alper@brs23-2204:~$ mount | grep "/proc "

proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
```

Kernel, çeşitli parametreleri kullanıcının okuyabileceği ya da yazabileceği
hale getirmek için `/proc` altında bunları birer dosyaymış gibi sergiler.
Biz buradan bir okuma yaptığımız zaman aslında diskten bir dosya okunmaz,
kernel bize döndürmek istediği değeri döndürür. İşte Linux'ta her şeyin dosya
olması böyle bir şeydir. `cat` aslında bir dosyadan okuma yapmak için
kullanılan bir komuttur, `cat dosya.txt` gibi. `cat` yine burada bir dosyadan
okuma yapmaktadır ama `cat` in bilmediği bir şey bu dosyanın aslında diskte
bir karşılığı olmadığıdır. İşte Linux üzerinde birçok arayüz standart dosya
arayüzü kullanılarak sağlanmıştır. Bu sayede `cat` gibi bir programı farklı
işler için kullanabiliyoruz. Benzer şekilde `echo` programını da `/proc` altındaki
dosyalara yazma yapmak için kullanabiliriz. Bu durumda da kernel'in ayarlarını
değiştirmiş olacağız. `/proc` altında *mount* edilmiş olan bu sanal dosya sistemi
**procfs** olarak da bilinmektedir. [Bknz](https://docs.kernel.org/filesystems/proc.html)
````

Kernel tipik olarak yeni proses yaratıldıkça `pid_max` değerine gidene kadar PID
değerlerini yeni oluşan proseslere verir. Bir proses sonlandığı zaman onun PID
değeri boşa çıkar. Ama sürekli geriye dönüp boşta değer var mı diye bakmak
kernel açısından maliyetli olacağından ileriye doğru bu sayı arttırılır.
`pid_max` değerine gelindiği zaman bu sefer başa dönülüp boşta olan değerler
aranılır. Elbette yıllarca çalışan bir sistemde `pid_max` tan kat kat fazla sayıda
proses yaratılıp, sonlandırılmış olabilir.

**Sistem üzerinde aynı anda `pid_max` tan fazla proses çalışamaz.** Diyelim ki
`pid_max` kadar proses aynı anda sistem üzerinde bulunuyor. Yeni proses yaratmak
istediğimiz zaman kernel boş bir PID değeri bulamayacağı için yeni proses
yaratılamaz. Elbette bu durum çoğu kez olası değildir ayrıca `pid_max` değeri de
arttırılabilir.

Henüz konumuz olmayan *threads* konusu ile ilgili olan bir limit değer daha
vardır:`threads-max` değeri, `/proc/sys/kernel/threads-max` dosyasından okunabilir.

`threads-max` sistemde çalışacak toplam thread sayısını limitler. Linux açısından
thread'ler ile prosesler benzer kavramlardır. Bir proses altında en az bir thread
bulunur ama birden fazla thread de bulunabilir. Buna genelde
*multi-thread programming* denir. `threads-max` toplam thread sayısını limitler.
Ama tüm process'leirmiz tek thread'li ise aslında toplam proses sayısını da
limitlemiş olacaktır.

```shell
alper@brs23-2204:~$ cat /proc/sys/kernel/threads-max
62198

alper@brs23-2204:~$ ps -e --no-headers | wc -l
281

alper@brs23-2204:~$ ps -eL | wc -l
1422
```

**Sistem üzerinde aynı anda `threads-max` tan fazla proses çalışamaz.**

Örneğin benin sistemimde `threads-max` değeri 62198'dir. Anlık olarak sistemde
281 adet proses ve 1422 adet thread çalışmaktadır. Yani ortalamada bir proses
5 adet thread'e sahiptir. Dikkat ederseniz sistemdeki `threads-max` değeri
`pid_max` tan (4194304) küçük çıktı. Yani benim açımdan aslında aynı anda
çalıştırabileceğim process değeri 62198 oluyor, o da her proseste sadece bir
thread varsa, yoksa daha düşük olacaktır.

Hazır konusu açılmışken kullanıcı limitlerinden de bahsetmek istiyorum. BASH'te
`ulimit` isimli bir built-in komut bulunuyor, `-u` flag'i ile bir sayı elde
edebiliyoruz.

```shell
alper@brs23-2204:~$ type ulimit
ulimit is a shell builtin

alper@brs23-2204:~$ ulimit -u
31099
```

Bir de bu şekilde bu komutu çalıştıran kullanıcının aynı anda çalıştırabileceği
maksimum proses sayısı (threads?) öğrenilebiliyor. [^2f] [^3f]

```text
RLIMIT_NPROC
    This is a limit on the number of extant process (or, more
    precisely on Linux, threads) for the real user ID of the
    calling process.  So long as the current number of
    processes belonging to this process's real user ID is
    greater than or equal to this limit, fork(2) fails with
    the error EAGAIN.

    The RLIMIT_NPROC limit is not enforced for processes that
    have either the CAP_SYS_ADMIN or the CAP_SYS_RESOURCE
    capability, or run with real user ID 0.
```

 Yani `pid_max` ya da
`threads-max` tan daha düşük bir değerse, ilgili kullanıcı bu sayı ile
limitlenecektir. Ama `root` kullanıcı tipik olarak bir limite takılmaz.

Bu tip konular çoğunlukla *Linux System Administrator* başlığı altında yer
almaktadır ama ucundan bakmış olduk.

## `getpid()` ve `pid_t`

Bir program çalıştığı zaman bir proses oluştuğunu söylemiştik. Peki biz kendi
programımız bir proses olup çalıştığı zaman bu prosese atanan PID değerini
programın içinden alabilir miyiz? Cevabımız evet.

`getpid()` fonksiyonu tam olarak da bu işe yarayan bir fonksiyon. [^4f]

```c
#include <unistd.h>

pid_t getpid(void);
```

Bildirimi `unistd.h` içerisinde bulunan bu fonksiyon bir parametre almıyor ve
`pid_t` türünden bir geri dönüş değerine sahip. `pid_t` bir `typedef` yani tür
eş ismi. `pid_t` işaretli bir tam sayı yani **signed integer** fakat *tam* olarak
hangisi olacağı (`short`, `int`, `long` vs) belirtilmiş değil, implementation
defined. [^5f] Örneğin x86 32-bit sistemlerde bunun `int` olacağını söylemek
pek yanlış olmaz. **POSIX standartlarına göre `pid_t` en fazla `long int`
büyüklüğünde olabilir.** [^6f] [^7f] [^8f] Bu detaylar C dilinde
`pid_t` yi veri kaybı yaşamadan ya da işaret hatası yapmadan kullanabilmemiz için
önemli.

**Özetle, `pid_t` en fazla `long int` büyüklüğünde olabilecek işaretli bir tam
sayı türüdür.**

```c
#include <unistd.h> //getpid(), pid_t
#include <stdio.h>

int main(void)
{
  pid_t pid;
  pid = getpid();

  printf("PID = %ld\n", (long)pid); (void)fflush(stdout);
  (void)getchar();
  return 0;
}
```

```{todo}
Burada kaldım.
```

## Kullanıcı ve Grup ID

Linux sistemleri çok kullanıcılı sistemlerdir. Her bir kullanıcının bir
kullanıcı adı vardır. Fakat işletim sistemi seviyesinde kullanıcı takipi isimler
ile değil numalar üzerinden yapılır. Buna *kullanıcı numarası*, **user ID** ya
da çoğu zaman **UID** adı verilir. Benzer şekilde kullanıcıların ait olduğu çoğu
grup ya da gruplar vardır. Güncel sistemlerde kullanıcılar tipik olarak birden
fazla gruba dahildir. Grupların da bir numarası vardır, **group ID** ya da
**GID** olarak belirtilir. Kullanıcı/grup ID mekanizması Linux üzerindeki temel
izin kontrol mekanizmasını oluşturur. Dosya sistemindeki her klasör ve dosyanın
da ID bilgileri vardır ve bir kullanıcının dosya sistemi üzerinde yapabileceği
şeyler (dosya yaratma, silme, var olan dosyayı değiştirme, okuma gibi) bu ID'ler
üzerinden kontrol edilir.

[^1f]: <https://elixir.bootlin.com/linux/v6.9.5/source/include/linux/sched.h#L748>
[^2f]: <https://man7.org/linux/man-pages/man2/getrlimit.2.html>
[^3f]: <https://www.reddit.com/r/bash/comments/m709uv/what_does_ulimit_apply_to>
[^4f]: <https://man7.org/linux/man-pages/man2/getpid.2.html>
[^5f]: <https://man7.org/linux/man-pages/man3/id_t.3type.html>
[^6f]: Advanced Programming in the UNIX Environment, 3rd Edition
[^7f]: <https://unix.stackexchange.com/a/150980/285808>
[^8f]: <https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_types.h.html>
