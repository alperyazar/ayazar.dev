---
giscus: acca3c53-47c2-463c-98c5-60203bed1d5e
---

# 🇻6️⃣ xv6

xv6, MIT tarafından ( günümüzde [CSAIL, Computer Science & Artificial
Intelligence Laboratory](https://pdos.csail.mit.edu/) altında duran [PDOS,
Parallel & Distributed Operating Systems Group](https://pdos.csail.mit.edu/)
tarafından, evet tarafından! [^3f]) İşletim Sistemi ders(ler)i için eğitim
amaçlı geliştirilmiş mini bir işletim sistemidir [^1f]. Unix baz alınarak
tasarlanmıştır. İlk olarak **2006** yılında x86 işlemciler için
geliştirilmiştir. Fakat **2019** yılında RISC-V mimarisine port edilmiştir
[^11f]. Orijinal x86 sürümü artık geliştirilmemektedir, x86 sürümüne son commit
2020 yılında yapılmıştır [^2f]. Gerçi hoş RISC-V sürümüne de son commit 2022
yılında yapılmıştır [^16f]. RISC-V için olan sürümü, `xv6-riscv` olarak da
anılmaktadır. Ben kısaca `xv6` diyeceğim.

xv6, [Version 6 Unix, v6](https://en.wikipedia.org/wiki/Version_6_Unix) dan
esinlenerek tasarlanmıştır. Meşhur [A Commentary on the UNIX Operating System,
Lions' Commentary on UNIX 6th
Edition](https://en.wikipedia.org/wiki/A_Commentary_on_the_UNIX_Operating_System)
kitabı gibi bir dokümantasyonu vardır. 2006 yılında xv6'nın tasarlanma amacı
orijinal Unix v6'nın standart olmayan bir C dili ile, PDP-11 gibi çok eski ve
adeta tarihi eser bir makine için tasarlanmış olmasıymış [^13f]. Adamlar da
güncel bir donanımda, x86'da, çalışabilecek ve standart bir C ile (ANSI C, 1989,
eski ama standart) yazılmış benzer bir işletim sistemi yapmışlar sınıfta
göstermek için.

## MIT İşletim Sistemi Kursları ve Tarihçesi

Kısa bir arama yapınca bile MIT'de verilen farklı kodlarda birçok işletim
sistemi dersleri çıkıyor, biraz karışık, bulduklarımı özetliyorum.

MIT'de uzun yıllar boyunca işletim sistemi kursu olmamış (çok ilginç, adamlar
*exokernel* diye bir çekirdek icat ediyorlar ama kusları mı yok?). İlk kurs 2002
yılında açılmış [^17f]. Bulabildiğim kadarıyla açılan bu kursun kodu ve adı
**6.097 Operating System Engineering**[^15f]. Bu kursta öğrencilere Lion's
Commentary kitabi ile klasik meşhur Unix v6 anlatılıyormuş. Labların sonunda da
öğrenciler x86 için Jos isminde bir
[exokernel](https://en.wikipedia.org/wiki/Exokernel) yazıyorlarmış. Derste hem
Unix görmek hem de exokernel yazmak geniş bir örnek görmek açısından iyi
oluyormuş. Fakat Unix v6 1975 yılında çıkan PDP-11 için yazılmış bir işletim
sistemi. Meşhur K&R C kitabının 1978 yılında yayınlandığını unutmamak lazım.
İşletim sisteminin hem *tarihi eser* bir donanım, PDP-11 için olması hem de
standart C'den önce, hatta K&R C'den önce (ilk C standartı olan ANSI C 1989
yılında yayınlanmıştır) olan bir C ile yazılmış olması öğrenciler açısından pek
motive edici olmuyormuş. Lablardan dolayı da x86'nın detaylarını öğrenmeleri
gerekiyormuş. Bu tarz problemlerin önüne geçmek için 2006 yılında Unix v6'dan
esinlenerek ANSI C'de x86 için Xv6 işletim sistemi yazılmış.

Yeniden eskiye doğru kurs tarihçesi ile ilgili bulabildiğim bilgiler:

- **6.1810 Operating System Engineering** Güncel durumda xv6 bu derste
  kullanılıyor, lisans dersi. [Link](https://pdos.csail.mit.edu/6.1810/2023/)
- **6.5810 Operating System Research Seminer** Grad dersi, xv6 ile ilgisi yok.
  Bulunsun diye koydum. [Link](https://kaashoek.github.io/65810-2023/)
- **6.S081 Operating System Engineering** Anladığım kadarıyla 6.1810'un eski
  kodu. 6.S081 MIT kurs kataloğunda *special subject* olarak geçiyor, yani bir
  *placeholder* kod gibi [^4f]. 2021 yılına kadar bu isim kullanılmış [^5f]
  [^7f] 2022 yılında kod 6.1810 olmuş gibi anladım [^6f] [^8f]. Her iki kursun
  da sitesi neredeyse aynı.
- **6.828 Operating System Engineering** Bu da 6.S081'den önceki kod sanırım.
  2018'e kadar 6.828 imiş [^9f], 2019'da 6.S081 kodu undergrad OS kursu olmuş,
  6.828 ise grad seminer kursu olmuş [^10f]. Öncesinde 6.828 grad kursu diye
  anlıyorum [^14f]. 2019'da 6.S081'in açılmasıyla xv6 da x86'dan, RISC-V'a
  geçmiş [^11f]. Kursun içeriği köklü değiştiyse `S` kodlu *special subject ?*
  kurs yapılmış. Birkaç sene sonra da 6.1810 yapılmış olabilir. ODTÜ EE'de de
  benzer bir şey oluyordu. Mesela yeni açılan grad dersleri EE7123 gibi
  açılıyor, bir süre sonra EE799 gibi 3 haneli oluyordu, neyse. 6.828'in sitesi
  en eski 2003 yılına kadar gidiyor bulabildiğim kadarıyla [^12f]. Elbette o
  zamanlar xv6 falan yok. İlk xv6'dan, 6.828'in 2006 sitesinde bahsediliyor
  [^13f].
- **6.097 Operating System Engineering** Bu da en eski kurs sanırım bu konudaki.
  İlk olarak 2002 yılında verilmiş [^15f]. 2003 yılında 6.828 var demiştik zaten
  [^12f], herhalde 6.097'in yerine 6.828 geçmiş.

🤔 Zaman içerisinde neden habire kurs kodu değişmiş, pek anlamadım. Günümüzdeki
güncel kurs numarası **6.1810**

## Diğer Üniversitelerdeki Kurslar

xv6'nın [Wikipedia sayfasına](https://en.wikipedia.org/wiki/Xv6) göre bu işletim
sistemi birçok üniversitede ders içeriği olarak kullanılmış. Benim dikkatimi
çeken kurslardan biri [Harvey Mudd College](https://www.hmc.edu/)'ta Neil Rhodes
tarafından verilen CS 134 oldu, çünkü YouTube'ta [videoları
var.](https://www.youtube.com/playlist?list=PLJJuQ2QZniL7LjcUD2G2BkizgxsfCkTSE)
Sanıyorum x86 için.

## Kitap Hakkında

xv6'nın bir de ders için yazılmış bir kitabı bulunuyor, bağlantısını aşağıda
`Kaynaklar` altında verdim. Bu kitapta temel işletim sistemi kavramları ve
xv6'nın tasarımından bahsediliyor. Kitabın yazarlarını araştırmak istedim.

**Russ Cox** Google çalışanı, Go dilinin yaratıcılarından biri. Daha fazla bir
şey demeye gerek yok sanırım 🙂. [Kişisel sitesi](https://swtch.com/~rsc/) ve
[YouTube](https://www.youtube.com/@rscgolang)

**Frans Kaashoek** MIT'de hoca. [Kişisel
sitesi](https://people.csail.mit.edu/kaashoek/)

**Robert (Tappan) Morris** MIT'de hoca. [Kişisel
sitesi](http://nil.lcs.mit.edu/rtm/) ve
[Wikipedia](https://en.wikipedia.org/wiki/Robert_Tappan_Morris). Wikipedia'ya
göre meşhur [Hacker News](https://news.ycombinator.com/) servisini sağlayan [Y
Combinator](https://en.wikipedia.org/wiki/Y_Combinator) oluşumunun
partnerlerinden birisiymiş. [Morris
worm](https://en.wikipedia.org/wiki/Morris_worm) u yapan kişi. Ayrıca babası
[Robert Morris](https://en.wikipedia.org/wiki/Robert_Morris_(cryptographer))
60'lı yıllarda Bell Labs'ta Multics ve Unix üzerine çalışmış, babadan oğla geçen
işletim sistemi sevdası adeta.
[Derslerde](https://pdos.csail.mit.edu/6.828/2023/schedule.html), `rtm` olarak
geçen kişi bu abimiz olmalı.

---

**Adam Belay** Kitap yazarlarından değil ama
[derslerde](https://pdos.csail.mit.edu/6.828/2023/schedule.html) `ab` olarak
geçen kişi bu kişi olmalı. [Kişisel sitesi](http://www.abelay.me/)

## 📝 Notlarım

xv6'ya bir süredir bakmak istiyordum. Sitemin bu kısmında aldığım notları
sizlerle paylaşacağım. **Aksini belirtmediğim sürece xv6-riscv üzerinden devam
edeceğim.** Aldığım notlar:

```{toctree}
---
maxdepth: 1
glob: true
---
merhaba-dunya.md
isletim-sistemi.md
user-space-giris.md
gdb-ile-debug.md
```

## 📚 Kaynaklar

Konu ile ilgili kaynaklar

- `xv6-riscv` kaynak kod: <https://github.com/mit-pdos/xv6-riscv>
- 📖 xv6 book, rev3:
  <https://pdos.csail.mit.edu/6.828/2023/xv6/book-riscv-rev3.pdf>
- `xv6-riscv-book` kaynak kod: <https://github.com/mit-pdos/xv6-riscv-book>
- `xv6` kaynak kod (x86, obsolete): <https://github.com/mit-pdos/xv6-public>
- `xv6-annotated` x86 olan için ama iyi: <https://github.com/palladian1/xv6-annotated>
- **MIT 6.1810 Operating System Engineering** [kurs
  sayfası](https://pdos.csail.mit.edu/6.828/2023/schedule.html)
- **MIT OCW 6.828 Operating System Engineering, Fall 2012 Grad** [kurs
  sayfası](https://ocw.mit.edu/courses/6-828-operating-system-engineering-fall-2012/)
  xv6 var fakat x86 için.
- **HMC CS 134 Operating Systems** MIT'nin kursu benzeri bir yapısı var fakat
  [sitede daha çok içerik var](https://www.cs.hmc.edu/~rhodes/cs134/schedule.html)
  Fakat x86 için, RISC-v değil.
- <https://ops-class.org/> genel olarak sevdiğim ve baktığım bir site
- <https://wiki.osdev.org/Xv6> OSDev
- 📺 2014 yılında, 6.828 kursuna ait [ders
  videoları](https://www.youtube.com/playlist?list=PLfciLKR3SgqNJKKIKUliWoNBBH1VHL3AP)
  xv6 var fakat x86 için
- 📺 Neil Rhodes, CS 134 [ders
  videoları](https://www.youtube.com/playlist?list=PLJJuQ2QZniL7LjcUD2G2BkizgxsfCkTSE)
  fakat x86 xv6 anlatılıyor.
- 📺 [Harry H. Porter III](http://web.cecs.pdx.edu/~harry/),
  [hhp3](https://www.youtube.com/@hhp3) tarafından hazırlanmış [xv6-riscv
  videoları](https://www.youtube.com/playlist?list=PLbtzT1TYeoMhTPzyTZboW_j7TPAnjv9XB)
- 📺 [Low Byte Productions](https://www.youtube.com/@LowByteProductions)
  tarafından hazırlanmış xv6-riscv üzerine birkaç
  [video](https://www.youtube.com/playlist?list=PLP29wDx6QmW4Mw8mgvP87Zk33LRcKA9bl)

### RISC-V

- [RISC-V An Overview of the
  ISA](http://web.cecs.pdx.edu/~harry/riscv/RISCV-Summary.pdf) by hhp3

İlginç geldi: MIT CSAIL'den çıkan
[spin-offlar](https://www.csail.mit.edu/about/spin-offs)

[^1f]: <https://en.wikipedia.org/wiki/Xv6>
[^2f]: <https://github.com/mit-pdos/xv6-public>
[^3f]: <https://www.youtube.com/watch?v=oBJjjvBAAhY>
[^4f]: <https://catalog.mit.edu/search/?P=6.S081>
[^5f]: <https://pdos.csail.mit.edu/6.S081/2021/schedule.html>
[^6f]: <https://pdos.csail.mit.edu/6.S081/2022/schedule.html>
[^7f]: <https://pdos.csail.mit.edu/6.1810/2021/>
[^8f]: <https://pdos.csail.mit.edu/6.1810/2022/>
[^9f]: <https://pdos.csail.mit.edu/6.1810/2018/>
[^10f]: <https://pdos.csail.mit.edu/6.1810/2019/>
[^11f]: <https://pdos.csail.mit.edu/6.1810/2019/xv6.html>
[^12f]: <https://pdos.csail.mit.edu/6.1810/2003/>
[^13f]: <https://pdos.csail.mit.edu/6.1810/2006/overview.html>
[^14f]: <https://ocw.mit.edu/courses/6-828-operating-system-engineering-fall-2012/>
[^15f]: <https://pdos.csail.mit.edu/archive/6.097/>
[^16f]: <https://github.com/mit-pdos/xv6-riscv>
[^17f]: <https://pdos.csail.mit.edu/6.828/2012/xv6.html>
