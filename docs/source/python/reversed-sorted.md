---
giscus: d8504d59-318d-49fa-a7d2-e32b307569ae
---

# `reversed()` ve `sorted()` Built-in Fonksiyonları

`15-1.39.20`

## `reversed()` Fonksiyonu

Python'da bir de `reversed()` isimli built-in bir fonksiyon vardır. Bu,
`list` sınıfının bir metodu değildir. Bu fonksiyon bizden dolaşılabilir bir
nesne alır. Onun ters çevrilmiş halini bize bir **dolaşım nesnesi** yani
**iterator** olarak verir, liste olarak değil. Bu fonksiyon ayrıca in-place
bir işlem yapmaz yani orijinal nesnede bir değişiklik yapmaz. Bizim değerleri
elde etmemiz için fonksiyonun geri verdiği dolaşım nesnesini dolaşmamız gerekir.

Dolaşım nesneleri, dolaşılabilir nesnelerden faklıdır, bir kere dolaşınca
"biterler." Onun dışında dolaşılabilir nesneler gibi kullanılabilirler.

Hatırlarsanız liste oluşturmanın bir yolunun da `list()` fonksiyonuna
bir dolaşılabilir nesne vermekti. Biz burada `reversed()` ile elde ettiğimiz
dolaşım nesnesini de verebiliriz. Bu sayede ters çevrilmiş bir nesne elde
ederiz.

Aşağıdaki örneği inceleyelim:

```text
>>> x = [1, 2, 3]
>>> y = reversed(x)

>>> type(y)
<class 'list_reverseiterator'>

>>> z = list(y)

>>> z
[3, 2, 1]

>>> z = list(y)

>>> z
[]

>>> type(y)
<class 'list_reverseiterator'>
```

Burada ilk olarak `y` nin türünün liste olmadığına `list_reverseiterator` gibi
"garip" bir tür olduğuna dikkat edelim. Ama olsun, `list(y)` olarak yeni
bir liste oluşturabildik. Fakat dolaşım nesneleri bittiği için aynı satırı
tekrar çalıştırdığımızda yeni liste boş oldu çünkü bir tur dolaştık ve bitti.

---

`reversed()` fonksiyonu argüman olarak herhangi bir dolaşılabilir nesneyi
alabilir (bunu birazdan yalanlayacağız!). Mesela `str` de dolaşılabilir bir
nesne demiştik. O zaman:

```text
>>> x = reversed('alper')

>>> type(x)
<class 'reversed'>

>>> list(x)
['r', 'e', 'p', 'l', 'a']

>>> list(x)
[]
```

```{attention}
`reversed()` fonksiyonun argümanı aslında herhangi bir dolaşılabilir nesne
OLAMAZ. Bu argümanın **reverse iterable** yani **tersten dolaşılabilir**
bir nesne olması gerekmektedir. `list` ve `str` bu özelliğe sahip olduğu
için bu fonksiyonla kullanabildik.
```

## `sorted()` Fonksiyonu

Bu da bir built-in fonksiyondur. Bize sıralanmış yeni bir `list` verir.
Fonksiyon dolaşılabilir bir nesneyi parametre olarak alabilir.

Örneğin:

```text
>>> x = sorted('alper')

>>> type(x)
<class 'list'>

>>> x
['a', 'e', 'l', 'p', 'r']
```

`15-1.55.35`
