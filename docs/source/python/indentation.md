---
giscus: 46fb3232-2b23-4a9d-8df2-265bf40fef5c
---

# Indentation

`10612`

```{note}
Bu yazıdaki bilgilerin doğruluğundan tam emin değilim. 🤔

Çünkü TAB ile SPACE'i karıştırırsak, buradaki 8 kat kuralına dikkat etsek
bile bu sefer de
`TabError: inconsistent use of tabs and spaces in indentation` hatası alıyoruz.
Hal böyle olunca buyazıdaki bilgileri nasıl kullanacağız bilmiyorum.
```

Bir satırın başından ilk boşluk olmayan karaktere kadarki SPACE sayısına
**girinti düzeyi** yani **indent level** denmektedir. Eğer satır başındaki
boşluk karakteri sadece SPACE karakteri ise, SPACE'lerin toplamı girinti
sayısını vermektedir. Fakat satır başında TAB karakteri de olabilir.

Her TAB karakteri görüldüğünde o anki kadarki SPACE sayısını 8'in katlarına
tamamlamak için `n` SPACE anlamına gelmektedir. `n`, 0 olmamaktadır.

```text
SPACE SPACE SPACE   -> Düzey 3
SPACE TAB SPACE     -> Düzey 1 + 7 + 1 = 9
SPACE TAB TAB SPACE -> Düzey 1 + 7 + 8 + 1 = 17
TAB TAB TAB SPACE   -> Düzey 8 + 8 + 8 + 1 = 25
```

Kullandığımız editörde aşağıdaki boşluklar aynı gözükmüyor olsa bile Python
yorumlayıcısı açısından aynıdır.

```text
SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE
SPACE TAB SPACE
```

Her ikisi de 9 SPACE karakteridir.

**Buradaki hesap editörün TAB hesabı ile aynı değildir.** Python yorumlayıcısı
kendi bir hesap yapar. Bir TAB, 8 SPACE olarak kabul edilir.

---

Python uyumlu editörlerin neredeyse hepsi programcı TAB'a basınca zaten `n` adet
SPACE karakteri yerleştirir. Bu durumda yorumlayıcı zaten TAB karakterlerini
görmez. Yani editörümüz zaten 8 SPACE kullanıyorsa editörde alt alta olan
satırlar Python yorumlayıcısı tarafından da alt alta olarak kabul edilir.

```{note}
Hoca [PEP 8](https://peps.python.org/pep-0008/) de önerilen TAB ayarı 8
SPACE diyor ama sanki ben 4 diye anlıyorum? ❓
```

---

**Python programlarının girinti düzeyi 0 ile başlamak zorundadır.** Yani
programlar sola dayalı yazılır.

`10667`
