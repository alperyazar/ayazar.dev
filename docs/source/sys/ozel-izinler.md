# Özel Dosya İzinleri

Şimdiye kadar bir dosya veya dizin izni hakkında konuşurken 3 farklı gurptan
(user, group, other) ve 3 farklı izinden, `rwx`, bahsettik. Linux sistemlerde
bu izinlerin dışında farklı senaryolarda bize faydalı olabilecek birkaç izin
daha bulunmaktadır. `rwx` izinlerinin her biri 1-bit ile ifade edilebilir, 3
farklı kategori olduğu için de dosya izinleri 9-bit ile tutulabilir. İşte bu
özel izinler de 3-bit ile tutulmaktadır, yani 3 farklı türde izin göreceğiz.
Toplamda 12-bit ediyor

Şimdi onlara bir bakalım.

## Sticky Bit (`1000`)

Sticky Bit, ilk olarak 1975 tarihinde Unix'in 5. sürümünde tanıtılmıştır. İlk
kullanımı, sadece çalıştırılabilir (executable) dosyalar içindir. Bu bit'i set
edilmiş çalıştırılabilir dosyaların `text` alanı çalıştırıldıktan ve çıktan
sonra swap alanında saklanırmış. Bu bit tipik olarak sık kullanılan programların
hızlı çalışmasını sağlmak içinmiş. Swap alanına *yapıştıkları* için *sticky*
olarak adlandırılmışlar. [^1f]

Günümüzde Linux gibi Unix benzeri işletim sistemlerini çok daha karmaşık ve
verimli bellek yönetim mekanizmalarının olmasından dolayı bu bit başka amaçlar
için kullanılmaktadır.

### Dizinlerde Sticky Bit

Bir dizinin sticky bit'i set edildiği zaman çeşitli davranış değişiklikleri
olmaktadır. Normalde bir dizine bir kişinin `wx` hakkı varsa o kişi o dizin
içerisindeki dosyaları silebilir ya da yeniden adlandırabilir. Bunu yapabilmesi
için sildiği dosyalara hakkı olması gerekmemektedir. Örnek:

```shell
alper@brs23-2204:/opt/sys$ ls -ld dizin
drwxrw---- 3 alper alper 4096 Jul 14 18:44 dizin

alper@brs23-2204:/opt/sys$ cd dizin
alper@brs23-2204:/opt/sys/dizin$ ls -l
total 4
-rw-rw-r-- 1 user1 user1    0 Jul 14 18:43 1
-rw-rw-r-- 1 user1 user1    0 Jul 14 18:44 2
drwxrwxr-x 2 user1 user1 4096 Jul 14 18:44 3

alper@brs23-2204:/opt/sys/dizin$ echo "bir" > 1
bash: 1: Permission denied
alper@brs23-2204:/opt/sys/dizin$ rm 1
rm: remove write-protected regular empty file '1'? y

alper@brs23-2204:/opt/sys/dizin$ mv 2 22

alper@brs23-2204:/opt/sys/dizin$ ls -l
total 4
-rw-rw-r-- 1 user1 user1    0 Jul 14 18:44 22
drwxrwxr-x 2 user1 user1 4096 Jul 14 18:44 3
```

Burada gördüğünüz üzere `dizin` üzerinde `alper` kullanıcısının tam yetkisi var.
İçerisindeki dosyalar ise `user1` e ait ve `alper` kullanıcısının sadece okuma
yetkisi var. Fakat dizin üzerinde `wx` yetkisi olduğu için `user1` e ait olan
dosyaları silebiliyor veya yeniden adlandırabiliyor. İşte sticky bit, burada
devreye giriyor.

**Sticky bit'i set edilmiş bir dizinin içerisinde yaratılan dosyaları sadece o
dosyanın sahibi veya sticky bit'i set edilmiş dizinin sahibi ya da root
kullanıcısı o dosyayı silebilir veya yeniden adlandırılabilir.** Eğer bu bit
olmasaydı, o dizinde yazma ve execute hakkı olan herkes altındaki dosyalarda bu
tarz değişiklikler yapabilirdi.

Örneği biraz değiştirelim:

```shell
alper@brs23-2204:/opt/sys$ ls -ld dizin
drwxrwx--- 3 root alper 4096 Jul 14 18:50 dizin

alper@brs23-2204:/opt/sys$ cd dizin
alper@brs23-2204:/opt/sys/dizin$ ls -l
total 4
-rw-rw-r-- 1 user1 user1    0 Jul 14 18:50 1
-rw-rw-r-- 1 user1 user1    0 Jul 14 18:50 2
-rw-rw-r-- 1 user1 user1    0 Jul 14 18:44 22
drwxrwxr-x 2 user1 user1 4096 Jul 14 18:44 3

alper@brs23-2204:/opt/sys/dizin$ rm 1
rm: remove write-protected regular empty file '1'? y
alper@brs23-2204:/opt/sys/dizin$ mv 2 222

alper@brs23-2204:/opt/sys/dizin$ ls -l
total 4
-rw-rw-r-- 1 user1 user1    0 Jul 14 18:44 22
-rw-rw-r-- 1 user1 user1    0 Jul 14 18:50 222
drwxrwxr-x 2 user1 user1 4096 Jul 14 18:44 3
```

Burada artık dizinin sahibi değil, dizinin grubuna ait bir kullanıcıyım. Ama
grup hakları da `rwx` olarak verildiği için yapabildiğim tüm şeyleri hala
yapabiliyorum. Şimdi `dizin` in sticky bit'ini set edelim.

```shell
alper@brs23-2204:/opt/sys$ sudo chmod +t dizin

alper@brs23-2204:/opt/sys$ ls -ld dizin
drwxrwx--T 3 root alper 4096 Jul 14 18:50 dizin
```

Dizinin sahibi `root` olduğu için `chmod` u `sudo` ile çağırmam gerekti. `ls`
ile baktığım zaman others'ın `x` inin yerinde bu sefer `T` görüyorum. `T`, sticky
bit set edildiyse ve others'ın `x` hakkı yoksa gözüküyor. Others'a `x` verirsek
`t` oluyor, ufalıyor. Tarihsel olarak programların `text` alanının cachelenmesi
için kullanıldığından `t` harfi seçilmiş diye anlıyorum.

```shell
alper@brs23-2204:/opt/sys$ sudo chmod o+x dizin

alper@brs23-2204:/opt/sys$ ls -ld dizin
drwxrwx--t 3 root alper 4096 Jul 14 18:50 dizin
```

Hala grup'tan dolayı dizin üzerinde tam yetkim var.

```shell
alper@brs23-2204:/opt/sys$ cd dizin/

alper@brs23-2204:/opt/sys/dizin$ ls -l
total 4
-rw-rw-r-- 1 user1 user1    0 Jul 14 18:44 22
-rw-rw-r-- 1 user1 user1    0 Jul 14 18:50 222
drwxrwxr-x 2 user1 user1 4096 Jul 14 18:44 3

alper@brs23-2204:/opt/sys/dizin$ rm 22
rm: remove write-protected regular empty file '22'? y
rm: cannot remove '22': Operation not permitted

alper@brs23-2204:/opt/sys/dizin$ mv 222 2222
mv: cannot move '222' to '2222': Operation not permitted
```

Fakat bu sefer sticky bit'ten dolayı `user1` e ait olan şeyleri silemedim, yeniden
adlandıramadım. Fakat kendime ait olan bir şeyler yapabiliyorum:

```shell
alper@brs23-2204:/opt/sys/dizin$ touch alper
alper@brs23-2204:/opt/sys/dizin$ mv alper alper2
alper@brs23-2204:/opt/sys/dizin$ rm alper2
```

İşte dizinlerdeki sticky bit bu işe yarıyor. Pratikte nerede görüyoruz? Tipik
örneği `/tmp` dizinidir.

```shell
alper@brs23-2204:~$ ls -ld /tmp
drwxrwxrwt 22 root root 4096 Jul 14 18:48 /tmp
```

Gördüğünüz üzere tüm kullanıcıların, others, `rwx` hakları vardır çünkü `t`
görüyoruz. Ayrıca sticky bit set edilmiştir. Bu demek oluyor ki herkes `/tmp`
altına bir şeyler yazabilir ama sticky bit set olduğu için sadece kendisine
ait olanları silebilir veya yeniden adlandırabilir. Bu sayede bir kullanıcı
dizinde `rwx` hakkı olmasına rağmen diğer kullanıcıların dosyalarına salça olamaz.

---

Kernel 3.6 ile beraber bu bite bir anlam daha yüklenmiştir. [^7f] [^13f] Symlink
ile tetiklenen [TOCTOU](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use)
atakların engellenmesi amaçlanmıştır:

```text
The solution is to permit symlinks to only be followed when outside
a sticky world-writable directory, or when the uid of the symlink and
follower match, or when the directory owner matches the symlink's owner.
```

### Dosyalarda Sticky Bit

Linux üzerinde dosyalara verilen sticky bit'lerin bir anlamı yoktur. Diğer
UNIX türevi işletim sistemlerinde farklı anlamlar içerebilir. [^1f] Yine de
Linux üzerinde istersek verebiliyoruz:

```shell
alper@brs23-2204:~/sys$ chmod +t script.sh

alper@brs23-2204:~/sys$ ls -l script.sh
-rwxrw-r-T 1 alper alper 30 Jul 14 19:12 script.sh
```

## Set UID, SUID (`4000`)

Bu flag *set user identity* anlamındadır. [^2f]

Dosya ve dizindeki anlamına ayrı ayrı bakalım. Çoğunlukla dosyalarda
kullanılmaktadır.

### Dosyalarda SUID

SUID, genellikle çalıştırılabilir dosyalarda kullanılmaktadır. Biz bir
çalıştırılabilir dosyayı çalıştırdığımızda oradan bir proses yaratılır. Dosya
sistemi üzerinde yapılacak tüm işlemlerin kontrolü için bu prosesin *efektif*
kullanıcı ve grup ID'si, EUID ve EGID, kullanılır. `./program` dediğimizde
yaratılan proses bizim kullanıcımızın ve dahil olduğumuz grubun haklarına sahip
olacaktır. Bir başka deyişle EUID ve EGID, kendi UID ve GID değerimizle aynı
olacaktır. `program` dosyasından yaratılan proses, o prosesi çalıştıran
kullanıcının ID'leri ile çalışır, bunlara *real* değerler de denmektedir,
`program` dosyasının diskteki UID ve GID değerleri ile değil.İşte SUID biti, bu
davranışı değiştirmektedir.

Kolaylık olsun diye aşağıdaki C programını ChatGPT'ye yazdırdım:

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    // Get Real UID and GID
    uid_t ruid = getuid();
    gid_t rgid = getgid();

    // Get Effective UID and GID
    uid_t euid = geteuid();
    gid_t egid = getegid();

    // Print Real UID, Real GID, Effective UID, and Effective GID
    printf("Real UID: %d\n", ruid);
    printf("Real GID: %d\n", rgid);
    printf("Effective UID: %d\n", euid);
    printf("Effective GID: %d\n", egid);

    return 0;
}
```

Bunu `id` olarak derledim.

```shell
alper@brs23-2204:~/sys$ ./id
Real UID: 1001
Real GID: 1001
Effective UID: 1001
Effective GID: 1001

alper@brs23-2204:~/sys$ id
uid=1001(alper) gid=1001(alper)
```

Çalıştırdığım zaman benim ID değerlerim ile çalışıyor.

`id` programının sahibi ben olsam bile ondan yaratılan process'ler onu yaratan
kullanıcının hakkıyla çalışıyor:

```shell
user1@brs23-2204:/opt$ ./id
Real UID: 1002
Real GID: 1002
Effective UID: 1002
Effective GID: 1002

user1@brs23-2204:/opt$ ls -l id
-rwxr-xr-x 1 alper alper 16136 Jul 14 19:42 id

user1@brs23-2204:/opt$ id
uid=1002(user1) gid=1002(user1) groups=1002(user1)
```

`user1` in ID değerleri `1002` ve görüldüğü üzere program bu haklarla çalışıyor.

---

Şimdi SUID flag'ini `chmod` komutu ile set edip duruma bakalım:

```shell
alper@brs23-2204:/opt$ chmod u+s id

alper@brs23-2204:/opt$ ls -l id
-rwsr-xr-x 1 alper alper 16136 Jul 14 19:42 id
```

`ls` ile baktığımızda `user` ın `x` nin yerinde `s` yi görüyoruz. Şimdi programı
iki kullanıcıdan tekrar çalıştıralım:

```shell
alper@brs23-2204:/opt$ ./id
Real UID: 1001
Real GID: 1001
Effective UID: 1001
Effective GID: 1001

user1@brs23-2204:/opt$ ./id
Real UID: 1002
Real GID: 1002
Effective UID: 1001
Effective GID: 1002
```

Dosyanın sahibi çalıştırınca bir fark yok fakat başka kullanıcıdan
çalıştırdığımda `Effective UID`, dosyanın sahibi kullanıcı oldu, programı
çalıştıran kullanıcı değil. Bu durumda bu program `alper:user1` hakları ile
çalışacaktır. Peki bu ne işe yarayacak?

---

Kullanıcılar ile ilgili bilgiler `/etc/passwd` ve `/etc/shadow` dosyalarında
saklanmaktadır.

```shell
$ ls -l /etc/passwd /etc/shadow
-rw-r--r-- 1 root root   2983 Jul 14 11:01 /etc/passwd
-rw-r----- 1 root shadow 1663 Jul 14 11:01 /etc/shadow
```

Her iki dosyada da standart kullanıcıların değişiklik yapma hakkı yoktur. Fakat
bizler `passwd` gibi komutlarla kendi şifremizi değiştirebiliriz, `sudo` olmadan.
Peki nasıl oluyor da standart kullanıcılar bu dosyaları değiştirebiliyor?

```shell
alper@brs23-2204:~$ which passwd
/usr/bin/passwd

alper@brs23-2204:~$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 59976 Feb  6 15:54 /usr/bin/passwd
```

`passwd` programının sahibi `root` kullanıcısı ve SUID bayrağı set edilmiş bir
dosya. Biz bu dosyayı çalıştırdığımız zaman aslında programı `root` kullanıcısının
hakları ile çalıştırıyoruz. Bu sayede `passwd` diyerek sadece `root` un yazma
hakkı olduğu dosyaları değiştirebiliyoruz.

Benzer bir durum `sudo` programında da vardır.

```shell
alper@brs23-2204:~$ which sudo
/usr/bin/sudo

alper@brs23-2204:~$ ls -l /usr/bin/sudo
-rwsr-xr-x 1 root root 232416 Apr  3  2023 /usr/bin/sudo
```

`sudo` programının da SUID biti set olduğu ve sahibi `root` olduğu için aslında
program `root` yetkileri ile çalışmaktadır. Bu sayede istediğimiz programı
çalıştırırken, fork/exec gibi mekanizmalarla, istediği kullanıcı ile programı
çalıştırabilmektedir. Buradaki mekanizma `passwd` tan biraz daha karmaşık ama
özünde SUID bitinin marifeti diyebiliriz.

```shell
$ sudo ./id
Real UID: 0
Real GID: 0
Effective UID: 1001
Effective GID: 0
```

Benzer durum `ping` programında da vardı [^3f] ama artık gerek duyulmamaktadır
kernel ayarlarından dolayı [^4f] , örnekler çoğaltılabilir.

```shell
alper@brs23-2204:~$ which ping
/usr/bin/ping

alper@brs23-2204:~$ ls -l /usr/bin/ping
-rwxr-xr-x 1 root root 76672 Feb  5  2022 /usr/bin/ping
```

Eğer SUID set edilen dosyada kullanıcının `x` hakkı yoksa, `s` olarak değil
`S` olarak gösterilmektedir.

```shell
alper@brs23-2204:~$ ls -l dosya

-rwSrw-r-- 1 alper alper 0 Jul 14 20:12 dosya
```

---

Eğer dosya çalıştırılabilir bir dosya değilse, yani hiç sahip/grup/others `x`
bit set edilmediyse bu durumda SUID bitinin bir anlamı yoktur. Mesela yukarıda
`S` owner'ın `x` hakkı olmadığını gösteriyor, benzer şekilde grup ve others'ın
da yok. Bu durumda zaten kimse dosyayı çalıştıramayacağı için SUID'nin bir
anlamı kalmıyor.

---

Bir çalıştırılabilir dosyayının sahibini `root` yapmak ve ardından SUID bitini
set etmek potansiyel olarak tehlikeli bir davranıştır. Bu dosyayı çalıştıran
herkes efektif olarak o programdan oluşan prosesleri `root` yetkileri ile
çalıştıracaktır. Böyle şeyler yaparsanız dikkatli olun. `passwd`, `sudo` gibi
programlar bu açıdan dikkatlice yazılmış programlardır.

```shell
alper@brs23-2204:/opt$ ls -l id
-rwsr-xr-x 1 root root 16136 Jul 14 19:42 id

alper@brs23-2204:/opt$ ./id
Real UID: 1001
Real GID: 1001
Effective UID: 0
Effective GID: 1001
```

---

Eğer çalıştırılabilir dosya bir binary dosya, `id` gibi derlenmiş C programı
örneğin, değil de interpret edilen BASH, Python script'i gibi bir dosya ise
bunlardaki SUID bitleri **kernel tarafından görmezden gelinir.** Bunun temel
sebebi de güvenliktir. [^5f] [^6f]

### Dizinlerde SUID

Linux üzerinde dizinlere SUID set edilmesinin bir etkisi yoktur, bu bit dizinlerde
ihmal edilmektedir. FreeBSD'de ise anlamı varmış ama biz şu an Linux ile
ilgileniyoruz. [^2f] Linux'ta yapabiliyoruz ama bir anlamı yok:

```shell
alper@brs23-2204:~/sys$ ls -ld dizin
drwsrwxr-x 2 alper alper 4096 Jul 14 21:31 dizin
```

## Set GID, SGID (`2000`)

SUID bitine benzer bir çalışma mantığı vardır ama SUID'e kıyasla daha çok
anlam yüklenmiştir. Yine dosya ve dizin olarak ayrı ayrı bakalım.

### Dosyalarda SGID

Çalıştırılabilir dosyalardaki anlamı SUID ile aynıdır. Benzer şekilde
program çalışınca oluşan prosesin efektif GID değeri, EGID, dosyanın grubu
olmaktadır.

```shell
alper@brs23-2204:/opt$ ls -l id
-rwsr-xr-x 1 root user1 16136 Jul 14 19:42 id

alper@brs23-2204:/opt$ ./id
Real UID: 1001
Real GID: 1001
Effective UID: 0
Effective GID: 1001
```

Örneğin SUID set olunca EUID dosyanın kullanıcısı yani `root` yani `0` oldu.
Şimdi SGID bitini de set edelim:

```shell
alper@brs23-2204:/opt$ sudo chmod g+s id

alper@brs23-2204:/opt$ ls -l id
-rwsr-sr-x 1 root user1 16136 Jul 14 19:42 id

alper@brs23-2204:/opt$ ./id
Real UID: 1001
Real GID: 1001
Effective UID: 0
Effective GID: 1002
```

Bunu da set edince EGID, programın grubu olan `user1` in ID'si oldu. Elbette
sadece SGID'i de set edebiliriz.

```shell
alper@brs23-2204:/opt$ sudo chmod u-s id

alper@brs23-2204:/opt$ ls -l id
-rwxr-sr-x 1 root user1 16136 Jul 14 19:42 id

alper@brs23-2204:/opt$ ./id
Real UID: 1001
Real GID: 1001
Effective UID: 1001
Effective GID: 1002
```

Bu durumda EUID çalıştıranın UID değeri fakat EGID dosyanın GID değeri oldu.

**Fakat burada SUID'den farklı bir durum var.** Eğer bir dosyanın kullanıcısının
`x` hakkı yoksa fakat SUID set edildiyse, yani `S` durumu, yine EUID dosyanın
UID değeri oluyor fakat grubun `x` hakkı yoksa ama SGID set edildiyse, yani `S`
durumu, EGID dosyanın GID değeri **olmuyor.** Bunun farklı bir anlamı var,
aşağıda konuşacağız.

```shell
alper@brs23-2204:/opt$ ls -l id
---Sr-xr-x 1 root user1 16136 Jul 14 19:42 id

alper@brs23-2204:/opt$ ./id
Real UID: 1001
Real GID: 1001
Effective UID: 0
Effective GID: 1001

alper@brs23-2204:/opt$ sudo chmod g-rx id
alper@brs23-2204:/opt$ sudo chmod g+s id
alper@brs23-2204:/opt$ ls -l id
---S--Sr-x 1 root user1 16136 Jul 14 19:42 id

alper@brs23-2204:/opt$ ./id
Real UID: 1001
Real GID: 1001
Effective UID: 0
Effective GID: 1001

alper@brs23-2204:/opt$ sudo chmod g+x id
alper@brs23-2204:/opt$ ./id
Real UID: 1001
Real GID: 1001
Effective UID: 0
Effective GID: 1002
```

---

SUID'nin hiçbir `x` biti set olmayan bir dosyada anlamlı olmadığını söylemiştik.
SGID için durum farklı. SUS standartları, `chmod()` fonksiyonunun `x` biti set
edilmemiş dosyalar için SGID set edilme isteğinin ihmal edilebileceğini bile
belirtiyor. [^7f] Ama Linux buna bir anlam yüklüyor.

Eğer bir dosyanın grubuna `x` hakkı verilmediyse fakat SGID biti set ise, yani
`S` durumu, bu durumda **mandatory locking** denen bir kavram ortaya çıkıyor.
[^7f] [^8f] Bu biraz *problemli* bir kernel özelliği ve kernel 5.15 ile
kaldırılmış durumda. [^8f] [^9f] [^10f] [^12f] Bunun çalışması için dosya
sisteminin `-o mand` seçeneği ile mount edilmiş olması gerekiyor. [^11f] Bu
konunun detaylarına dosya kilit mekanizmalarında belki bakarız ama güncel kernel
sürümlerinde olmayan bir özellik. **Aklımızda kalması gereken şu:** SUID'nin
aksine, SGID'in efektif olması için grup izinlerinde `x` in olması gerekiyor.
Yani grup kısmında `s` yerine `S` görüyorsak, SGID çalışmıyor, en azından Ubuntu
22.04, kernel 6.5'te böyle gözlemledim.

### Dizinlerde SGID

Dizinerde SUID'nin bir anlamı yoktu fakat SGID için durum farklı.

Linux sistemlerde bir dizin içerisinde bir dosya veya dizin oluşturulduğu zaman
yeni oluşturulan dizin/dosyanın GID değeri onu yaratan kullanıcının, daha doğrusu
prosesin EGID değeri olmaktadır, yaratıldığı dizinden bağımsız olarak. Bu, AT&T
UNIX'te de böyledir, Linux da böyle davranmaktadır. Bir diğer tercih de içinde
yaratıldığı dizinin grup bilgilerini almaktır, yaratan kişiden bağımsız olarak.
Bu da BSD tarzı olarak geçmektedir. Linux'ta istersek `mount -o bsdgroups` veya
`mount -o grpid` ile mount edersek BSD tarzı davranışa ulaşabiliriz. Bir diğer
yol da SGID kullanmaktır. SGID biti set edilmiş dizinlerin altındaki dizin ve
klasörler de böyle yaratılır. Yaratılan dizinlerin de SGID biti set edilmiş olur.

Örnek:

```shell
alper@brs23-2204:/opt/sys$ mkdir dizin
alper@brs23-2204:/opt/sys$ chmod o+rwx dizin
alper@brs23-2204:/opt/sys$ chmod g+s dizin

alper@brs23-2204:/opt/sys$ ls -ld dizin
drwxrwsrwx 2 alper alper 4096 Jul 15 09:02 dizin

alper@brs23-2204:/opt/sys$ cd dizin
alper@brs23-2204:/opt/sys/dizin$ touch alper
alper@brs23-2204:/opt/sys/dizin$ ls -l
total 0
-rw-rw-r-- 1 alper alper 0 Jul 15 09:03 alper
```

Burada `alper` kullanıcısı ile bir dizin yarattım ve `g+s` ile SGID bitini set
ettim. Aynı kullanıcı ile bu dizin altında bir şeyler yaratınca farkı görmüyorum.
Ama şimdi gidip `user1` kullanıcısı ile altında bir şeyler yaratayım. Bunu
yapabilmek için `o+rwx` ile izin verdim, SGID ile ilgisi olan bir konu değil

```shell
user1@brs23-2204:/opt/sys/dizin$ touch user1
user1@brs23-2204:/opt/sys/dizin$ mkdir user1-dir
user1@brs23-2204:/opt/sys/dizin$ cd user1-dir/
user1@brs23-2204:/opt/sys/dizin/user1-dir$ touch user1
user1@brs23-2204:/opt/sys/dizin/user1-dir$ cd ..

user1@brs23-2204:/opt/sys/dizin$ ls -l
total 4
-rw-rw-r-- 1 alper alper    0 Jul 15 09:03 alper
-rw-rw-r-- 1 user1 alper    0 Jul 15 09:03 user1
drwxrwsr-x 2 user1 alper 4096 Jul 15 09:04 user1-dir

user1@brs23-2204:/opt/sys/dizin$ cd user1-dir/
user1@brs23-2204:/opt/sys/dizin/user1-dir$ ls -l
total 0
-rw-rw-r-- 1 user1 alper 0 Jul 15 09:04 user1
```

İşte burada farkı görüyoruz. `user1` ile yarattığım `user1` isimi dosyanın
grubu `alper` oldu çünkü altında bulunduğu dizinin grubu `alper` ve SGID set
edilmiş durumda. Benzer şekilde `user1-dir` isimli dizinin de grubu `alper` oldu
ve SGID otomatik olarak set edildi, `s` oldu. Onun altındaki dosyalar da benzer
şekilde davranıyor.

Bu davranış özellikle ortak dizinlerde çalışırken iyi olabiliyor, dosya koyan
herkesin koyduğu dosyalar bir gruba dahil oluyor.

## Kaynaklar

- <https://wpollock.com/AUnix1/FilePermissions.htm>

[^1f]: <https://en.wikipedia.org/wiki/Sticky_bit>
[^2f]: <https://en.wikipedia.org/wiki/Setuid>
[^3f]: <https://stackoverflow.com/a/58123923/1766391>
[^4f]: <https://unix.stackexchange.com/a/592914/285808>
[^5f]: <https://unix.stackexchange.com/a/2910/285808>
[^6f]: <http://www.faqs.org/faqs/unix-faq/faq/part4/section-7.html>
[^7f]: <https://wpollock.com/AUnix1/FilePermissions.htm>
[^8f]: <https://www.kernel.org/doc/Documentation/filesystems/mandatory-locking.txt>
[^9f]: <https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?h=linux-5.15.y&id=f7e33bdbd6d1bdf9c3df8bba5abcf3399f957ac3>
[^10f]: <https://stackoverflow.com/a/77976994/1766391>
[^11f]: <https://linux.die.net/man/2/mount>
[^12f]: <https://man7.org/linux/man-pages/man2/fcntl.2.html>
[^13f]: <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=800179c9b8a1e796e441674776d11cd4c05d61d7>
