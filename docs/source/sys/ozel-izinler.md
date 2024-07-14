# Özel Dosya İzinleri

```{todo}
Yazı yarımdır.
```

Şimdiye kadar bir dosya veya dizin izni hakkında konuşurken 3 farklı gurptan
(user, group, other) ve 3 farklı izinden, `rwx`, bahsettik. Linux sistemlerde
bu izinlerin dışında farklı senaryolarda bize faydalı olabilecek birkaç izin
daha bulunmaktadır. `rwx` izinlerinin her biri 1-bit ile ifade edilebilir, 3
farklı kategori olduğu için de dosya izinleri 9-bit ile tutulabilir. İşte bu
özel izinler de 3-bit ile tutulmaktadır, yani 3 farklı türde izin göreceğiz.
Toplamda 12-bit ediyor

Şimdi onlara bir bakalım.

## Sticky Bit (`01000`)

Sticky Bit, ilk olarak 1975 tarihinde Unix'in 5. sürümünde tanıtılmıştır. İlk
kullanımı, sadece çalıştırılabilir (executable) dosyalar içindir. Bu bit'i
set edilmiş çalıştırılabilir dosyaların `text` alanı çalıştırıldıktan ve çıktan sonra
swap alanında saklanırmış. Bu bit tipik olarak sık kullanılan programların hızlı
çalışmasını sağlmak içinmiş. Swap alanına *yapıştıkları* için *sticky* olarak
adlandırılmışlar. [^1f]

Günümüzde Linux gibi Unix benzeri işletim sistemlerini çok daha karmaşık ve
verimli bellek yönetim mekanizmalarının olmasından dolayı bu bit başka amaçlar
için kullanılmaktadır.

### Dizinlerde Sticky Bit

Bir dizinin sticky bit'i set edildiği zaman çeşitli davranış değişiklikleri
olmaktadır. Böyle bir dizinin içerisinde yaratılan dosyaları sadece o dosyanın
sahibi veya sticky bit'i set edilmiş dizinin sahibi ya da root kullanıcısı o
dosyayı silebilir veya yeniden adlandırılabilir. Eğer bu bit olmasaydı, o dizinde
yazma ve execute hakkı olan herkes altındaki dosyalarda bu tarz değişiklikler
yapabilirdi.

[^1f]: <https://en.wikipedia.org/wiki/Sticky_bit>
