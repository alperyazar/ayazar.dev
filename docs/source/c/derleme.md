# Bir C Programı Derlenirken Olanlar

C, derlenen yani *compiled* bir dildir. Bknz: [](properties.md).

Gerçi bir dilin derlenen veya yorumlanan *interpreted* bir dil olmasına doğrudan
dilin bir özelliği de deneyebiliriz. Örneğin Python interpreter'ı yerine bir C
interpreter'ı pekala yazılabilir. Burada önemli olan dilin kurallarının doğru
uygulanması ve doğru sonuçların üretilmesidir. Özellikle Python gibi dillerde
çeşitli teknolojilerle çalışan yorumlayıcılar bulunmaktadır. Ama C dilini
düşündüğümüz zaman C'yi her zaman derlenen bir dil olarak düşünebiliriz.

Bir C programı tipik olarak birden fazla `.c` ve `.h` uzantılı dosyalardan
oluşur. Bu dosyalar özünde birer metin dosyasıdır. Bizler programcılar olarak bu
metin dosyalarına ya metin editörleri ile ya da IDE gibi daha kompleks
yazılımlar kullanarak C dilinde çeşitli kodlar yazarız. Programımız bittiği
zaman **derleyici** yani **compiler** tarafından bu dosyalar bir **derleme**
yani **compilation** işlemine tutulur ve sonuç olarak doğrudan işlemci üzerinde
çalıştırılabilecek makine kodu içeren bir **çalıştırılabilir dosya** yani
**executable file** oluşur.

```{note}
Bir dilde yazılan programları başka dile çeviren yazılımlara **translator**
yani **çevirici** denir. Eğer hedef dil, kaynak dilden daha düşük seviyede
ise bu tarz çevirici programlara da **derleyici** yani **compiler** adı
verilir.
```

[GCC](https://en.wikipedia.org/wiki/GNU_Compiler_Collection),
[Clang](https://en.wikipedia.org/wiki/Clang),
[MSVC](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B) günümüzde en
çok kullanılan C derleyicilerinden bazılarıdır.

## Derleme Adımları

Bir C programı derlenirken gerçekleşen birkaç temel adım bulunmaktadır.
Elbette her derleyicinin kendi tasarımına göre gerçekleştirdiği onlarca adım
olabilir ve bunlar derleyici tasarımına göre değişiklik gösterecektir. Burada
derleyiciden derleyiciye değişmeyen ve **bilmemiz gereken** temel adımlara
bakacağız.

C dili **separte compilation model**e sahip bir dildir. Bunun ne olduğuna
birazdan değineceğim.

```{important}
Bir C programının nasıl derlendiğini bilmek, C dilindeki bazı kuralların
nedenini anlamakta, karşılaştığımız hata ve uyarıların sebeplerini kavramakta
ve daha optimum kod yazmakta bizler için oldukça faydalı olacaktır.
```

Yazdığımız her `.c` uzantılı dosya birer kaynak dosya yani *source file*
olmaktadır. `.h` dosyaları da birer kaynak dosya olsa da tipik olarak doğrudan
derleyici tarafından ele alınmazlar. Bir `.c` dosyası içerisinde `#include` gibi
direktiflerle koda dahil edilip, `.c` dosyası içierisinde ele alırlar.

Bir programı derlemeye başladığımızda **her bir `.c` dosyası ayrı ayrı ve tek
tek derlenir, daha sonra birleştirilir.** İşte buna **separte compilation
model** diyoruz. Şimdi tek bir `.c` dosyasının başına gelenlere bakalım.

### Preprocessor (Önişlemci)

Bir `.c` dosyası derlenmeye başandığında ilk olarak **önişlemci** yani
**preprocessor** denen ve tipik olarak derleyicinin içerisinde bulunan bir
yazılım çalışır. C kodu içerisinde `#` ile başlayan satırlara **preprocessor
directives** yani **önişlemci komutları** adı verilir. İşte preprocessor bu
satırları işler. Bunların detaylarına sonra bakacağız. Bu işleme ya da bu ana da
**preprocessing time** adı verilir. Preprocessor çıktısı **translation unit**
yani **çeviri birimi** olarak adlandırılır. Translation unit içerisinde artık
`#` ile başlayan satırlar bulunmaz. Derleyiciler tipik olarak bu ara çıktıyı
diskte tutmazlar. Ama deneysel olarak biz bu dosyayı derleyiciden isteyebiliriz.
Aşağıdaki C kodunu ele alalım:

```{code-block} c
:emphasize-lines: 1, 4
:caption: test.c
:lineno-start: 1
#define PI 3.14

double area(double r) {
  return PI * r * r;
}
```

Burada `1` nolu satırda `#define` önişlemci komutu ile bir makro tanımlanmakta
ve `4` nolu satırda da ilgili makro kullanılmaktadır. Derleyici, önişlemciyi
çalıştırdığı zaman `4` nolu satırda bulunan `PI` atomu, `3.14` ile yazısı ile
önişlemci tarafından değiştirilir ve çıktısı olan translation unit dosyasında
artık `1` nolu satır bulunmaz ve `4` nolu satırda da `PI` yerine `3.14` yazar.
GCC'ye `-E` flag'ini vererek translation unit dosyasını tutmasını söyleyebiliriz.
Translation unit dosyaları tipik olarak `.i` uzantısına sahiptir.

```shell
gcc -E test.c -o test.i
```

Sonuç (gereksiz satırları attım):

```{code-block} c
:caption: test.i
:lineno-start: 1
double area(double r) {
  return 3.14 * r * r;
}
```

Eğer `-E` vermeden `gcc` yi doğrudan çağırırsanız bu ara çıktıyı göremezsiniz.

```{note}
Siz de `#include <stdio.h>` ekleyerek aynı işlemi tekrarlayın ve `stdio.h`
içerisinden ne kadar fazla *satır* geldiğini kendiniz görün.
```

Önişlemci çıktısı tam da tahmin ettiğimiz gibi olmuştur. O zaman şimdiye kadar
öğrendiklerimizi çizelim:

```text
---------------
|             |
| Kaynak Kod  |
|    .c       |
|             |
---------------
      |
      |
  Preprocessor
      |
      ↓
---------------
|             |
| Translation |
|    Unit     |
|     .i      |
---------------
```

### Compiler (Derleyici)

Derleme işleminin tamamına yapan yazılıma aslında *compiler* diyoruz. Ama burada
spesifik olarak bir aşamada göre alan yazılıma (ya da yazılım bileşenine)
**compiler** diyoruz. Derleme sırasında bu işlemin geçtiği ana da **compile time**
adını veriyoruz.

Compiler'ın girdisi *translation unit* olmaktadır ve çıktısı da *tipik olarak*
hedef platformun **assembly code** u olmaktadır. Yani derleyici tipik olarak
C kodunu alıp, assembly koduna çevirir. Ama böyle olmak zorunda da değildir.
Biraz sonra *object code* dan konuşacağız. Derleyici assembly'e çevirmeden
*object code* a da çevirebilir.

GCC'de benzer şekilde `-S` seçeneği ile derleyicinin çıkardığı assembly kodunu
alabiliriz. Yukarıdaki koddan devam edelim.

```shell
gcc -S test.c -o test.s
```

Assembly kodlarının bulunduğu dosyalar tipik olarak `.s` uzantısına sahiptir.
Eğer `test.s` dosyasını bir metin editörü ile açarsanız işlemcinizin assembly
dilinde yazılmış kod parçaları görebilirsiniz.

Oluşturulan assembly kodu **assembler** adı verilen bir yazılıma sokulur, burada
artık makine kodlarına çevrilen yazılım **object code**a yani **hedef kod**a
dönüştürülür. Buradaki *object*, *objective* den gelmektedir. OOP'nin
içerisindeki object ile bir ilgisi yoktur. Derleyici isterse translation
unit'ten doğrudan object code'da geçebilir ama hayal etmek açısından arada bir
assembler olduğunu düşünebiliriz.

GCC'nin `-c` flag'i ile object code ya da başka deyişle object file'ı elde
edebiliriz. Bu dosyaların uzantısı tipik olarak `.o` olmaktadır.

```shell
gcc -c test.c -o test.o
```

Object file'lar **sıradan metin dosyaları değildir.** Bu dosyaları metin editör
ile açarsanız anlamlı şeyler çıkmayacaktır. Onun yerine
[objdump](https://www.gnu.org/software/binutils/) gibi başka yazılımlar ile bu
dosyalar analiz edilebilir.

```shell
objdump -d test.o
```

gibi... Bu komutu çalıştırırsanız makine kodlarını ve `objdump` un o kodlardan
geri dönerek gösterdiği sembolik makine dili, assembly, kodlarını görebilirsiniz.

Çizimimizi güncelleyelim:

```text
---------------
|             |
| Kaynak Kod  |
|    .c       |
|             |
---------------
      |
      |
  Preprocessor
      |
      ↓
---------------
|             |
| Translation |
|    Unit     |
|     .i      |
---------------
      |
      |
  Compiler
      |
      ↓
---------------
|             |
|  Assembly   |
|    Code     |
|     .s      |
---------------
      |
      |
  Assembler
      |
      ↓
---------------
|             |
|   Object    |
|    Code     |
|     .o      |
---------------
```

Object code içerisinde artık makine kodları vardır, yazdığımız C kodundan adeta
eser kalmamıştır. Bu dosya içerisinde bir sonraki aşama için ihtiyaç duyulacak
başka *metadata* bilgiler de bulunmaktadır.

### Linker (Bağlayıcı)

Yukarıda bahsettiğim tüm işlemler (önişlemci, derleyici ve assembler) her `.c`
kodu için ayrı ayrı yapılır. Fakat biz günün sonunda tek bir çalıştırılabilir
dosya istiyoruz, bu nasıl olacak? Şu an elimizde her bir `.c` dosyası için bir
`.o` dosyası var. İşte bu aşamada **linker** yani **bağlayıcı** tüm object
file'ları alıp birleştiriyor ve bir adet **executable file** yani
**çalıştırılabilir dosya** çıkartıyor. İşlemin bu anına da **link time** adını
veriyoruz.

```text
---------------      ---------------     ---------------
|             |      |             |     |             |
| Kaynak Kod  |      | Kaynak Kod  |     | Kaynak Kod  |
|    .c       |      |    .c       |     |    .c       |
|             |      |             |     |             |
---------------      ---------------     ---------------
      |                    |                   |
      |                    |                   |
  Preprocessor         Preprocessor        Preprocessor
      |                    |                   |
      ↓                    ↓                   ↓
---------------      ---------------     ---------------
|             |      |             |     |             |
| Translation |      | Translation |     | Translation |
|    Unit     |      |    Unit     |     |    Unit     |
|     .i      |      |     .i      |     |     .i      |
---------------      ---------------     ---------------
      |                    |                   |
      |                    |                   |
  Compiler             Compiler            Compiler
      |                    |                   |
      ↓                    ↓                   ↓
---------------      ---------------     ---------------
|             |      |             |     |             |
|  Assembly   |      |  Assembly   |     |  Assembly   |
|    Code     |      |    Code     |     |    Code     |
|     .s      |      |     .s      |     |     .s      |
---------------      ---------------     ---------------
      |                    |                   |
      |                    |                   |
  Assembler            Assembler           Assembler
      |                    |                   |
      ↓                    ↓                   ↓
---------------     ---------------     ---------------
|             |     |             |     |             |
|   Object    |     |   Object    |     |   Object    |
|    Code     |     |    Code     |     |    Code     |
|     .o      |     |     .o      |     |     .o      |
---------------     ---------------     ---------------
      |                    |                    |
      |→-------------------|-------------------←|
                        Linker
                           |
                           ↓
                    ---------------
                    |             |
                    | Executable  |
                    |    File     |
                    |  ELF, EXE   |
                    ---------------
```

Yukarıdaki çizimde 3 farklı `.c` dosyasından bir C programının derleme
aşamalarını görüyoruz. Her bir `.c` dosyası bağımsız bir şekilde derleniyor,
object code oluşuyor ve sonunda linker bu object file'ları birleştirerek tek bir
çalıştırılabilir dosya üretiyor.

---

Burada her ne kadar 4 farklı aşama veya yazılım var gibi düşünsek de bir derleme
işlemi yaptığımızda temelde 2 aşamadan veya araçtan bahsederiz: **compiler** ya
da **compile time** ve **linker** ya da **link time**. Linker dışındaki tüm
araçları **compiler** a dahil edebilirsiniz. Günümüzde derleyici dediğimiz zaman
bu araçların tümünü içeren yazılımları anlıyoruz yani `.c` dosyalarını alıp,
çalıştırılabilir dosyaya götürebilen ve bu aşamaları yapan araçlara derleyici
diyoruz. Ama eski yıllarda önişlemciler, derleyiciler ve bağlayıcılar ayrı birer
program olarak bulunuyormuş. Şimdilerde ise GCC gibi araçlara bu yazıda
gösterdiğim gibi çeşitli flag'ler geçerek daha alt parçaları çalıştırabiliyoruz.

## Time'lar

Çalıştırılabilir dosyanın çalıştırılma aşamasına da **run time** adı veriliyor.
Yani 4 farklı adım var:

- Preprocessing time
- Compile time (Assembler dahil)
- Link time
- Run time

Bunları bilmek önemli çünkü bir meslektaşınızla konuşurken *Compile time'da mı
hata alıyorsun yoksa link time da mı?* ya da *Compiler mı patlıyor linker mı?*
ya da *Run time'da patladık abi!* gibi cümleler kurabilir ya da duyabilirsiniz.

Biz *derleme* dediğimiz zaman aslında bu sürecin tamamından bahsediyoruz. Yani
genelde *Kodu derle* denildiğinde *Derle ama link etme* denmez. Derleme
sırasında hata alındığında bunun compile time hatası mı yoksa link time hatası
mı olduğunu anlamak hatayı hızlı bulmak açısından faydalı olacaktır. Örneğin
aşağıdaki kodu ele alalım:

```{code-block} c
:caption: main.c
:lineno-start: 1
#include <stdio.h>

double area2(double);

void main(void) {
  printf("Area is :%f", area2(5.5));
}
```

Bu kodu `gcc main.c` ile derlediğimizde

```text
/usr/bin/ld: /tmp/ccaCdmLo.o: in function `main':
main.c:(.text+0x15): undefined reference to `area2'
collect2: error: ld returned 1 exit status
```

hatası arlıyoruz. Bu bir link time hatası, `ld` de linker'ın adı aslında.
Eğer `gcc -c main.c -o main.o` derseniz ve linker'ın çalışmadan sürecin durmasını
sağlarsanız hiçbir hata olmadığını göreceksiniz. Kodda bir hata olsaydı fakat
bu derleme aşamasında fark edilecekti.

Şimdilik bu kadar...

## Kaynaklar

- [](resources.md)
