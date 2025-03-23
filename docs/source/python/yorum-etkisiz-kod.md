---
giscus: abedc2ee-e3b4-4935-bb75-0e49e6364e0f
---

# Yorum ve Etkisiz Kod Kavramları

Python'da yorum ve açıklama yazmak için `#` karakteri kullanılmaktadır.
Buna *comment* ya da *remark* denmektedir. Bir satırda `#` görüldükten sonra
o satır sonuna kadar olan diğer kısımlar dikkate alınmamaktadır.

```python
print("Burada # yorum değildir") # artık yorum
# Bu da yorumdur.
x = 3 + 4 # + 5
print(x)
# Çok satırlı yorumlarda
# Her satıra
# # karakterini
# koymamız
# gerekir.
```

Çıktı:

```text
Burada # yorum değildir
7
```

## Etkisiz Kod, Dead Code, Code as No Effect Kavramı

Python'da etkisiz kod yazmak serbesttir.

```python
x = 5
10 + 20
print(x)
```

Burada `10 + 20` deyiminin hiçbir etkisi yoktur.

C, C++, Python gibi dillerde bu şekilde etkisiz kodlar yazabiliriz. C# ve
Java'da ise kural ihlali olmaktadır.

Python implementasyonları tipik olarak *optimize* çalışırlar. Kodumuz
satır satır çalışsa da Python yorumlayıcıları genelde tüm kodu önce bir gezer,
sentaks kontrolü yapar ve bu aşamada çeşitli optimizasyonlar yapabilir. İşte
bu şekilde etkisiz kodlar bu aşamada atılabilir. Derleyiciler ve yorumlayıcılar
*kodun gözlenebilir akışında* bir değişiklik olmadığı sürece ve doğru akışı ve
çıktıyı oluşturdukları sürece kodda istedikleri optimizasyonu yapabilirler.

Peki bunu avantajımıza kullanabilir miyiz?

```python
x = 5
'Anlamsız bir metin'
print(x)
```

Burada `'Anlamsız bir metin'` yazısı da benzer durumdadır, optimizasyon
kapsamında atılacaktır. İşte [](sabitlerin-turleri.md) yazısında öğrendiğimiz
`""""` ve `'''` ile oluşturulan çok satırlı metinleri çok satırlı yorum
yazmak için kullanabiliriz.

```python
x = 5

"""
Çok
satırlı
bir
yorum
"""

print(x)
```

Burada bir `str` sabit oluştursak da hiçbir yerde kullanmadığımız için
bu kodu çalıştırırken bize bir ek yük getirmez.

Bu yöntem Python'un yaratıcısı Guido van Rossum tarafından da önerilmektedir.

> Python tip: You can use multi-line strings as multi-line comments. Unless used
> as docstrings, they generate no code! :-) [^1f]

Üç tırnaklı yazılar **Docstring** oluşturmada kullanılmaktadır. Şimdilik
konumuzun dışındadır. [^2f]

[^1f]: <https://x.com/gvanrossum/status/112670605505077248>
[^2f]: <https://peps.python.org/pep-0257/>
