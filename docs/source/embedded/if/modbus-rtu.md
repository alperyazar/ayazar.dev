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

- Master açılınca `Idle` state'inde duruyor. Bu state'te değilse request
  atamıyor. Yani bir request attıktan sonra Idle'a gelene kadar başka request
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

BURADAYIM

[^1f]: [MODBUS over Serial Line Specification & Implementation Guide](https://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf)
