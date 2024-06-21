# Dosya Dizin İzin

Gelin, Linux sistemlerinin önemli bir parçası olan dosya ve dizinlerin sahiplik
ve izin yapılarına bir bakalım.

Linux sistemlerde bir dosyanın ve dizinin ait olduğu bir kullanıcı ve bir grup
vardır. Dosya veya dizine verilmiş olan haklara göre bir kullanıcı bazı işlemleri
yapabilir ya da yapamayabilir. Linux sistemler üzerinde çalışırken de genelde
bu izin problemleri ile karşılaşırız. Bu tarz durumlarda konuyu anlamak yerine
eğer hakkımız varsa `sudo` kullanarak problemleri çözmeyi tercih edebiliyoruz
ama bu çok iyi bir yol değil, o yüzden bu konuyu olabildiğince anlamaya çalışalım.

Şimdi gelin bir dizinde bir dosya yaratalım ve yaratılmış dosyaya `ls` komutu
ile bir bakalım.

```shell
ay@2204:~$ touch dosya.txt

ay@2204:~$ ls -l dosya.txt
-rw-rw-r-- 1 ay ay 0 Jun 21 21:14 dosya.txt

```

`ls -l` komutu ile bir dosyanın detaylı bilgilerini görebiliyoruz. En başta 10
karakterlik bir alan var bu durumda: `-`, `rw-`, `rw-`, `r--` şeklinde
ayırabiliriz. En baştaki karakter dosyanın türünü belirtiyor. `-`, bildiğimiz
dosya yani **regular file** demek. Ondan sonra gelen 3 karakter dosyanın sahibi
olan kullanıcının, benim durumumda `ay`, dosya üzerindeki haklarını belirtiyor.
`rw-`, bu kullanıcı bu dosyayı okuyabilir ve yazabilir demek. Bu alanlar `rwx`
bayrakları olarak da geçiyor. `-` olması kullanıcının o dosya üzerinde `x`
hakkının olmadığını gösteriyor. `x`, e`x`ecute kelimesinden geliyor. Daha çok
çalıştırılabilir dosyalarda yani programlarda ve dizinlerde anlamlı oluyor.
İkinci üçlü grup ise dosyanın grup izinlerini gösteriyor. Bu dosyanın grubunun
adı da `ay`, kullanıcı adı ile aynı olması kafanızı karıştırmasın. Bu durumda
`ay` grubunun hakları `rw-` olarak verilmiş. Yani `ay` grubuna dahil olmuş olan
bir kullanıcı dosyayı okuyabilir, yazabilir ama çalıştıramaz. Son üçlü grup ise
diğer kişilerin yani **others** ın haklarını gösteriyor. Eğer kullanıcı `ay`
değilse ve `ay` grubunda değilse bu sefer bu dosya için *others* olmuş oluyor.
`r--` ise *others* kullanıcılarının dosyada sadece okuma yapabildiğini
gösteriyor.

## Dosya Türleri

İlk karakterin dosya türünü gösterdiğini söylemiştik. `-` ise bildiğimiz sıradan
dosyaları gösteriyordu. Peki başka neler var? Detaylara sonra değiniriz, şimdi
kabaca bakalım.

---

`d` dizinleri göstermektedir. Dizinler de dosya sistemi üzerinde adeta birer
sıradan dosya gibi bulunurlar.

```shell
ay@2204:~$ ls -ld /home

drwxr-xr-x 3 root root 4096 May 26 17:59 /home
```

Mesela `/home` bir dizindir ve `ls` ile listelediğimiz zaman `d` ile gösterilir.

---

`p` pipe yani boru dosyaları için kullanılır. Pipe, Linux üzerinde kullanılabilecek
bir prosesler arası haberleşme, IPC, mekanizmalarından biridir. Kabuk üzerinde
`mkfifo` komutu ile yaratabiliriz:

```shell
ay@2204:~/temp$ mkfifo pipe

ay@2204:~/temp$ ls -l pipe
prw-rw-r-- 1 ay ay 0 Jun 21 21:26 pipe
```

Bu sefer de dosya türü olarak `p` karakterini görüyoruz.

---

`s` ise socket gösterimi için kullanılır.

```shell
ay@2204:~$ ls -l /var/run/snapd.socket

srw-rw-rw- 1 root root 0 Jun 21 21:12 /var/run/snapd.socket
```

Sistemde var olan bir socket'i listelediğim zaman `s` karakterini görüyoruz.
Socket'ler de pipe'lar gibi bir IPC mekanizmasıdır fakat detaylar daha sonra.

---

`l` ise sembolik bağlantılar, symbolic links, soft links için kullanılmaktadır.
`ln -s` ile var olan bir dosyaya symlink oluşturup bakalım.

```shell
ay@2204:~/temp$ ln -s dosya.txt soft-link
ay@2204:~/temp$ ln dosya.txt hard-link

ay@2204:~/temp$ ls -l dosya.txt hard-link soft-link

-rw-rw-r-- 2 ay ay 0 Jun 21 21:39 dosya.txt
-rw-rw-r-- 2 ay ay 0 Jun 21 21:39 hard-link
lrwxrwxrwx 1 ay ay 9 Jun 21 21:39 soft-link -> dosya.txt
```

Gördüğünüz üzere `soft-link` isimli symlink dosyası `l` karakteri ile
gösteriliyor. Örneği genişletmek için bir de *hard link* oluşturdum. Hard link
dosyaları normal dosya gibi gözükmektedir. Detaylar sonra.

```shell
ay@2204:~/temp$ ls -il dosya.txt hard-link soft-link

7474044 -rw-rw-r-- 2 ay ay 0 Jun 21 21:39 dosya.txt
7474044 -rw-rw-r-- 2 ay ay 0 Jun 21 21:39 hard-link
7474045 lrwxrwxrwx 1 ay ay 9 Jun 21 21:39 soft-link -> dosya.txt
```

Hard link dosyaların *inode* numarası aynıdır ama şimdi sırası değil.

---

`b` ise *block device* için kullanılır. Bu konu *device driver* yani
*aygıt sürücüsü* konusu ile daha çok ilgilidir. Şu an sadece tanıyoruz.

```shell
ay@2204:~/temp$ ls -l /dev/sda

brw-rw---- 1 root disk 8, 0 Jun 21 21:11 /dev/sda
```

gibi...

---

`c` ise *character device* anlamına gelir. Şimdilik ismen bilelim yeter.

```shell
ay@2204:~/temp$ ls -l /dev/tty

crw-rw-rw- 1 root tty 5, 0 Jun 21 21:13 /dev/tty
```

gibi...

---

Yani gördüğünüz üzere `ls` komutu ile listeme yaptığımız zaman görebileceğimiz
7 tür dosya türü bulunmaktadır. [^1f]

## Dosya İzinleri

Belirttiğim gibi bir dosya ve dizin 3 farklı açıdan 3 farklı izne sahiptir. Bir
dosyanın izni bir kullanıcı, *user*, bir grup, *group* ve kalan kişiler,
*others* için ayrı ayrı belirtilir. Bir dosya okunabilir, *r*, yazılabilir, *w*,
ya da çalıştırılabilir, *x*. `ls` çıktısında ilgili izin yoksa iznin olmayışı
`-` karakteri ile gösterilir. Örneğin bir dosyanın izni `rwxr-x--x` ise bu dosya
sahibi kullanıcı tarafından okunabilir, yazılabilir ve çalıştırılabilir fakat
dosyanın sahibi olan grup yazma yapamaz, diğerlerini yapabilir, kalan
kullanıcılar ise sadece dosyayı çalıştırabilir.

## Dizin İzinleri

Dizinler de aslında dosyalara benziyorlar fakat `rwx` bayrakları tam hayal
ettiğimiz gibi çalışmıyor olabiliyor dizinler üzerinde. Dizin izinlerini
daha iyi anlamak için dosya sistemlerini biraz daha anlamamız iyi olabilir,
örneğin *inode* gibi kavramları. Dizin izinlerine, bu kavramlara biraz
baktıktan sonra devam edelim.

[^1f]: <https://en.wikipedia.org/wiki/Unix_file_types>
