# Inode Kavramı

Önceki yazıda dosya ve dizin kavramı ile beraber sahiplik, *ownership* ve izin
yani *permission* kavramına bir giriş yapmıştık. Özellikle dizin izinlerini
anlamak için Linux üzerinde bir dosya sisteminin nasıl oluşturulduğunu anlamamız
iyi olacaktır.

Güncel bir Linux çekirdeği 20'den fazla dosya sistemini destekleyebilir. [^1f]
Günlük yaşantımızda Ext2/3/4, Btrfs, FAT32, NTFS, XFS gibi dosya sistemlerini
duymuş olabiliriz. Bir Linux sistemi dendiğinde aksi belirtilmiyorsa genelde
Ext4 dosya sisteminin kullanıldığı düşünülür. Kernel açısından bu kadar farklı
dosya sistemini desteklemek kolay bir iş değildir. Her dosya sisteminin kendine
özgü implementasyon detayları vardır. Kullanıcı tarafına geçtiğimiz zaman da
kernelin altta yatan dosya sistemini soyutlamasını isteriz. Sistem programlama
yapan kişiler olarak tercihimiz altta yatan dosya sisteminden bağımsız olarak
*unified* bir arayüz kullanmak olacaktır. Standart API fonksiyonları ile dosya
sisteminden bağımsız olarak (mümkün olduğunca) işlerimizi yapmak isteriz. İşte
Linux kerneli içerisinde altta yatan dosya sistemini soyutlayan **Virtual File
System (VFS)** isimli bir katman bulunur. Bu katmanın temel amacı, user space
katmanına tek bir arayüz sunmaktır. Temel olarak bizler, `open()`, `write()`,
`read()` ve `close()` sistem fonksiyonlarını alttaki dosya sisteminin ne
olduğunu bilmeden kullanabilir, bu tarz *dosya API* ları ile birçok dosya
sistemindeki dosyalarla işlemler yapabiliriz. Bunda, VFS'in payı da vardır.

```{figure} assets/VFS.gif
:align: center

Alıntıdır: [starlab.io](https://www.starlab.io/blog/introduction-to-the-linux-virtual-filesystem-vfs-part-i-a-high-level-tour)
```

VFS, kernel içerisinde olan bir yapıdır. Kernel programlama yapmadığımız sürece,
örneğin kendi dosya sistemimizi uydurup kernele tanıtmıyorsak, VFS'in detayları
bizler için çok önemli değildir. Aklımızda kalması gereken şey, dosya
sistemlerinin kernel tarafından soyutlanmaya çalışıldığı ve kullanıcıya benzer
arayüzlerle sunulduğudur. Kernel içerisindeki VFS'i bir çekirdek yapı gibi
düşünürsek dosya sistemleri adeta ona bir plugin gibi eklenir. VFS genel dosya
sistemi mantığı sunar ama günün sonunda dosya sisteminin kendi implementasyonu
ile bir şey yapmak gerekirse VFS gider bunu dosya sistemine yaptırır.

## Bazı Terimler

VFS veya genel olarak Linux üzerinde dosyaları konuşmaya başladığımız zaman
karşımıza çıkan 4 adet terim vardır:

- super-block
- inode
- directory
- file

Super-block, bizler için şu aşamada önemli değil. Bu yazıda temel olarak
**inode** kavramını konuşacağız.

## inode Kavramı

Dosya sistemi dediğimiz şeyler, disk üzerinde bulunan veri yapılarıdır.
Kullanıcılar olarak dosya sistemlerinden çeşitli beklentilerimiz bulunur. En
temelde verilerimizi kaybetmeden saklamalarını isteriz. Bunun dışında ani güç
kesintilerinde veri kaybı yaşamamak, ya da minimal yaşamak, bizler için
önemlidir. Temel gereksinimleri sağladıktan sonra bu sefer de performans ile
ilgili özelliklere gözümüz takılır. Örneğin dosya kopyalamak, silmek ya da
aramak hızlı oluyor mu? Kolay bir şekilde yedek ya da *snapshot* alabiliyor
muyuz? Bu yedekler az yer kaplıyor mu? gibi gibi.. İşte bazı dosya sistemleri
bazı problemleri daha etkili çözmek için farklı veri yapıları kullanabilir. VFS,
bizi bunlardan soyutlar.

UNIX'in yazıldığı 1970'li yıllarda ortaya çıkan **Unix File System (UFS)**
tarihsel açıdan önemli bir dosya sistemidir. [^2f] Bilgisayar dünyası, **inode**
kavramı ile tanışmıştır ve UFS'in tasarımı günümüzdeki birçok dosya sistemi
tasarımının temelini oluşturur. `node` düğüm demektir. `i` harfinin ise `index`
olduğu kabul edilmektedir [^3f]. inode kullanımı, bir dosya sistemi tasarlama
kalıbıdır, çerçevesidir, bir veri yapısı olarak düşünebiliriz. Bir dosya sistemi
inode temelli olmak zorunda değildir. Ext2/3/4, XFS, JFS, ZFS, Btrfs, APFS
(Apple File System) sistemlerinin hepsi inode temelli sistemlerdir. Fakat FAT,
exFAT, NTFS gibi dosya sistemleri de inode temelli değildir. Dediğim gibi, bu
bir tasarım kararıdır. Elbette artı ve eksileri vardır. Fakat dikkat ederseniz
*Linux native* diyebileceğimiz dosya sistemlerinin inode temelli olduğunu
görebilirsiniz.

---

İlerlemeden önce basit bir demo yapalım. Bir Linux sistem üzerinde bir sanal
disk oluşturup FAT32 şeklinde formatlayalım ve bunu mount edip birkaç deneme
yapalım.

```shell
ay@2204:~/temp$ dd if=/dev/zero of=mydisk.img bs=1M count=512
512+0 records in
512+0 records out
536870912 bytes (537 MB, 512 MiB) copied, 1.00448 s, 534 MB/s

ay@2204:~/temp$ mkfs.vfat -F 32 mydisk.img
mkfs.fat 4.2 (2021-01-31)
ay@2204:~/temp$ sudo mkdir /mnt/mydisk

ay@2204:~/temp$ sudo mount -o loop mydisk.img /mnt/mydisk

ay@2204:~/temp$ df -h /mnt/mydisk
Filesystem      Size  Used Avail Use% Mounted on
/dev/loop11     511M  4.0K  511M   1% /mnt/mydisk
```

Yukarıda 512 MB'lık, `mydisk.img` isminde bir dosya oluşturuyorum. Bunu FAT32
ile formatlayıp, `/mnt/mydisk` olarak mount ediyorum, detaylara takılmayın.

```shell
ay@2204:/mnt/mydisk$ cd /mnt/mydisk/
ay@2204:/mnt/mydisk$ sudo touch a.txt
ay@2204:/mnt/mydisk$ sudo mkdir b

ay@2204:/mnt/mydisk$ ls -il
total 4
4 -rwxr-xr-x 1 root root    0 Jun 22 16:17 a.txt
5 drwxr-xr-x 2 root root 4096 Jun 22 16:17 b
```

Yukarıda FAT32 diskin içine girip, bir adet dosya ve klasör yaratıyorum ve daha
sonra `ls` komutu ile bunları listeliyorum. `-i` seçeneği inode bilgisini de
görmemizi sağlıyor. inode konusuna birazdan geleceğiz. Burada gördüğümüz `4` ve
`5` sayıları o dosya ve dizinlerin inode numaraları oluyor.

**Burada şunu vurgulamak istiyorum:** FAT32 dosya sisteminin kendisinde bir
dosyaya ait sahiplik bilgisi, kullanıcı ve grup, izin bilgileri, `rwx` gibi yer
almaz. Yani bu bilgiler FAT32 formatlı bir diskin içerisinde saklanmaz. Ayrıca
FAT32 inode temelli bir dosya sistemi de değildir. Peki biz nasıl oluyor da
FAT32 formatında olan bir diskin içerisinde bu bilgileri görüyoruz. **İşte
burada kernel devreye giriyor ve FAT32'yi sanki bir Linux native dosya sistemi
gibi emule ediyor.** Bu tam olarak VFS tarafından yapılan bir şey değil, daha
alt seviyede oluyor (bildiğim kadarıyla) fakat elbette yine kernelin bir
marifeti. Yani bizler kullanıcı olarak bu seviyeden baktığımızda FAT32'nin
içerisinde olduğumuzu bile anlamıyoruz. Elbette Linux üzerinde *Linux native*
dosya sistemlerini kullanmak daha doğru bir tercih olacaktır. Çünkü örneğin Ext
dosya sistemleri içerisinde disk üzerinde bu bilgiler doğrudan yer alır [^4f].

Günün sonunda Linux üzerinde emule edilmiş veya native şekilde bir inode temelli
dosya sistemi görüyoruz. Peki nedir bu inode?

## inode Temelli Dosya Sistemleri

Linux üzerinde bir sıradan dosyayı ele alalım, adı `metin.txt` olsun ve içinde de
bir miktar yazı bulunsun. Bu dosyaya ait çeşitli *üst veriler* yani *meta-data*
verileri olacaktır: dosyanın sahibi olan kullanıcı ve grup, dosya izinleri,
dosyanın yaratılma ve değiştirilme tarihi gibi. inode temelli sistemlerde
bu veriler temelde 3'e bölünerek saklanır.

- Dosyanın adı
- Dosyanın içerisindeki veriler
- Metadata verileri

**İşte dosyanın metadata verilerinin saklandığı blok inode, index node olarak
adlandırılır.** inode içerisinde, konuştuğumuz metadata'lara ek olarak disk
üzerinde dosya içeriğine ait verilerin nerede saklandığı pointer mantığı ile
tutulur. **Fakat inode içerisinde dosya adı yer almaz.** Örnek olarak ext2
dosya sistemini [inceleyebilirsiniz.](https://wiki.osdev.org/Ext2#Inodes)

Her inode'un bir tam sayı karşılığı vardır, 5, 24, 3123123 gibi. Inode dediğimiz
zaman genelde bu değerlerden bahsederiz. Bir dosya sisteminde bir her inode
numarası unique yani tekildir. Fakat bir Linux sisteme birden fazla dosya
sistemi mount edilmişse, ayrı dosya sistemlerinde aynı inode numarasına sahip
farklı dosyalar olabilir. Yani sistemin genelinde unique olması garanti değildir
fakat o dosya sistemi içerisinde unique olacaktır.

Peki *node* ne demek? Burada biraz da tahmin yürüteceğim çünkü net bir bilgi
bulamadım, detaylı da bakmadım işin doğrusu. Dosya sistemlerini hiyerarşik
veri yapılarına benzetebiliriz. Dizinler içerisinde ilerledikçe *tree* benzeri
bir veri yapısı çıkıyor. İşte buradaki her bir eleman bir *node* olarak
düşünülebilir.

```{figure} assets/node-inode.png
:align: center

Kırmızı yuvarlaklar *node* oluyor. Her bir node'u gösteren bir index node yani
*inode* var.
```

Yalnızca dosyalar değil dizinler de birer node olmaktadır. inode'lar ise bu
node'lar hakkında bilgi tutan index node'lardır. Her bir inode'un bir numarası
vardır, çizimde göstermedim. Bir dosya veya dizini işaret etmek, ondan bahsetmek
için o node'a ait inode'un numarasını söylemek yani o numarayı bilmemiz yeterlidir.
Ne demiştik, dosya sistemi içerisinde inode numaralı unique olmaktadır.

---

**Peki dosya isimleri nerede tutulur?**

Bunun için dizin (diğer sistemlerdeki adıyla klasör) nedir, bir anlayalım.

Dizinlerin içerisinde dosyalar ve diğer dizinler bulunur. Gerçekten de fiziksel
klasörlere de benzerler. Inode temelli dosya sistemlerinde dizinlerde tipik
olarak saklanan şey **dosya ismi - inode** çiftidir. Bu ilk başta garip
gelebilir. Yani dosya ismi ne dosyanın içerisinde ne de o dosyaya ait inode
içerisinde saklanır. Dosya ismi, o dosyanın bulunduğu klasörün içerisinde
saklanır. **Dizinler de aslında sıradan dosyalardan farklı değillerdir.** Bir
metin dosyası içerisinde nasıl yazılarımız bulunuyorsa bir dizin içerisinde de o
dizin ile ilgili bilgiler bulunur, ama bunlar bizlerin doğrudan okuması için
tasarlanmamıştır. Bir dizin node'una ait inode içerisinde o node'un bir dosya
değil bir dizin olduğu işaretlenir ve o inode tarafından gösterilen yerdeki
veriler dizin formatında yorumlanır.

```{figure} assets/ext2-directory.png
:align: center

Ext2 dosya sisteminde bir dizin içerisinde saklanan bilgi o dizinde bulunan
dosyaların adları ve o dosyaların inode numaralarıdır.
[Kaynak](https://piazza.com/class_profile/get_resource/il71xfllx3l16f/inz4wsb2m0w2oz)
```

---

Şimdi gelin biraz sistem üzerinde egzersiz yapalım.

```text
.
├── a.txt
└── b
    └── c.txt
```

Yukarıdaki gibi bir yapı oluşturdum, oldukça basit: `a.txt` ve `b/c.txt` var.
Şimdi burada `ls -li` diyelim.

```shell
ay@2204:~/temp/test$ ls -li

total 4
7868892 -rw-rw-r-- 1 ay ay    0 Jun 22 21:01 a.txt
7868890 drwxrwxr-x 2 ay ay 4096 Jun 22 21:01 b
```

En başta gördüğümüz sayılar inode numaraları. `b` bir dizin ama onun da bir
inode numarası var. `stat` kabuk komutu ile dosyalar hakkında daha çok bilgi
elde edebiliriz:

```shell
ay@2204:~/temp/test$ stat a.txt

  File: a.txt
  Size: 0               Blocks: 0          IO Block: 4096   regular empty file
Device: fd00h/64768d    Inode: 7868892     Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/      ay)   Gid: ( 1000/      ay)
Access: 2024-06-22 21:01:20.540916031 +0300
Modify: 2024-06-22 21:01:20.540916031 +0300
Change: 2024-06-22 21:01:20.540916031 +0300
 Birth: 2024-06-22 21:01:20.540916031 +0300
```

Burada gördüğümüz bilgilerin hemen hemen hepsi 7868892 nolu inode veri yapısı
içerisindedir. Sadece dosya ismi inode içerisinde tutulmaz ama onun dışındaki
erişim ve sahiplik bilgileri, zaman bilgileri inode içerisinde tutulur.

Benzer şekilde dizinler için de aynı komutu kullanabiliriz:

```shell
ay@2204:~/temp/test$ stat b

  File: b
  Size: 4096            Blocks: 8          IO Block: 4096   directory
Device: fd00h/64768d    Inode: 7868890     Links: 2
Access: (0775/drwxrwxr-x)  Uid: ( 1000/      ay)   Gid: ( 1000/      ay)
Access: 2024-06-22 21:01:27.557284912 +0300
Modify: 2024-06-22 21:01:25.557179784 +0300
Change: 2024-06-22 21:01:25.557179784 +0300
 Birth: 2024-06-22 21:01:18.348800728 +0300
```

Şimdi `b` klasörüne gidip `ls -lai` diyelim.

```shell
ay@2204:~/temp/test/b$ ls -lai

total 8
7868890 drwxrwxr-x 2 ay ay 4096 Jun 22 21:01 .
7868876 drwxrwxr-x 3 ay ay 4096 Jun 22 21:01 ..
7869056 -rw-rw-r-- 1 ay ay    0 Jun 22 21:01 c.txt
```

Peki buradak `.` ve `..` nedir? Dikkat ederseniz `.` nın solundaki inode numarası
ile `stat b` dediğimizdeki inode numarası aynı: 7868890. Bundan ne anlamalıyız?
Bunlar da bir sonraki yazının konusu olsun 🙂.

## İlgili Kaynaklar

: [^5f] [^6f] [^7f] [^8f]

[^1f]: <https://en.wikipedia.org/wiki/Category:File_systems_supported_by_the_Linux_kernel>
[^2f]: <https://en.wikipedia.org/wiki/Unix_File_System>
[^3f]: <https://en.wikipedia.org/wiki/Inode>
[^4f]: <https://wiki.osdev.org/Ext2#Inode_Data_Structure>
[^5f]: <https://opensource.com/article/19/3/virtual-filesystems-linux>
[^6f]: <https://www.linux.it/~rubini/docs/vfs/vfs.html>
[^7f]: <https://askubuntu.com/a/696543>
[^8f]: <https://unix.stackexchange.com/q/154119/285808>
