---
giscus: 49592e32-8deb-483f-8843-1fe194dc7b9f
---

# `while` Döngüleri

`11262`

Python'da döngü deyimleri minimalist tasarlanmıştır ve sadece `while` ile `for`
vardır.

C gibi dillerde *kontrolün başta yapıldığı while döngüleri* ve
*kontrolün sonda yapıldığı while döngüleri (do-while)* gibi seçenekler vardır.
**Python'da `do-while` yoktur.**

---

```text
while <ifade>: <suite>
[else: <suite>]
```

gibi genel bir biçim vardır. `while` anahtar sözcüğünden sonra bir ifade ve
sonra da `:` atomu olmalıdır. Sonra da bir `suite` gelmelidir.

---

Burada önce `while` anahtar sözcüğünün sağındaki ifadenin türüne bakar
yorumlayıcı. Eğer `bool` türünden değilse o `bool` türüne dönüştürülür. İfade
`True` ise `suite` deyimleri çalıştırılır. Sonra başa döner. `False` ise çalışma
sonlandırılır.

```python
i = 0
while i < 10:
  print(i)
  i += 1
```

## Walrus operatörü ve `while`

Atama operatörü, aslında deyim demiştik, bir değer oluşturmadığı için Walrus
operatöründen bahsetmiştik. `while` ile Python'da kullanılan sık bir kalıp da

```python
while (n := int(input('Bir değer giriniz:'))) != 0:
  print(n * n)
```

Burada Walrus kullanmasaydık ise

```python
val = 1
while val != 0:
  val = int(input('Bir değer giriniz:'))
  print(val * val)
```

gibi bir şey yazmamız gerekirdi.

Hatta

```python
while n := int(input('Bir değer giriniz:')):
  print(n * n)
```

yazabiliriz.

---

Elbette `while` içerisindeki `suite` içerisinde başka `while` da olabilir.

---

`while` ise sonsuz döngü oluşturmak için `while True:` kullanılır, aslında
`while 1:` de kullanabiliriz ya da sıfırdan başka herhangi bir değer ama
genel geçer gören `True` kullanımıdır.

## `while-else`

İsteğe bağlı bir `else` kısmı da olabilir. **Bu kısım `break` ya da `exception`
dışında normal bir biçimde çıkılırken bir kere çalıştırılır.**

```python
i = 0
while i < 5:
  print(i)
  i += 1
else:
  print('ends', i)
```

Çıktı:

```text
0
1
2
3
4
ends 5
```

Eğer `while`ın koşulu en başta hiç sağlanmıyor olsa bile `else` kısmı varsa yine
çalıştırılır.

```python
i = 0
while i < 5:
  print(i)
  i += 1
print('ends', i)
```

Bunun `else` olandan farkı `print(...)` deyiminin her türlü çalıştırılacak
olmasıdır. Örneğin döngüden `break` ile çıksak da çalışır ama `else` durumunda
`break` ile çıkarsak çalışmaz.

`11554`
