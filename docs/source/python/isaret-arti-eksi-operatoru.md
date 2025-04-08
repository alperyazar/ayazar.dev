---
giscus: 469e3085-2892-492c-94e7-01963f4f8c7a
---

# İşaret Artı `+` ve Eski `-` Operatörleri

`+` ve `-` karakterleri daha doğrusu atomları iki farklı operatörü temsil
etmektedir. İlk grup, birkaç önceki yazıda gördüğümüz ve bildiğimiz dört işlem
operatörlerinden olan artı yani toplama operatörü `+` ve eksi yani çıkarma
operatörü olan `-`. Bunlar binary operatörlerdi yani iki adet operand alıyordu.
Bir de bu yazıda tanıyacağımız ve tek operand alan yani unary olan `+` ve `-`
operatörleri var. Bunlara da *işaret artı* ve *işaret eksi* diyebiliriz.

İşaret artı ve işaret eksi operatörleri doğrudan sayıların önüne gelirler ve
sayının işaretini belirtmek için kullanılırlar: `+5`, `-2` gibi.

Tahmin edebileceğiniz şekilde anlamları da şöyledir: `-`, operandının negatif
değerini üretir. `+` nın bir etkisi yoktur, daha çok kod okunabilirliğini
arttırmak için kullanılır. İşaret operatörlerinin önceliği aritmetik
operatörlerden yüksektir.

> Bakınız: [](operator-oncelikleri.md)

Şu örneği ele alalım:

```python
b = -----3
```

Yukarıdaki ifadede tüm `-` sembolleri işaret eksi operatörüdür. Bu öncelik
seviyesinde birleş sağdan sola olduğu için operatörler aşağıdaki sırada
işleme alınırlar:

```text
İ1: -3
İ2: -İ1
İ3: -İ2
İ4: -İ3
İ5: -İ4
İ6: b = İ5
```

Günün sonunda bu `b = -3` ile eş değerdir.

C ve benzeri dillerin aksine Python'da `--` ve `++` operatörleri yoktur. Bundan
dolayı Python'da da var olan *maximal munch* kuralının diğer dillerdeki kadar
bize "sürpriz" durumlar oluşturması söz konusu olmaz.

Aşağıdaki örneği ele alalım.

```python
a = 4----2
```

Burada soldan ilk `-` sembolü çıkarma operatörünü temsil etmektedir, kalanlar
ise işaret eksi operatörüdür. Öncelik tablosuna göre sıralama şu şekilde
olmaktadır:

```text
İ1: -2
İ2: -İ1
İ3: -İ2
İ4: 4 - İ2
İ5: a = İ4
```

Yukarıdaki ifade `a = 4 - (-2)` ile eşdeğerdir ve sonuçta `a = 6` olur.
Python'da `--` ve `++` operatörlerinin olmadığını tekrar hatırlatmış olayım.
