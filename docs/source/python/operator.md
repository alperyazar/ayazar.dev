---
giscus: 5449b40c-0739-432a-a4df-a02257c804b3
---

# Operatör Kavramı ve Sınıflandırılması

Bir programlama dilindeki en önemli kavramlardan biri de o dildeki
opertörlerdir.

**Operatör** bir işleme yol açan ve işlem sonucunda bir değerlerin üretilmesini
sağlayan atomlara operatör demekteyiz. `+`, `-` gibi semboller operatör olsa da
`is` de bir operatördür. Ayrıca operatörler birden fazla atomdan, token,
oluşabilir. Örneğin `is not` operatörü tek bir operatör olmasına rağmen `is` ve
`not` ayrı atomlardır.

## Operatörlerin Sınıflandırılması

Genelde operatörler 3 biçimde sınıflandırılır:

- 1️⃣ İşlevlerine Göre (Toplama mı yapıyor? Karşılaştırma mı? vs.)
- 2️⃣ Operand Sayılarına Göre
- 3️⃣ Operatörün Konumuna Göre

---

İşleve göre sınıflandırmada operatörün hangi konu ile ilgili işlem yapıldığına
bakılır. Şu sınıfları oluşturabiliriz:

- Aritmetik Operatörler, Arithmetic Operators, `+`, `-`, `/` gibi
- Karşılaştırma Operatörleri, Comparison Operators ya da İlişkisel Operatörler,
  Relational Operators, `>`, `<` gibi
- Mantıksal Operatörler, Logical Operators, `and`, `not`, `or` gibi
- Bit Operatörleri, Bitwise Operators. Sayıları bütün olarak değil de karşılıklı
  bitleri üzerinde işlem yapan operatörler. `<<`, `>>`, `~` gibi
- Özel Amaçlı Operatörler, Special Purpose Operators, `is`, `is not` gibi

---

Operatörün işleme soktuğu ifadelere, expressions, **operand** denmektedir.

Operatörler

- 1️⃣ Tek operandlı, unary
- 2️⃣ İki operandlı, binary
- 3️⃣ Üç operandlı, ternary

olarak operand sayılarına göre sınıflandırılabilir. `not a` ifadesindeki `not`
tek operandlı, `a / b` ifadesindeki `/` iki operandlı bir operatör olmaktadır.

---

Bir operatör, operandların önüne yani soluna getirilerek kullanılıyorsa bunlara
**prefix** yani *önek* operatör denmektedir. Sonuna yani sağına getirilerek
kullanılıyorsa **postfix** yani *sonek* operatör denmektedir. Eğer operandların
arasında ise **infix** yani *araek* operatör denmektedir. Mesela `a + b`
ifadesindeki `+` bir infix operatördür. `not a` ifadesinde ise `not` bir prefix
operatördür.

## Örnekler

Fonksiyon çağırma da benzer bir yapıdadır. Örneğin `print(a)` dediğimizde `()`
bir operatördür. `print` ise operand'tır. Bu durumda `()` burada bir postfix
operatör olmaktadır. Tek operatörlü, sonek, özel amaçlı bir operatördür,
*unary postfix special purpose operator*

Örneğin bölü, `/`, operatörü iki operandlı, araek (infix), aritmetik bir
operatördür, *binary infix arithmetic operator*

`not` operatörü, tek operandlı, önek, mantıksal bir operatördür, *unary prefix
logical operator*

```{attention}
Dillerdeki bazı operatörler birbirine benzer, örneğin `+` ve `*` gibi. Ama
`++` operatörü C'de varken Python'da yoktur. `**` operatörü de Python'da varken
C'de yoktur.
```
