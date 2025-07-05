---
giscus: af1ea24a-2223-4e9d-8785-87396710b827
---

# Deyim (Statement) Kavramı

`10667`

Bir programlama dilinde çalıştırma birimlerinde **deyim** yani **statement**
demekteyiz. **Imperative** dillerde program aslında deyimlerin çalışması ile
çalıştırılır. Python implementasyonları da yukarıdan aşağıya deyimleri tek
tek çalıştırır. C, C++, Java, C# gibi bir çok dilde `main` ya da `Main`
isimli özel bir fonksiyondan çalışmaya başlanır.

**Python'da ise kod `main` gibi bir yerden değil en tepeden çalışmaya başlar.**

Deyimler, iki gruba ayrılır:

1. Basit Deyimler (Simple Statements)
2. Bileşik Deyimler (Compound Statements)

---

Python'da basit deyimler tek parçadan oluşur. Tek satıra yazılabilmektedir.
Bileşik deyimler ise birden fazla parçadan oluşan ve tek satır üzerine
yazılamayan ya da yazılmak zorunda olmayan deyimlerdir.

Basit deyimlerin en önemli özelliği birden fazla basit deyimin aynı satıra
aralarına `;` atomu getirilerek yazılabilmesidir.
**Ancak bileşik deyimlerle diğer deyimler hiçbir zaman aynı satıra yazılamaz.**
Örneğin `if`, `for` gibi deyimler Python'da *bileşik deyim* grubundadır.
Her iki deyim kategorisinin de çeşitli biçimleri vardır.

## Expression Statement (İfade Deyimi) (İfadesel Deyim)

Bir ifade, programın parçası haline getirildiğinde aslında artık bir deyim
olur. Bunlara ifadesel deyim diyoruz.

```python
print(z)
intput('giriniz:')
```

Bu iki deyim ifadesel deyimdir. Bir ifadeyi bir satıra yazdığımızda artık o
ifade bir deyim haline gelmektedir. Elbette ifadeler başka deyimlerin
parçası olabilir.

```python
if val % 2 == 0:
  print('çift')
else:
  print('tek')
```

Burada `if` cümlesinin tamamı tek bir deyimdir. `val % 2 == 0` bir ifadedir
ancak burada deyim değildir. **İfade, bağımsız satıra yazılınca deyim olur.**

## Atama bir deyimdir

Bunu önceden de söylemiştik. Python'da atama işlemi aslında bir operatör değil
bir deyimdir. Buna **atama deyimi** yani **assignment statement** denir.

```python
x = 10     # Atama deyimi
y = 20     # Atama deyimi
z = x + y  # Atama deyimi
print(z)   # İfadesel deyim
```

Yukarıdaki deyimlerin hepsi basit deyimdir. İstersek tek satıra da yazabiliriz:

```python
x = 10; y = 20; z = x + y; print(z)
```

## Bileşik deyim kuralları

`10725`

Her dilin bileşik deyimler iin farklı kuralları vardır. Örneğin C, C++, Java
ve C# gibi dillerde bloklama tekniği, `{}`, kullanılır.

**Python'da ise bloklama için girinti düzeyi, indent level, kullanılır.**

```text
if koşul:
  ifade1
  ifade2
  ifade3
ifade4
```

Dediğimiz zaman `ifade1`, `ifade2`, `ifade3` aynı girinti düzeyinde olduğundan
bileşik deyimin bir parçası olur. `ifade4` ise `if` deyiminin dışındadır.

---

Fakat

```text
if koşul:
  ifade1
    ifade2
    ifade3
ifade4
```

**geçersiz bir yazımdır.** Bileşik deyim içersindeki deyimlerin aynı girinti
düzeyinde olması gerekir.

---

Python'da bileşik deyimler genel olarak bir anahtar sözcük ile başlatılır,
sonra bunu bir ya da birden fazla ifade izler sonra da bir `:` atomu
bulundurulur.

## Suit kavramı

`10765`

Python'da bileşik deyimin anahtar sözcüğü ile aynı satıra yazılan birden
fazla basit deyime ya da farklı satırlara aynı girinti düzeyi ile yazılan
birden fazla deyime **suit** denmektedir. Python'da pek çok deyim bir suit
içerir.

Örneğin:

`while ifade: ifade1; ifade2; ifade3` dediğimiz zaman `ifade1`, `ifade2` ve
`ifade3` bir suit belirtir.

```text
while ifade:
  ifade1
  ifade2
  ifade3
```

Burada da yine aynı şekilde `ifade1`, `ifade2` ve `ifade3` bir suite
belitir.

```text
while ifade: ifade1
  ifade2
  ifade3
```

Burada ise `ifade1`, `ifade2` ve `ifade3` bir suit belirtmez. Çünkü anahtar
sözcük ile aynı satırda değil ya da farklı satırlara yazılmış aynı girinti
düzeyinde değildir.

```text
while ifade:
  ifade1
  ifade2; ifade3
```

Burada yine bir suite vardır.

```text
while ifade:
  ifade1
   ifade2
  ifade3
```

Burada ise bir suite belirtmez çünkü aynı girinti düzeyinde değildir.

Arada boş satırlar olması sıkıntı değildir.

```text
while ifade:
  ifade1
  ifade2

  ifade3
  ifade4
```

Bunlar da bir suit yazımıdır.

```{note}
*suite* olayının ne işe yaradığını ileride göreceğiz.
```

`10819`
