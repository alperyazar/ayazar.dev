---
giscus: 76b2aa79-93f5-4e32-bec9-c7b6c2c1488b
---

# Temel Kavramlar

Bu bölümde, çoğu Python'dan bağımsız olan temel kavramlara bakacağız.

## Çeviriciler, Derleyiciler ve Yorumlayıcılar

Bir programlama dilinde yazılmış bir programı başka bir dile çeviren programlara
**translator** yani `çevirici 🇹🇷` program denmektedir. Çevirici programın
girdi olarak aldığı dile kaynak dil yani source language, hedef olarak çıktı
ürettiği dile de hedef dil yani target veya destination language denir.

Eğer işlem sırasında hedef dil sembolik makina dili (assembly), saf makina dili
(binary), ara kod gibi alçak seviyeli yani low-level dil ise bu çevirici
programlara **compiler** yani `derleyici 🇹🇷` adı verilir. Her compiler bir
translator sayılmakta fakat her translator bir compiler olmamaktadır. Burada
hedef dile bakmak gerekir. [^1f]

---

Biz bir C kodunu C derleyicisi ile derlediğimizde günün sonunda elimizde saf
makina dilinde bir program olur. Bazı programlar ise bu şekilde bir dönüşüm
yapılmadan, hedef kod üretilmeden doğrudan çalıştırılır. Bu tarz program
çalıştıran programlara **interpreter** yani `yorumlayıcı 🇹🇷` adı verilir.
Yorumlayıcı ile çalışan programlar, derlenen programlara göre tipik olarak daha
yavaş çalışır. Ayrıca bu tarz programlar kaynak kodu üzerinden çalıştırıldığı
için programın dağıtımı sırasında genellikle kodu da başkalarına vermek gerekir,
bu da bazen istenmeyebilir.

C, C++, C#, Java gibi diller derleyicilere sahiptir. PHP, Perl gibi diller ise
yorumlayıcılar tarafından çalıştırılır. Basic, Swift, Python gibi dillerin ise
hem yorumlayıcıları hem de derleyicileri vardır.

```{attention}
Yorumlama ya da derleme aslında dilin bir özelliği değildir. Bir dilde yazılmış
bir programı alıp, dilin kurallarına göre çıktı üreten bir *implementasyon*u
teorik olarak hem yorumlayıcı hem derleyici olarak yapmak mümkündür. Fakat
pratikte bu her zaman kolay ya da anlamlı olmayabilir. Her ne kadar bu
özellikler doğrudan dilin doğrudan özelliği olmasa da bir dil ağırlıklı olarak
derleyiciler ile çevriliyor ise o dil *derlenen dil*, yorumlayıcılar ile
çalıştırılıyorsa *yorumlanan dil* olarak adlandırılır.
```

Genellikle genel amaçlı diller, general purpose, daha çok derleyiciler ile
çalıştırılırken bir alana özgü olan, domain specific, diller yorumlayıcılar yolu
ile çalıştırılır. Yorumlayıcı yazmak, genelde derleyici yazmaktan daha kolay
olmaktadır. Elbette bunların hepsi genellemedir.

---

CPython'dan örnek verecek olursak, CPython C dilinde yazılmış bir Python
implementasyonudur.

```python
x = 42
print(x)
```

Yukarıdaki Python kodu CPython ile çalıştırılırken aslında satır satır okunur,
CPython tarafından yapılmak istenen şey arka planda C kodları yardımıyla
yapılır. **Yani aslında Python kodu doğrudan işlemci üzerinde çalıştırılmaz,
dolaylı yoldan çalıştırılmış olur.** İşte bu yüzden Python tipik olarak yavaş
bir dildir. Elbette yorumlayıcılar da kodu hızlandırmak için detayları burada
verilmeyen, benim de çoğunu bilmediğim, birçok teknik kullanmaktadır.

Yorumlanan dillerin bir avantajı da tipik olarak *cross-platform* olmalarıdır.
Yani bu programlar, ilgili platformda yorumlayıcıları olmak şartı ile, genelde
kaynak kodunda değişiklik olmadan çalıştırılabilirler. Derleyici çıktıları
ise platforma özgüdür ve kolayca taşınamazlar.

## Doğal Kod, Ara Kod, JIT

İşlemciler, kendilerinin anladığı makina komutlarını çalıştırabilmektedir.
Yazdığımız programın bir şekilde bu makina komutları aracılığı ile
çalıştırılması gerekmektedir. C, C++ gibi dillerin derleyicileri çalıştığında
çıkardıkları çalıştırılabilir dosya içerisinde doğrudan makina komutları yer
alır. İşte doğrudan CPU üzerinde çalışan makina komutları ile çalışmaya **native
code** yani `doğal kodlu 🇹🇷` çalışma denmektedir.

Bazı sistemler ve derleyiciler ise yazılan programları bir CPU'nun
anlayabileceği makina komutlarına çevirmez. Onun yerine, gerçekte olmayan adeta
*sanal* bir CPU'nun makina kodlarına çevirir. Bu yapay kodlar ise **intermediate
language** yani `ara kod 🇹🇷` olarak adlandırılır. Bu tarz çalışma Java ve .NET
dünyasında kullanılmaktadır. Java dünyasında bu ara kod **Java Bytecode**, .NET
dünyasında yani
[CLI](https://en.wikipedia.org/wiki/Common_Language_Infrastructure) dünyasında
ise **CIL, Common Intermediate Language** denmektedir.

Ara kodlu çalışmada derleyicinin çıkardığı ve aslında işlemcinin desteklemediği
kodların bir şekilde gerçek bir işlemci üzerinde çalıştırılması gerekecektir.
İşte burada ilgili dilin başka bir bileşeni devreye girecektir. Java dünyasında,
Java Virtual Machine yani Java Sanal Makinası, .NET ortamında da CLR yani Common
Language Runtime sistemi/yazılımı bu ara kodları alıp, gerçek işlemci üzerinde
çalıştırır. Burada çeşitli yöntemler kullanılmaktadır. Bir tanesi, ara kodun
çalıştırılmadan önce gerçek işlemcinin komutlarına çevrilmesi yani derlenmesi
işlemidir. Bu işlem tam program çalıştırılacağı sırada yapıldığı için buna
**JIT, Just-in-time compilation** denmektedir. Örneğin JVM, JIT yeteneğine
sahiptir ama tüm kodlar JVM tarafından hemen derlenmez. Burada önce JVM
tarafından yorumlanıp, bu şekilde çalıştırılıp *profile* edildikten sonra
gerekirse hızlandırmak için JIT ile derlenebilir. [^2f] Yani derleyici tarafında
apayrı yazıları hak eden teknikler kullanılabilmektedir. JIT işlemi sırasında da
hedef dil düşük seviyeli bir dil, saf makina dili, olduğu için bu işlem de
derleme olarak adlandırılabilir.

Java ile ilgili ChatGPT'den özet:

```text
Not every Java bytecode instruction is JIT (Just-In-Time) compiled by the JVM.
The JIT compiler selectively compiles certain parts of the bytecode based on
execution patterns. Here's how it works:

JVM Execution Model

Java bytecode is initially executed using an interpreter, which directly
interprets the instructions. This allows the JVM to start executing code quickly
without waiting for compilation.
```

JIT'in tersi genelde [ahead-of-time compilation
(AOT)](https://en.wikipedia.org/wiki/Ahead-of-time_compilation) olarak verilir.
C kodunun çalıştırılmadan önce derlenip kenara konması gibi.

Ara kodlu çalışma, doğal kodlu çalışmaya göre %20 daha yavaş olabilir (duruma
göre). O zaman bunu yapmanın mantığı nedir? Doğal kodlu çalışmada çıkan
programın taşınabilir olmadığından bahsetmiştik. Her işlemci ve platform için
tekrar derleme gerekecektir. C gibi dillerde programlar kayna kod yani *source
code portable* olsalar da derleyici çıktısı olan çalıştırılabilir program
*binary portable* değildir. Aynı kaynak kodun farklı platformlar için tekrar
derlenmesi gerekecektir. Oysa ki ara kodlu çalışma binary portable olmaktadır.
Elbette bunun olabilmesi için ilgili sistemde o ara kodu çalıştırabilecek
yazılımların hazır olması gerekir. Ama Java, .NET gibi örneklerde bunlar zaten
firma ya da topluluk tarafından hazırlanmıştır, programcının bir şey yapmasına
gerek yoktur. Programcı bu sayede derlediği kodun "her yerde" çalışacağından
emin olur ve her platform için tekrar derleme yapmaz.

```{tip}
Konu ilginizi çektiyse [](../embedded/capraz-derleme.md) isimli videoma
bakabilirsiniz.
```

---

Şimdi bu açıdan ilk [](merhaba.md) yazısında da bahsettiğim *Python
implementation*larına bir bakalım.

**Jython** ve **IronPython** aslında birer yorumlayıcı değil, **Python
derleyicisidir.** Jython, Python dilinde yazılmış bir programı Java Bytecode'a
IronPython ise Common Intermediate Language (CIL)'e (yanılmıyorsam) çevirir.
Her iki durumda da hedef dil düşük seviyeli bir dil olduğu için bu çevirim,
derleme olarak adlandırılabilir.

**CPython** da ise durum biraz ortadadır. CPython aslında Python kodlarını
yorumlayıcı olarak çalıştırmadan önce *kendince* bir çevirme işlemine tabii
tutar. Ama bu işlemin sonunda çıkan *ara kodumsu* yapı üzerinde tekrar bir JIT
derlemesi yapılmaz, adeta satır satır yorumlanır. Yani bizim gördüğümüz kaynak
kod değil de ondan türetilmiş bir şey yorumlanır. Yani aslında CPython,
yorumlamayı daha verimli yapmak için kodu önce bir "elden geçirir." Bu işlem de
genel olarak ana script kodları üzerinde değil, Python modülleri üzerinde
yapılır. Bunun amacı da aslında tekrarlı çalıştırmalarda performans artışı
sağlamaktır. CPython'nun yaptığı bu işlemler sırasında çıkan "ara gösterim"in
bir standardı yoktur. Yani bu, CPython'a özgü bir durumdur ve Python'un
standardize ettiği bir şey değildir. Oysa ki Jython ve IronPython'da durum böyle
değildir, onlarınki gayet de standarttır. Python standartları aslında
implementasyon yazanlara *Nasıl yapıyorsan yap, beni bağlamaz yeter ki Python
programcısı dil ile ne yapmak istiyorsa kurallar çerçevesinde onu yap!*
demektedir.

**PyPy** ise bir JIT derlemesi yapmaktadır. Bu yüzden PyPy, genelde hızı ile
"övünür."

```{note}
CPython yani halk arasında bilinen adı ile "Python" ile çalışırken (*Abi Python
kurdum* dediğimizde aslında tipik olarak CPython kurmuş oluyoruz) `.pyc`
dosyaları oluştuğunu görebilirsiniz. Bunlar Python standardında yer almayan,
CPython'nun kendi "uydurduğu", performans artışı için oluşturulan dosyalardır.
Burada aslında Java Bytecode'a benzeyen Python Bytecode konsepti vardır.
Benzer şekilde Python Virtual Machine (PVM) ve Python Bytecode Interpreter
sözcüklerini de duyabilirsiniz.

Bknz: [If Python is interpreted, what are .pyc
files?](https://stackoverflow.com/questions/2998215/if-python-is-interpreted-what-are-pyc-files)
ve [Can someone explain the interaction between Python Virtual Machine and
running the Python command in the
terminal?](https://www.reddit.com/r/learnpython/comments/u13qr2/can_someone_explain_the_interaction_between/)
```

## Mülkiyet Kavramı

Programların bir kısmı firmalar tarafından ticari amaçlarla yazılmaktadır. Aynı
durum programlama dilleri için de geçerli olmaktadır. Örneğin MATLAB dili,
MathWorks firması tarafından geliştirilmiştir ve mülkiyeti bu firmaya aittir.
Birçok popüler programlama dilin ise böyle değildir, bir firmaya ait değildir.
Bunlara *proprietary* diller denmektedir. Python da, C ve C++ gibi dillerde
olduğu gibi bir firmaya, özel bir gruba ait bir dil değildir. Bu tarz diller
**non-proprietary** olarak adlandırılır. Böyle diller bir firmanın veya grubun
özel amaçları için geliştirilmezler, daha çok topluluk tarafından
ilerletilirler.

## Dil Olgusu

Dil, çok da kolay tanımlanabilen bir olgu değildir. Türkçe gibi diller *native*
yani `doğal 🇹🇷`; Python gibi programlama dilleri de *constructive*, `kurgusal
🇹🇷` veya *artificial*, `yapay 🇹🇷` dil olarak kategorilendirilir.

Diller üzerinde temel iki kavramdan bahsedebiliriz: *syntax* yani `sentaks 🇹🇷`
ve *semantic* yani `semantik 🇹🇷`. Bu iki bileşen dilin gramerini oluşturur.
Bir dili oluşturan en yalın ögelere *token* yani `sembol 🇹🇷` ya da `atom 🇹🇷`
adı verilir. Doğal dillerdeki atomlar, sözcüklerdir.

Geçerli sentaks, söz diziminin ve kelimelerin doğru olması iken geçerli semantik
olması için oluşan cümlelerin de anlamlı olması gerekir.

| Örnek | Sentaks | Semantik | Açıklama |
| ----- | ------- | -------- | -------- |
| Ali okula gidiyor. | ✅ | ✅ | Yazım hatası yok, dizilim doğru ve cümle anlamlı |
| Kalem yemeğe gitti. | ✅ | ❌ | Yazım hatası yok, dizilim doğru fakat cümle anlamsız |
| Ali gidiyor okul. | ❌ | - | Kelime sırası yanlış, sentaks hatası |
| Herkez çok mutluydu. | ❌ | - | Kelimede yazım hatası var, sentaks hatası |

Örneğin aşağıdaki C kodu da sentaks olarak doğru semantik olarak yanlıştır.

```c
double pi = 3.14159;
printf("%d\n", pi);  // %d yi, double bir değişkenle eşlemek doğru değildir.
```

---

Türkçe gibi doğal dillerde sentaks ve semantik kurallarını formülize etmek
neredeyse imkansızdır. İnsanla beraber gelişen ve yıllar içerisinde evrilen
bu tarz dillerde birçok istisna durum oluşmaktadır. Bunu en iyi başka bir yabancı
dili öğrenirken hissederiz. Bu yüzden yeni bir dil öğrenmek bizleri zorlar.

Bilgisayar bilimlerinde kullanılan dillere **computer language** yani
`bilgisayar dilleri 🇹🇷` demekteyiz. Eğer bir bilgisayar dilinde bir akış varsa
ona aynı zamanda **programming language** yani `programlama dili 🇹🇷` deriz.
Örneğin HTML bir bilgisayar dilidir ama programlama dili değildir. Python ise
programlama dilidir, aynı zamanda bilgisayar dili olmaktadır.

Bilgisayar dilleri yapay diller oldukları için doğal dillerin aksine kuralları
çok daha kolay formülize edilebilir. Burada en çok tercih edilen notasyon
[BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form) ve
[EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form)
notasyonu olmaktadır. Birçok programlama dilinin "resmi" dokümanlarında dilin
grameri bu şekilde tariflenir. Elbette dili bu kurallara bakarak öğrnemek pek
pratik değildir bu notasyonlar genelde dili öğrendikten sonra referans kaynak
olarak, bir şeylerin detaylarına bakarken bizler için anlamlı olmaktadır.

## Programlama Dilleri Kategorileri

Programlama dillerini birçok açıdan kategorilendirmek mümkündür. Bununla ilgili
C özelinde yazdığım [](../c/properties.md) yazısında genel birçok açıklama da
bulunmaktadır, ona da göz atabilirsiniz. Ayrıca [List of programming
languages](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type)
by type başlıklı Wikipedia yazısında da birçok kategoriyi görebilirsiniz.

[İlk yazıda](merhaba.md), programlama dillerindeki çeşitli paradigmalardan yani
programlama modellerinden kısaca bahsetmiştim: procedural, object-oriented,
functional ve multi-paradigm. Burada kısaca **object-oriented** ve
**object-based** kavramlarını da karşılaştırmak isterim.

Eğer bir dilde,

- Sınıf kavramı
- Türetme kavramı
- Çok biçimlilik (polymorphism)

varsa o dil **object-oriented** yani `nesne yönelimli 🇹🇷` dil olmaktadır. Sınıf
kavramı var fakat çok biçimlilik yok ise o zaman **object-based** yani
`nesen tabanlı 🇹🇷` bir dil olmaktadır. C++, Java, C#, Python gibi diller nesne
yönelimli dillerdir.

## Python nerededir?

Dilleri birçok açıdan kategorilendirmek mümkün ama Python'ı temel açılardan
ele alacak olursak bu dilin:

- Yüksek seviyeli
- Genel amaçlı
- Çok paradigmalı/modelli (multi-paradigm) (ağırlıklı prosedürel ve nesne
  yönelimli olsa da fonksiyonel özellikleri de barındırıyor, impure functional language)
- Implementasyona göre derlenen ve yorumlanan (birini seç deseler yorumlanan
  kategorisine giriyor ama önceden de bahsettiğim gibi dilleri bu açıdan
  kategorilendirmek çok da doğru değil)
- Concurrent programlama destekleyen
- Dynamically typed, dinamik tür sistemine sahip
- Interaktif
- Iterative
- Reflective
- Strongly typed

bir dil olduğunu söyleyebiliriz.

[^1f]: 📖 Compilers: Principles, Techniques, and Tools
[^2f]: <https://stackoverflow.com/questions/41497761/what-exactly-is-the-jit-compiler-inside-a-jvm>
