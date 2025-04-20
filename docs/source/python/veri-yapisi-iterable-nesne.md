---
giscus: f4eadefb-9cdf-4eb0-8918-3fa2df25b504
---

# Veri Yapısı ve Iterable Nesne Kavramı

`13-1.18.12`

Aralarında fiziksel ya da mantıksal ilişki olan bir grup nesneden oluşan
topluluğa **veri yapısı** yani **data structure** denilmektedir.

Python'da built-in bulunan, bir şeyleri `import` etmeden kullanabileceğimiz,
çeşitli veri yapıları vardır. Bunlar

- liste, list
- demet, tuple
- sözlük, dictionary
- küme, set
- string, str

olarak sayılabilir. Görece düşük seviyeli dillerin aksine, örneğin C, Python'da
görece veri yapıları dilin içerisinde doğrudan desteklenmektedir.

## Dolaşılabilir, Iterable Nesne Kavramı

Python'da çok sık kullanılan bir terimdir. Bazı sınıflara ilişkin nesneler
**dolaşılabilir** yani **iterable** olmaktadır. Bir nesnenin bu özelliğe sahip
olması dolaştıkça o nesneden birtakım değerlerin elde edilmesi anlamına gelir.
Bu nesneler üzerinde **dolaşım** yani **iteration** işlemi yapılabilir.

Dolaşılabilir nesneler genellikle kendi içerisinde birtakım nesneleri tutar.
Biz dolaştıkça bize o nesneleri verirler.

Başka nesneleri tutan nesnelere Java ve C# dilinde **collection**, C++'da ise
**container** denilmektedir.

Örneğin şimdiye kadar gördüğümüz `str` bir iterable türdür. Gördüğümüz diğer
temel türler bu özelliğe sahip değildir. `str` nesnesi dolaşıldığı zaman
içerisindeki karakterler elde edilir. Python'da ise karakter diye bir tür
yoktur. `str` dolaşıldığı zaman her bir karakter birer `str` olarak elde
edilir. Tabii dolaşılabilir nesnelerin dolaşınca bize neler vereceğini nesne
türü özelinde bilmemiz gerekmektedir.

---

İsim olarak benzeyen bir de **iterator** yani **dolaşım** nesneleri vardır.
Dolaşım nesneleri yani iterator nesneler aynı zamanda dolaşılabilir yani
iterable nesnelerdir. Bir dolaşılabilir nesne dolaşıldıktan sonra yeniden
dolaşılabilir. Bu durumda yine aynı nesneleri elde ederiz. Ancak dolaşım
yani iterator nesnesi ise bir kez dolaşıldıktan sonra artık biter. Biz onu
dolaşmak istersek tekrar, bir şey elde edemeyiz.
