---
og:description: Programlama dillerini öğrenirken ve onları kıyaslarken bu endeks karşımıza çıkmaktadır. Peki nedir? Güvenilir midir?
og:image: assets/social/blog/23/tiobe-index.jpg
---

# 🇹🇷 TIOBE Index nedir? Güvenebilir miyiz?

```{figure} /extra/assets/social/blog/23/tiobe-index.jpg
:align: center
:figclass: thmbnl
```

---

*Programlama dillerini öğrenirken ve onları kıyaslarken bu endeks karşımıza
çıkmaktadır. Peki nedir? Güvenilir midir?*

TIOBE Index, programlama dillerinin popüleritesini gösteren bir endekstir. Aylık
olarak güncellenen bu endeks bize bir programlama dilinin dünyada ne kadar
popüler olduğunu göstermektedir.

> The TIOBE Programming Community index is an indicator of the popularity of
> programming languages.

---

Peki **bir dilin popüler olması ne demektir?** **Bunu nasıl ölçebiliriz?** En
önemlisi de **popülerite bizler için ne ifade etmelidir?**

---

TIOBE Index, bilinirliği yüksek bir endeks olsa da birçok kişi tarafından
kullandığı yöntem dolayısıyla eleştirilmektedir. Aralık 2023 itibariyle
oluşturulan sıralama şu şekildedir:

```{figure} assets/tiobe-1.png
:align: center

Kendiniz bakın: [TIOBE Index](https://www.tiobe.com/tiobe-index/)
```

Siteyi ziyaret edip dillere tıkladığınız zaman güzel bir arayüz üzerinden ilgili
dilin popülerliğinin yıllar boyunca nasıl değiştiğini de görebiliyoruz. Ben
arayüzünü beğeniyorum.

TIOBE firması, kendini the software quality company olarak tanımılıyor [^1f]:

> TIOBE is specialized in assessing and tracking the quality of software. We
> measure the quality of a software system by applying widely accepted software
> metrics to it. TIOBE checks more than 1 billion lines of software code for its
> customers worldwide, real-time, each day. We measure software code quality
> with the goal to achieve a bug-free world through software quality expertise.

Ben ürünlerini kullanmadım. Belirtmek istediğim şey ise TIOBE Index'in bu
firmanın ana ürünü olmadığı. Bu endeks, ek olarak sundukları bir şey.

## TIOBE Index nasıl hesaplanıyor?

TIOBE Index, temel olarak çeşitli arama motorlarında, bir programlama dili ile
ilgili bulunan sonuç sayısı kullanılarak hesaplanıyor.

> Basically the calculation comes down to counting hits for the search query...

TIOBE, güncel durumda 25 adet arama motoru kullanıyor ve aramaların nasıl
yapıldığı, hangi sonuçların değerlendirildiği ve bu arama motorlarının
ağırlıkları kendi sayfalarında anlatılıyor [^2f]. İşte TIOBE Index ile ilgili
tartışmalar da burada başlıyor. Çünkü bu yöntemin doğru olmadığı ile ilgili
birçok görüş mevcut. Öncelikle Internet üzerinde bulup, seçtiğim görüşleri
paylaşmak istiyorum:

> So how does TIOBE calculate this index? You might not believe this, but they
> count the number of search engine results for each programming language. Not
> the number of people querying, not the number of queries they’re making, not
> sentiment. It relies entirely on that useless number that search engines
> report.

Source: [Please stop citing
TIOBE](https://blog.nindalf.com/posts/stop-citing-tiobe/)

> This means that (for an example, in theory) you can have a language that
> everyone is talking about that has a lot of hits and gets a high rating even
> though nobody uses it, and you can have a language that lots of people are
> using but there aren’t many web pages/hits so it gets a low rating. It doesn’t
> even take into account what the web pages contain (for example, imagine a
> million web pages saying a certain language is aweful, that all increase the
> language’s TIOBE index).

Source: [How accurate are the language ratings published in the TIOBE Index?](https://qr.ae/pKNreM)

> Tiobe’s rankings are nothing more than a calculation of web spam on Google.
> Bad languages with lots of articles are ranked just as high as loved
> languages. Languages such as C, get ranked artificially high, most likely due
> to a flaw in the way they are determining Google search results for the single
> letter C. So no, C is not the most widely used, loved or anything language.
> It’s simply a bad algorithm.

Source: [Why the Tiobe Index Can’t Be Trusted](https://www.codehawke.com/blogs/why_the_tiobe_index_can_t_be_trusted.html)

Üstteki görüş bir noktada hatalı. TIOBE C dilinin popülerliğini ölçmek için,
Google'da `C` diye arama yapmıyor, `"+C Programming"` olarak arama yapıyor
[^2f]. Yani yazının iddia ettiği gibi tek harf `C` sonuçları sonuca dahil
olmuyor. Internet üzerinde okuduklarınıza (benim bu yazım dahil) hemen
güvenmemek için bir örnek daha...

Bu arada ilginizi çekebilir:
[Google Search Operators: The Complete List (44 Advanced Operators)](https://ahrefs.com/blog/google-advanced-search-operators/)

> But it is so much fun to cite TIOBE! People always become happy when you say
> how Python beats Java now. :)

😂

Source: [Please stop citing TIOBE (Reddit)](https://www.reddit.com/r/programming/comments/we8kxc/please_stop_citing_tiobe/)

**Ve gelelim benim en çok sevdiğim görüşe:**

> Here is the thing: people want some authoritative source backed by science and
> statistics. The TIOBE index checks all these boxes: it is by a reputable (I
> guess) company, it uses a reproducible method, and it publishes its
> methodology. The fact that the methodology and result are complete garbage is
> irrelevant.

Source: [Reddit](https://www.reddit.com/r/programming/comments/we8kxc/comment/iip4tv6/)

Bu son görüşü gerçekten çok beğendim, adeta akademik dünyanın da bir özeti gibi...

Peki TIOBE Index'e alternatifler neler?

## Alternatifler

Alternatif endeksler var mı diye Internet üzerinde *kısa* bir araştırma yaptım,
ChatGPT de yardımcı oldu sağ olsun. Örnek olarak C diline de baktım. **TIOBE
Index'te C, 2. sırada.**

- [Github Octoverse](https://octoverse.github.com/)
- [Stackoverflow Survey
  2023](https://survey.stackoverflow.co/2023/#technology-most-popular-technologies)
  **Bu ankete göre C dili 10. sırada.** Anket sonuçları en popüler dillerin web
  teknolojileri ile ilgili olduğunu gösteriyor (şaşırtıcı olmaz).
- [The RedMonk Programming Language Rankings: January
  2023](https://redmonk.com/sogrady/2023/05/16/language-rankings-1-23/) Burada
  da C dili **10\. sırada.**
- [PYPL PopularitY of Programming Language](https://pypl.github.io/PYPL.html)
  C/C++ (beraber) **4\. sırada.**

Her ölçümün yöntemi kendi sitesinde anlatılıyor, bağlantılara tıklayarak
gidebilirsiniz. Örnek olarak aldığım C dilinin sırası 2 ile 10 arasında
değişiyor.

*Kısa* bir araştırma yapmamın sebebi de programlama dillerinin popülerliğini pek
de önemsememem, ilerleyen kısımlarda bahsedeceğim.

## Popülerlik nedir?

Cambridge Dictionary, *popularity* nin tanımını şöyle
[veriyor](https://dictionary.cambridge.org/dictionary/english/popularity):

> the fact that something or someone is liked, enjoyed, or supported by many
> people

TDK'da ise popüler kelimesi

> Herkesçe tanınan, bilinen

olarak tanımlanmış.

Özellikle TDK'nın tanımı doğrultusunda TIOBE'nin yaptığı gibi arama motoru sonuç
sayısına bakmak çok da mantıksız durmuyor. Popülerlik ile o konu hakkında
yazılan yazı ve çekilen video sayısı arasında bir korelasyon olmasını
bekleyebiliriz. O yüzden popülerlik açısından bu yöntem çok kötü olmayabilir.
Gelin bir konuyu toparlayalım.

## Yani?

```{figure} https://c.tenor.com/SUZ7brjm0PcAAAAd/tenor.gif
:align: center
:figclass: thmbnl

[GIF](https://tenor.com/view/but-why-so-what-idgaf-idk-idc-gif-16391724)
```

Peki ne yapalım sizce? TIOBE Index'teki en popüler dilleri mi öğrenelim yoksa
bir daha bu endeksin sayfasını açmayalım mı? Elbette hiçbiri. Konuyu biraz da
naçizane tavsiyeler vererek tamamalamak istiyorum.

TIOBE Index sayfasında `VHDL` i arattığımızda sıralamasının 50 - 100 arasında
olduğunu görüyoruz. `Verilog` ve `System Verilog` sorguları ise **sonuç bile
dönmüyor**, yani kaçıncı sırada olduğu belli bile değil! Şimdi bu endekse göre
düşünseydik FPGA/ASIC işi yapan sayısal tasarım ve doğrulama mühendislerinin
herhalde aç kalması gerekirdi değil mi? Ama durumun böyle olmadığını muhtemelen
siz de biliyorsunuz. FPGA alanında çalışacaksanız bu endekste (ve muhtemelen tüm
endekslerde) sırası çok düşük diye HDL dillerini öğrenmeme lüksünüz yok.

Bir örnek daha vereyim: NASA,
[Voyager](https://en.wikipedia.org/wiki/Voyager_program) programını idame etmek
için Cobol (1959), Fortran (1957) ve Algol (1958) bilen programcı
[arıyordu.](https://www.popularmechanics.com/space/a17991/voyager-1-voyager-2-retiring-engineer/)
Bu diller günümüzde adeta "pek yüzüne bakılmayan" diller olsa da tasarımların
yapıldığı 70'li yıllarda altın çağını yaşıyordu. Benzer şekilde eski dillerin
mainframe kullanan bankacılık, havacılık gibi sektörlerde eski kodlarda
bulunduğu ve risklerinden dolayı idame ettirildiği söylenir. Muhtemelen
buralarda çalışan programcılar, dili bilen kişilerin çok az olmasından dolayı
dolgun ücretler alabiliyorlar ama çalışabilecekleri iş sahaları da oldukça
sınırlı. Çok sınırlı sayıda olan bir işe girebiliriz ve girersek de iyi
kazanabiliriz diye tutup sırf bu sebepten Cobol mu öğreneceğiz? E bu da pek
mantıklı gelmiyor size değil mi?

Mesela bakın, uzun yıllardır eski sistemleri ayakta tutmak için COBOL ile
çalışan Veronica ablamız da artık bu işten *sıkılmış* (para kazanıyor olmasına
rağmen) ve bırakmış. Bir dilin para kazandırıyor olması da sürekli
yapabileceğimiz anlamına gelmiyor, insan işte...

```{youtube} ZoVrilcJvjg
:align: center
:width: 100%
```

```{figure} assets/tiobe-2.jpg
:align: center

Merak edenler için: [Year 2000 problem](https://en.wikipedia.org/wiki/Year_2000_problem)
```

COBOL konusunu mainframe denince akla ilk gelen firmalardan IBM'in daha 2 hafta
önce attığı şu videonun linkini bırkarak kapatıyorum, konuyu biraz uzattım:
[Technical Debt and Modernizing
COBOL](https://www.youtube.com/watch?v=-CI8hb-077E)

---

"Hangi programlama dilini öğrenmeliyim?" diye düşünürken aslında çalışmak
istediğimiz alanı düşünmek gerekiyor. AI/ML alanında çalışacaksanız Python'un,
gömülü sistem ve sistem programlama ve benzeri düşük seviye yüksek performans
işler yapacaksanız C/C++'ın ve hatta Assembly'nin, web işleri yapacaksanız
JavaScript'in, sayısal tasarım yapacaksanız VHDL/Verilog/System Verilog'un
popülerlikleri ve herhangi bir endeksteki sıralaması ne olursa olsun
öğrenilmesinin neredeyse zorunlu olduğunu söyleyebiliriz. Kendi alanınız ne
olursa olsun biraz Python bilmenin de faydalı olacağını düşünüyorum. Python son
yıllarda veri bilimi ve yapay zeka konularında parlasa da aslında günümüzün
adeta genel geçer bir script dili gibi de kullanılıyor. Her alan için
geliştirilmiş Python temelli araçlar bulunabiliyor. Python ve JavaScript genel
amaca da hitap ediyorlar. Ama örneğin sayısal tasarımcı iseniz önceliğiniz
bunlar değil HDL dilleri olmalıdır.

Yukarıda TIOBE Index'e alternatif gösterilen ölçümlerden bahsettim. Buradaki
sonuçlar TIOBE'den daha anlamlı mı? Muhtemelen evet. Geliştiriciler ile yapılan
geniş çaplı anketler, GitHub gibi açık kaynak projelerin bulunduğu yerlerdeki
dil dağılımları, iş ilanlarında aranan programlama dilleri TIOBE'nin baz aldığı
arama motoru sonuçlarına göre daha iyi bir gösterge olabilir. Örneğin
belirttiğim gibi C dilinin sıralaması 2-10 arasında yer alıyor, ölçümden ölçüme
değişiyor. C dilinin sırası 50 de olsa gömülü yazılım yapacaksanız bu dili
öğreneceksiniz, en azından günümüzde böyle. Dünya üzerinde yazılım alanında o
kadar farklı problemler ve platformlar var ki global bir şekilde her şeyi
kapsayan bir endeks oluşturmak da çok anlamlı olmuyor. O yüzden alana göre
düşünmek gerekiyor. Bunun için doğru yaklaşımların da o alandaki iş ilanlarına
bakmanın, alanda çalışan kişilerle konuşmanın, o konu ile ilgili yapılan açık
kaynak projelerde kullanılan dillere göz atmanın olacağını düşünüyorum.

Elbette bu TIOBE Index dahil olmak üzere bu endekslere bakmayalım demiyorum. Ben
de Stack Overflow'un anket sonuçlarına, aklıma geldikçe TIOBE Index'e bakıyorum
(10-15 saniye kadar) insanlar nelerle ilgileniyor, dünya nereye gidiyor bunu
kaçırmamak adına. Örneğin TIOBE Index'te
[Python](https://www.tiobe.com/tiobe-index/python/) sayfasına bakarsanız
Python'ın nasıl popülerleştiğini görebilirsiniz, dediğim gibi elbete bir
korelasyon var, ne kadar güçlü tartışmaya açık. Bu veriler anlamsız değil. Ama
"ne öğrenmeliyim?" diye kendime sorarken, **karar verme algoritmamda** kullandığım
girdilerden biri olan bu tarz endeks puanlarının algoritmamdaki kat sayısı
düşük. TIOBE de kendi ölçümü ile ilgili şunları söylüyor:

> It is important to note that the TIOBE index is not about the *best*
> programming language or the language in which *most lines of code* have been
> written.

Ayrıca:

> The index can be used to check whether your programming skills are still up to
> date or to make a strategic decision about what programming language should be
> adopted when starting to build a new software system.

Problem TIOBE Index'e gereğinden fazla "değer" verince oluşuyor. Adamlar da
kendi ölçümlerinin ne anlama gelip gelmediğini anlatıyorlar. **Siz bir
programlama dilini öğrenmek için seçerken bir kurum veya birinin popüler
demesine bakıyorsanız sorun biraz da sizde oluyor ne yazık ki.** Günün sonunda
kariyer açısından TIOBE "şu dil bundan popüler" dese ne olacak demese diye
düşünüyorum, **çok da şaapmamak lazım.**

TIOBE Index, yukarıda **en sevdiğim görüş** olarak belirttiğim Reddit yorumu
gibi. Yani birilerini bir dilin popüler olduğuna ikna etmek istiyorsanız
kullanabileceğini bir kaynak. O dil listede yoksa (HDL dilleri) gibi TIOBE Index
konusunu hiç açmayabilirsiniz de 🙊 (akademik dünyayı özetledim).

Buraya kadar okduğunuz için teşekkür ederim. **Varsa görüşlerinizi yorum olarak
iletebilirsiniz.**

Görüşmek üzere... 🙋‍♂️

## İlgili Kaynaklar

- [A Hacker News discussion on TIOBE
  Index](https://news.ycombinator.com/item?id=19767725)
- [Kapak fotoğrafı
  hakkında](https://knowyourmeme.com/memes/la-noire-doubt-press-x-to-doubt)

[^1f]: [About us - TIOBE](https://www.tiobe.com/about-us/)
[^2f]: [TIOBE Programming Community Index
    Definition](https://www.tiobe.com/tiobe-index/programminglanguages_definition/)

```{disqus}
:disqus_identifier: c1a09e21-f9a6-4a88-b80b-aa6e7e2f05ec
```
