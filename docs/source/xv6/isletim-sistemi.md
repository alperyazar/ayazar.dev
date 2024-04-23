---
giscus: cc32c812-9f88-4c7f-8072-c18e6d7015e6
---

# İşletim Sistemi nedir? + Unix

Adettendir, işletim sistemi nedir bir konuşalım, kısa keseceğim.

En altta donanım var, üstte kullanıcı yazılımları arada da işletim sistemi, OS.

İşletim sisteminin kalbine kernel deniyor. OS'un yaptığı temel şeylerden biri
her şeyi sanallaştırmak. Buradaki sanallaştırmayı Virtual Box, VMWare gibi
şeylerle karıştırmayın. Aslında tüm çalışan uygulamalara *Bilgisayarda bir tek
sen çalışıyorsun, tüm donanım ve kaynaklar senin, valla bak!* şeklinde yalan söylemeye
yarıyor. Yani tüm uygulamalar bütün bellek kendisindeymiş, tüm CPU
kendisindeymiş gibi çalışıyor. Yani işlemci, bellek gibi donanımların
sanallaştırılmasını sağlıyor. Bunun yanında dosya sistemi, file system FS, gibi
hizmetleri sunuyor. Ayrıca TCP/IP katmanı gibi ağ protokolleri de yine kernel
tarafından implement ediliyor. Elbette bunlar genel geçer laflar, xv6 bu kadar
yetenekli değil.

Bir önemli işlevi de donanımın soyutlanmasıdır. Yani mesela Firefox gibi bir
internet tarayıcısı üzerinde çalıştığı donanımın detaylarını pek bilmez, hangi
marka işlemci, hangi marka disk, hangi marka arayüz gibi. Bunlar işletim
sistemi tarafından soyutlanır.

Bknz: [](../sys/arayuz.md)

OS *policy* belirler fakat tipik olarak *implementation* donanım tarafından
yapılır. Yani OS, *Şu program buralara erişsin başka yere erişemesin* diye
kuralı koyar ama bu kuralı çoğu zaman donanım kontrol eder, CPU veya MMU
mekanizmaları ile. İzin verilmeyen işlemleri donanım durdurur, OS'a ispiyonlar
*Bak şu process şunu yaptı* diye. Kararı OS verir. Mesela erişmemesi gereken bir
belleğe bir process erişirse işlemci bu erişim durdurur, OS'a haber verir, OS da
tipik olarak process'i öldürür, `SIGSEGV`.

OS uygulamaları birbirinden izole eder, birbirlerinin bellek alanına eriştirmez.
Aynı donanımın (mesela ekran, yazıcı) birden fazla uygulama tarafından
paylaşılmasını sağlar.

Bir işletim sisteminin kullanışlı olması için uygulama geliştirenlere
kullanılabilir, doğru düzgün arayüzler sunması gerekiyor.

Bu arayüzler

- verimli
- basit
- güvenli
- esnek
- ileriye ve geriye dönük uyumlu
- karmaşık işlerin yapılmasına izin veren

olmalı. Bu kolay bir iş değil.

## Unix

xv6'nin Unix temelli olduğundan bahsetmiştik. Biraz Unix'e bakalım.

Unix, bilgisayar ve işletim sistemi tarihinde çok önemli bir işletim sistemidir.
*Unix felsefesi* denen bir kavram oluşmuştur (burada değinmiyorum) [^1f].
Programcılara sunduğu arayüz tasarımı o kadar tutulmuştur ki günümüzde
kullandığımız Linux, BSD, macOS, Solaris gibi işletim sistemleri (ucundan
Windows da) bu arayüz tasarımını benimsemiştir.

Altta duran **kernel**, programlara kullanabileceği servisler sunar. Çalışan her
programa **process** diyoruz. Her process'in bir bellek alanı var. Burada
çalışacak **komutlar (instructions)**, **data** ve **stack** alanı var.

Process kernelden bir şey istemek iin **system call** ya da kısaca **syscall**
yapmalı. Bir process'in çalışma zamanının bir kısmı **user space** içerisinde
geçiyor bir kısmı da **kernel space** içerisinde geçiyor. Yani bazen
(çoğunlukla) kullanıcının yazdığı kod çalışıyor ama syscall yaparsa o program o
syscall kernel fonksiyonlarını çalıştırdığı için kernel kodlarında da zaman
geçiyor.

```{figure} assets/os.png
:align: center

`shell`, `cat` bunlar kullanıcı uygulamaları, user space'te. kernel space'te bir
tek kernel var (hiç aklınıza gelmemişti di mi). user space uygulamaları syscall
yaparak kernel ile konuşuyor.
[Kaynak](https://github.com/mit-pdos/xv6-riscv-book/blob/xv6-riscv/fig/os.pdf)
```

Bknz: [](../sys/kernel-arayuz.md) ve [](../sys/merhaba-dunya.md)

User space'te çalışan kodlar çeşitli kısıtlamalara sahiptir. OS, işlemciyi
ayarlayarak bu kısıtlamaları getirir. Bazı komutlar user space'te çalıştırılamaz
ve belleğin bazı alanlarına erişilemez. Fakat kernel space içerisinde bu
kısıtlamalar genelde olmaz. Bu yüzden bazı işlerin mecburen syscall'lar ile
kernel tarafından yapılması gerekir.

Kernel bir syscall seti sunar, kullanıcı bunu kullanabilir. xv6, Unix tarzı
syscall'ları destekler. Kitapta `Figure 1.2` olarak verilmiş ben tek tek
yazmıyorum. Ama başlıcaları: **fork, exit, open, write, read, exec**

### shell

Unix, Linux gibi sistemlerde kullanıcılar tipik olarak bir shell üzerinden
işlerini yaparlar, GUI olayı ayrı elbette. BASH, ZSH, Fish vs bunlar shell
örneğidir. Shell, özel bir program değildir, o da standart bir user programdır
yani bir ayrıcalığı yoktur kernel açısından. O da tüm uygulamaların
kullanabileceği desteklenen syscall'lar ile işini yaptırır.

xv6'da Unix Bourne shell'den esinlenilmiş basit bir
[shell](https://github.com/mit-pdos/xv6-riscv/blob/riscv//user/sh.c#L1) bulunur.

## Kaynaklar

- <https://pdos.csail.mit.edu/6.828/2023/lec/l-overview.txt>
- <https://pdos.csail.mit.edu/6.828/2023/xv6/book-riscv-rev3.pdf> Chapter 1
- Ayrıca bknz: [genel kaynaklar](index.md)

[^1f]: <https://en.wikipedia.org/wiki/Unix_philosophy>
