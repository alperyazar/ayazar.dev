---
og:description: "'Diskimde en çok hangi klasörler yer kaplıyor?' sorusuna cevap bulun!"
og:image: assets/social/blog/22/windirstat.png
giscus: 0f4f1dfc-3a8c-41ec-97d5-57bac19fb60d
---

# WinDirStat

```{figure} /extra/assets/social/blog/22/windirstat.png
:align: center
:figclass: thmbnl
```

---

- <https://windirstat.net/>
- Açık kaynak
- Windows

WinDirStat, açılımı ile **Windows Directory Statistics**, özellikle diskim dolmaya
yaklaştığı zaman kullandığım bir yazılım. Çünkü böyle durumlarda bir kurban
seçip onu silmem gerekiyor. Bir noktadan sonra hangi klasörün içinde gerekli
gereksiz ya da büyük küçük hangi dosyalar var insan unutuyor. Bu yazılım ile bu
tarz klasörleri hemen bulmak mümkün.

Yazılımı çok tarif edecek bir kullanımı yok aslında, kurup çalıştırınca
aşağıdaki gibi karşılama ekranında dilerseniz istediğiniz bir diski komple
taratabilir (uzun sürebilir) ya da seçtiğiniz bir klasörü analiz
ettirebilirsiniz.

```{figure} assets/windirstat.png
:align: center

WinDirStat Karşılama Ekranı
```

Seçim yaptıktan sonra `OK` dediğimizde Analiz bitiyor ve dosya tiplerini, alt
klasörlerin ne kadar yer kapladığını görüyoruz. Bu noktadan sonra dilerseniz
`Clean Up` menüsünden ya da doğrudan Windows'un dosya yöneticisinden dosyaları
silebilirsiniz.

```{attention}
⚠️ Programın içinden ya da Windows dosya yöneticisinden `Del` tuşu ile silme
yapılırsa dosyalar çöp kutusuna gideceği için yer açmaya çalıştığınız diskte
muhtemelen durmaya devam edecekleri için aslında yer açmamış olacaksınız. Silme
işlemlerinin `Shift + Del` tuşu ile yapılması bunu engelleyecektir.
```

## Linux

Linux'ta benzer bir arayüz sunan
[K4DirStat](https://github.com/jeromerobert/k4dirstat) yazılımını tercih
ediyorum.

*İlk yayın: 2022-01-29*
