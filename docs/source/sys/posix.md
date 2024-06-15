---
giscus: df2203f1-d317-47df-b174-913d50457ccc
---

# POSIX, SUS ve LSB

*Linux sistem programlama* konuşulmaya başlandığı zaman masaya hemen "POSIX"
kelimesi gelecektir, kaldı ki [bir önceki yazıda](arayuz.md) ben de bahsettim
durdum. POSIX ile beraber anılan iki terim daha var: SUS ve LSB. Bu yazıda, bu
kavramlardan bahsedeceğim.

Her bir terimin bir tarihi var. İşin doğrusu tarihleri ile şu aşamada çok ilgili
değilim. Biraz okumaya anlamaya çalıştım fakat maşallah bir Türk dizisi kadar
karışıklar. O yüzden ben de çok kısa özet geçeceğim. Dilerseniz Michael
Kerrisk'in [The Linux Programming Interface](https://man7.org/tlpi/) kitabının
ilk ünitelerine bakabilirsiniz.

70lerin sonu, 80li yılların başı Unix ve Unix türevi işletim sistemler için
altın zamanlardır. Piyasada birçok Unix türevi işletim sistemi bulunuyordu
[^1f]. `Nerede çokluk orada ...` ilkesinden yola çıkarsak bu çeşitlilik hemen
bir takım problemler doğurmuştu. Her işletim sisteminin kullanıcıya sunduğu
komutlar, programcılara sunduğu arayüzler birbirinden farklıydı. Tamam, belki
tamamen ayrı değildi ama bu farklılıklar taşınabilir programların yazılmasının
önüne geçiyordu. Bu da Unix ekosisteminde hem işletim sistemi satan hem de
program geliştiren firmalar için bir problemdi. Hemen bir standartlaşma yoluna
gidilmeye çalışıldı. İşte bu girişimlerin ilklerinden biri IEEE tarafından
yürütülen **POSIX**, or **Portable Operating System Interface** olmuştu. Resmi
olmasa da daha önceleri UNIX üreticileri `/usr/group` isimli bir topluluk
altında bir şeyleri standartlaştırmaya çalışıyordu. İlk POSIX standartı,
POSIX.1'in çalışmalarına 1984 yılında bu grup altındaki kurallar baz alınarak
başlanıldı. 1988 yılında IEEE tarafından resmi olarak tanındı ve **IEEE 1003**
kodunu aldı. 1990 yılında ise ISO tarafından **ISO/IEC 9945-1:1990** olarak
tanındı. POSIX ismi, GNU'nun yaratıcısı Richard Stallman tarafından
önerilmiştir.

POSIX, sadece C programcıları için standart arayüz fonksiyonları, API,
tanınmlamamktadır. Sık kullandığımız kabuk komutları (`cat`, `chmod`, `cp`,
`tee` gibi) ve bu komutların argümanları da POSIX tarafından
standartlaştırılmıştır. Bir işletim sisteminin **POSIX uyumlu (compliant)**
olması için çeşitli otonom kabul testlerini geçmesi gerekmektedir. Ayrıca
sertifika için iyi miktarda bir ücret de gerekmektedir. **Linux dağıtımlarının
çok büyük bir kısmı resmi olarak POSIX uyumlu değildir.** Fakat Linux
dağıtımları, POSIX kurallarını çok sıkı şekilde takip ederler. POSIX
kurallarının bir kısmı Linux tarafından gerçekleştirilmemiştir. Bazen de Linux,
POSIX'te olmayan ek özellikleri programcılara sunar.

Günümüzde **UNIX** markası IEEE'ye değil [The Open
Group](https://unix.org/trademark.html) isimli oluşuma aittir. Bu yüzden IEEE,
herhangi bir işletim sistemine resmi olarak *UNIX* ya da *UNIX uyumlu*
diyememektedir.

**SUS** ya da **Single Unix Specification** ise burada devreye girmektedir,
POSIX'e benzemektedir. Eğer geliştirdiğiniz işletim sistemine resmi olarak *UNIX
uyumlu* ya da *UNIX* demek istiyorsanız işletim sisteminizin bu standarta uyması
ve sertifikasyon süresini geçmesi gerekmektedir. Elbette sertifika için para da
ödemelisiniz...

**LSB** ya da **Linux Standard Base** karşımıza çıkabilecek bir diğer kavramdır.
Çıkış amacı POSIX ve SUS'a benzemektedir fakat Linux dağıtımlarının
standartlaşması için ortaya çıkmıştır. POSIX ve SUS'un üzerine kurulmuştur ve
daha geniş kapsamda (kütüphaneler, dosya sistemi düzeni gibi) bir standart
oluşturmaya çalışır [^2f].

**Tarihsel olarak baktığımızda tüm bu girişimlerin amacı hem kullanıcıların hem
uygulama geliştiricilerin hem de işletim sistemi geliştiricilerin daha az
korkuyla çalışabileceği uyumlu bir ortam yaratmakır.**

---

POSIX gibi standartların amacı Linux, macOS gibi Unix türevi işletim sistemlerin
arasında taşınabilir kodlar yazmaktır. Bu seride benim kişisel amacım sadece
Linux üzerinde çalışacak kodlar yazmaktır. O yüzden şahsen POSIX ile taşınabilir
kod yazmayı fazla önemsemiyorum. Konu bütünlüğü olması açısından standartlardan
biraz bahsetmek istedim.

POSIX fonksiyonlarının önemli bir kısmı en az bir sistem çağrısı yani syscall
yapmaktadır. Bir kısmı ise hiç sistem çağrısı yapmayabilir. Syscall'ların isimleri
genelde `sys_x()` formatındadır. Özetleyecek olursak:

- `foo()` isimli POSIX fonksiyonu hiç syscall yapmadan, tamam userspace'te
  kalarak çalışabilir.
- `hede()` isimli POSIX fonksiyonu bir adet `sys_hodo()` isimli syscall
  yapabilir.
- `bar()` isimli POSIX fonksiyonu `sys_baz()`, `sys_qux()` gibi birden fazla
  syscall yapabilir.

Günümüzde, son POSIX ve SUS sürümü pratikte aynı düşünülmektedir. Buradan son
standarta erişebilirsiniz. Ben ise genelde POSIX veya SUS dokümanları yerine
*man Sayfaları* na bakacağım.

## Özet

- Linux bir UNIX işletim sistemi değildir. UNIX türevi olarak bazı açılardan
  düşünülebilir. UNIX felsefesi ve yaklaşımı baz alınarak tasarlandığından UNIX
  sistemlere benzer.
- Linux sistemlerin büyük bir çoğunluğu POSIX, SUS ya da LSB uyumlu değildir.
  Pratikte çok büyük ölçüde uyumludur.

## Kaynaklar

- [](kaynak.md)
- [What is Linux? Unix? POSIX? (YouTube)](https://www.youtube.com/watch?v=hy4OeVCLGZ4)
- [What is the meaning of "POSIX"? (SO)](https://stackoverflow.com/questions/1780599/what-is-the-meaning-of-posix)
- [What exactly is POSIX? (SO)](https://unix.stackexchange.com/q/11983)
- [Officially recognized UNIX systems](https://www.opengroup.org/openbrand/register/)
- [SUS, POSIX, and Other Standards](https://dcjtech.info/topic/sus-posix-and-other-standards/)
- [POSIX Compliance Explained: Does It Even Matter In 2020 (YT)](https://www.youtube.com/watch?v=728Eu5RFoTs)

[^1f]: <https://en.wikipedia.org/wiki/List_of_Unix_systems>
[^2f]: <https://en.wikipedia.org/wiki/Linux_Standard_Base>
