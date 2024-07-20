# Modbus RTU

```{todo}
Doküman yarımdır.
```

Modbus bir seri kanal üzerinde, RS-232 veya RS-485 üzerinde implement edildiği
zaman ve veri binary olarak taşındığı zaman Modbus RTU adını almaktadır. Binary
değil de text olarak taşınıyorsa da Modbus ASCII olmaktadır. RTU'yu anlamak için
Modbus dokümanını temel alacağız. [^1f]

---

RTU'da hattaki master node Modbus client, slave node'lar Modbus server olmaktadır.

Seri bir haberleşme hattı üzerinde implement edilen Modbus RTU'da sadece 1
adet master olmaktadır ve maksimum 247 adet slave olabilir.

- İletişim her zaman master tarafından başlatılır.
- Master'dan bir şey sorulmadan slave kendi başına gaza gelip bir mesaj atmaz
- Slave'ler kendi arasında konuşamaz.
- Master aynı anda sadece 1 adet transaction başlatabilir.

---

İki tip mode tanımlıdır. **Unicast mode** da master bir adet slave'e bir şey
der, slave de bunun cevabını verir. Burada transaction dediğimiz şey bu iki
paketten oluşur. Her slave'in `[1-247]` arası (sınırlar dahil) adresi vardır.

**Broadcast mode** da ise master bir isteği tüm slave'lere yollar. Burada
slave'ler tarafından bir cevap verilmez yani transaction dediğimiz şey
tam da tanımlı değildir ama tanımlamak istersek tek mesajdan oluşuyor gibi
düşünebiliriz. Adres `0` gönderilen paketler broadcast paket olmaktadır ve
tüm slave'ler bu paketi almalıdır.

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

Modbus RTU dokümanında master ve slave node'lar için state diyagramlar verilmiştir.

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
- Bir paket geldiği zaman eğer gelen pakette CRC hatası gibi hatalar varsa
  paket slave tarafından discard edilebilir. Bu durumda slave'in bir cevap
  vermesine gerek yoktur.
- Eğer pakette slave'in yapamayacağı bir şey isteniyorsa ya da paketin içeriği
  hatalı ise master'a cevap dönülmelidir.
- Her şey yolunda ise master'ın istediği yapıldıktan sonra ve paket **unicast
  ise** master'a cevap dönülmelidir.

```{note}
🤔 State diyagramında ve açıklamada ne olmayan bence şöyle bir kısım var:
Broadcast paketinin içeriğinde hata varsa slave yine cevap dönmeli mi? Bence
broadcast mesajında böyle bir durum olmamalı. Birden fazla frame cevap dönmeye
çalışırs ne olacak hata durumunda?
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
bağlıdır. Onun dışındaki bekleme süreleri ise slave'lere göre seçilmelidir.
Ne kadar sürede mesaj işlenebiliyor vs.

## Transmission Modes

BURADAYIM

[^1f]: [MODBUS over Serial Line Specification & Implementation Guide](https://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf)
