---
giscus: 2610ab7f-7904-4bff-aa0a-e654a9142f3f
---

# Bellek Düzeni

```{todo}
Yazı henüz yazım aşamasındadır.
```

İşletim sistemi, bizim için teme 3 farklı donanımı soyutlar: **işlemci**,
**bellek** ve **disk.**

**Disk**, dosya sistemleri ile soyutlanır. Aslında *ham* veri depolama cihazı olan
diskler dosya, klasör nedir bilmez. Bunlar dosya sisteminin sağladığı bir
soyutlama katmanıdır. Dosya sistemleri de tipik olarak kernel tarafında
gerçekleştirilir.

**İşlemci**, farklı thread'ler arasında paylaştırılır. Thread, işlemcide koşan bir
iş parçasıdır yani CPU'da yürütülen komutlar. Bir sistemde aynı anda aktif olan
birden fazla thread olsa da her thread sanki sadece kendisi varmış gibi
işlemciyi kullanır. İşlemci kaynağının birden fazla thread arasında
paylaştırılması işi işletim sisteminin bir görevidir. Linux gibi modern işletim
sistemlerinin çoğu, *multi-thread* programlamayı desteklerler yani kernel
desteği ile multi-thread çalışan programlar mümkün olabilmektedir. Process ise
aslında işletim sisteminin uydurduğu bir bileşke veri yapısıdır. Yani bir
programın thread'leri + file descriptor table + bellek yapılandırması bir
process oluşturur. xv6'da bir process sadece tek bir thread'ten oluşabilir.
Elbette kullanıcı kendi kodu ile multi-thread ilüzyonu yaratabilir fakat xv6
kernelinin böyle bir desteği yoktur. O yüzden xv6 ile ilgili konuların çoğunda
`thread` ve `process` kelimeleri aynı anlama geliyor gibi düşünülebilir. Fakat
process, thread dışında başka veri yapıları da içeren bir yapıdır.

```{figure} assets/bellek-duzeni-process.jpg
:align: center

Genel process mantığı bu şekildedir. Buradaki çizimde multi-thread bir uygulama
gösterilmiş, 3 adet thread barındıran. Fakat xv6 bir process içerisinde
bir adet thread destekliyor. Bu çizim xv6 için tamamen doğru değil fakat genel
mantık olarak doğru bir gösterim.

`struct proc` un en önemli elemanlarından birinin file descriptor table olduğundan
bahsetmiştik. Burada da File Handle olarak ilgili tablodan satırlar gösterilmiş
aslında. Elbette xv6'daki `struct proc` içerisinde başka elemanlar da var.

[Kaynak](https://ops-class.org/slides/2016-01-30-processes/deck.html#slide-48)
```

**Bellek**, yani RAM, işletim sistemi üzerinde koşan tüm programlar yani
process'ler ve kernel tarafından aslında paylaşılıyor. Biz bir programı
çalıştırdığımız zaman program, işletim sistemi tarafından program belleğe
açılıyor yani yükleniyor. Belleğin tam olarak hangi adresine yükleneceği ise
işletim sisteminin vereceği bir karar. Çünkü bilgisayarda bir adet bellek olduğu
ve bu belleğin birden fazla program tarafından paylaşılması gerektiği için
burada her programa önden bir yer ayırmak mümkün değil, adeta bellek alanları
çalışan programlara kiralanıyor. **Fakat programın belleğin neresine açılacağını
derleme sırasında bilmesi mümkün değil.** Ayrıca aynı program işletim sistemi
tarafından belleğin farklı taraflarına yerleştirilebilir. Diyelim ki program
içerisinde temel load/store instruction'ları yani komutları (ya da buyruk) var.
Bu komutların belleğin neresine erişeceğini bilmesi lazım. Fakat programın
belleğin gerçekten neresinde olduğunu bilmezse bu komutların adresleri ne
olacak? Buna bir çözüm bulunması gerekiyor **bu çözümün donanımsal olarak
işlemci tarafından da desteklenmesi lazım.** İşte işletim sisteminin yaptığı
önemli soyutlamalardan biri de belleğin soyutlanmasıdır. Tipik olarak programlar
tüm belleğin onlara ait olduğunu düşünürler ve bir **sanal bellek** e erişirler,
**virtual memory**. Sanal belleğe olan yazma/okuma işlemlerinin gerçek, fiziksel
belleğe yani RAM entegresine dönüşümü, gerçekte belleğin neresine erişileceği
konusu işlemci desteği ile sağlanır. Bu yazıda belleğin soyutlanmasına yani
sanallaştırılmasına bakacağız. xv6'ye gelmeden önce probleme biraz daha genel
bakalım. Bu konular ile ilgili olan anahtar kelimeler: **virtual memory**,
**paging**, **swapping**, **segmentation**

---

Yapabileceğimiz kötü çözümlerden biri çalışabilecek her program için fiziksel
olarak bellekte belli bir alanı rezerve etmek ve bunu programa derleme
aşamasında söylemek olurdu. Yani diyecektik ki 0-512MB arası firefox'a ait,
512MB-1G arası VS Code kullansın gibi. Elbette burada birçok problem var,
kesinlikle ölçeklenebilir bir çözüm değil. Kullanılmayan programlar için rezerve
edilmiş bellek, başka programlar tarafından kullanılamıyor, bu en temel
problemlerden biri. Bu yöntemin çalışmayacağı belli oldu.

---

## Kaynaklar

- <https://www.youtube.com/watch?v=Hr8Dck3re3k>
- <https://www.youtube.com/watch?v=o91pWKnr0Mk>
- <https://www.youtube.com/watch?v=SGeDjFoYAis>
- <https://en.wikipedia.org/wiki/Memory_segmentation>
- <https://lass.cs.umass.edu/~shenoy/courses/fall12/lectures/Lec12.pdf>
- <https://pages.cs.wisc.edu/~remzi/OSTEP/vm-segmentation.pdf>
