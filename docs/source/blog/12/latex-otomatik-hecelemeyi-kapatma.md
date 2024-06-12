---
og:description: "LaTeX'in sunduğu otomatik hecelemeyi her zaman istemeyebiliriz."
giscus: 532754c1-0672-4091-9bd6-72a13690e314
---

# LaTeX'te Otomatik Hecelemeyi Kapatma

Bu aralar biraz LaTeX ile uğraşmam gerekti. Yaklaşık bir sene önce bir rapor
yazarken ilk olarak kullanmıştım LaTeX'i. Gerçekte istediğiniz formatta rahatça
yazı yazmanızı sağlıyor.Başlamak, Microsoft Office gibi programları kullanmaya
göre zor. Özellikle bilgisayar kodu yazma tecrübesi olmayanlar biraz daha
zorlanabilir. Fakat sonradan LaTeX'te istediğiniz gibi formatta yazı
çıkarabildiğinizi görmek (Tabi başlarda istediğiniz formata ulaşmak için
internette araştırma yapmanız gerekecek. :) ) zevk verici. En azından Microsoft
Office, OpenOffice, LibreOffice gibi WYSIWYG tipi yazılımların yazı yazma
sırasında yaptığı ve saçınızı başınızı yolmanıza neden olan saçmalıkları
yapmıyor. Dediğim gibi başlaması biraz zor olabilir belki. Fakat ben ilk
denememde 60-70 sayfalık, resim tablo gibi birçok nesne içeren bir dökümanı
yazabilmiştim.

LaTeX'in reklamını yaptıktan sonra gelelim yazının konusuna. Kendime sonradan
referans olması açısından ve birilerine de faydalı olabilir diye ufak bir
sorunumun kolay bir çözümünü paylaşmak istedim.

LaTeX, yazılan kelimeleri eğer bir şekilde satıra sığdıramazsa, otomatik
heceleme yapabiliyor. Fakat bazı durumlarda bu özelliği kapatmak isterseniz,
aşağıdaki kodu yazınızın başına koyabilirsiniz:

```latex
\usepackage[none]{hyphenat}
```

Bu sayede LaTeX kelimelerinizi otomatik olarak hecelemeyecektir. Fakat adam
zaten düzgün sığdıramadığı için hecelediğinden, döküman görüntüsünü
bozabilirsiniz. Bu arada en son uğraştığım dökümanı Türkçe yazdığımdan bende en
başta şu kodlar da ekli:

```latex
\usepackage[utf8]{inputenc}

\usepackage[turkish]{babel}
```

**Direkt İngilizce olarak üstekki paketleri kullanmadan hecelemeyi kapatabiliyor
musunuz denemedim.** Sadece Babel'e özgü olabilir, bilemiyorum. Denerseniz bana
da haber verirseniz sevinirim.

*İlk yayın: 2012-06-03*
