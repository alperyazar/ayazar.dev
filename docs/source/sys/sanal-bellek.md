---
giscus: e859a822-bee2-4366-9c19-37ffbac5b2de
---

# Sanal Bellek, Virtual Memory

```{todo}
Henüz bitmemiştir.
```

`35-1.27.40`

**Sanal bellek (virtual memory)** bir programın tamamının değil belli kısmının
belleğe yüklenerek disk ile RAM arasında yer değiştirmeli bir biçimde
çalıştırılmasına yönelik bir mekanizmadır. Bu mekanizma sayesinde örneğin 100
MB'lık bir programın başlangıçta yalnızca 64K'lık kısmı RAM'e yüklenebilir.
Sonra program çalışmaya başlar. Çalışma sırasında programın bellekte olmayan bir
kısmına erişildiğinde işletim sistemi programın bellekte olmayan kısmını o anda
diskten belleğe yükler ve çalışma kesintisiz devam ettirilir. Ayrıca gündelik
hayatta *sanal adres* mekanizması da *sanal bellek* olarak adlandırılabilmektedir.
Bu paragrafta aslında biraz da ileride konuşacağımız *swap* mekanizması ağırlıklı
bir açıklama yaptık.

Şu aşamada detay olabilir belki ama Linux'ta **Working Set** denilen bir kavram
vardır. Bir prosesin kaç sayfasının gerçekten fiziksel bellekte olduğunu
gösteren bir kavramdır. [^1f] Bildiğim kadarıyla kernelde bir proses
başlatıldığında kaç adet sayfanın fiziksel belleğe yüklenebileceğini
belirleyebiliyoruz (initial working set size ?). Bu kavramlar yine ağırlıklı
*swap* ve *page fault* gibi terimlerle alakalı.

## Swap In/Out

`35-1.40.40`

Sanal bellek kullanımında yine fiziksel RAM sayfalara ayrılır. Her sayfaya bir
numara verilir. İşletim sistemi RAM'in hangi sayfasının hangi programın neresini
tuttuğunu bir biçimde oluşturduğu veri yapılarıyla bilir duruma gelir. Bir
programın RAM'de olmayan bir sayfasının diskten RAM'e yüklenmesine **swap in**
denilmektedir. Ancak zamanla RAM'deki tüm fiziksel sayfalar dolu duruma
gelebilir. Bu durumda işletim sistemi bir programın bir parçasını RAM'e
çekebilmek için RAM'deki bir sayfayı da RAM'dan atmak durumunda kalır. Bu işleme
ise **swap out** denilmektedir. Tabii işletim sistemi hangi programın RAM'deki
hangi sayfasının boşaltılacağı konusunda iyi bir karar vermek durumundadır.
İşletim sistemine göre *gelecekte kullanılma olasılığı en düşük olan sayfanın*
RAM'den atılması en iyi stratejidir.

Bu durumda bir program çalışırken aslında sürekli bir biçimde disk ile RAM
arasında yer değiştirmeler yapılmaktadır. Bu yer değiştirmelere genel olarak
işletim sistemi dünyasında **swap** işlemi denilmektedir. Şüphesiz swap işlemi
yavaş bir işlemdir ve toplam performans üzerinde en önemli zayıflatıcı
etkilerden birini oluşturmaktadır. Swap işlemlerinin olumsuz etkisini azaltmak
için ilk akla gelen şey fiziksel RAM'i büyütmektir. Ancak fiziksel RAM'in
büyütülmesi maliyet oluşturmaktadır. Bugünkü SSD'ler hard disklere göre oldukça
iyi performans göstermektedir. Dolayısıyla bilgisayarımızda hard disk yerine SSD
varsa swap işlemleri daha hızlı yürütülecektir. Şüphesiz en önemli unsur aslında
sayfaların yer değiştirilmesi konusunda uygulanan algoritmalardır. Bunlara
**page replacement** algoritmaları denilmektedir. Tabii bugünkü işletim
sistemleri bilinen en iyi algoritmaları zaten kullanmaktadır.

`35-1.51.30`

**Pekiyi işletim sistemi programın RAM'de olmayan bir sayfasını yüklemek
istediğinde RAM'den sayfa boşaltacağı zaman boşaltılacak sayfa üzerinde daha
önce yazma işlemleri (update) yapıldıysa ne olacaktır?** İçeriği değiştirilmiş
olan sayfanın RAM'den atılırken mecburen diskte saklanması gerekir. İşte işletim
sistemleri bu işlemler için diskte ismine **swap file** ya da **page file**
denilen dosyalar tutmaktadır. Değiştirilmiş olan sayfaları bu dosyalara
yazmaktadır. Linux işletim sistemi swap alanı olarak genellikle ayrı bir disk
bölümünü kullanmaktadır. Ancak herhangi bir dosya da swap dosyası olarak
kullanılabilmektedir. Kullanılacak swap disk alanının ya da dosyalarının toplamı
bazen önemli olabilir. Çünkü sistemin toplam sanal bellek kapasitesi bu swap
dosyalarıyla da ilgilidir. Linux sistemlerinde o andaki toplam swap alanları
`/proc/swaps` dosyasından elde edilebilir. Ya da `swapon -s` komutuyla aynı
bilgi elde edilebilir. Örnek:

```shell
ay@2204:~$ cat /proc/swaps
Filename                Type        Size        Used    Priority
/swapfile                               file        2097148     0   -2

ay@2204:~$ swapon -s
Filename                Type        Size        Used        Priority
/swapfile                               file        2097148     0       -2
```

**Pekiyi sistemin kullandığı swap alanı dolarsa ne olur?** İşte bu durumda
sistemin sanal bellek limiti dolmuş kabul edilir. Yapılacak şey sisteme yeni
swap alanları eklemektir. Bunu anlatan tonla kaynak vardır.

**Pekiyi işletim sistemi programı belleğe yüklerken baştan kaç sayfayı
yüklemektedir?** İşte buna **minimum working set**, (initial working set size ?)
denilmektedir. İşletim sistemleri genel olarak bir program için en az
yüklenebilecek sayfa sayısını belirlemiş durumdadır. **Böylece yüklenmiş her
programın en azından "minimum working set" kadar sayfası RAM'de bulunmak
zorundadır.**

## Kaynaklar

[](kaynak.md) fakat ağırlıklı CSD notları.

Videolar:

```{youtube} 5lFnKYCZT5o
:align: center
:width: 100%
```

- [Working Set Size Estimation](https://www.brendangregg.com/wss.html)

```{todo}
<https://www.brendangregg.com/wss.html> adresindekine benzer deneyler
yapabilirsin.
```

[^1f]: <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/4/html/introduction_to_system_administration/s2-memory-concepts-wset#s2-memory-concepts-wset>
