# `rwx`, Dosya, Dizin

```{todo}
Yazı henüz bitmemiştir.
```

Bu yazıda, `rwx` bayrak yani *flag* lerinin dosya ve dizinlerde ne anlama
geldiğini örneklerle anlatmaya çalışacağım.

Önceki yazılarda da bahsettiğim gibi Linux üzerinde bir dosya veya dizinin
izinleri 3 farklı kategoride verilmektedir: *user* yani dosya veya dizine sahip
olan kullanıcının izinleri, *group* yani dosya veya dizine sahip olan grubun
izinler ve *others* yani dosyanın ait olduğu kullanıcı ve grup dışında kalan
kişilerin sahip olduğu izinler. Her bir kategoride de 3 farklı, birbirinden
bağımsız izin türü bulunuyordu: `r`, `w` ve `x`. Şimdi bunların anlamına
bakalım.

## İzinlerin Kontrol Sırası

Kernel tarafında izinler ilk olarak kullanıcı izni ve sonra grup izni olarak
kontrol edilmektedir. İşlem yapmak isteyen kullanıcı, üzerinde işlem yapılmak
istenen dosya veya dizinin sahibi ise *user* izinleri kontrol edilir. Eğer
kullanıcı aynı zamanda dosya veya dizinin sahibi olan **gruba ait olsa bile**
tekrar bir kontrol yapılmaz. Yani kabaca şöyle:

```text
if (kullanıcı == dosya/dizin sahibi kullanıcı)
  user izinlerini uygula
else if (kullanıcı == dosya/dizin sahibi gruba ait)
  group izinlerini uygula
else
  others izinlerini uygula
```

Şimdi bunu göstermek için bir örnek yapalım:

```shell
ay@400:~/sys $ echo "Yazı" > yazi.txt

ay@400:~/sys $ ls -l
total 4
-rw-r--r-- 1 ay ay 6 Jul  6 13:52 yazi.txt

ay@400:~/sys $ chmod u-rw yazi.txt

ay@400:~/sys $ ls -l
total 4
----r--r-- 1 ay ay 6 Jul  6 13:52 yazi.txt

ay@400:~/sys $ groups
ay

ay@400:~/sys $ cat yazi.txt
cat: yazi.txt: Permission denied
```

Yukarıda `yazi.txt` isminde bir dosya oluşturuyorum, içinde de `Yazı` yazıyor.
Bu dosya `ay` kullanıcısına ve `ay` grubuna ait. İlk `ls` komutu ile `ay`
kullanıcısının `rw` haklarının, `ay` grubunun da `r` hakkının olduğunu
görebiliyoruz. Hatta sistemdeki herkesin yani *others* grubunun da okuma hakkı
var. Daha sonra `chmod` komutu ile `ay` kullanıcısının tüm haklarını elinden
alıyorum. İkinci `ls` te bunu görüyoruz, `ay` kullanıcısının hiçbir hakkı yok,
`---` yazıyor. Fakat `ay` grubunun ve aslında sistemdeki tüm kullanıcıların `r`
yani okuma hakkı var. `groups` komutu ile `ay` grubuna ait olduğumu görüyorum.
Fakat `cat` ile dosyayı okumaya çalıştığımda yetki hatası alıyorum. Aslında
dahil olduğum `ay` grubunun okuma hakkı var hatta sistemdeki herkesin yani
*others* ın bile hakkı var ama ben okuyamıyorum! Neden? Çünkü kernel kontrolü
yukarıda yazdığım *pseudo code* gibi yapıyor. Ben dosyanın kullanıcısı olduğum
için dosyanın kullanıcıya ait izinlerine tabi oluyorum. Tutup da şunu demiyor:
"Bu kişi aynı zamanda dosyanın ait olduğu grupta, onun izinlerini de
uygulayayım." Elbette böyle bir durumda gariplikler ortaya çıkabiliyor, eğer
izinleri bu şekilde verirseniz. Yani dosya size ait, siz okuyamıyorsunuz ama
sizin dışınızdaki herkes okuyabiliyor. Kernel *others* ya da *group* izinlerine
bakarak size otomatik yetikler vermiyor.

**Bu yüzden tipik olarak dosya/dizin izinlerinde izinler kullanıcıdan gruba ve
diğerleri kısmına geçerken genelde kısıtlanarak geçer, diğer türlü garip
durumlar oluşabiliyor.** Bir başka deyişle grubun izinleri kullanıcıdan,
diğerlerinin izinleri de gruptan fazla olmuyor.

---

Şimdi çeşitli minik deneyler üzerinden izinleri anlamaya çalışalım. Dosya
üzerindeki izinler kolay anlaşılıyor fakat dizin üzerinde izinler, özellikle `x`
izni, biraz karışabiliyor.

## Tekrar: Dizin ve inode Kavramı

Önceki yazılarda inode kavramından ve dizinlerin aslında ne olduğundan
bahsetmiştim. Bunu iyi anlarsak özellikle dizin izinlerinde işimiz daha
kolaylaşacaktır. O yüzden biraz tekrar yapalım.

Şimdi bir dosya yarattığımız zaman, dosyanın içerisinde bir içerik oluyor,
dosyanın adı oluyor ve dosya ile ilgili çeşitli bilgiler oluyor: izin bilgileri,
yaratılma tarihi gibi şeyler. Bu tarz bilgileri *meta data* diyebiliriz. Yani
bir dosyanın içeriğinin yanında dosya ile ilgili tutulan başka bilgiler de var.
Linux, bu bilgileri 3 parçaya bölüyor:

- Dosyanın adı
- *Meta data* bilgileri
- Dosyanın içeriği

Her bir dosyaya ait bir **inode** bulunuyor. İşte inode içerisinde dosyaya ait
*meta data* bilgileri tutuluyor. inode içerisinde tutulan bilgilerden biri de
dosyanın içeriğinin disk üzerinde nerede olduğu. Bunu C dilindeki pointerlara
benzetebiliriz. inode içerisinde adeta dosyanın içindeki verinin diskte nerede
olduğunu tutan bir pointer bulunuyor. Dosya adı ise ne inode, ne de dosya
içeriğinde tutuluyor.

Linux üzerinde dizin yani klasör dediğimiz şeyler de aslında birer dosyadır,
fakat özel dosyalardır. İçerlerinde ise `inode-dosya ismi` çiftleri adeta bir
liste gibi bulunur, dizin dediğimiz özel dosyanın içerisinde bu bilgiler yer
alır. Yani dosyanın ismi adeta dizinin bir özelliğidir. Hemen minik bir örnek
yapalım:

```text
a
├── b.txt
├── c.txt
└── d
    └── e.txt
```

Burada `a` isimli bir dizin var. İçinde `b.txt` ve `c.txt` dosyaları var, bir de
`d` isimli bir dizin var. Onun içerisinde de `e.txt` bulunuyor.

```shell
$ ls -li a

total 4
392227 -rw-r--r-- 1 ay ay    0 Jul  6 17:59 b.txt
392228 -rw-r--r-- 1 ay ay    0 Jul  6 17:59 c.txt
392354 drwxr-xr-x 2 ay ay 4096 Jul  6 17:59 d
```

Şimdi burada `a` nın içerisindeki girdilerin inode sayılarını da görüyoruz. O
halde `a` dediğimiz dizinin içerisinde aslında şöyle bir şey yazıyor gibi
düşünebiliriz:

```text
392227 b.txt
392228 c.txt
392354 d
```

Benzer durum `d` için de geçerli:

```text
$ ls -li a/d

total 0
392356 -rw-r--r-- 1 ay ay 0 Jul  6 17:59 e.txt
```

Benzer şekilde `d` dediğimiz dizinin içinde de şöyle bir bilgi var:

```text
392356 e.txt
```

Şimdi `a` nın içeriğini tekrar düşünelim. Linux'ta dosya uzantıları pek anlamlı
değil. Yani `b.txt` yerine `b` diye de bir metin dosyası oluşturabilirdim. `a`
nın içeriğine baktığımız zaman bir liste şeklinde `inode-dosya ismi` çiftleri
görüyoruz. Peki buradan `b` veya `d` bir dosya mı, dizin mi hatta daha da
açarsak socket mi anlayabiliyor muyuz? Hayır. Bunun için numarası verilen
inode'a gidip "Kardeş sen nesin?" dememiz gerekiyor. Dosya türüne bakmak, sık
yapılan bir iş. `ls` dediğimiz zaman bile dosya türleri gösteriliyor. Özellikle
içeriği fazla olan dizinlerde veya recursive listelemede her girdinin türüne
bakmak için inode'a gitmemiz oldukça maliyetli. Bu yüzden Ext dosya sistemleri
tipik olarak dizin girdisi içerisinde dosya türü ile ilgili de bir bilgi
tutuyor. Benzer bilginin aynısı o dosyanın inode'u içerisinde de yer alıyor.
Fakat kavramları konuşmamız için dizin yapısını sadece `inode-dosya ismi` çifti
olarak hayal etmek bizi yanıltmıyor. İşleri basit tutmak için böyle düşünmeye
devam edelim. Girdi türünün dizin içerisinde de tutulmasını işleri hızlandırmak
için bir *önbelleğimsi* mekanizma olarak hayal edebilirsiniz.

Yukarıdaki organizasyonu şöyle hayal edebiliriz:

```{figure} assets/inode-icerik-iliskisi.png
:align: center

inode temelli yapıyı bu şekilde hayal edebiliriz. inode veri yapısı içerisinde
dizin ve dosyaların `Tür` kısımlarının farklı olduğuna dikkat ediniz.
```

---

Sıradan dosyalar üzerinde **read** ve **write** ın ne anlama geldiğini biliyoruz.
**execute** kısmına en son bakalım. İş, dizinlere geldiği zaman daha çok karışıyor.

Ne demiştik, dizinler aslında `inode-dosya adı` çifti tutan özel dosyalardır.
Diyelim ki bir dizin üzerinde sadece **read** hakkımız var ve başka bir hakkımız yok.
Bu durumda ne yapabiliriz? Alabileceğimiz iki bilgi var, içersindeki dizin ve dosyaların isimleri ve inode bilgileri. `a` dizininde sadece `r` hakkım olsun:

```shell
$ ls -l

total 4
dr--r-xr-x 3 ay ay 4096 Jul  6 17:59 a
```

`a` nın içerisinde var olanları görebiliyor muyum? E hemen deneyelim:

```text
$ ls -l a

ls: cannot access 'a/b.txt': Permission denied
ls: cannot access 'a/c.txt': Permission denied
ls: cannot access 'a/d': Permission denied
total 0
-????????? ? ? ? ?            ? b.txt
-????????? ? ? ? ?            ? c.txt
d????????? ? ? ? ?            ? d
```

Hmm, ilginç şeyler oluyor. `a` nın içerisinde olan dizin ve dosyaları gördük fakat erişim hataları da aldık. Yani içinde olanları biliyoruz fakat içerisinde olan şeylerin bilgileri elimizde yok, `?` işareti olarak geldi. Peki neden? **Çünkü dizin üzerinde execute yani `x` hakkımız yok!**. Dizinler üzerindeki `x` hakkını şuna benzetebiliriz: Dizini okuyarak içerisinde bulunanların adlarını ve inode bilgilerini aldık. Fakat içerideki şeylerin bilgilerini edinmemiz için her birinin inode veri yapısına ulaşmamız gerekiyor. İşte bir dizinde *execute* hakkımız olmadığı zaman o dizinin altında bulunan inode'lara erişemiyoruz gibi düşünebiliriz. Örneğin `b.txt` nin inode değerini biliyoruz fakat `a` dizininde `x` hakkımız olmadığı için bu inode'un içeriğine bakamıyoruz. **Dizinler üzerindeki execute hakkını adeta bir geçiş noktası gibi de düşünebiliriz.** **O dizinin içine de giremiyoruz.**

```text
$ cd a

bash: cd: a: Permission denied
```

Şöyle bir benzetme yapabiliriz:

Dizinleri kapısı olan birer oda gibi düşünelim. Bu kapının bir camı var ve içeride de ışık var. Peki içeride ne var? Dizinin içerisinde bulunan dosya ve dizinlerin isim ve inode bilgileri. Dizinler üzerinde `r` ve `x` haklarını şöyle hayal edebiliriz:

- `r` YOK, `x` YOK: Kapının anahtarı yok, içerideki ışık da kapalı. İçeriye giremiyoruz. Kapının camından baksak da içersi gözükmüyor. Yani dizinin içerisinde ne olduğunu da bilmiyoruz.
- `r` VAR, `x` YOK: Kapının anahtarı yok, fakat içerisinin ışığı yanıyor. İçeriye giremiyoruz. Ama kapının camından içeriye bakarsak ne olduğu gözüküyor. Dizinin içerisinde ne var ve nerede duruyor biliyoruz. Ama anahtarımız olmadığı için kapıyı açıp, içeriklere erişemiyoruz.
- `r` YOK, `x` VAR: Kapının anahtarı var, fakat içerisi karanlık. İçeride ne olduğunu göremiyoruz. Ama bildiğimiz bir içerik varsa ona devam edebiliyoruz. Yani zifiri karanlık ama yollar açık. Sadece nereye gideceğimizi bilirsek ilerleyebiliriz.
- `r` VAR, `x` VAR: Kapının anahtarı var, içerisi de aydınlık. Her şeyi görüp, yolumuza devam edebiliyoruz.

İşte kendimizi dosya sisteminde odalar yani dizinler arasında gezen biri olarak hayal edersek `cd` komutu ile ilgili odaya yani dizine girmeye çalışıyoruz. `x` hakkımız yoksa yani odanın anahtarı bize verilmediyse içeriye de giremiyoruz.

---

Şimdi yukarıdaki örneğe geri dönelim. Sadece `r` hakkımız vardı. Odanın içine bakabildik, ışığı yanıyor ama içeriye giremiyoruz. Dikkatinizi bir şey çekti mi? İsimle beraber bir bilgi daha var: tür bilgisi yani `-` ve `d` karakterleri. Demiştik ki bunlar aslında ilgili inode içerisinde bulunuyor. **Bunlara erişemiyorsak, `ls` komutu `d` ve `-` bilgilerini nerden alıyor?** Biraz önce de belirttiğim gibi aslında dizin içerisinde erişim kolaylığı için bu bilgiler saklanıyor. Bu sayede `r` hakkı ile görebiliyoruz. Yani aslında `inode-isim-tür` şeklinde üçlü bir veri seti var gibi düşünebiliriz. Ama bu kısım bence gerçekten önemli değil. Yani `r` hakkı varken tür bilgisi görebiliyor muyuz sorusu bence çok detay, ana konudan sapmayalım.

O zaman bir de inode bilgisini bulmaya çalışalım içerideki dosya ve dizinlerin. `a` yı okuyabildiğimize göre bu bilgileri alabilmemiz lazım değil mi?

```shell
$ ls -il a

ls: cannot access 'a/b.txt': Permission denied
ls: cannot access 'a/c.txt': Permission denied
ls: cannot access 'a/d': Permission denied
total 0
? -????????? ? ? ? ?            ? b.txt
? -????????? ? ? ? ?            ? c.txt
? d????????? ? ? ? ?            ? d
```

Hmm, inode bilgisi yerine yine `?` aldık, en sağdaki. Niye böyle oldu? Bu `ls` komutunun inode bilgisini edinme yöntemi ile ilgili. `strace` ile çalıştırırsanız [statx](https://man7.org/linux/man-pages/man2/statx.2.html) sistem çağrısını yaptığını görebilirsiniz. Bu çağrı direkt hedef dosya üzerinde yapılıyor, `a/b.txt` gibi. Fakat `a` üzerinde `x` hakkımız olmadığı için bu sistem çağrısını `ls` komutunun yetkisi yetmiyor. Yani `ls`, `a` nın kapısından geçip içeriye ulaşıp bilgileri toplamak istiyor. Ama inode değerini alabileceğimizi size göstereceğim:

```text
$ find . -name b.txt -printf "%f - %i\n"

b.txt - 392227
```

`find` komutu ile aynı sistemde `b.txt` nin inode değerini alabildik. `strace` ile bakarsak `find` komutunun [stat](https://man7.org/linux/man-pages/man2/stat.2.html) çağrısı yaptığını görüyoruz. Burada `statx` veya `stat` ile ilgili bir çıkarım yapmıyorum. Demek istediğim şey `ls` ve `find` farklı birer program olduğu için farklı davranabiliyorlar. `find` komutu, dizin üzerinde execute hakkı olmadan içerisinde bulunan dosyanın inode bilgisini bize verebiliyor.

---

Bence zor kısmı atlattık. Dizinde `r` hakkımız varsa içeriğini görebiliyoruz ama `x` hakkımız yoksa o içeriklere erişemiyoruz, sadece adını görmüş oluyoruz hatta dizinin *içine de giremiyoruz.*

Şimdi `a` üzerinde sadece `x` hakkımız olsun.

```text
$ ls -l

total 4
d--xr-xr-x 3 ay ay 4096 Jul  6 17:59 a
```

`a` nın içeriğine bakabilir miyiz?

```text
$ ls -l a

ls: cannot open directory 'a': Permission denied
```

Hayır! Oda benzetmesine devam edelim. `a` nın kapıları açık ama içerisi zifiri karanlık. İçinde ne var bilmiyorum. Ama biz içinde `b.txt` olduğunu biliyoruz. Bunun içeriğine erişebilir miyiz?

```text
$ cat a/b.txt

Ben b.txt nin icerigiyim
```

Cevabımız evet! Yani `a` dan geçip `b.txt` ye ulaştım ama `b.txt` nin varlığını bildiğim için.

Benzer şekilde `cd a` diyerek de `a` nın içine girebiliyorum ama her yer karanlık. İçeride iken `ls` dersem yine hata alıyorum, göremiyorum ki içinde ne var!

---

Peki dizinlerdeki `w` hakkı nedir. Dizinleri `inode-dosya ismi` tutan bir dosya gibi düşünürsek burada yazma hakkımız varsa bu listeyle de oynayabiliriz demek. Ne yapabiliriz? Dosya isimlerini değiştirebiliriz. Yeni dosyalar ekleyebiliriz ve **dosya silebiliriz.** Dosya silme işi ilginç. Bir dosyayı silmek için o dosyaya yazma hakkımızın olması gerekmiyor. O dosyanın bulunduğu dizine yazma hakkımız olsa bu yeterli. Bir dosyayı sildiğimiz zaman diskten silineceği garanti değil, bu konuya hard ve soft link konusunda değiniriz. Ama bir örnek yapalım.

`a` ya `rwx` haklarımı verip içine girdim, `b.txt` dosyasından herkesin tüm haklarını aldım.

```shell
$ ls -lah
total 16K
drwxr-xr-x 3 ay ay 4.0K Jul  6 17:59 .
drwxr-xr-x 3 ay ay 4.0K Jul  6 17:59 ..
---------- 1 ay ay   25 Jul  6 19:16 b.txt
-rw-r--r-- 1 ay ay    0 Jul  6 17:59 c.txt
drwxr-xr-x 2 ay ay 4.0K Jul  6 17:59 d

ay@400:~/sys/a $ cat b.txt
cat: b.txt: Permission denied

ay@400:~/sys/a $ echo "yazma denemesi" > b.txt
bash: b.txt: Permission denied
```

Ne yazabiliyorum ne okuyabiliyorum. Peki silebiliyor muyum? Evet! Silebiliyoruz çünkü `a` ya yazma hakkımız var. `rm b.txt` dediğimiz zaman `remove write-protected regular file` diyor, dosyada yazma hakkımız olmadığı için emin misin diyor fakat buna `y` dersek çatır çutur siliyor.

---

`a` dizindeki haklarımızı `-w-` konumuna getirelim. Bu durumda `cd` ile giremeyiz. Ama *uzaktan* değişiklikler yapabilir miyiz?

```text
$ ls -l
total 4
d-w-r-xr-x 3 ay ay 4096 Jul  6 19:40 a

ay@400:~/sys $ rm a/c.txt
rm: cannot remove 'a/c.txt': Permission denied

ay@400:~/sys $ touch a/f.txt
touch: cannot touch 'a/f.txt': Permission denied
```

Hmm, ilginç. `a` da `w` hakkım var. O yüzden `inode-dosya adı` tablosunu değiştirebiliyorum. Peki neden `c.txt` yi silemedim? Çünkü `a` da `x` hakkım yok. `rm` ile dosya silerken olan birkaç işlem var. `a` nın içerisinden `c.txt` satırının silindiği doğru fakat `c` nin inode'u içerisinde de değişiklik yapılması gerekiyor, örneğin hard link sayısı 1 eksiltilecek. Fakat `a` da `x` hakkım olmadığı için `c` nin inode'una da erişemiyorum.

**O yüzden bir dizinde `x` hakkı olmadan `w` hakkının olması pratikte anlamlı olmamaktadır.** [^1f]

```{todo}
Dosya execute kavramından devam et.
```

## İlgili Bağlantılar

- <https://unix.stackexchange.com/q/13858>
- <https://unix.stackexchange.com/q/18095>

[^1f]:<https://unix.stackexchange.com/q/149184>

