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

Her bir function code'un anlamı ve ne yapılacağı Modbus dokümanında
anlatılmıştır. [^1f] Bunları tekrar yazmak pek anlamlı değildir. Temel
kavramları aktarmaya çalışacağım. RTU ile ilgili bilgileri de Modbus
dokümanından alacağım. [^2f]

## Read Coils, `0x01`

Modbus protokolünde *coil* 1-bit genişliğinde yazma ve okuma yapılabilen bir
alan olarak düşünülebilir. Bu komut server'dan (RTU'da slave) bu register'ları
okumak için kullanılır. Modbus'a göre 65536 adet coil olabilmektedir. Bu komut
ile okunmak istenen coillerin base adresi ve range'i verilir. Ardışıl olan
coiller okunabilir. Bir komut ile maksimum 2000 adet coil okunabilir. Cevap
paketinde de her coil 1 bit ile ifade edilir.

İstek:

- Function code: `0x01`
- Data, ilk 2 byte: `0x0000-0xFFFFF`, coil başlangıç adresi yani okunacak en
  düşük adresli coil adresi.
- Data, sonraki 2 byte: `1-2000`, kaç adet coil'in okunacağı.

İstek paketi toplam 5 byte'tan oluşmaktadır. Modbus bellek modelinde
paketlerdeki adresleme ile bellek adresleri arasında 1 fark olduğundan
bahsetmiştik. Yani cihaz belleğinde coil adresleri `1-65536` arasında iken
haberleşme sırasında coiller `0-65535` ile adreslenir. Bu tüm veri modelleri
için geçerlidir.

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

Coil status kısmı, base adres ile başlar yani en düşük adresli coil. İlk byte'ın
LSB biti en düşük adresli coil'in durumunu içermelidir. `1`, ON; `0`, OFF
demektir. Örneğin slave bu byte'ın değerini `1010 1101` olarak gönderirse:

```text
Bit:   1  0  1  0  1  1  0  1
Coil: 27 26 25 24 23 22 21 20
```

olarak anlamdırırız. Fakat unutmayın ki Modbus RTU'da data'nın önce LSB biti
konur. Yani osiloskop ile bakıyorsak hatta aslında `1011 0101` görürüz.

Adresleme bu şekilde artarak devam eder. En son byte'ta bpşluklar olabilir,
örneğin bu örnekte 4 bit padding yapılması gerekmektedir. Bunlar 0 ile pad
edilmelidir. Son byte:

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

Görebileceğimiz gibi farklı hata durumlarında farklı hatalar dönmelidir. Hata
durumlarında 1 byte function code, istek function code'un `0x80` ile ORlanması
ile oluşturulur. Daha sonra 1 byte data olarak `ExceptionCode` konur.

Diyelim ki master olmayan bir adresteki coil'i okumak istedi. Bu durumda da `02`
nolu exception dönüyorsak

Cevap:

```text
| Adres | 0x81 | 0x02 | CRC-l | CRC-h |
```

olacaktır.

---

Yazının geri kanalındaki komutların çalışma biçimi bu komuta benzediği için daha
yüzeysel anlatacağım.

## Read Discrete Inputs, `0x02`

Read coils, `0x01`, ile aynı çalışmaktadır.

## Read Holding Registers, `0x03`

Coil ve discrete input okumak ile benzerdir özünde. Holding Registers, Modbus
standartında 16-bit olarak tanımlanmıştır. Buna göre protokolde değişiklikler
olmaktadır. Farklı olarak tek seferde en fazla 125 adet register okunabilir, her
biri 16-bit. Bir register 2 byte şeklinde gönderilir. Modbus'a uygun olacak
şekilde ilk olarak MSB byte hatta konur, yani big endian order kullanılır.

## Read Input Registers, `0x04`

Read Holding Registers, `0x03`, ile aynı çalışmaktadır.

## Write Single Coil, `0x05`

Tek 1-bit lik coil register'ın değerini değiştirmek için kullanılır.

RTU İstek:

```text
| Adres | 0x05 | 0x0000 - 0xFFFF | 0x0000 or 0xFF00 | CRC-l | CRC-h |
```

CRC ve adres hariç 5 byte'lık bir pakettir. Function code sonrası ilk 2 byte
yazma yapılacak regsiter adresini belirtir. Önceki paketlerde olduğu gibi `1`
offset olayı burada da vardır. İlgili register'ı `ON` yapmak için `0xFF00`,
`OFF` yapmak için `0x0000` yazılır. Diğer değerler geçersizdir.

## Write Single Register, `0x06`

Tek bir holding register'a (16-bit) yazmak için kullanılır. Write Single Coil,
`0x05`, e oldukça benzer. Data kısmı sabit iki adet 16-bit veri yerine yazılması
istenen 16-bit veridir.

## Read Exception Status, `0x07`

**Sadece seri kanal** implementasyonlarında vardır. 8-bit bir değer okunuyor ama
ne işe yarıyor anlamadım.

## Diagnostics, `0x08`

**Sadece seri kanal** implementasyonlarında vardır. Slave cihazdan (server)
çeşitli sorgular ve test yapmaya yarar. 2 byte'lık sub-function code'lar ile
istek şekillendirilir. Detayları Modbus dokümanında vardır.

- Loopback test
- Bir slave cihazı susturmak
- İletişimi resetlemek
- Çeşitli istatistik register'larını okumak için

kullanılır.

## Get Comm Event Counter, `0x0B` ve Get Comm Event Log, `0x0C`

**Sadece seri kanal** implementasyonlarında vardır. Detayları dokümanlardan
okunabilir. Özünde seri kanal ile çeşitli istatistikleri döner.

## Write Multiple Coils, `0x0F`

Birden fazla 1-bit genişliğinde olan coil'e yazmaya yarar. Write Single Coil,
`0x05` den farkı birden fazla, ardışıl 1-bit register'a yazma imkanı sunmasıdır.
Tek seferde en fazla `1968` adet register'a yazma yapılabilir.

## Write Multiple Registers, `0x10`

Ardışıl 16-bit genişliğindeki holding register'lara yazma yapmayı sağlar.
Write Single Register, `0x06` komutundan farklı olarak birden fazla register'a
tek seferde yazmaya yarar. Bu komut ile tek seferde `123` adet register'a kadar
yazma yapılabilir.

## Report Server ID, `0x11`

**Sadece seri kanal** implementasyonlarında vardır. Cihaza özgü bir cevabı vardır.

## Read File Record, `0x14`

Modbus'ta *file* denen bir kavram vardır. Fiziksel olarak tam neye karşılık
geldiği bence net değil, üreticiye bırakılmış. Örneğin data logger gibi bir
cihazda file, capture edilen bir waveform'u gösterebilir. [^3f] Ya da uzaktan
yazılımını güncelleyeceğimiz bir cihazın flash'ında duran yazılımı bir file
gibi kurgulayabiliriz. Bu kısım, slave cihaz üreticisine bağlı.

Kurgusual olarak her bir dosyanın bir numarası vardır, bu numara aralığı
`1-65535` arasındadır. Bu numara, dosya ismi gibidir. Her bir dosya **record**
adı verilen 2-byte genişliğindeki parçalara bölünmüştür. Her bir dosya da
en fazla (?), `10000` adet record bulunabilir. **Böylece bir dosya en fazla
`20000 = 2 * 10000 byte, ~19.53 KB` boyutunda olabilir.**

Bu komut ile istenirse birden fazla file'dan ardışıl olmak üzere birden fazla
uzunlukta *record* okunabilir. Detayları dokümanında vardır. Protokol açısında
maksimum paket boyutunu geçmememiz lazım.

## Write File Record, `0x15`

Okuma komutuna benzer, paket formatı olarak da. Bu da yazma yapmak için kullanılır.

## Mask Write Register, `0x16`

Bir adet 16-bit genişliğindeki holding register'a doğrudan veri yazmadan, bit
bit bazı bitleri AND ve OR işlemine tutarak, yani maskeleyerek, set veya reset
etmeye yarar. Yani diyelim ki 10.bit'i set etmek, aynı anda 4.bit'i reset etmek
için bunu kullanabiliriz.

## Read/Write Multiple registers, `0x17`

Tek bir transaction ile birden fazla 16-bit holding register'ı, ardışıl olmak
şartı ile, okuma yapmaya ve yazma yapmaya (aynı adres aralığında olmak zorunda
değil okuma ile yazma fakat ikisi de kendi içinde ardışıl olmalı) yarar. Modbus
standardına göre önce yazma sonra okuma yapılır.

## Read FIFO Queue, `0x18`

Anladığım kadarıyla Modbus'ta genişliği 16-bit yani bir holding register
genişliğinde olan bir FIFO data modelinden bahsediliyor. Bu FIFO teorik
olarak `65535 + 31` derinliğinde. Bu komut ile FIFO'nu herhangi bir offsetine
gidip maksimum `31` adet veri okuyabiliyoruz. Bu komut ile FIFO'dan okuma
yapıldığı zaman FIFO içeriği silinmemektedir.

## Encapsulated Interface Transport, `0x2B`

Bu komut ile Modbus'a *tünelleme* yaptırılabilir. SSH Tünel gibi Modbus üzerinden
başka bir protokolün taşınması sağlanabilir. Modbus dokümanlarında CANOpen
mesajlarının taşınması anlatılmıştır. Tünelleme ihtiyacı olunca dönüp
bakılabilir.

## MODBUS Exception Responses

Modbus dokümanlarında çeşitli exception'lar tanımlanmıştır. Bunlar
protokollerin içinde de anlatılmaktadır. Diyelim ki desteklenmeyen komut attık,
yanlış parametre attık, bu durumda *exception response* gelecektir. Detayları
dokümanda anlatılmıştır. Bu durumda daha önceden bahsettiğimiz gibi
*function code*, `0x80` ile ORlanmaktadır.

[^1f]: <https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>
[^2f]: <https://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf>
[^3f]: <https://product-help.schneider-electric.com/ED/ES_Power/NT-NW_Modbus_IEC_Guide/EDMS/DOCA0054EN/DOCA0054xx/Master_NS_Micrologic_Data/Master_NS_Micrologic_Data-21.htm>
