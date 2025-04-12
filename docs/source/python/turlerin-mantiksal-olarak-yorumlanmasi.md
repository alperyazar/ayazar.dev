---
giscus: 2a8cf286-4966-4fac-9fd7-88615a34655d
---

# 🕳️ Türlerin Mantıksal Olarak Yorumlanması

`11-2.08.55`

Değeri sıfırdan farklı olan `int` ve `float` nesnelerin mantıksal işlemler
sırasında `True`, sıfır olanların da `False` olarak yorumlandığını görmüştük.
Diğer türler için nasıldır?

---

Boş `str` nesneler `False`, değilse `True` olarak yorumlanmaktadır.

Örnek:

```python
print('alper' or 0, '*')
print('' or 10, '*')
print('0' and 10, '*')
print('' and 10, '*')
print(' ' or 10, '*')
```

Çıktı:

```text
alper *
10 *
10 *
 *
  *
```

Bir string'in içi boşluklardan oluşsa bile o string *dolu* olarak
değerlendirilir.

---

`None` ise mantıksal olarak ele alınırken `False` olarak yorumlanır.

Örnek:

```python
print(not None)        # True
print(None or 'alper') # 'alper'
```

---

İleride göreceğimiz türlerde de dönüşüm şöyle yapılır:

- Bir liste, list, dolu ise `True`, boş ise `False`
- Bir demet, tuple, dolu ise `True`, boş ise `False`
- Bir sözlük, dictionary, dolu ise `True`, boş ise `False`
- Bir küme dolu ise `True`, boş ise `False`

olarak mantıksal açıdan ele alınır.

`11-2.21.50`
