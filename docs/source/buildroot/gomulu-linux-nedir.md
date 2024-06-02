---
giscus: c17ab8a5-c588-4915-9f61-c76bc4f80ab6
---

# Gömülü (Embedded) Linux nedir? Buildroot ve Yocto ne işe yarar?

```{youtube} Nv5_U1VWXlk
:align: center
:width: 100%
```

---

[Video](https://www.youtube.com/watch?v=Nv5_U1VWXlk)

## Videoda Geçen Bağlantılar

- [Protection Ring (Wikipedia)](https://en.wikipedia.org/wiki/Protection_ring)
- [Revolution OS (IMDb)](https://www.imdb.com/title/tt0308808/)
- [Linux Kernel](https://www.kernel.org/)
- [GNU](https://www.gnu.org)
- [It should be i.e. "GNU/systemd/linux", discuss?
  (Reddit)](https://www.reddit.com/r/linuxmasterrace/comments/36jcfa/it_should_be_ie_gnusystemdlinux_discuss)
- Necati Ergin Bey'den aldığım C kursunu değerlendirdiğim ve neden Embedded C
  yani Gömülü C diye ayrı bir C dili olmadığından da bahsettiğim yazım
- [BIOS (Wikipedia)](https://en.wikipedia.org/wiki/BIOS)
- [Devicetree (Wikipedia)](https://en.wikipedia.org/wiki/Devicetree)
- <https://distrowatch.com/>
- [systemd](https://systemd.io/),
  [SysVinit](https://wiki.archlinux.org/title/SysVinit),
  [BusyBox](https://en.wikipedia.org/wiki/BusyBox)
- [Circular dependency (Wikipedia)](https://en.wikipedia.org/wiki/Circular_dependency)
- [Linux From Scratch!](https://www.linuxfromscratch.org/)
- [Cross Compiler (Wikipedia)](https://en.wikipedia.org/wiki/Cross_compiler)
- [Patch (Wikipedia)](https://en.wikipedia.org/wiki/Patch_(Unix))

## Notlar

- Hatırlatma: `RootFS` kavramındaki `root` kelimesi ile `root` kullanıcısının
  bir bağlantısı yoktur. Tipik olarak en tepeden, kök dizinden yani
  *root* noktasından yani, `/` noktasından *mount* edilen dosya sistemine
  **Root File System, RootFS** denir.
- Videoda kütüphaneler için de "uygulama" diyorum. Burada kastettiğim şey aslında
  Firefox gibi uygulamalar gibi kütüphanelerin de birer **userspace** bileşeni
  olması. Videoda uygulama + kütüphanelerden "uygulama" olarak bahsediyorum.
  Elbette kütüphaneler, bizlerin bildiği klasik uygulamalar gibi değil. Yani
  biz doğrudan kütüphaneler ile etkileşime geçmiyoruz ya da kütüphaneler tek
  başlarına bir şey yapmıyorlar. Sağladıkları şey, uygulamaların bazı şeyleri
  daha kolay ve taşınabilir şekilde yapmasını sağlamak. `glibc` gibi bir C
  kütüphanesi ile BASH gibi bir uygulama işletim sisteminin **userspace**
  kısmında çalışıyor. Bu videodaki bağlamda hepsinden uygulama olarak bahsetmek
  o yüzden sınıflandırma açısından da yanlış değil.
