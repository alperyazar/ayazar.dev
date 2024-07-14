# Dizin İzinleri

Dizin izinleri ile ilgili ayrı bir yazı yazmanın iyi olacağını düşündüm. Önceki
yazılarda bunlardan bahsettim ama şöyle bir toparlayalım.

Dizin izinleri kafa karıştırıcı olabiliyor. İnternetteki açıklamaların bir kısmı
yanlış, bir kısmı da tüm durumları karşılamıyor. Adam anlatmış anlatmış ama
"öyle olursa böyle bir exception var", "şöyleyse böyle" diye bir sürü istisna
tanımlamış, akılda tutmak kolay değil. Ben de tüm durumları kapsayacak bir model
uydurdum. Şimdi uydurduğum modele bir bakalım. Sonra örneklerle destekleriz.

## Oda, Kapı, Kilit, Cam

```{figure} assets/dizin-oda.png
:align: center
```

Bu modelde dosya sistemindeki dizinleri iki kapısı olan bir odaya benzetiyoruz.
Dizinin altında olan diğer dizin ve dosyalar odanın devamında yer alıyor.
Altındaki dizin ve dosyalara erişmek sadece bu dizin ile mümkün oluyor. Çöp adam
bizi daha doğrusu kernel'i temsil ediyor. Biz dosya sisteminde *gezinirken*
odadan odaya geziniyor gibi düşünelim.

Odanın `/` tarafına yani "tepeye" yakın olan kısmındaki kapının bir camı var,
içerisi gözükebiliyor. İçeride ise bir tahtada tablo var. İşte bu tablo dizinin
içeriği. Dizin dediğimiz şeyin `isim - inode` çiftlerinden oluştuğundan
bahsetmiştik. Linux üzerinde aslında bir 3. sütünun olduğundan bahsedebiliriz, o
da `tür`. Bu bilgi hem dizin içerisinde hem de `inode` içerisinde saklanıyor,
tipik olarak. Odanın çıkış kapısında ise cam yok ve kilit de bulunmuyor. Dizinin
içerisindeki dosya ve dizinlerin inode verilerine ulaşmak için odadan çıkıp, Her
satırda 3 adet veri tutan bu dizin veri yapısının *key* kısmı `isim` olmaktadır.
Dizinlerde kullanabileceğimiz `çöz()` diye bir fonksiyon var diyelim. Buna merak
ettiğimiz ismi verince biz diğer iki bilgiyi veriyor. Mesela `çöz("x")` diyoruz,
bize `5, f` dönüyor. Şimdi bu model üzerinden `rwx` haklarını konuşalım.

- `r` Bu hakkımız var ise dizinin içerisindeki tabloyu açıkça görebiliyoruz, tüm
  satırları.
- `w` Bu hakkımız var ise dizinin içerisindeki tabloyu değiştirebiliyoruz.
- `x` hakkı bize giriş kapısının anahtarını veriyor. Kapıyı açıp içeriye
  girebiliyoruz. İçeriye girebildiğimiz için odanın içerisindeki `çöz()`
  fonksiyonunu da kullanabiliyoruz.

---

Şimdi 8 adet olasılığı da tek tek inceleyelim.

## `r--`

Dizinde sadece `r` hakkımız var. Dizinin önüne kadar geldik. Fakat kapıyı açıp
içeriye giremiyoruz çünkü kapının anahtarı yani `x` hakkı yok. Fakat kilitli
kapı camlı olduğu için camdan içeriye bakıp, tabloyu görebiliyoruz. Tek
yapabildiğimiz bu. Tabloyu görerek de dizinin altında bulunan dosya ve dizinler
ile ilgili inode numarası ve tür bilgilerine ulaşabiliyoruz. Doğrudan tabloyu
gördüğümüz için `çöz()` fonksiyonunu kullanamasak da, çünkü odanın içinde değiliz
`x` hakkımı yok, tablodan doğrudan bilgileri görebiliyoruz.

Bu hakkı olan kullanıcı dizinin içerisindeki olanların adını, türünü ve inode
numarasını görmek dışında bir şey yapamaz. Odaya giremediği için odadan çıkıp
inode'lara ve dosya içeriklerine ulaşamaz.

```shell
alper@brs23-2204:~/sys$ ls -lad a
dr--rwxr-x 3 alper alper 4096 Jul 14 14:10 a

alper@brs23-2204:~/sys$ cd a
bash: cd: a: Permission denied

alper@brs23-2204:~/sys$ ls a
ls: cannot access 'a/x': Permission denied
ls: cannot access 'a/z': Permission denied
ls: cannot access 'a/y': Permission denied
x  y  z

alper@brs23-2204:~/sys$ ls -il a
ls: cannot access 'a/x': Permission denied
ls: cannot access 'a/z': Permission denied
ls: cannot access 'a/y': Permission denied
total 0
? -????????? ? ? ? ?            ? x
? -????????? ? ? ? ?            ? y
? d????????? ? ? ? ?            ? z

alper@brs23-2204:~/sys$ find . -name x -printf "%f - %i\n"
x - 8521330
find: ‘./a/z’: Permission denied
```

`x` hakkı yani kilit olmadığı için `cd` ile dizinin içerisine giremiyorum. `ls`
ile de dosya türleri ve isimlerini görebiliyorum, `-i` ile inode bilgilerini
görememe sebebim de `ls` komutunun çalışma şeklinden geliyor. `ls`, adeta
dizin kaydındaki inode bilgisini kullanmıyor da dosyanın kendisine gidip inode
bilgilerini bulmaya çalışıyor. `find` ile dizin içerisindeki tabloyu okuyarak
bu bilgiyi edinebiliyoruz. Bunu kantılamak için ChatGPT'ye `readdir()` kullanarak
bir program yazdırmasını söyledim:

```c
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

void print_file_type(unsigned char d_type) {
    switch(d_type) {
        case DT_REG:
            printf("Regular file");
            break;
        case DT_DIR:
            printf("Directory");
            break;
        case DT_LNK:
            printf("Symbolic link");
            break;
        case DT_BLK:
            printf("Block device");
            break;
        case DT_CHR:
            printf("Character device");
            break;
        case DT_FIFO:
            printf("FIFO/pipe");
            break;
        case DT_SOCK:
            printf("Socket");
            break;
        default:
            printf("Unknown");
            break;
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <directory_path>\n", argv[0]);
        return 1;
    }

    DIR *dir;
    struct dirent *entry;

    if ((dir = opendir(argv[1])) == NULL) {
        perror("opendir");
        return 1;
    }

    while ((entry = readdir(dir)) != NULL) {
        printf("Inode: %lu - Name: %s - Type: ", entry->d_ino, entry->d_name);
        print_file_type(entry->d_type);
        printf("\n");
    }

    closedir(dir);
    return 0;
}
```

Bu programı `gcc myls.c -o myls` olarak derleyip `r--` hakkımın olduğu dizinde
çalıştırınca:

```shell
alper@brs23-2204:~/sys$ ./myls a

Inode: 8521330 - Name: x - Type: Regular file
Inode: 8521332 - Name: z - Type: Directory
Inode: 8521331 - Name: y - Type: Regular file
Inode: 8520985 - Name: .. - Type: Directory
Inode: 8521270 - Name: . - Type: Directory
```

Gördüğünüz üzere bu bilgileri almak için, inode bilgisi dahil, dizinde `r`
hakkımızın olması yeterli.

## `-w-`

Dizinde sadece `w` hakkımız olunca odanın anahtarı elimizde yok fakat `r` hakkı
olmadığımız için dizin içerisindeki tabloyu da kapının camından okuyamıyoruz.
`w` hakkı bize o tabloyu değiştirme hakkı veriyor. Ama odaya giremedik, `x` yok.
Bu açıdan `w` hakkı, tek başına işe yaramıyor ne yazık ki, `---` ile aynı
noktadayız.

## `--x`

Dizinde `x` hakkı olduğu zaman kapının anahtarı bizde, içeriye girebiliyoruz ve
çıkış kapısından çıkabiliyoruz. İçeriye girebildiğimiz için `çöz()` fonksiyonunu
da kullanabiliyoruz. Fakat `r` hakkımız olmadığı için tabloyu göremiyoruz. Eğer
adını bildiğimiz bir dosya var ise `çöz()` fonksiyonunu çağırabildiğimiz için
onun bilgilerini alıp, içeriğine erişebiliriz. Ama dizin içerisindeki girdileri
göremiyoruz, listeleyemiyoruz.

```shell
alper@brs23-2204:~/sys$ ls -ld a
d--xrwxr-x 3 alper alper 4096 Jul 14 14:10 a

alper@brs23-2204:~/sys$ ls a
ls: cannot open directory 'a': Permission denied

alper@brs23-2204:~/sys$ cat a/x
Ben x'im
alper@brs23-2204:~/sys$ cat a/y
Ben y'yim

alper@brs23-2204:~/sys$ ls -li a/x
8521330 -rw-rw-r-- 1 alper alper 9 Jul 14 14:10 a/x
```

Gördüğünüz gibi `ls` ile klasörün içeriğini alamadım çünkü `r` hakkım yok. Ama
içerisinde `x` ve `y` isimli dosyaların olduğunu biliyorum. Bu sayede dosyaların
içeriklerini okuyabildim ve inode bilgilerine (izin, sahiplik) erişebildim. `r`
hakkı olmadan `x` hakkı vermek kullanıcının bildiği dosyaları görmesini sağlıyor,
pek pratik değil.

## `rw-`

`x` hakkı olmadan `w` hakkına sahip olmak çok kullanışlı değil. `rw-` ile `r--`
aynı şeyleri yapabilecektir.

## `r-x`

Bu sık kullanılan izinlerden biri. Bu izne sahip olunduğunda klasör içeriği `ls`
ile görüntülenebilir, çünkü tabloyu görebiliyoruz ve `x` hakkı olduğu için
içeriye girip işler yapabiliyoruz. `w` hakkı olmayınca ne yapamıyoruz? `w` hakkı
olmadığı için dizin içerisindeki bilgileri değiştiremiyoruz. Dosyaların adının
değiştirilmesi ve silinmesi, yeni dosya eklenmesi bu tablonun değiştirilmesini
gerektiriyor. O yüzden bu durumda dizin içerisinde değişiklik yapamayız ama
hedef dosyalarda yazma hakkımız varsa elbette içeriklerini değiştirebiliriz.

```text
alper@brs23-2204:~/sys$ ls -ld a
dr-xrwxr-x 3 alper alper 4096 Jul 14 14:10 a

alper@brs23-2204:~/sys$ ls a
x  y  z
alper@brs23-2204:~/sys$ cd a

alper@brs23-2204:~/sys/a$ touch yeni
touch: cannot touch 'yeni': Permission denied

alper@brs23-2204:~/sys/a$ rm x
rm: cannot remove 'x': Permission denied

alper@brs23-2204:~/sys/a$ mv x xx
mv: cannot move 'x' to 'xx': Permission denied

alper@brs23-2204:~/sys/a$ cat x
Ben x'im

alper@brs23-2204:~/sys/a$ echo "Artik x degilim" > x
alper@brs23-2204:~/sys/a$ cat x
Artik x degilim
```

gibi.

## `-wx`

Bu da pek pratikte kullanılacak bir izin değil. Tabloyu okuyamıyoruz yani `ls`
ile listeliyemiyoruz fakat tabloyu değiştirebiliriz. Ayrıca bildiğimiz dosyalara
erişebiliyoruz. `w` hakkımız olduğu için dosyaları silip, yenilerini
ekleyebiliyoruz.

```shell
alper@brs23-2204:~/sys$ ls a
ls: cannot open directory 'a': Permission denied

alper@brs23-2204:~/sys$ rm a/x

alper@brs23-2204:~/sys$ touch a/xx

alper@brs23-2204:~/sys$ echo "xx" > a/xx

alper@brs23-2204:~/sys$ cat a/xx
xx

alper@brs23-2204:~/sys$ cd a
alper@brs23-2204:~/sys/a$
```

## `rwx`

Tam yetki, her şey serbest.

## `---`

Hiçbir yetki yok.

## Özet

Dizinde `x` hakkı olmadığı zaman aslında bir çok şeyi yapamıyoruz. Diyelim ki
`/` tepe dizininden başlayarak aşağıya doğru ilerliyoruz. Yolda `x` hakkımızın
olmadığı bir dizinle karşılaşırsak aslında arkasında bulunan dosyaları
okuyamayız.

Diyelim ki bir dizinde `rw-` hakkımız var. Dizinin adı `a` ise, bu durumda
arkasındaki dosyaları silemeyiz. Çünkü bir dosyayı silmek, onun inode'u
içerisinde de değişiklik yapmayı gerektiriyor. En azından link sayısı 1
düşürülmeli. Fakat `x` hakkımız olmadığı için zaten odaya giremiyoruz.
Odaya giremediğimiz için, dizin tablosunda da değişiklik yapamıyoruz. Bu açıdan
`rm`, `mv` gibi komutları çalıştırabilmemiz için o dizinde `x` hakkımızın olması
gerekiyor.

## Kaynaklar

- <https://wpollock.com/AUnix1/FilePermissions.htm>
