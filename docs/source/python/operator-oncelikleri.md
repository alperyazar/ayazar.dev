---
giscus: a9307cfe-5d3e-4d65-945d-678289925fed
---

# Operatör Öncelikleri

Python'da ve diğer programlama dillerinde de bir ifadenin genelde en az bir
operatör içerdiğini söyleyebiliriz. Bir ifadede birden fazla operatör olması da
çok yaygın bir durumdur. Peki bu durumda hangi operatör diğerlerinden daha önce
işleme sokulacaktır? Operatörlerin çalıştırılma sırası nasıl olacaktır? İşte bu
bölümde değineceğimiz **operatör önceliği** konusu bu sorunun cevabını
vermektedir.

`c = a + b * c` ifadesini örnek olarak ele alalım. Matematik kuralları
çerçevesinde çarpma, `*`, işleminin toplama, `+`, işlemine göre önce
yapılacağını söyleyebiliriz. Yani `b` ve `c` çarpılacak, sonra bu çarpımın
sonucu `a` ile toplanacak. Python kuralları açısından da gerçekten de böyledir.
Yani bu durumda matematik kuralları ile yaptığımız tahmin Python açısından da
tutarlıdır. Fakat her zaman böyle olmak zorunda değildir. Kaldı ki matematikte
olmayan çeşitli operatörler programlama dillerinde bulunur. Bu durumda elimizde
tahmin yapacağımız bir dayanak da kalmaz.

Yukarıdaki örnek ifadedeki operatörlerin değerlendirilme sırasını şu şekilde
gösterebiliriz:

```text
İ1: b * c
İ2: a + İ1
İ3: c = İ2
```

`İ`, `İ`şlem demektir.

Şimdi de `a = b + c + d` ifadesini ele alalım. Bunda da sıra şu şekilde
olacaktır.

```text
İ1: b + c
İ2: İ1 + d
İ3: a = İ2
```

Burada hala matematik ile açıklayabileceğimiz bir durum var. Peki neden `b + c`
işlemi `c + d` den önce yapılıyor dedik? İşte yavaş yavaş Python'ın kurallarını
bilmemiz gereken kısımlara geliyoruz.

## Parantez, `()`

Matematikten de bilebileceğimiz gibi parantez, `()`, kullanarak işlem sırasını
kontrol edebiliyoruz. Örneğin `a = (b + c) * d` yazdığımız zaman bu sefer
`+` operatörü daha önce işleme alınacaktır. Yani `b` ve `c` önce toplanacak,
sonra toplamın sonucu `d` ile çarpılacaktır.

Programcılar, parantez kullanılmadığı zaman zaten operatör öncelikleri ile
istenilen sonuç alınıyorsa boş yere parantez kullanmama eğiliminde
olabilmektedir. Fakat bazı durumlarda kod okunabilirliğini arttırmak adına
sonuca etki etmese de parantez kullanımı iyi bir tercih olabilir.

## Operatör Öncelik Tablosu

Python'daki operatörlerin öncelik sıralamasını gösteren bir tablo yapalım.
`Öncelik` numarası düşük olan operatörlerin önceliği yüksek olmaktadır. Yani
tablonun altına doğru ilerledikçe öncelik düşmektedir, yukarı çıktıkça da
artmaktadır. Bir öncelik derecesini birden fazla operatör paylaşabilmektedir.
Bu operatörlerin tablodaki sırası bir şey ifade etmemektedir. Örneğin `*` ve
`/` operatörleri aynı öncelik derecesine sahiptir. Tabloda ise bir birinin
üstündedir. Bu, üstte olanın daha yüksek öncelikli olduğu anlamına gelmez.
Aynı öncelik derecesine sahip operatörler bir ifadede bulunduğunda bunların
kendi aralarında hangi sıra ile çalıştırılacağı operatörlerin *birleşme* yani
*associativity* özelliği ile ilgilidir.

```{todo}
Tablo yarımdır. Notlarda ilerlendikçe tablo da genişletilmektedir.
```

| Öncelik       | Operatör | Açıklama                                                            | Associativity (Birleşme) |
|---------------|----------|---------------------------------------------------------------------|--------------------------|
| 1 (en yüksek) |          |                                                                     | soldan sağa              |
|               | `()`     | Hem fonksiyon çağrı operatörünü hem de öncelik parantezini gösterir |                          |
| 2             |          |                                                                     | sağdan sola              |
|               | `+`      | İşaret artı operatörü                                               |                          |
|               | `-`      | İşaret eski operatörü                                               |                          |
| 3             |          |                                                                     | soldan sağa              |
|               | `*`      | Çarpma                                                              |                          |
|               | `/`      | Bölme                                                               |                          |
|               | `//`     | floordiv                                                            |                          |
|               | `%`      | Modulo (mod alma) operatörü                                         |                          |
| 4             |          |                                                                     | soldan sağa              |
|               | `+`      | Toplama                                                             |                          |
|               | `-`      | Çıkarma                                                             |                          |
| 5             |          |                                                                     | sağdan sola              |
|               | `=`      | Atama ‡                                                             |                          |

‡: C gibi dillerin aksine Python'da atama operatörü, `=`, bir ifade oluşturmaz,
bir deyim oluşturur. Bu yüzden tabloda `=` operatörünün bulunması C gibi
dillerdekinin aksine çok da anlamlı değildir. Ama bütünsellik adına tabloda
bulundurulmaktadır. [^1f] [^2f]

## Tabloyu nasıl okumalıyız?

Birden fazla operatör bir ifadede bulunduğu zaman önceliği yüksek olan, nümerik
olarak düşük önceliğe sahip olan, 1 en yüksek, operatör ilk olarak çalıştırılır.
Daha sonra sıra ile en düşük önceliğe doğru gidilir. **Peki aynı öncelik
derecesine sahip olan birden fazla operatör bir ifadede varsa ne olacak?**
İşte bu durumda da ilgili önceliğin associativity yani birleşme özelliği
devreye girecektir. Eğer o grubun özelliği *soldan sağa* ise ifadenin en solunda
bulunan operatör ilk olarak değerlendirilir yani çalıştırılır. Benzer şekilde
*sağdan sola* ise en sağdaki operatör önce çalıştırılır. Bu, öncelik seviyesinin
bir özelliğidir. Aynı öncelik seviyesindeki operatörler aynı sırayı paylaşır.

## Örnekler

`a = b / c * d` ifadesinde `*` ve `/` operatörleri aynı öncelik sırasını paylaşır.
Bu seviye için birleşme soldan sağadır. Bu durumda ifadede `/` operatörü `*`
operatörünün solunda olduğu için önce `b /c` işlemi yapılır sonra bunun sonucu
ile `d`, `*` operatörü sayesinde çarpılır.

`a = b = c` ifadesinde atama operatörünün, `=`, birleşme özelliği sağdan sola
olduğu için önce `b = c` işlemi yapılır. Daha sonra `a = b` işlemi yapılır.

`a = foo() + 2` ifadesinde de `()` aslında bir operatördür, öncelik parantezi
değildir. Fonksiyon çağrı operatörüdür. Önceliği `+` operatöründen daha yüksek
olduğu için önce `foo` fonksiyonu çağrılır. Onun geri dönüş değeri ile `+`
operatörü ile `2` değeri toplanır ve son olarak `=` operatörü ile bu değer
`a` ya atanır.

[^1f]: <https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-assignment_stmt>
[^2f]: <https://stackoverflow.com/a/2603981/1766391>
