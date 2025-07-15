---
# License: CC-BY-SA-4.0.
giscus: aa15a9cb-532d-4945-8f8e-0702583ddd88
---

# 🔴 Gömülü Sistemler, FPGA, Elektronik, Yazılım, Linux... | Ortaya Karışık - 2

```{note}
İçerik, video olarak sunulmuştur. Bu yazıda (varsa) düzeltmeler ve videoda
geçen bağlantılar veya videoya ek notlar sunulmuştur.
```

```{youtube} b8S4bKZV5Ao
:align: center
:width: 100%
```

---

## Bakılacak Sorular ve Cevapları

Canlı yayında bazı soruları not alıyoruz, sonradan bakalım diye. Bu kısımda
o soruları yayın sonrası araştırarak yanıtlamaya çalışıyoruz.

### FTDI Entegrelerini Xilinx JTAG Programlayıcıya Çevirmek

Bu soru videonun `17:20` dakikasında geliyor. Soruyu ilk başta anlamıyoruz ama
sonradan anlıyoruz ki, soru sahibi ile de sonradan özel mesajla konuşmuştuk
diye hatırlıyorum Yunus ile, kendi yaptıkları ve FTDI entegresi koydukları
bir karta JTAG özelliği getirilmek isteniyor. Kendiniz bir demo board yapıp
ona dahili JTAG özelliği getirmek gibi düşünebilirsiniz.

Normalde Digilen'ten kullanabileceğiniz *JTAG Module* ürünleri var, fakat bunlar
gerçekten pahalı. Örneğin
[JTAG-SMT2](https://digilent.com/shop/jtag-smt2-surface-mount-programming-module/)
ürününün güncel satış fiyatı **54 USD**, "biraz" fazla bence.

---

Vivado'nun ya da benzer diğer EDA araçlarının FTDI entegresini kendilerinin
tanıyabileceği şekilde görmesi için FTDI entegresinin programlanması gerekiyor.
Aksi taktirde örneğin Xilinx için Platform Cable olarak bu cihazlar gözükmüyor.
Fakat bu atılması gereken program/konfigürasyon açıkça bulunmuyordu.

Güncel durum için şunu söyleyebiliriz: Vivado 2022.1'den itibaren Xilinx resmi
olarak FTDI'a ait FT232H, FT2232H ve FT4232H entegrelerinin bu şekilde
programlanmasını destekliyor. [^1f] Yani günümüzde artık bunu bu şekilde
yapabiliriz.

Bundan önce de bazı kişiler çalışan FTDI entegrelerinden içeriği *dump* edip
çeşitli yerlerde paylaşmışlar ve kendi programlayıcılarını yapmışlar. Artık
çok gerekli olmasa da ilgili olabilecek bağlantılar:

- <https://www.reddit.com/r/FPGA/comments/ydt7fx/xilinx_now_supports_custom_ftdibased_usbjtag/>
- <https://github.com/anthony-bernaert/ftdi-jtag-programmer>
- <https://github.com/dragonlock2/ftdi_dumps>

*Geçen Çin'den ucuzcana bir Xilinx Platform Cable klon ürün aldım, onu da takınca
Digilent olarak gördü Vivado, herhalde benzer şekillerde yaptılar 🤣*

*İlk yayın: 2025-06-22*

[^1f]: <https://docs.amd.com/r/2022.1-English/ug908-vivado-programming-debugging/Programming-FTDI-Devices-for-Vivado-Hardware-Manager-Support>
