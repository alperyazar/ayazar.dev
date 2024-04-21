---
giscus: 5cb38afb-1edd-40ce-a597-0039ffeec672
---
# Linux Sistem Programlama nedir? + bazı SSS

Bu sayfada Linux Sistem Programlama ile ilgili çeşitli kavramları ve bazı
sık sorulan soruları (SSS) anlatmaya çalışacağım. Hadi başlayalım!

## Sistem Programlama nedir?

Linux Sistem Programlama (Linux System Programming) kavramına bakmadan önce
dilerseniz *Sistem Programlama* nedir, ona bir bakalım.

Sistem programlama, *klasik* yani çoğu programlama işinin aksine donanıma daha
yakın şekilde çalışacak programların yazılması eylemidir. Sistem programlama yapan
kişilerin donanımı, *uygulama programı* yazan kişilere göre genelde daha iyi
bilmesi gerekmektedir. Uygulama programları genel olarak kullanıcı ile doğrudan
etkileşime girer iken sistem programları doğrudan kullanıcı ile etkileşime
girmezler, onun yerine uygulama programları gibi diğer programlara hizmet
verirler. En önemli sistem programlarından biri **işletim sistemleri (OS)** dir.
İşletim sistemleri, uygulama geliştiren programcıları donanımın karmaşıklığından
soyutlar. Sistem programları tipik olarak az kaynak tüketen, bellek tüketimi ya
da işlemci kullanımı (CPU cycle) açısından verimli olan programlardır. İşletim
sistemi üzerinde koşan birçok sistem programı bulunmaktadır. Bu programlar
genelde doğrudan ya da standart C kütüphanesi gibi çok *ince* bir kütüphane
katmanı ile işletim sisteminin çekirdeği ile konuşarak çalışırlar.
**Derleyiciler, gömülü yazılımlar, antivirüsler, hypervisor yazılımları** ya da
**container runtime** yazılımları sistem programlarına birer örnektir. Bu
yazılımlar genelde **Assembly, C, C++** gibi düşük seviyeli ya da **Rust** gibi
bu tarz amaçlar için oluşturulmuş modern dillerde yazılırlar.

## Linux Sistem Programlama nedir?

İşte benzer şekilde Linux çekirdeği üzerinde yapılan yani bir Linux dağıtımı
içerisinde yapılan sistem programlama faliyetilerine Linux Sistem Programlama
diyoruz. Benzer şekilde Windows çekirdeği üzerinde yapılan sistem programlama
ise *Window Sistem Programlama* olarak adlandırılır.

Ubuntu, Arch, Fedora gibi Linux dağıtımları adı Linux olan bir çekirdekten
(kernel) ve bu çekirdeğin sunduğu hizmetleri kullanarak çalışan ve bir araya
gelmiş birçok uygulamadan oluşur. Eğer bizler de bu tarz işletim sistemleri
üzerinde (neredeyse) doğrudan çekirdek ile konuşarak çalışan programlar yazarsak
biz de *Linux Sistem Programlama* yapmış oluruz. Bir de *Linux Kernel
Programlama* vardır, bu ikisi farklıdır. Sistem programlamada kernel tipik
olarak bir kara kutu olarak düşünülür, içerisindeki yapı ile pek ilgilenmeyiz.
Sistem programlamada daha çok kernelin sunduğu hizmetlerden faydalanır. Elbette
bahsettiğimiz Linux kernelinin de kendisi bir yazılımdır (hem de çok büyük).
İşte kernelin kendisinin geliştirilmesine ya da kernel içerisinde çalışan aygıt
sürücülerinin (device driver) oluşturulmasına *(Linux) Kernel Programlama* adı verilir.

Linux üzerinde yazdığımız tüm programlamlar otomatik olarak *sistem programı*
olmamaktadır. Örneğin Python gibi yüksek bir seviyeli dilde, kernel ile doğrudan
konuşmayarak yazdığımız bir program Linux üzerinde çalışssa bile bu programlama
faliyeti bir sistem programlama olmamaktadır. Çünkü bu durumda, Python yorumlayıcısı
ve kütüphanelerinden dolayı kernel ile aramızda *kalın* bir soyutlaştırma katmanı
vardır. Fakat doğrudan [POSIX](https://en.wikipedia.org/wiki/POSIX) kütüphenelerini
kullanarak (ilerleyen kısımlarda değineceğim) yazdığımız bir C programı bir sistem
programı olacaktır. Bu farkı henüz tam anlamamış olabilirsiniz, ki çok normal.
Biraz elinizi kirlettikçe bu konuyu daha iyi anlayacaksınız.

## Bu Seri Hakkında

Web sitemde oluşturduğum bu serideki amacım Linux Sistem Programlama konusundaki
bilgimi aktarmaktadır, asla iyi bildiğimi söylemiyorum, hatalar olabilir.
Fark ettiğiniz hatalı kısımları benimle paylaşırsanız çok sevinirim.

## Kaynaklar

- [](kaynak.md)
- [Systems programming (Wikipedia)](https://en.wikipedia.org/wiki/Systems_programming)

