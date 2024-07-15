# Modbus

Modbus, OSI modelinde en tepede yani application layer'da duran bir protokoldür.

1979 yılından beri hayatımızdadır.

Modbus şu açıdan ilginç bir protokoldür: Hem TCP/IP, hem de RS232/RS422 gibi
asenkron seri kanal protokolleri üzerinde çalışabilir. **Modbus TCP/IP**,
adı üstünde TCP/IP üzerinde de çalışmaktadır. **Modbus RTU** ve **Modbus ASCII**
ise RS-485 gibi seri kanal protokolü üzerinde çalışmaktadır. RTU, **R**emote
**T**erminal **U**nit demektir. RTU'da iletişim binary olurken, ASCII olanda
ASCII karakterler üzerinden olmaktadır. RTU'da `0xAB` göndereceksek bir byte
olarak `0xAB` gönderiyoruz, ASCII olanda iki byte gidiyor `'A'` ve `'B'`. ASCII
olanı daha verimsiz bir protokol olsa da doğrudan "yazı" olarak gönderilip,
monitör edilmesi bazı işleri kolaylaştıracaktır. Modbus'ta pek bir verim
ihtyiacı zaten yoktur.

Modbus TCP/IP, standart olarak 502 TCP'de çalışmaktadır.

**Server/client**, **request/reply**, **master/slave** şeklinde tasarlanmıştır.

Bir de Modbus Plus vardır, bu doküman dışında o konu.

```{figure} assets/modbus-stacks.png
:align: center

Modbus protokolü birçok farklı katman üzerinde çalışabilmektedir.
Görsel alıntıdır. `[1]`
```

## Protokol

```text
| ---------- ADU: Application Data Unit -------- |

| Adres | Function Code |   Data   | Error Check |

        | PDU: Protocol Data Unit  |
```

PDU, Modbus tarafından altta kullanılan iletişim yönteminden (seri kanal,
ethernet vs) tanımlanmaktadır. `PDU` içerisinde, `Function Code` ve `Data`
vardır.

Alttaki katmana göre yukarıdaki örnekteki gibi ek katmanlar gelebilir. PDU ve ek
paketler ise ADU'yu oluşturur.

İletişim client tarafından başlatılır, ADU paketini client oluşturur. RS-485
üzerinde çalışan Modbus üzerinde master node client olmakta ve diğer nodlar ise
slave ve server olmaktadır.

Function Code ile yapılması istenen iş söylenir, 1 byte genişliktedir. Anlamlı
`1-255` arası değerler alabilir. `128-255` arası değerler exception cevaplar
için ayrılmıştır ve rezervedir. `0` geçerli değildir. Özelte `1-127` arası
(sınırlar dahil) function code değerleri geçerlidir.

Sub-function code'ları fonksiyonun ne yapacağını detaylandırmak için eklenebilir.
Bazı function code'lar, yapılacak eylemi detaylandırmak için Data kısmında
sub-function code barındırır.

---

Data kısmı olmayabilir, 0 uzunlukta olabilir. PDU sadece Function Code'dan
oluşabilir.

---

Eğer her şey yolunda ise cevap paketinde function code aynen geri konur. Eğer
hata durumu ile karşılaşıldı ise `0x80` ile OR'lanır yani function code'un MSB
biti set edilir. Bu yüzden geçerli function code'lar `127` ye kadar (dahil) dir.

---

İlk tasarlan RS485 temelli Modbus protokolünde ADU maksimum 256 byte olarak
tanımlanmıştır. Bu protokolde, 1 byte adres ve 2 byte CRC vardır. Bu yüzden
Modbus'taki maksimum PDU, 256-1-2 = 253'tür. 253 üzerinde TCP Modbus için ilgili
ekleri koyarsak, bunlar da 7 byte ediyormuş, TCP MODBUS ADU maksimum 260 byte
olarak bulunur.

## MODBUS PDU

MODBUS, 3 farklı PDU tanımlamaktadır:

- Request PDU, `mb_req_pdu`
- Response PDU, `mb_rsp_pdu`
- Exception Response PDU, `mb_excep_rsp_pdu`

### Request PDU

Bu PDU'da 1 byte function code ve n byte data vardır. Data kısmının anlamı
function code'a bağlıdır.

### Response PDU

Bu da request PDU ile aynı yapıdadır.

### Exception Response PDU

2 byte büyüklüğünde bir pakettir. 1 byte'lık function code, request PDU'da
bulunan function code'un, `0x80` ile OR'lanması ile oluşur. 1 byte'lık data
kısmında ise *MODBUS Exception Code* vardır. Bununla ilgili açıklamalar Modbus
dokümanının `7 MODBUS Exception Responses` kısmında anlatılmıştır, 9 tane kod
tanımlanmıştır. [^1f]

## Data Encoding

Big Endian kullanılmaktadır. 1 byte'ı aşan büyüklükler, 1 byte'lık parçalara
bölünür. Hatta ilk olarak MSB konur. Örneğin `0x1234` göndereceksek önce `0x12`
sonra `0x34` gönderilir.

## Data Model

Modbus, endüstriyel uygulamalar için tasarlanmıştır, o yüzden
dokümantasyonundaki bazı terimler garip gelebilmektedir.

Modbus dokümanlarında, protokol ile cihazın belleğindeki çeşitli değerlere
erişildiği (okuma veya yazma) düşünülmüştür. 4 farklı temel blok
tanımlanmıştır. Bu 4 adet blok adeta cihazın belleğinde durmaktadır ve bizler
Modbus üzerinden bunlara erişmekteyiz.

| Blok | Nesne Tipi | R/W |
| ----- | ---------- | --- |
| Discrete Input | 1-bit | R |
| Coils | 1-bit | R/W |
| Input Registers | 16-bit word | R |
| Holding Registers | 16-bit word | R/W |

```{figure} assets/modbus-figure-6.jpg
:align: center

Bellekte sanki bir bölgede Discrete Input, bir yerde Coils, bir yerde Input
Registers varmış gibi düşünebiliriz. Görsel alıntıdır. `[1]`
```

Elbette bu kısımlar overlap edebilir. Yani 16-bit genişliğindeki bir register'ı
hem Input Registers ile word genişliğinde hem de Coils ile bitwise görebiliriz.
Yani bellekteki bazı lokasyonlar birbirinin *alias* ı olabilir.

```{figure} assets/modbus-figure-7.jpg
:align: center

Burada da tüm 4 blok alias durumdadır. Görsel alıntıdır. `[1]`
```

Bellekteki bu alanların değerlerinin ne ifade edeceği tamamen **vendor
bağımlıdır.** Modbus'un sunduğu bu veri modelinin, uygulamaya nasıl bağlanacağı
IEC-61131 gibi *application model* ler ile belirlenir.

Modbus protokollerinde bu 4 farklı türdeki hafıza, bir numara ile
adreslenmektedir. Modbus paketlerinde, PDU içerisinde, bu adresler `0-65535`
arasında olmaktadır. Fakat Modbus data model'i denen bir modelde adres `1` den
başlamaktadır. Örneğin 3 nolu Discrete Input türünden bir biti okumak için
gerekli olan Modbus paketindeki adres değeri 2 olmalıdır, kafa karıştırıcı değil
mi...

```{figure} assets/modbus-figure-8.jpg
:align: center

Paket'te `n` yazıyorsa hafızada `n+1` e erişiyoruz. Görsel alıntıdır. `[1]`
```

## Function Codes

Yukarıda `1-127` (sınırlar dahil) arasındaki function code'ların geçerli
olduğundan bahsetmiştik.

```{figure} assets/modbus-figure-10.jpg
:align: center

Function code'ların bir kısmı rezerve, bir kısmına da önden anlamlar
yüklenmiştir. Görsel alıntıdır. `[1]`
```

Bu aralıktaki kodların bir kısmı Modbus tarafından PUBLIC olarak işaretlenmiş ve
genel amaçlıdır. Bir kısmı ise User Defined olarak bırakılmıştır.

Bunları da başka bir yazıda irdeleyelim, burada genel bir bakış attık.

## Kaynaklar

- <https://en.wikipedia.org/wiki/Modbus>
- `[1]`: <https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>

[^1f]: <https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>
