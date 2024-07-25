# Modbus Function Codes

Bu yazıda, Modbus standartında belirtilen **Function Code** lara bakacağız.
Serideki diğer yazılarda Modbus ve Modbus RTU'yu konuştuk:

- [](modbus.md)
- [](modbus-rtu.md)

---

`1-127` arası function code'ların geçerli olduğundan bahsetmiştik. Bir
hatırlayalım:

```{figure} assets/modbus-figure-10.jpg
:align: center

Function code'ların bir kısmı rezerve, bir kısmına da önden anlamlar
yüklenmiştir. Görsel alıntıdır. `[1]`
```

Bu aralıktaki kodların bir kısmı Modbus tarafından PUBLIC olarak işaretlenmiş ve
genel amaçlıdır. Bir kısmı ise User Defined olarak bırakılmıştır.

```{figure} assets/modbus-function-codes-tablo.jpg
:align: center

Yukarıdaki görsel Modbus dokümanından alınmıştır. Bazı satırların neden sarı ile
highlight edildiğini bilmiyorum. Görsel alıntıdır. `[1]`
```

Her bir function code'un anlamı ve ne yapılacağı Modbus dokümanında anlatılmıştır.
[^1f] Bunları tekrar yazmak pek anlamlı değildir. Temel kavramları aktarmaya
çalışacağım.

## Read Coils, `0x01`

Modbus protokolünde *coil* 1-bit genişliğinde yazma ve okuma yapılabilen bir
alan olarak düşünülebilir. Bu komut server'dan (RTU'da slave) bu register'ları
okumak için kullanılır. Modbus'a göre 65536 adet coil olabilmektedir. Bu komut
ile okunmak istenen coillerin base adresi ve range'i verilir. Ardışıl olan coiller
okunabilir. Bir komut ile maksimum 2000 adet coil okunabilir. Cevap paketinde de
her coil 1 bit ile ifade edilir.

İstek:

- Function code: `0x01`
- Data, ilk 2 byte: `0x0000-0xFFFFF`, coil başlangıç adresi yani okunacak en
  düşük adresli coil adresi.
- Data, sonraki 2 byte: `1-2000`, kaç adet coil'in okunacağı.

İstek paketi toplam 5 byte'tan oluşmaktadır. Modbus bellek modelinde paketlerdeki
adresleme ile bellek adresleri arasında 1 fark olduğundan bahsetmiştik. Yani
cihaz belleğinde coil adresleri `1-65536` arasında iken haberleşme sırasında
coiller `0-65535` ile adreslenir. Bu tüm veri modelleri için geçerlidir.

Cevap:

- Function code: `0x01`
- Data, ilk 1 byte: Arkada kaç byte'lık data olacağı, `N` diyelim
- Data, sonraki `N` byte: Coil status bilgileri

Eğer 16 adet coil status okunmak istendiyse `N` 2 olacaktır fakat 17 adet
istendiyse 3 olacaktır. Sayının 8'e bölümünün üste yuvarlanması ile `N` sayısı
elde edilir.

Diyelim ki `20-39` adreslerindeki coilleri okumak istiyoruz. Modbus RTU üzerinde
aşağıdaki gibi olacaktır. Modbus'ın byte order'nın big endian, RTU'daki CRC'nin
ise little endian olduğunu hatırlayalım.

İstek:

```text
| Adres | 0x01 | 0x00 | 0x13 | 0x00 | 0x14| CRC-low | CRC-high |
```

Başlangıç adresimiz 20 fakat haberleşmede 1 eksiğini alıyoruz, 19 yani 0x13
oluyor. Okumak istediğimiz aralık ise `20 = 39 - 20 + 1` adet coil içeriyor,
yani 0x14.

20/8 = 2.5, bunu 3'e yuvarlıyoruz yani 3 byte cevap vereceğiz.

Cevap:

```text
| Adres | 0x01 | 0x03 | Coil 27-20 | Coil 35-28 | Coil 39-36 | CRC-l | CRC-h |
```

olacaktır.

Coil status kısmı, base adres ile başlar yani en düşük adresli coil.
İlk byte'ın LSB biti en düşük adresli coil'in durumunu içermelidir. `1`, ON;
`0`, OFF demektir. Örneğin slave bu byte'ın değerini `1010 1101` olarak
gönderirse:

```text
Bit:   1  0  1  0  1  1  0  1 
Coil: 27 26 25 24 23 22 21 20
```

olarak anlamdırırız. Fakat unutmayın ki Modbus RTU'da data'nın önce LSB biti
konur. Yani osiloskop ile bakıyorsak hatta aslında `1011 0101` görürüz.

Adresleme bu şekilde artarak devam eder. En son byte'ta bpşluklar olabilir,
örneğin bu örnekte 4 bit padding yapılması gerekmektedir. Bunlar 0 ile
pad edilmelidir. Son byte:

```text
Bit:   0  0  0  0  1  1  1  1 
Coil: -- -- -- -- 39 38 37 36
```

gibi...

---

Bir de **hata durumlarına** bakalım. Dokümanda gayet güzel gösterilmiş:

```{figure} assets/modbus-function-codes-11.jpg
:align: center

Görsel alıntıdır. `[1]`
```



[^1f]: <https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>
[^2f]: <https://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf>