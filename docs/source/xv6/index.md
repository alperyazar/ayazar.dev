---
giscus: acca3c53-47c2-463c-98c5-60203bed1d5e
---

# xv6

```{todo}
Yazı henüz tamamlanmamıştır.
```

xv6, MIT tarafından (sanıyorum günümüzde [CSAIL, Computer Science & Artificial
Intelligence Laboratory](https://pdos.csail.mit.edu/) altında duran [PDOS,
Parallel & Distributed Operating Systems Group](https://pdos.csail.mit.edu/)
tarafından, evet tarafından! [^3f]) İşletim Sistemi ders(ler)i için eğitim
amaçlı geliştirilmiş mini bir işletim sistemidir [^1f]. İlk olarak 2006 yılında
x86 işlemciler için geliştirilmiştir. Fakat 2019 yılında RISC-V mimarisine port
edilmiştir [^11f]. Orijinal x86 sürümü artık geliştirilmemektedir, x86 sürümüne
son commit 2020 yılında yapılmıştır [^2f]. Gerçi hoş RISC-V sürümüne de son
commit 2022 yılında yapılmıştır [^16f]. RISC-V için olan sürümü, `xv6-riscv`
olarak da anılmaktadır. Ben kısaca `xv6` diyeceğim.

xv6, [Version 6 Unix, v6](https://en.wikipedia.org/wiki/Version_6_Unix) dan
esinlenerek tasarlanmıştır. Meşhur [A Commentary on the UNIX Operating System,
Lions' Commentary on UNIX 6th
Edition](https://en.wikipedia.org/wiki/A_Commentary_on_the_UNIX_Operating_System)
kitabı gibi bir dokümantasyonu vardır. Yani UNIX tarzı bir işletim sistemidir.
2006 yılında xv6'nın tasarlanma amacı orijinal Unix v6'nın standart olmayan bir
C dili ile, PDP-11 gibi çok eski ve adeta tarihi eser bir makine için
tasarlanmış olmasıymış [^13f]. Adamlar da güncel bir donanımda, x86'da,
çalışabilecek ve standart bir C ile (ANSI C, 1989, eski ama standart) yazılmış
benzer bir işletim sistemi yapmışlar sınıfta göstermek için.

Ben de bir süredir bu konudaki içeriklere bakmak istiyordum. Bakarken de sitemde
notlar almaya karar verdim, belki sizler de faydalanırsınız.

## MIT İşletim Sistemi Kursları

Kısa bir arama yapınca bile MIT'de verilen farklı kodlarda birçok işletim
sistemi dersleri çıkıyor, biraz kafam karıştı. Bulduklarımı özetliyorum:

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

🤔 Zaman içerisinde neden habire kurs kodu değişmiş, pek anlamadım.

## 📚 Kaynaklar

Konu ile ilgili kaynaklar

- `xv6-riscv` kaynak kod: <https://github.com/mit-pdos/xv6-riscv>
- 📖 xv6 book, rev3: <https://pdos.csail.mit.edu/6.828/2023/xv6/book-riscv-rev3.pdf>
- `xv6-riscv-book` kaynak kod: <https://github.com/mit-pdos/xv6-riscv-book>
- `xv6` kaynak kod (x86, obsolete): <https://github.com/mit-pdos/xv6-public>
- **MIT 6.1810 Operating System Engineering** [kurs
  sayfası](https://pdos.csail.mit.edu/6.828/2023/index.html)
- **MIT OCW 6.828 Operating System Engineering, Fall 2012 Grad** [kurs
  sayfası](https://ocw.mit.edu/courses/6-828-operating-system-engineering-fall-2012/)
  xv6 var fakat x86 için.
- 📺 2014 yılında, 6.828 kursuna ait [ders
  videoları](https://www.youtube.com/playlist?list=PLfciLKR3SgqNJKKIKUliWoNBBH1VHL3AP)
  xv6 var fakat x86 için

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
