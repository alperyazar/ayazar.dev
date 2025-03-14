---
giscus: fec264f4-d4ff-4d70-8441-41081fc12e51
---

# Nedir bu Zephyr?

[Zephyr](https://www.zephyrproject.org/), günümüzde popüler bir **RTOS
ekosistemi**dir. Sadece bir RTOS, Gerçek Zamanlı İşletim Sistemi, değil bir
ekosistem, adeta bir framework'tür. Örneğin yine popüler bir RTOS olan
FreeRTOS'u ele alacak olursak FreeRTOS ağırlıklı olarak temel kernel
fonksiyonlarını sunan bir projedir. Her ne kadar Amazon'un AWS IoT hizmetleri
için FreeRTOS'u desteklemesi ile *kütüphane* tarafı biraz daha genişlese de
Zephyr gibi bir ekosistem sunmadığını söylemek bence yanlış olmaz. Elbette bu
salt iyi ya da kötü bir şey değildir, mühendisliğin neredeyse tüm sorularında
olduğu gibi cevap duruma göre değişir.

Zephyr'in kalbinde elbette tüm RTOS projelerinde olduğu gibi bir kernel yani
çekirdek yer almaktadır. Yine bu kernel ile beraber yazılımcıya sunulan birçok
kütüphane ve katman da vardır.

```{figure} assets/zephyr-layers.jpg
:align: center

Zephyr ile beraber sadece bir RTOS kernel değil aynı zamanda birçok üst katman
bileşen de sunulmaktadır.
```

Zephyr'in özellikle *connectivity* açısından güçlü olduğunu söyleyebilirim.
Birçok kablolu ve kablosuz bağlantı protokolüne ve bu bağlantılar üzerinde
çalışan daha üst seviye protokollere ihtiyaç duyan uygulamalar, Zephyr ile
görece kolay yazılabilir.

## Kconfig, Devicetree ve West

Eğer gömülü Linux ile uğraşıyorsanız Zephyr'de size tanıdık gelecek çeşitli
bileşenler göreceksiniz: Kconfig ve Devicetree. Zephyr, düşük kaynak içeren
MCU'ları da hedefleyen bir RTOS olmasına rağmen gömülü Linux geliştirme
sürecinde bulunan çeşitli akışları bünyesinde barındırır. Bunlardan en belirgin
olanı Devicetree'dir. Bir Zephyr projesinde de MCU ve ona bağlı olan donanımlar
[Devicetree](https://docs.zephyrproject.org/latest/build/dts/index.html)
aracılığı ile tanıtılır. Zephyr'de, **device driver** modeli bulunmaktadır.
Projede ayrıca konfigürasyon işlemleri için yine Linux kernel'de de kullanılan
[Kconfig](https://docs.zephyrproject.org/latest/build/kconfig/index.html)
kullanılmaktadır.

Zephyr'de bir de Python temelli
[west](https://github.com/zephyrproject-rtos/west) isimli bir *meta tool*
bulunmaktadır. Bu araç aslında bir Zephyr tabanlı proje yaparken işleri koordine
etmeye yarar. Projeyi oluşturma, projedeki dependency'leri Git repoları
üzerinden çekme, projeyi derleme, derlenmiş projeyi karta atma yani *flaşlama*
(bu terimi pek sevmiyorum ama *flashing* olarak da resmi dokümanlarda geçiyor.
Gençler de kullanıyor bu terimi ama ben bir ısınamadım bir türlü) işlemleri
`west` üzerinden yapılabilmektedir.

Zephyr'e genel olarak ele aldığımızda projenin Yocto, Buildroot gibi gömülü
Linux geliştirmeye yönelik projeler gibi, hatta belki onlardan da fazla,
kapsamlı bir proje olduğunu söyleyebiliriz. İşte bu yüzde Zephyr sadece bir RTOS
değil bir RTOS ekosistemidir. Elbette bu giriş yazısında bahsedemediğim irili
ufaklı başka özellikleri de vardır.

## Tarihçe

Zephyr'in temelleri DSP'ler için geliştirilen **Virtuoso RTOS** isimli başka bir
projeye dayanmaktadır. Bu proje Belçikalı Eonic Systems tarafından
geliştirilmiştir. 2001 yılında Wind River Systems bu firmayı satın almıştır.
2015'te Wind River Systems, projenin adını **Rocket** olarak değiştirmiş ve açık
kaynak hale getirimiştir. Wind River'ın meşhur ürünlerinden biri yine bir RTOS
olan VxWorks'tür. VxWorks'ün aksine Rocket daha küçük bellek alanına ihtiyaç
duymaktadır ve küçük cihazla için uygundur. VxWorks tipik olarak 200 KB civarı
belleğe ihtiyaç duyarken Rocket 4 KB bellek ile çalışabilmektedir.

**2016** itibariyle Rocket projesi Linux Foundation'un kanatları altına girmiş
ve adı Zephyr olmuştur. Wind River, Rocket'i satmaya devam etmiş ve adeta
Rocket, Zephyr'in ticari versiyonu olmuştur.

Günümüzde Zephyr, [Apache
2.0](https://www.tldrlegal.com/license/apache-license-2-0-apache-2-0) lisansı
ile yayınlanan bir açık kaynak projedir ve ticari amaçlarla kullanılabilir.

Zephyr, adını **Zephyrus**, yani **Zefiros** tan alır. Kendisi, Yunan
mitolojisinde "batı" rüzgarı tanrısıdır. `west` isimli aracı hatırladınız değil
mi... 😉 Tam net bir kaynak bulamasam da ben bunla bir bağlantı kurdum kafamda.

Git reposu: <https://github.com/zephyrproject-rtos/zephyr>

**C** dilinde yazılmış olup, C ve C++ dilinde uygulama geliştirmeyi destekler.
Özellikle Mart 2025'te yayınlanan 4.1.0 sürümü ile beraber Rust ile uygulama
yazma da daha deneysel olarak getirilmiştir. Güncel durumda Zephyr'in kendisini
Rust ile yazma gibi bir plan yoktur. [^1f]

Versiyon v1.6 öncesi microkernel yapısında iken 2016 yılında v1.6 ile beraber
monolithic kernel yapısına geçilmiştir. [^2f]

Kasım 2024'te yayınlanan v4.0.0 sürümü ile beraber projede 100bin'in üzerinde
commit yapılmış ve 2500'den fazla geliştirici projeye katkı sunmuştur. [^3f]
Diğer açık kaynak RTOS'lara kıyasla Zephyr birim zamanda en çok katkı sunulan
projedir. [^4f] Elbette bu gerçek, Zephyr'in sizin durumunuzda en iyi tercih
olacağı anlamına gelmez. *Hype* olan şeylere her zaman atlamak iyi değildir ❗

## Kaynaklar

- <https://www.zephyrproject.org/wp-content/uploads/2025/01/Zephyr-Overview-20250113.pdf>

[^1f]: <https://www.youtube.com/watch?v=TOIwI9XrHZM>
[^2f]: <https://en.wikipedia.org/wiki/Zephyr_(operating_system)>
[^3f]: <https://www.zephyrproject.org/>
[^4f]: <https://www.zephyrproject.org/wp-content/uploads/2025/01/Zephyr-Overview-20250113.pdf>
