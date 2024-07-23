# Modbus RTU

Modbus bir seri kanal üzerinde, RS-232 veya RS-485 üzerinde implement edildiği
zaman ve veri binary olarak taşındığı zaman Modbus RTU adını almaktadır. Binary
değil de text olarak taşınıyorsa da Modbus ASCII olmaktadır. RTU'yu anlamak için
Modbus dokümanını temel alacağız. [^1f]

---

RTU'da hattaki master node Modbus client, slave node'lar Modbus server
olmaktadır.

Seri bir haberleşme hattı üzerinde implement edilen Modbus RTU'da sadece 1 adet
master olmaktadır ve maksimum 247 adet slave olabilir.

- İletişim her zaman master tarafından başlatılır.
- Master'dan bir şey sorulmadan slave kendi başına gaza gelip bir mesaj atmaz
- Slave'ler kendi arasında konuşamaz.
- Master aynı anda sadece 1 adet transaction başlatabilir.

---

İki tip mode tanımlıdır. **Unicast mode** da master bir adet slave'e bir şey
der, slave de bunun cevabını verir. Burada transaction dediğimiz şey bu iki
paketten oluşur. Her slave'in `[1-247]` arası (sınırlar dahil) adresi vardır.

**Broadcast mode** da ise master bir isteği tüm slave'lere yollar. Burada
slave'ler tarafından bir cevap verilmez yani transaction dediğimiz şey tam da
tanımlı değildir ama tanımlamak istersek tek mesajdan oluşuyor gibi
düşünebiliriz. Adres `0` gönderilen paketler broadcast paket olmaktadır ve tüm
slave'ler bu paketi almalıdır.

---

Adres alanı 1 byte'tan oluşmaktadır:

| Adres | Fonksiyon |
| ----- | --------- |
| `0` | Broadcast adresi |
| `[1-247]` | Slave adres |
| `[248 - 255]` | Rezerve |

Bir adres iki adet slave'e atanamaz. Master mode'un bir adresi olmak zorunda
değildir, sadece slave node'ların adresi olması zorunludur.

---

RTU'da paket formatı şöyledir:

```text
| Adres (1 byte) | Function code (1 byte) | Data (0-252 byte) | CRC (2 byte) |
```

---

Modbus RTU dokümanında master ve slave node'lar için state diyagramlar
verilmiştir.

## Master State Diagram

```{figure} assets/modbus-rtu-figure-7.jpg
:align: center

Görsel alıntıdır. `[1]`
```

- Master açılınca `Idle` state'inde duruyor. **Bu state'te değilse request
  atamıyor.** Yani bir request attıktan sonra Idle'a gelene kadar başka request
  atılamaz.
- Unicast mode'da bir slave adreslenerek mesaj atıldıysa master cevap beklemeye
  geçer. Bir yandan da bir time-out süresi saymaya başlar. Time-out süresi
  implementation defined olarak bırakılmıştır.
- Diyelim ki mesaj geldi. Başka bir slave cevap verdiyse ya da gelen pakette CRC
  hatası vs varsa ya da time-out olduysa hata durumuna gidilir. Master isterse
  retry yapabilir.
- Broadcast mesajlarda slave'ler bir cevap dönmez. Ama master slave'lerin bunu
  işlemesi için **trunaround delay** kadar beklemelidir. Bu bekleme sırasında
  yeni mesaj atamaz.
- 9600 bps için turnaround delay tipik olarak 100-200 ms yani ~96 - ~192 byte
  arası, time-out süresi ise saniyeler mertebesindedir.

## Slave State Diagram

```{figure} assets/modbus-rtu-figure-8.jpg
:align: center

Görsel alıntıdır. `[1]`
```

- Slave açılınca `Idle` state'inde duruyor.
- Bir paket geldiği zaman eğer gelen pakette CRC hatası gibi hatalar varsa veya
  master'ın attığı paket ile ilgili slave adreslenmediyse, paket slave
  tarafından discard edilebilir. Bu durumda slave'in bir cevap vermesine gerek
  yoktur.
- Eğer pakette slave'in yapamayacağı bir şey isteniyorsa ya da paketin içeriği
  hatalı ise master'a cevap dönülmelidir.
- Her şey yolunda ise master'ın istediği yapıldıktan sonra ve paket **unicast
  ise** master'a cevap dönülmelidir.

```{note}
🤔 State diyagramında ve açıklamada ne olmayan bence şöyle bir kısım var:
Broadcast paketinin içeriğinde hata varsa slave yine cevap dönmeli mi? Bence
broadcast mesajında böyle bir durum olmamalı. Birden fazla frame cevap dönmeye
çalışırsa ne olacak hata durumunda? Bunun cevabını Modbus dokümanı içerisinde
yakalayabiliyoruz `[1]`:

It comprises also the error detected in broadcast messages even if an
exception message is not returned in this case.

Yani diyor ki broadcast durumunda hata oluşursa cevap dönülmez. Yine de açıkça
state diagramda belirtilirse daha iyi olurmuş.
```

## Örnek Akış

```{figure} assets/modbus-rtu-figure-9.jpg
:align: center

Görsel alıntıdır. `[1]`
```

Yukarıdaki görselde 3 adet transaction verilmiştir.

İlk olanda, yani `i-1` olanda, master bir istek atmakta, arkasından da slave
cevap vermektedir. Burada slave'in paketi aldıktan sonra işlemesi bir müddet
vakit almaktadır: `Request treatment`. Daha sonra slave cevap atmakta ve
master'da bir süre gelen cevabı incelemektedir.

Bir sonrakinde, `i` olanda, master bir broadcast mesajı atmakta ve broadcast
mesajlarında slave'ler cevap vermemektedir. Fakat master `Turnaround delay`
kadar bir süre *open loop* şekilde beklemektedir. Bu süre, slave'lerin mesajı
işlemesi için master'ın beklediği bir süredir.

Son `i+1` isimli transaction'da slave paketi hatalı almakta, CRC hatası örneğin,
ve paketi drop etmektedir. Bu durumda slave bir cevap oluşturmaz. Master time
out'a girer ve bir sonraki transaction'a geçer.

`REQUEST`, `REPLY`, `BROADCAST` gibi süreler paket uzunluğuna ve baud rate'e
bağlıdır. Onun dışındaki bekleme süreleri ise slave'lere göre seçilmelidir. Ne
kadar sürede mesaj işlenebiliyor vs.

## Transmission Modes

Seri kanal üzerinde implement edilen Modbus protokolü için iki adet
*transmission mode* tanımlanmıştır: **RTU** ve **ASCII**. RTU modu tüm cihazlar
tarafından implement edilmelidir, ASCII opsiyoneldir. İki modu implement eden
cihazlarda default mode RTU olmalıdır. Mode, verinin mesaj içerisine nasıl
paketleneceğiniz ve nasıl gösterileceğini belirler. ASCII, text modu RTU ise
binary mode olarak düşünülebilir. Bu dokümanda sadece RTU'ya odaklanıyorum.

## RTU

*Bildiğimiz* seri kanal mesajlarından oluşur.

```text
| 1 bit start | 8 bit data (LSB önce) | 1 bit parity | 1 bit stop |
```

Data gönderilirken önce LSB biti hatta konur. Default olarak **even parity**
kullanılır. Opsiyonel olarak odd parity veya no parity de desteklenebilir.
Modbus dokümanları geniş bir destek aralığı için no parity'nin de
desteklenmesini önermektedir. Eğer parity kullanılmazsa yerine stop biti
konulmalıdır, yani 2 stop bit gönderilmelidir.

## CRC

RTU formatını hatırlayalım:

```text
| Adres (1 byte) | Function code (1 byte) | Data (0-252 byte) | CRC (2 byte) |
```

Burada CRC'nin önce LSB byte'ı sonra MSB byte'ı gönderilmelidir:

```text
CRC Low (1 byte) | CRC High (1 byte)
```

şeklinde.

Parity'nin olup olmamasından bağımsız olarak CRC olmak zorundadır.

CRC gözüktüğü gibi 16-bit genişleğindedir.

CRC, tüm mesaj üzerinden hesaplanır yani `Adres`, `Function code` ve `Data`
hesaplaması CRC'ye dahil edilir.

Modbus dokümanlarında CRC'nin hesaplanması detaylı olarak anlatılmaktadır. [^1f]
Pratikte aşağıdaki sitelerden CRC hesaplaması yapılabilir:

- <https://crccalc.com/> `CRC-16/MODBUS` kullanılmalıdır.
- <https://www.lammertbies.nl/comm/info/crc-calculation> `CRC-16 (Modbus)`
  kulanılmalıdır.

Yukarıdaki sitelere veri girerken `ASCII` değil `HEX` girdiğinizden emin olun.
Modbus dokümanlarından devam edecek olursak elimizdeki frame `0207` den
oluşuyorsa, yani adres `0x02` ve function code `0x07` ise yani data yoksa CRC,
`0x1241` olarak bulunmalıdır. Fakat bu CRC hatta konulduğu zaman hatta `0x41` ve
`0x12` görülmelidir. Çünkü Modbus protokolünde CRC'nin önce düşük byte'ı, LSB,
sonra yüksek byte'ı, MSB, gönderilmelidir.

## Framing

RTU mesajlaşmada **frame'ler arasında en az 3.5 karakter boşluk bulunmalıdır.**
**Peki karakter süresi ne kadardır?** Bir karakter 8 bit olarak mı yoksa 11 bit
(1 bit start + 8 bit data + 1 bit parity + 1 bit stop) olarak mı alınmalıdır?
Ben Modbus dokümanında net bir tanım göremedim. 8 bit, 11 bit, hatta 10 bit alan
var (bence en alakasızı bu, en azında RTU için ASCII modda 10 bit almak doğru
olacaktır). [^2f] 8 bit bence yanlış çünkü dokümantasyonda bir yerde

> Only the eight bits of data in each character...

diye bir laf geçiyor. Demek ki character 8 bit'ten fazla. 10 bit doğru değil
bence, parity var. O yüzden 11 bit olarak düşünmek mantıklı geliyor.

Bir frame içinde de karakterler arasında **1.5 karakter süresinden fazla boşluk
olmamalı.** Böyle bir durumda o frame eksik kabul edilir ve alıcı taraıfndan
ihmal edilmelidir.

3.5 karakterlik süre `t3.5`, 1.5 karakterlik süre de `t1.5` olarak geçmektedir.
Driver implementasyonuna bağlı olarak timer kullanımı CPU interrupt yükünü
arttırmaktadır. Baud rate arttıkça timer interrupt sıklığını arttırmamak için
Modbus dokümanı baud rate'ten bağımsız sabit değerler kullanılmasını
önermektedir. Buna göre:

```text
if baud rate > 19200
  t3.5 = 1750 us
  t1.5 =  750 us
else
  t3.5 = (3.5 * 11) / baud rate
  t1.5 = (1.5 * 11) / baud rate
```

Karakter süresinin kaç bit olacağı dediğim gibi net değildir. 19200 bps
değerindeki bu sayıları tutturmak için 11 değil 10 almak daha uygun oluyor ama
19200 bps değerinde bu sayılar tam örtüşecek diye bir şey de yok. Örneğin
[bu](https://github.com/BlackBrix/Simple-Modbus-Master/blob/217cb83d943cd7194faf2c577214a8ccca37b815/SimpleModbusMaster.cpp#L417)
kütüphanede de benim gibi 11 bit almışlar, neyse...

```{figure} assets/modbus-rtu-figure-13.jpg
:align: center

Görüldüğü gibi frame'ler arası en az 3.5 karakter süresi olmalıdır. Elbette
4.5 gibi daha büyük bir sayı da olabilir.

Görsel alıntıdır. `[1]`
```

Benzer şekilde:

```{figure} assets/modbus-rtu-figure-t15.jpg
:align: center

Bir frame içerisinde iki karakter arasında 1.5 karakter süresinden daha fazla
boşluk bulunamaz. Bu durumda alan kişi mesajı discard etmelidir.

Görsel alıntıdır. `[1]`
```

Hem master hem de slave açısından şöyle bir state diagram çizilebilir:

```{figure} assets/modbus-rtu-figure-14.jpg
:align: center

Görsel alıntıdır. `[1]`
```

- En az 3.5 karakter süresi boyunca bir iletim olmazsa hat *idle* olarak kabul
  edilir.
- Alan taraf `t3.5` bittikten sonra frame'in bittiğini düşünüp işler.
- Alan taraf isterse işlem kolaylığı açısından CRC'yi beklemeden adres alanını
  işleyip, eğer kendisi adreslenmediyse frame'in bitişini beklemeye
  başlayabilir. Devamını almasa da olur.

---

Modbus dokümanının devamında RS-485/422 protokolü ile ilgili daha genel bilgiler,
elektriksel özellikler, konnektör ve LED önerileri bulunmaktadır. Bu bilgileri
buraya tekrar almıyorum, çoğu da zaten Modbus'tan bağımsız bilgiler. Yine
de dokümandan takip edilebilir [^1f].

[^1f]: [MODBUS over Serial Line Specification & Implementation
    Guide](https://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf)
[^2f]: <https://stackoverflow.com/questions/20740012/calculating-modbus-rtu-3-5-character-time>
