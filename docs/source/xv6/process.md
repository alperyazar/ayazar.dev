---
gicus: 487f15ed-23d8-4855-906c-e63d9f2d8436
---

# Process Kavramı ve xv6 Çekirdeğindeki Gerçekleştirimi

Şimdi gelin bir işletim sisteminin en temel kavramlarından biri olan **process**
kavramına bakalım.

```{note}
Bu kelime Türkçe'ye genelde proses olarak çevriliyor ama tam Türkçe bir kelime
gibi durmuyor. `Süreç` denebilir belki ama o da orijinal anlamından kaymış mı
oluyor bilemiyorum, [terimler.org](https://terimler.org/)'da `süreç` olarak
çevrilmiş. [Bilgisayar
Kavramları](https://bilgisayarkavramlari.com/2007/11/18/islem-process/)
sitesinde ve
[Vikipedi](https://tr.wikipedia.org/wiki/%C4%B0%C5%9Flem_(bilgisayar))'de
`işlem` olarak belirtilmiş. Ben tahmin ediyorum ki el alışkanlı `process`
yazmaya devam edeceğim ama benim kulağıma `işlem` daha doğru geliyor.
```

*Bilgisayar programı* dediğimiz şeyler genelde sabit diskte duran ve işletim
sistemi tarafından çalıştırılabilen dosyalar. İşletim sistemine göre bu
çalıştırılabilir dosyaların formatları ve uzantıları değişebiliyor. Örneğin
Windows sistemlerde tipik olarak `.exe` uzantısından ve formatından bahsediyoruz,
xv6 gibi Unix temelli sistemlerde, Linux dahil olmak üzere, bu formatın adı
[ELF](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) oluyor.
Bu tarz sistemlerde dosya uzantısının pek bir önemi yok. Biz bir programı
çalıştırdığımız zaman, masaüstü ortamında çift tıklayarak, ya da komut satırından
çalıştırarak bir dizi işlem gerçekleşiyor. İşletim sisteminin çeşitli bileşenleri
ve çekirdeği bu dosyayı okuyor, ana belleğe yani RAM'e açıyor ve programın içerisinde
bulunan CPU komutlarını çalıştırmaya başlıyor.
**İşte çalışan programlara temel olarak process diyoruz.**

Process'ler kernel tarafından oluşturulan ve takip edilen birimler. Kernel
içerisinde her process için bir veri yapısı içerisinde çeşitli bilgiler
tutuluyor. Bu tutulan bilgilerin ne olduğu işletim sisteminden işletim sistemine
değişiyor. xv6, Linux gibi sistemlerde process'e ait temel bilgiler arasında
**PID** yani **P**rocess **ID** geliyor. İşletim sistemi, her process'e herhangi
bir `t` anında sistemde tekil yani unique olan bir tam sayı atıyor, TC kimlik no
gibi düşünün ama çok daha kısa. Yani herhangi bir anda aynı PID değerine sahip
iki farklı process sistemde yer almıyor. Bununla beraber bir process ile tutulan
en önemli bilgilerden biri de **file descriptor table** yani o process'e açık
olan dosyalar ile ilgili bilgiler. Örneğin biz `open()` ile dosya açtıkça
aslında kernel bu tablonun bir satırında dosya ile ilgili bilgiler tutuyor.

Elbette tahmin edersiniz ki C'de adı `tablo` olan bir tür ya da veri yapısı yok.
Ama satırlardan oluşan tabloyu çok güzel modelleyebilen bir C aracımız var:
array yani diziler!

## xv6: `proc`, `struct proc` ve `struct file`

Şimdi xv6 kernel kodunda bu veri yapılarını bulmaya çalışalım. xv6 minimal ve
temiz yazılmış kodlara sahip, o yüzden bulmak zor olmuyor.

```{note}
Yazının ilerleyen kısımlarında `f5b93ef` nolu
[commit](https://github.com/mit-pdos/xv6-riscv/tree/f5b93ef12f7159f74f80f94729ee4faabe42c360)'i
referans alacağım.
```

Önce şu koda bakalım:

```{code-block} c
:caption: kernel/proc.c
:lineno-start: 9
:emphasize-lines: 3

struct cpu cpus[NCPU];

struct proc proc[NPROC];

struct proc *initproc;
```

Her bir process için tutulan veri yapısının türü `struct proc`. xv6 basit bir
kernel olduğu için aynı anda sistemde bulunabilecek process sayısı limitlenmiş.
Bu maximum sayı, `NPROC`, kadar `struct proc` türünden eleman tutabilecek `proc`
isimli bir dizi oluşturuluyor. Yani kernel maximum sayıda process olacakmış gibi
bu alanı en baştan ayırıyor. Elbette bu yöntem en optimum yöntem değil. Çünkü
biz çoğu zaman 1-2 process çalıştırıyor oluyoruz. Bu da bellek tüketimi
açısından verimli bir yaklaşım değil, kullanmadığımız birçok alan kalıyor. Diğer
bir problemli yanı da genişlemeye imkan sağlamıyor olması. Yani derleme
zamanında belli olan `NPROC` değerini çalışma zamanında yani runtime sırasında
değiştiremiyoruz. Yine de basit bir kernel için mantıklı bir tasarım tercihi
diyebiliriz.

`NPROC` ise şurada tanımlı:

```{code-block} c
:caption: kernel/param.h
:lineno-start: 1
:emphasize-lines: 1

#define NPROC        64  // maximum number of processes
#define NCPU          8  // maximum number of CPUs
#define NOFILE       16  // open files per process
```

Varsayılan olarak bu değer 64. Elbette ilgili dosyayı değiştirerek bu değerle
oynayabiliriz. Peki `struct proc` nasıl bir şey?

```{code-block} c
:caption: kernel/proc.h
:lineno-start: 84
:emphasize-lines: 3,6,13,18,19,20,21,22

// Per-process state
struct proc {
  struct spinlock lock;

  // p->lock must be held when using these:
  enum procstate state;        // Process state
  void *chan;                  // If non-zero, sleeping on chan
  int killed;                  // If non-zero, have been killed
  int xstate;                  // Exit status to be returned to parent's wait
  int pid;                     // Process ID

  // wait_lock must be held when using this:
  struct proc *parent;         // Parent process

  // these are private to the process, so p->lock need not be held.
  uint64 kstack;               // Virtual address of kernel stack
  uint64 sz;                   // Size of process memory (bytes)
  pagetable_t pagetable;       // User page table
  struct trapframe *trapframe; // data page for trampoline.S
  struct context context;      // swtch() here to run process
  struct file *ofile[NOFILE];  // Open files
  struct inode *cwd;           // Current directory
  char name[16];               // Process name (debugging)
};
```

Oldukça kalabalık bir veri yapısı. Elbette Linux gibi "gerçek" işletim
sistemlerinde daha da çok eleman oluyor fakat mantık olarak aynı. Burada
dikkat ederseniz başka kullanıcı tanımlı veri yapıları da var, `enum` ve diğer
`struct` lar.

`int pid` elemanı, process id'yi tutuyor. `char name[16]` ile process'in adı
tutuluyormuş ama yorumda *debug* amaçlı olduğu söyleniyor. Yani insanlar için
konmuş, kernel bir process'i `pid` değerinden tanıyor, isim onun için önemli
değil.

Burada bulunan tüm elemanlara şu an bakmamız pek doğru olmaz, zamanı geldikçe
inceleriz. Ama birkaç tanesini görelim:

```{code-block} c
:caption: kernel/proc.h
:lineno-start: 82

enum procstate { UNUSED, USED, SLEEPING, RUNNABLE, RUNNING, ZOMBIE };
```

`enum procstate` ile process'in state'i yani durumu belirtiliyor. Bu kavramlara
ilerleyen kısımlarda muhtemelen *scheduler* başlığı altında değiniriz. Bir process,
çalışmayı bekliyor (RUNNABLE), aktif olarak CPU'da çalışıyor (RUNNING) gibi
durumlarda olabilir.

```{code-block} c
:caption: kernel/proc.h
:lineno-start: 1

// Saved registers for kernel context switches.
struct context {
  uint64 ra;
  uint64 sp;

  // callee-saved
  uint64 s0;
  uint64 s1;
  uint64 s2;
  uint64 s3;
  uint64 s4;
  uint64 s5;
  uint64 s6;
  uint64 s7;
  uint64 s8;
  uint64 s9;
  uint64 s10;
  uint64 s11;
};
```

Bir diğer ilginç eleman da `struct context` türünden olan. Bu tür, context
switch işlemleri sırasında CPU registerlarını depolamak için kullanılıyor.
Bunlar RISC-V işlemciye ait register'lar.

Şimdi gelelim **file descriptor table** a yani `struct file *ofile[NOFILE];`
elemanına. Burada `NOFILE` isminde sembolik bir sabit var.

```{code-block} c
:caption: kernel/param.h
:lineno-start: 1
:emphasize-lines: 3

#define NPROC        64  // maximum number of processes
#define NCPU          8  // maximum number of CPUs
#define NOFILE       16  // open files per process
```

Burada da `NPROC` gibi bir mantık var aslında. Bir process'in bir `t` anında
açık tutabileceği maksimum dosya sayısı `NOFILE` ile limitlenmiş durumda.
`NPROC` için söylediğimiz her şey burada da geçerli (bellek verimliliği konuları
ve limitler).

`struct file *ofile[NOFILE];` ifadesine bir bakalım. Burada `ofile` isminde bir
dizi var, `NOFILE` kadar eleman tutabiliyor, yani varsayılan değeri ile 16 adet.
Her bir elemanın türü `struct file*`, yani `struct file` türünden bir nesneye
bir pointer. Yani burada bir pointer dizisi var.

```{code-block} c
:caption: kernel/file.h
:lineno-start: 1

struct file {
  enum { FD_NONE, FD_PIPE, FD_INODE, FD_DEVICE } type;
  int ref; // reference count
  char readable;
  char writable;
  struct pipe *pipe; // FD_PIPE
  struct inode *ip;  // FD_INODE and FD_DEVICE
  uint off;          // FD_INODE
  short major;       // FD_DEVICE
};
```

`struct file` türü bu şekilde tanımlanmış. Örneğin her bir dosyanın bir türü,
yani `type` değeri var. Ya da dosya `readable` mı ve `writable` mı? Bunlar da
burada tutuluyor. Tüm elemanlara şimdi bakmayalım, dosya sistemi bölümüne
saklayalım. Buradaki önemli elemanlardan biri de `uint off;` elemanı yani,
offset değeri. Biz dosyaya okuma ve yazma yaptığımız zaman bir sonraki okuma ve
yazmanın nereye yapılacağı bu `off` elemanında saklanıyor. Örneğin arka arkaya
`write(fd, "Merhaba Dunya!\n", 15)` çağırırsak aslında bunlar aynı dosyada üst
üste değil, ard arda yazılacaktır. Çünkü her yazmada ve okumada kernel bu değeri
değiştirmekte daha doğrusu arttırmaktadır. Bu sayede biz `write()` ve `read()`
çağrıları yaptıkça otomatik olarak dosyada ilerleriz. Burada her iki fonksiyon
için ayrı birer offset değeri **olmadığına** dikkat edelim. Yani `write()`
yaptıkça `off` değerinin değişmesi ardından yapılacak `read()`in nereden
yapılacağını etkiliyor.

---

```{figure} assets/process-struct-proc-ve-struct-file.jpg
:align: center

`struct pointer` ve `struct file` arasındaki ilişki görüldüğü gibidir. `ofile[]`
dizisinin elemanları birer `struct pointer*` dır yani pointer'dır. Her biri
bir `struct file` türünü gösterir. Elbette açık olan dosya sayısı kaç ise,
o kadar `ofile` elemanın gösterdiği yer geçerlidir. Yukarıdaki örnekte 3 adet
açık dosya varmış gibi düşünebilirsiniz.
```

## Verilerin Bellekte Tahsis Edilmesi

`struct file *ofile[NOFILE];` ifadesini hatırlayalım. Bir process oluşturulduğu
zaman bu pointer dizisinin gösterdiği elemanların bellekte tahsis edilmesi
gerekmektedir. Çünkü bunlar birer pointer fakat gösterdikleri yerde gerçekten
de `struct file` türünden nesneler olmalı ki dereference edebilelim, yani `*ptr`
şeklinde erişebilelim.

Aşağıdaki koda bakalım:

```{code-block} c
:caption: kernel/sysfile.c
:lineno-start: 344
:emphasize-lines: 1

if((f = filealloc()) == 0 || (fd = fdalloc(f)) < 0){
  if(f)
    fileclose(f);
  iunlockput(ip);
  end_op();
  return -1;
}
```

Yukarıdaki kodda `f`, `struct file *f` şeklinde tanımlanmış. Burada minik bir C
hilesi var. `if` içerisindeki `||` yani logical OR operatörü bir *sequence
point* tanımlıyor ve ayrıca bu operatörün *short circuit* özelliğinden
faydalanılmış. Burada ilk olarak `f = filealloc()` işleminin yapılacağı C
standartları tarafından garanti ediliyor. Eğer `== 0` ile karşılaştırma doğru
olursa yani `f` aslında null-pointer olursa, `fd = fdalloc(f)` işlemi `||`
operatörünün short-circuit özelliğinden dolayı yapılmıyor. Böylece, `fd =
fdalloc(f)` ifadesinin sadece `f` in null-pointer olmadığı yani `filealloc()`
işleminin başarılı olduğu durumda yapılacağı garanti ediliyor.

```{code-block} c
:caption: kernel/file.c
:lineno-start: 28
:emphasize-lines: 3, 8

// Allocate a file structure.
struct file*
filealloc(void)
{
  struct file *f;

  acquire(&ftable.lock);
  for(f = ftable.file; f < ftable.file + NFILE; f++){
    if(f->ref == 0){
      f->ref = 1;
      release(&ftable.lock);
      return f;
    }
  }
  release(&ftable.lock);
  return 0;
}

// Increment ref count for file f.
struct file*
filedup(struct file *f)
{
  acquire(&ftable.lock);
  if(f->ref < 1)
    panic("filedup");
  f->ref++;
  release(&ftable.lock);
  return f;
}
```

`filealloc()` yani *file allocate* fonksiyonu bize bir yerlerden bir
`struct file` nesnesi buluyor ve bunun adresini dönüyor. Peki nereden?
`ftable` denen bir yerden. Bu da yine aynı dosyada tanımlı.

```{code-block} c
:caption: kernel/file.c
:lineno-start: 17

struct {
  struct spinlock lock;
  struct file file[NFILE];
} ftable;
```

Yine bir sembolik sabit ile karşlaştık, `NFILE`.

```{code-block} c
:caption: kernel/param.h
:lineno-start: 4

#define NFILE       100  // open files per system
```

Bu sefer de sistem genelinde açık olabilecek toplam dosya sayısının bir limiti
olduğunu gördük. Yani varsayılan olarak bir process 16 adet dosya açabiliyordu,
`NOFILE`, fakat sistem genelinde toplamda 100 adet açık dosya olabiliyor, `NFILE`.
Elbette bunlar varsayılan değerler, değiştirebilirsiniz.

Yani `filealloc()` aslında zaten derleme sırasında statik olarak allocate
edilmiş bir diziden bize bir adres dönüyor.

```{code-block} c
:caption: kernel/sysfile.c
:lineno-start: 37
:emphasize-lines: 4

// Allocate a file descriptor for the given file.
// Takes over file reference from caller on success.
static int
fdalloc(struct file *f)
{
  int fd;
  struct proc *p = myproc();

  for(fd = 0; fd < NOFILE; fd++){
    if(p->ofile[fd] == 0){
      p->ofile[fd] = f;
      return fd;
    }
  }
  return -1;
}
```

`fdalloc()` ise bu `struct file` türünden nesnenin adresini o processin boş
olan ilk `ofile[]` elemanına yerleştiriyor ve bu elemanın indeks değerini
dönüyor. Yani günün sonunda `open()` ile bu şekilde bir file descriptor değeri
almış oluyoruz. Bu kod sayesinde `open()` ile alacağımız fd değerinin olabilecek
en düşük değer olacağı garanti ediliyor.

Hatırlarsanız bir önceki örneklerde `fd` değeri olarak `3` değerini alıyorduk.
Çünkü `ofile[0]`, `ofile[1]` ve `ofile[2]` dolu oluyordu. Bunlar sırası ile
`stdin`, `stdout` ve `stderr` dosyalarını gösteriyorlar.

## Hadi Gözlemleyelim! 👀

Madem elimizde QEMU ve GDB var, e bunlara bir bakalım.

Okumadıysanız: [](gdb-ile-debug.md)

Standart debug altyapımız ile sistemi boot edip, `gdb` den kernel içerisinde
bulunan bu veri yapılarına bakmaya çalışalım.

```text
(gdb) file kernel/kernel
Reading symbols from kernel/kernel...
(gdb)

(gdb) c
Continuing.
```

Şimdi şu `ftable` ı bir görmeye çalışalım. `ctrl-c` ile durduruyoruz ve `print`
ediyoruz.

```text
(gdb) p ftable
$1 = {lock = {locked = 0, name = 0x80008648 "ftable", cpu = 0x0}, file = {{
      type = FD_DEVICE, ref = 6, readable = 1 '\001', writable = 1 '\001',
      pipe = 0x0, ip = 0x80016f08 <itable+160>, off = 0, major = 1}, {
      type = FD_NONE, ref = 0, readable = 1 '\001', writable = 1 '\001',
      pipe = 0x0, ip = 0x80016f08 <itable+160>, off = 0, major = 1}, {
      type = FD_NONE, ref = 0, readable = 0 '\000', writable = 0 '\000',
      pipe = 0x0, ip = 0x0, off = 0, major = 0} <repeats 98 times>}}
(gdb)
```

`ftable` yapısını hatırlayalım:

```c
struct {
  struct spinlock lock;
  struct file file[NFILE];
} ftable;
```

İlk olarak `lock` elemanının içeriğini görüyoruz, türü `struct lock`. Şimdilik
bununla ilgilenmiyoruz. Daha sonra `file[0]` ın içeriğini görüyoruz.
`struct file` ı hatırlayalım:

```c
struct file {
  enum { FD_NONE, FD_PIPE, FD_INODE, FD_DEVICE } type;
  int ref; // reference count
  char readable;
  char writable;
  struct pipe *pipe; // FD_PIPE
  struct inode *ip;  // FD_INODE and FD_DEVICE
  uint off;          // FD_INODE
  short major;       // FD_DEVICE
};
```

Türü, `FD_DEVICE` olan bir dosya sistemde açık, şimdilik bununla ilgilenmiyoruz.
Onun dışında sanki açık dosyamız yok. Di mi? Diğerleri hep `FD_NONE`. Daha
doğrusu `ref=0` bize o elemanın bir dosyayı göstermediğini bize söylüyor.

Bu çok garip değil çünkü hiç bir program çalıştırmıyoruz, hiç bir dosya açmadık.

Şimdi bir tane dosya açıp biz programı sonlandırana kadar bekleyen bir program
yazalım.

```{code-block} c
:caption: user/acbekle.c
:lineno-start: 1

#include "kernel/types.h"
#include "user/user.h"
#include "kernel/fcntl.h" //O_WRONLY vs

static char buf[1];

int main() {
  int fd;

  fd = open("not.txt", O_RDWR|O_CREATE|O_TRUNC);

  if (fd < 0){
    fprintf(2, "fd = %d not.txt acilamadi!\n", fd);
    exit(1);
  }

  printf("fd = %d\n", fd);

  read(0, buf, 1);

  exit(0);
}
```

```{note}
`acbekle.c` de Aç Bitir gibi oldu, ürün yerleştirme yaptım!
```

Yukarıdaki program, `not.txt` isimli bir dosyayı açıyor ve kullanıcıdan
`stdin` den bir girdi gelene kadar bekliyor. Bu noktada `not.txt` hep açık
kalıyor.

Şimdi tekrar debug başlatalım. Programımızı çalıştıralım ve program `read()`
kısmında beklerken `gdb` üzerinden `ftable` içeriğine tekrar bakalım.

```text
xv6 kernel is booting

hart 1 starting
hart 2 starting
init: starting sh
$ acbekle
fd = 3
```

GDB:

```text
(gdb) print ftable
$1 = {lock = {locked = 0, name = 0x80008648 "ftable", cpu = 0x0}, file = {{
      type = FD_DEVICE, ref = 9, readable = 1 '\001', writable = 1 '\001',
      pipe = 0x0, ip = 0x80016f08 <itable+160>, off = 0, major = 1}, {
      type = FD_INODE, ref = 1, readable = 1 '\001', writable = 1 '\001',
      pipe = 0x0, ip = 0x80016f90 <itable+296>, off = 0, major = 1}, {
      type = FD_NONE, ref = 0, readable = 0 '\000', writable = 0 '\000',
      pipe = 0x0, ip = 0x0, off = 0, major = 0} <repeats 98 times>}}
(gdb)
```

Burada gördüğünüz üzere şimdi `file[1]` de dolu, `FD_INODE` tipinde ve `ref = 1`
olmuş. Dosya sistemi konusuna ileride bakarız ama bu bizim dosyamız mı bunu
görebilir miyiz?

`struct file` ın `ip` elemanı `struct inode` türünden bir nesneye bir pointer.
Burada adresinin değerinin `ip = 0x80016f90` olduğunu görüyoruz. Bu adresi,
`struct inode` türüne cast edip içeriğine bakalım.

```text
(gdb) p (struct inode)*(0x80016f90)
$2 = {dev = 1, inum = 25, ref = 1, lock = {locked = 0, lk = {locked = 0,
      name = 0x80008638 "sleep lock", cpu = 0x0}, name = 0x80008570 "inode",
    pid = 0}, valid = 1, type = 2, major = 0, minor = 0, nlink = 1, size = 0,
  addrs = {0 <repeats 13 times>}}
```

Şimdi dediğim gibi dosya sistemi konusuna gelmedik ama burada `inum = 25`
değerine dikkat edelim.

Şimdi programımızı klavyeden bir şeye basarak sonlandıralım. Tabii öncesinde
GDB'de `c` ile devam edelim. xv6 üzerinde bir `ls` çekelim:

```shell
$ ls
.              1 1 1024
..             1 1 1024
README         2 2 2305
xargstest.sh   2 3 93
cat            2 4 32848
echo           2 5 31696
forktest       2 6 15824
grep           2 7 36224
init           2 8 32192
kill           2 9 31656
ln             2 10 31480
ls             2 11 34784
mkdir          2 12 31712
rm             2 13 31696
sh             2 14 54144
stressfs       2 15 32584
usertests      2 16 180624
grind          2 17 47536
wc             2 18 33800
zombie         2 19 31056
merhaba        2 20 31160
loop           2 21 31792
not            2 22 31912
acbekle        2 23 31512
console        3 24 0
not.txt        2 25 0
```

`not.txt` nin yanındaki `25` değeri dikkatinizi çekti mi? İşte bu değer o dosyanın
i-node değeri. Yani `ftable.file[1]` gerçekten de bu dosyaymış!

İşte bu da `ls` in bastığı 25 değerinin i-node olduğunun kanıtı (açık kaynağın
gücü 🤪):

```{code-block} c
:caption: user/ls.c
:lineno-start: 46
:emphasize-lines: 2

case T_FILE:
  printf("%s %d %d %l\n", fmtname(path), st.type, st.ino, st.size);
  break;
```

---

Bu sefer process'imize ait `struct proc` içeriğindeki `ofile[3]` ün, çünkü
`fd = 3` görüyoruz, `ftable.file[1]` nesnesini gösterdiğinden emin olalım.
`struct proc proc[NPROC]` içerisinden bizim process'in bilgilerini bulmak için
`PID` değerine ihtiyacımız olacak. Neyse ki xv6'nın `int getpid(void);` şeklinde
bildirilen bir fonksiyonu var. Bu bizim processimizin PID değerini bizi söylecek.
Programımızı modifiye edelim:

```{code-block} c
:caption: user/acbekle.c
:lineno-start: 1

#include "kernel/types.h"
#include "user/user.h"
#include "kernel/fcntl.h" //O_WRONLY vs

static char buf[1];

int main() {
  int fd;

  fd = open("not.txt", O_RDWR|O_CREATE|O_TRUNC);

  if (fd < 0){
    fprintf(2, "fd = %d not.txt acilamadi!\n", fd);
    exit(1);
  }

  printf("fd = %d\n", fd);
  printf("PID = %d\n", getpid());

  read(0, buf, 1);

  exit(0);
}
```

Bunu derleyip biraz önceki gibi debug edelim:

```text
xv6 kernel is booting

hart 1 starting
hart 2 starting
init: starting sh
$ acbekle
fd = 3
PID = 3
```

Ne tesadüftür ki `PID` değerimiz de 3 imiş. O zaman gdb'den `proc` a bir bakalım.

```text
(gdb) p proc

...
{lock = {locked = 0, name = 0x800081b8 "proc", cpu = 0x0},
state = SLEEPING, chan = 0x80021d28 <cons+152>, killed = 0, xstate = 0,
pid = 3, parent = 0x80008ed8 <proc+360>, kstack = 274877878272,
sz = 16384, pagetable = 0x87f43000, trapframe = 0x87f60000, context = {
  ra = 2147488962, sp = 274877882000, s0 = 274877882048, s1 = 2147520576,
  s2 = 2147518784, s3 = 1, s4 = 4096, s5 = 1, s6 = 1, s7 = 4,
  s8 = 18446744073709551615, s9 = 10, s10 = 361700864190383365,
  s11 = 361700864190383365}, ofile = {0x80018a70 <ftable+24>,
  0x80018a70 <ftable+24>, 0x80018a70 <ftable+24>, 0x80018a98 <ftable+64>,
  0x0 <repeats 12 times>}, cwd = 0x80016e80 <itable+24>,
name = "acbekle\000\000\000\000\000\000\000\000"},
...

```

Bunun çıktısı biraz kalabalık oluyor, ben sizin için temizledim. Şimdi, `pid=3`
olan `struct proc` nesnesini bulduk. Burada `ofile` kısmına bakalım.
Dikkat edersek ilk 4 elemanı dolu, sonrası 0. İlk 3 eleman process'in
standart akımları. Fakat 4. eleman yani `[3]` olan bizim `not.txt` dosyamız.
Değerinin `0x80018a98` olduğuna dikkat edelim. Bu ilgili `struct file`
nesnesinin adresi olmalı. Peki öyle mi? Bir önceki GDB çıktısında bu dosyanın
aslında `ftable.file[1]` olduğunu görmüştük. GDB'ye bunun adresini soralım:

```text
(gdb) print &ftable.file[1]
$2 = (struct file *) (gdb) print &ftable.file[1]
$2 = (struct file *) 0x80018a98 <ftable+64> <ftable+64>
```

Ve bize `0x80018a98` değerini döndü.

**Yani process'in 3 nolu file descriptor değeri gerçekten de not.txt'yi
gösteriyormuş**

Siz dilerseniz başka şeyleri de gözlemleyebilirsiniz. Mesela yazma ve okuma
yaptıkça `struct file` ın `off` üyesinin değeri nasıl değişiyor, buna
bakabilirsiniz. Ben artık burada kesiyorum.

## Özet

Bu bölümde, genel olarak process kavramına ve xv6 üzerindeki implementasyonuna
baktık. GDB ile de çalışan bir sistem üzerinde gözlemledik. Process'lerle ilgili
kernelde saklanan en önemli verilerden biri de **file descriptor table** dır.
Elbette `struct proc` içerisindeki
Buna vurgu yapmamın sebebi ilerleyen bölümlerde göreceğimiz `fork()` ve `exec()`
sistem çağrıları ve bu arada yapılan I/O redirection işlemleridir.
