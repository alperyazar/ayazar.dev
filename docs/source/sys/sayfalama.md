---
giscus: 6a1008ca-7e11-47f9-8fd8-03cfefb43916
---

# Sayfalama, Paging

`34-2.02.45`

Modern, kapasiteli mikroişlemcilerde **sayfalama (paging)** denilen önemli bir
mekanizma vardır. Örneğin Intel işlemcileri bu sayfalama mekanizmasına **80386**
modelleriyle birlikte sahip olmuştur. ARM Cortex A serisi
işlemcilerin de bu mekanizmaları vardır. Itanium, PowerPC gibi işlemcilerde de
sayfalama mekanizması bulunmaktadır. **Genellikle koruma mekanizmasına sahip
işlemciler sayfalama mekanizmasına da sahip olurlar. Ancak koruma mekanizmasına
sahip olduğu halde sayfalama mekanizmasına sahip olmayan işlemciler de vardır.**

```{note}
Bu notlar kapsamında çalıştığımız işlemcilerin hem sayfalama hem de koruma
mekanizmasının olduğunu düşünebiliriz.
```

Sayfalama mekanizması güçlü işlemcilerde bulunan bir mekanizmadır. Genel olarak
mikrodenetleyicilerde bu mekanizma yoktur. Örneğin ARM'ın Cortex M serisi
mikrodenetleyicilerinde sayfalama mekanizması bulunmamaktadır. Ayrıca
işlemcilerdeki bu sayfalama mekanizması aktif ve pasif duruma
getirilebilmektedir. Yani işlemci sayfalama mekanizmasına sahip olduğu halde
sistem programcısı bu mekanizmayı açmayabilir ve kullanmayabilir. İşlemciler
reset edildiğinde sayfalama mekanizması genel olarak pasif durumdadır. İşletim
sistemleri bazı ön hazırlıkları yaptıktan sonra bu mekanizmayı açmaktadır.

`34-2.12.55`

Sayfalama mekanizmasında fiziksel RAM aynı zamanda **sayfa (page)** denilen
ardışıl bloklara ayrılır. Sayfa uzunluğu sistemden sisteme hatta aynı işlemcide
işlemcinin modundan moduna değişebilir. Ancak en tipik kullanılan sayfa uzunluğu
**4096 (4K) byte**tır. Gerçekten de bugün Linux, Windows ve macOS sistemleri
4K'lık sayfalar kullanmaktadır. Sayfalama mekanizması etkin hale getirildiğinde
işlemci RAM'deki her sayfaya bir sayfa numarası karşılık getirir. Örneğin ilk
4096 byte 0'ıncı sayfaya, sonraki 4096 byte 1'inci sayfaya ilişkindir. Sayfalar
bu biçimde ilk sayfa 0'dan başlatılarak ardışıl biçimde numaralandırılmaktadır.
Yani günün sonunda bellekteki her byte aslında bir sayfa içerisinde bulunur.

`34-2.27.10`

```{note}
İşlemcide sayfalama yani sanal adresler açıldığı zaman reset sonrası kernel
kodları da (sistem fonksiyonları, driver vs) sanal adresler kullanmaktadır.
Bildiğim kadarıyla user space sanal adreslerde çalışsın ama kernel sanal adres
kullanmasın gibi bir durum pratikte yok.
```

## Sanal Adres, Virtual Address

`34-2.31.15`

**Bir program içerisinde kullanılan yani derleyicinin ürettiği adresler aslında
gerçek fiziksel adresler değildir.** Bu adreslere **sanal adresler (virtual
addresses)** denilmektedir. Derleyiciler kodları sanki geniş bir RAM'de program
tek başına çalışacakmış gibi üretmektedir. Yani örneğin 32
bit Linux sistemlerinde (Windows ve macOS'te de böyle) sanki derleyiciler
program 4 GB bellekte 4 MB'den itibaren tek başlarına yüklenecekmiş gibi bir kod
üretmektedir. Her program derlendiğinde aynı biçimde kod üretilmektedir. Çünkü
derleyicinin ürettiği bu adresler sanal adreslerdir. **Pekiyi her program aynı
biçimde sanki RAM'in 4 MB'sinden başlanarak ardışıl bir biçimde yüklenecekmiş
gibi bir koda sahipse bu programlar nasıl çalışmaktadır?**

```{todo}
Burada neden 4 MB diye sorabiliriz. Aslında tipik olarak
*null pointer dereference* koruması için böyle şeyler yapılıyor. 4 MB biraz
bu iş için büyük, tam sebebini öğrenince burayı güncelle.
```

## Sayfa Tablosu, Page Table

İşte sayfalama mekanizmasına sahip olan CPU'lar aslında **sayfa tablosu (page
table)** denilen bir tabloya bakarak çalışırlar. Sayfa tablosu sanal sayfa
numaralarını fiziksel sayfa numaralarına eşleyen bir tablodur. Sayfa tablosunun
görünümü aşağıdaki gibidir:

```text
Sanal Sayfa No              Fiziksel Sayfa No
...                         ...
4562                        17456
4563                        18987
4564                        12976
...                         ...
```

Şimdi Intel işlemcisinin aşağıdaki gibi bir makine kodunu çalıştırdığını düşünelim:

```text
MOV EAX, [05C34782]
```

Burada makine komutu bellekte `0x05C34782` numaralı adresten başlayan 4 byte
erişmek istemektedir. İşlemci önce bu adres değerinin kaçıncı sanal sayfaya
karşılık geldiğini hesaplar. Bu hesap işlemci tarafından oldukça kolay bir
biçimde yapılır. Sayı 12 kere sağa ötelenirse (4K sayfa boyutundan dolayı) başka
bir deyişle sayının sağındaki 3 hex digit atılırsa bu sanal adresin kaçıncı
sanal sayfaya karşılık geldiği bulunabilir:

```text
05C34782 >> 12 = 05C34 (sanal sayfa no, decimal 23604)
```

Artık işlemci sayfa tablosunda `0x5C34` yani decimal `23604` numaralı girişe
bakar. Sayfa tablosunun ilgili kısmı şöyle olsun:

```text
Sanal Sayfa No  (decimal/hex)   Fiziksel Sayfa No (decimal/hex)
...                         ...
23603 (5C33)                      47324 (B8DC)
23604 (5C34)                      52689 (CDD1)
23605 (5C35)                      29671 (73E7)
...                         ...
```

Burada `23604 (5C34)` numaralı sanal sayfa `52689 (CDD1)` fiziksel sayfasına
yönlendirilmiştir. **Pekiyi işlemci hangi fiziksel adrese erişecektir?** İşte bizim
sanal adresimiz 05C34782 idi. Bu adres iki kısma ayrıştırılabilir:

```text
05C24   Sanal sayfa no (hex)
782     Sayfa offset'i (hex)
```

Bu durumda işlemci aslında fiziksel RAM'de `52689 (CDD1)`uncu fiziksel sayfanın
`1922 (782)` byte'ına erişecektir. O zaman gerçek bellekteki erişim adresi
`52689 (CDD1) * 4096 (1000) + 1922 (782)` olacaktır.

---

**Burada özetle anlatılmak istenen şey şudur:** İşlemci her bellek erişiminde
erişilecek sanal adresi iki kısma ayırır: `Sanal Sayfa No` ve `Sayfa Offset'i`.
Sonra sayfa tablosuna giderek sanal sayfa numarasına karşı gelen fiziksel sayfa
numarasını elde eder. O fiziksel sayfanın `sayfa offet'i` ile belirtilen
byte'ına erişir. Örneğin şöyle bir fonksiyon çağırmış olalım:

```c
foo();
```

Derleyicimiz de şöyle bir kod üretmiş olsun:

```text
CALL 06F14678  (hex)
```

Burada `06F14678`, `foo()` fonksiyonunun sanal adresidir. Derleyici bu adresi
üretmiştir. Ancak program çalışırken işlemci bu adresi ikiye ayırır (hex olarak
konuşacağız):

```text
06F146      Sanal Sayfa No (hex)
678         Sayfa Offseti (hex)
```

Sonra sayfa tablosuna gider ve `06F146` sayfasının hangi fiziksel sayfaya
yönlendirildiğini tespit eder. Bu fiziksel sayfanın hex olarak `7C45` olduğuna
düşünelim. O zaman işlemcinin erişeceği fiziksel adres `7C45000 + 678` hex
adresi olacaktır.

---

`34-2.55.15`

Buraya kadar şunları anladık:

- Derleyici 32 bit bir sistemde sanki program 4 GB'lik bir RAM'de tek başına 4
  MB'ye yüklenerek çalıştırılacakmış gibi bir kod üretmektedir.
- İşlemci kodu çalıştırırken her bellek erişiminde sayfa tablosuna bakıp aslında
  o sanal adresleri fiziksel adreslere dönüştürmektedir.

---

**Pekiyi sayfa tablosunu kim oluşturmaktadır?** Sayfa tablosu işletim sistemi
tarafından proses belleğe yüklenirken (`exec()` fonksiyonları tarafından)
oluşturulmaktadır. İşletim sisteminin yükleyicisi (loader) programı 4K'lık
parçalara ayırarak sanal sayfa numaraları ardışıl ancak fiziksel sayfa
numaraları ardışıl olmayabilecek biçimde fiziksel RAM'e yüklemektedir. Yani
işletim sistemi fiziksel RAM'deki boş sayfalara bakar. Programın 4K'lık
kısımlarını bu fiziksel RAM'deki boş sayfalara yükler ve sayfa tablosunu buradan
hareketle oluşturur. Elbette fiziksel bellekte ardışıl boş yerler varsa fiziksel
bellekten de bu sayfalar ardışıl ayrılabilir ama böyle bir zorunluluk yoktur.

Aslında sayfa tablosu bir tane değildir. **İşletim sistemi her proses için ayrı
bir sayfa tablosu oluşturmaktadır.** CPU'lar sayfa tablolarını belli bir
yazmacın gösterdiği yerde ararlar (Örneğin Intel işlemcilerinde sayfa tablosu
`CR3` yazmacının gösterdiği yerdedir.) İşletim sistemi thread'ler arası geçiş
(context switch) yapıldığında çalışmasına ara verilen thread ile yeni geçilen
thread'in aynı prosesin thread'leri olup olmadığına bakar. Eğer yeni geçilen
thread ile çalışmasına ara verilen thread aynı prosese ilişkinse sayfa tablosu
değiştirilmez. **Çünkü aynı prosesin thread'leri aynı sanal bellek alanını
kullanmaktadır.** Ancak yeni geçilen thread kesilen thread'le farklı proseslere
ilişkinse işletim sistemi CPU'nun gördüğü sayfa tablosunu da değiştirmektedir.
Böylece aslında bir prosesin thread'i çalışırken CPU o prosesin sayfa tablosunu
gösterir durumda olur.

**Her prosesin sayfa tablosu birbirinden farklı olduğu için iki farklı
prosesteki sanal adresler aynı olsa bile bu adreslerin fiziksel karşılıkları
farklı olacaktır.** Örneğin aynı programı iki kez çalıştıralım. Bu durumda bu
iki proses için işletim sistemi iki farklı sayfa tablosu kullanıp aynı sanal
adresleri farklı fiziksel sayfalara yönlendirecektir. Böylece aslında aynı sanal
adreslere sahip olan programlar farklı fiziksel adreslere sahip olacaktır.

```{todo}
Minik bir demo ekle
```

---

`34-3.21.00`

Bir programı debugger ile incelerken gördüğümüz adresler sanal adreslerdir. Bare
metal, embedded çalışma gibi durumlar farklı olabilir, Linux'u ele alıyoruz.

Peki sayfalama mekanizması işlerimizi yavaşlatmaz mı? Teorik olarak sayfalama
mekanizması CPU'nun çalışmasını yavaşlatabilir. Ancak bugünkü CPU'ların çalışma
hızları zaten bu sayfalama mekanizmasının aktif olduğu durumla belirlenmektedir.
Dolayısıyla donanımsal olarak sayfalama mekanizması iyi bir biçimde
oluşturulduğu için buradaki hız kaybı önemsenecek ölçüde değildir. Ayrıca
işlemciler sayfa tablosuna erişimi azaltmak için zaten onun bazı bölümlerini
kendi içlerindeki bir cache sisteminde tutabilmektedir. Ayrıca sayfa girişlerine
hızlı erişim için işlemciler **TLB (Translation Lookaside Buffer)** denilen bir
cache mekanizması da oluşturmaktadır.

---

`35-0.0`

İşletim sistemi her proses için ayrı bir sayfa tablosu oluşturduğuna göre ve bu
sayfa tablosunda aynı sanal sayfa numaralarını zaten farklı fiziksel sayfalara
yönlendirdiğine göre aslında hiçbir proses diğerinin alanına erişemez. Yani
proseslerin birbirlerinin alanlarına erişmesi zaten sayfalama mekanizmasıyla
engellenmiş olmaktadır. Bu duruma *sayfalama mekanizması ile proseslerin
fiziksel bellek alanlarının izole edilmesi* denilmektedir. Örneğin aşağıdaki
gibi iki prosesin sayfa tablosu söz konusu olsun:

```text
Proses-1

Sanal Sayfa No  (decimal/hex)   Fiziksel Sayfa No (decimal/hex)
...                         ...
23603 (5C33)                      47324 (B8DC)
23604 (5C34)                      52689 (CDD1)
23605 (5C35)                      29671 (73E7)
...                         ...

Proses-2

Sanal Sayfa No  (decimal/hex)   Fiziksel Sayfa No (decimal/hex)
...                         ...
23603 (5C33)                      84523 (14A2b)
23604 (5C34)                      62981 (F605)
23605 (5C35)                      42398 (A59E)
...                         ...
```

İki prosesin sayfa tablosunda `Fiziksel Sayfa Numaraları` birbirinden
ayrıldığında zaten bu iki proses asla birbirlerinin alanlarına erişemeyecektir.

---

`35-15.45`

**Pekiyi 32 bit bir mimaride işletim sisteminin sayfa tablosu yukarıdaki
şekillere göre ne kadar yer kaplar?** 32 bit mimaride fiziksel RAM en fazla 4 GB
olabilir. Proseslerin sanal bellek alanları da 4 GB'dir. O halde toplam sayfa
sayısı `4GB/4K = 2^32/2^12 = 2^20 = 1 MB` olur. Her sayfa tablosu girişi Intel
mimarisinde 4 byte'tır. Dolayısıyla yukarıdaki şekillere göre bir prosesin sayfa
tablosu 4 MB yer kaplar. Bu alan sayfa tablosu için çok büyüktür. Bu nedenle
işlemcileri tasarlayanlar sayfa tablolarının kapladığı alanı küçültmek için
sanal adresleri iki parçaya değil, üç ya da dört parçaya ayırma yoluna
gitmişlerdir (multi-level page table [^1f]). Gerçekten de örneğin Intel'in 32 bit
mimarisinde bir sanal adres üç parçaya ayrılmaktadır.

```text
Intel: Sayfa Offset'i, Dizin Offset'i, Dizin Tablosu Offset'i
```

Biz gösterim kolaylığı açısından notların başında olduğu gibi ikili gösterimden,
sayfa no + offset, devam edeceğiz.

`35-27.20`

Biz yukarıda 32 bit sistemlere göre örnekler verdik. **Pekiyi 64 bit sistemlerde
durum nasıldır?** 64 bit sistemlerde fiziksel RAM'in teorik büyüklüğü `2^64 = 16
exabyte` olmaktadır. Dolayısıyla prosesin sanal bellek alanı da bu kadar
olacaktır. Burada eğer sanal adres iki parçaya ayrılırsa sayfa tablolarının
aşırı büyük yer kaplaması kaçınılmazdır. **Bu nedenle 64 bit sistemlerde
genellikle işlemcileri tasarlayanlar sanal adresleri dört parçaya
ayırmaktadır.** Bu konu yine bu notların kapsamı dışındadır. Ancak 64 bit
sistemlerde değişen bir şey yoktur. Program yine çok geniş bir sanal belleğe
sanki tek başına yüklenecekmiş gibi derlenir. Yine işletim sistemi proses için
sayfa tablosu oluşturarak sanal sayfa numaralarını gerçek fiziksel sayfa
numaralarına yönlendirir. Tabii pek çok işletim sistemi 16 exabyte sanal bellek
alanı çok büyük olduğu için bunu kısıtlama yoluna gitmektedir. **Örneğin Linux
yalnızca 256 TB alanı kullanmaktadır. Windows ise yalnızca 16 TB alan
kullanır.** Bu alanlar bile bugün için çok büyüktür.

Sayfa tablolarının gerçek organizasyonu için Intel'in, AMD'nin ve ARM
işlemcilerinin orijinal dokümanlarına bakılmalıdır.

## Ama neden?

`35-39.20`

**Pekiyi sayfalama (paging) mekanizmasının ne faydası vardır?** İşte sayfalama
mekanizmasının iki önemli işlevi vardır:

1. Sayfalama mekanizması programların fiziksel RAM'e ardışıl yüklenmesinin
  zorunluluğunu ortadan kaldırır. Böylece **bölünme (fragmentation)** denilen
  olgunun olumsuz etkisini azaltır.
2. Sayfalama mekanizması **sanal bellek (virtual memory)** denilen olgunun
  gerçekleştirimi için gerekmektedir.

## Bölünme, Parçalanma, Fragmentation

`35-1.02.55`

**Bölünme (fragmentation)** bellek yönetimi konusunda önemli bir problemdir. Bir
nesnenin belleğe yüklenmesi ardışıl bir biçimde yapılırsa zamanla yükleme
boşaltma işlemlerinin sonucunda bellekte çok sayıda küçük alan oluşmaktadır. Bu
küçük alanlar ardışıl olmadığı için genellikle bir işe yaramamaktadır. Küçük
alanların toplamı oldukça büyük miktarlara varabilmekte ve toplam belleğin
önemli miktarını kaplayabilmektedir. Bu olguya **bölünme (fragmentation)**
denilmektedir.

🚗 Bunu yol kenarına park eden arabalar arasında park ararken yaşamış
olabilirsiniz. Aracınızın sığacağı kadar büyüklükte tek bir yer yok ama bütün
boş yerlerin uzunluğunu toplarsanız aracınızdan çok daha uzun ediyor. Yani park
etmiş arabaları bir şekilde sıkıştırsanız çok yer açılacak ama park alanı
*fragmente* olduğu ve aradığınız büyüklükte bir yer olmadığı için arabanızı park
edemiyorsunuz.

Bölünmenin engellenmesi için ardışıl yükleme zorunluluğunun
ortadan kaldırılması gerekir. Bu durumda bellek bloklara ayrılır. Yüklenecek
nesne bloklara bölünerek ardışıl olmayacak biçimde boş bloklara atanır. Ancak
nesnenin hangi parçasının hangi bloklarda olduğu da bir biçimde kaydedilir. Bu
teknik hem RAM yönetiminde hem de disk yönetiminde benzer biçimde
kullanılmaktadır.

🚗 Araba park örneğinden devam edecek olursak belleği bloklara ayırmayı arabayı
4 eşit parçaya bölüp parçaları ayrı ayrı park edebilmenin mümkün olması gibi
düşünebilirsiniz. Böylece ufak tefek kalmış boş alanları kullanabiliriz.

Ancak bloklama yöntemiyle bölünme ortadan kaldırılmaya çalışıldığında bu sefer
başka bir problem ortaya çıkmaktadır. **Nesnelerin son bloklarında kullanılmayan
alanlar kalabilmektedir.** Bu da bir çeşit bölünmedir. Bu bölünme durumuna
**içsel bölünme (internal fragmentation)** denilmektedir. İçsel bölünmede
yapılabilecek bir şey yoktur. Ancak içsel bölünmenin etkisi diğerine göre daha
az olmaktadır.

`35-1.20.00`

```{note}
50'li yıllarda işletim sistemleri sistemi anlık durdurup belleği sıkılaştırıyormuş,
bölünmenin önüne geçmek için. Bazı sistemler de çeşitli yöntemlerle çalışma sırasında
pointer adreslerini vs değiştirerek bellek parçalanmasını azaltmaya çalışıyormuş.
Windows'ta eskiden bellek sıkıştırma gibi bir seçenek varmış. Bu kısım mış'lı
oldu çünkü bu ifadeleri doğrulamış değilim.
```

`35-1.27.40`

## Kaynaklar

[](kaynak.md) fakat ağırlıklı CSD notları.

[^1f]: <https://stackoverflow.com/q/59816941/1766391>
