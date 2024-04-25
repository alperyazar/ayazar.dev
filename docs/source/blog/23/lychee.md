---
og:description: "CI entegrasyonu yapabileceğiniz, Markdown ve HTML'de link kontrolü yapan bir araç"
og:image: assets/social/blog/23/lychee.png
giscus: ff974989-6621-449f-8c1d-cf69ac15c8cf
---

# lychee: Kırık Link Kalmasın

```{figure} /extra/assets/social/blog/23/lychee.png
:align: center
:figclass: thmbnl
```

---

Bu yazımda kısaca şu an görmekte olduğunuz kişisel web sitemde de kullandığım
bir araçtan bahsetmek istiyorum:
[lychee](https://github.com/lycheeverse/lychee). (Ayrıca bakınız:
[Liçi](https://tr.wikipedia.org/wiki/Li%C3%A7i) meyvesi)

lychee, Rust dilinde yazılmış bir araç. Temel işlevi Markdown, HTML gibi dosyaları
tarayarak, olası "kırılmış" ya da "ölmüş" linkleri yani bağlantıları bulmak.

```{note}
⚠️ [Lychee](https://github.com/LycheeOrg/Lychee) isminde bir de bir fotoğraf
yönetim yazılımı bulunuyor, bunun ile karıştırmayın. Şu an incelediğimiz
aracın adının tüm harfleri küçük.
```

## Neden kullanıyorum?

Seyrek de olsa 2011 yılından beri yazdığım yazılar var. Bu yazıların içerisinde
başka sitelere bağlantılar oluyor. Bir okuyucu olarak gezindiğim sitelerdeki
linklerin olmayan sayfalara gitmesi benim için hoş bir deneyim olmuyor. Kendi
yazılarımdaki kırık linkleri de otomatik bir şekilde bulabilmek adına Github
Actions ile bu aracı kullanıyorum.

lychee'yi bilgisayarınıza çeşitli yollarla kurabilirsiniz, sitesinde
[anlatılıyor.](https://github.com/lycheeverse/lychee#installation) En pratik
kullanım ise bence Docker kullanmak, hele bir de Windows üzerinde çalışıyorsanız.
Komut satırından çalışan bu araç, bir komut satırı uygulamasına göre renkli ve
hoş görünüşlü çıktılar da üretiyor.

```{figure} assets/lychee-a.png
:align: center

*Şunun tatlılığına bir bak abisi!*
```

[Kendi sayfasındaki](https://github.com/lycheeverse/lychee) dokümantasyonu oldukça
iyi, o yüzden ben biraz kendi kullanımımdan bahsedeceğim.

Yazılımı çağırırken komut satırı argümanları ile veya bir TOML formatındaki
konfigürasyon dosyası ile (oldukça fazla) çeşitli ayarlar geçirmek mümkün.
Varsayılan olarak `lychee.toml` isimli bir dosyayı okuyor. Bu web sitesinde
kullandığım TOML dosyasına
[buradan](https://github.com/alperyazar/home/blob/master/lychee.toml)
erişebilirsiniz.

Ben Markdown dosyaları üzerinde bu aracı çalıştırıyorum. Benim gibi statik bir
web sitesi üreteci kullanıyorsanız (bu site [Jekyll](https://jekyllrb.com/) ile
üretiliyor, en azından bu yazının yazıldığı zaman) oluşturulan HTML dosyaları
üzerinde de lychee'yi çalıştırabilirsiniz. Bu sayede hem Markdown'dan verdiğiniz
linkleri hem de üretecin ürettiği ve ağırlıklı site içi navigasyon linklerini de
test edebiliriz. Kendi durumumda Markdown dosyalarında kontrol ettirmeyi yeterli
gördüm. Markdown içerisinde verilmiş göreceli (relative) bağlantı ve görsel
gösterme kısımlarını da kontrol ettiğini gözlemledim.

Konfigürasyon dosyasında veya komut satırı argümanlarında çeşitli seçenekler
geçirirken [glob](https://en.wikipedia.org/wiki/Glob_(programming)) kullanabiliyoruz,
`**` gibi karakterler, ama alışkın olduğumuz Bash stilinden sanıyorum biraz farklı
davranıyor. Bu yüzden aracın dokümantasyonuna bakmakta fayda var.

lychee, elbette bu işi yapan tek araç değil. Kendi sitesinde de diğer araçlarla
yapılmış detaylı bir karşılaştırma tablosu
[var.](https://github.com/lycheeverse/lychee#features) Mesela zamanında Jekyll
ile beraber kullandığım
[html-proofer](https://github.com/gjtorikian/html-proofer) diye bir araç daha
var. Bu araç Ruby temelli ve HTML üzerinde çalışıyordu. Hatırladığım kadarıyla
lychee'den daha yavaştı. Böyle birçok araç bulabilirsiniz.

## Docker

lychee Docker ile çok pratik bir şekilde çalıştırılabilir. Kendi sitem için:

```shell
docker run --init --rm -it -v ${PWD}:/input lycheeverse/lychee -c /input/lychee.toml --exclude-path /input/vendor "/input/**/*.md"
```

ifadesi yeterli oluyor örneğin. Bu kullanımda Windows üzerinde de rahatlıkla
çalıştırılabiliyor.

## CI

lychee kolaylıkla CI pipeline'larına entegre olabiliyor. İlk olarak Gitlab ile
başlayalım

### Gitlab CI

```yaml
lychee:
  image:
    name: lycheeverse/lychee
    entrypoint: [""]
  needs: []
  before_script:
    - lychee --version
  script:
    - lychee -c lychee.toml "./docs/**/*.md"
```

Gitlab CI ile tipik olarak bu şekilde kullanılabilir. Dikkat ederseniz burada
`ENTRYPOINT` i override ediyorum ve sanki terminal üzerinden kullanıyorum gibi
bir script hazırlıyorum. Bu bana daha kolay geldi, varsayılan olarak `ENTRYPOINT
["/usr/local/bin/lychee"]`
[tanımlanmış](https://hub.docker.com/layers/lycheeverse/lychee/latest/images/sha256-0ee1779a9102c57d6bd4e3133e557d26d4fe6ca9fe9c05382d5eb2cd8a091cf8?context=explore)
durumda.

## Github Actions

Bu web sitesinde Github Actions ile kullanıyorum. İlgili workflow'ların çıktılarına
[buradan](https://github.com/alperyazar/home/actions/workflows/md-link-check.yml)
bakabilirsiniz.

Kullandığım konfigürasyon da şu şekilde (şimdilik):

```yaml
# Ref: https://github.com/lycheeverse/lychee-action
# Ref: https://github.com/selfhostedshow/wiki/blob/master/.github/workflows/brokenLinks.yml
name: Check markdown links

on:
  schedule:
    # UTC Time, At 15:00 on day-of-month 1.
    - cron: "0 15 1 * *"
  workflow_dispatch:
  repository_dispatch:

jobs:
  linkChecker:
    permissions:
      issues: write
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Link Checker
        uses: lycheeverse/lychee-action@v1.8.0
        with:
          args: --verbose './**/*.md'

      - name: Create Issue From File
        if: env.lychee_exit_code != 0
        uses: peter-evans/create-issue-from-file@v4
        with:
          title: Link Checker Report
          content-filepath: ./lychee/out.md
          labels: report, automated issue, broken-link
          assignees: alperyazar
```

Güncelini [buradan](https://github.com/alperyazar/home/blob/master/.github/workflows/md-link-check.yml)
kontrol etmekte fayda var. Burada [lychee-action](https://github.com/lycheeverse/lychee-action)
ile beraber [create-issue-from-file](https://github.com/peter-evans/create-issue-from-file)
ı da kullanıyorum. Böylece lychee kırık linkler bulduğu zaman bana bir issue da
açmış oluyor. Uygun bir zamanda ben de bunları düzeltiyorum.

Tüm linklerin her merge öncesi kontrol edilmesi hem gereksiz hem de uzun süren
bir iş olduğu için (alternatif olarak o merge ile eklenen yeni linklerin
kontrol edilmesi yapılabilir ama o da ayrı bir iş) ben periyodik bir kontrol
yapıyorum. Güncel durumda ayda 1 link kontrolü Github Actions tarafından yapılıyor
ve bir sorun olursa bana issue açılıyor. Kendi sitem için bu sıklık ve otomasyon
yeterli.

```{figure} assets/lychee-1.png
:align: center

*Bu websitesinin reposunda otomatik olarak açılmış bir issue:*
[Link](https://github.com/alperyazar/home/issues/4)
```

## Son Sözler

Rust dilinde olduğundan mıdır nedir bilmem 😝 lychee oldukça hızlı çalışıyor
ve birçok değiştirilebilir ayara da sahip. Docker imajı sayesinde de lokalde
ya da CI'da kolaylıkla kullanılabiliyor. Ek olarak doğrudan Github Actions'ta
da yer alması işimizi kolaylaştırıyor. Komut satırına da renkli ve tatlı çıktılar
üretiyor. Şimdilik severek kullanıyorum.

lychee belirttiğim gibi Markdown dosyaları içerisinde verilmiş göreceli (relative)
sayfa (diğer Markdown dosyalarına) bağlantılarını ve görselleri
(`![]()` formundakiler) kontrol ediyor. Bu kısım, Markdown dosyalarını "sade"
bir şekilde kullanıyorsanız yani bir başka araç ile HTML çıktılar üretmiyorsanız
da faydalı olabilir, mesela Markdown dosyalarını doğrudan Github, Gitlab ya da
VS Code ile görüntülüyorsanız. Bu gibi durumlardaki iç bağlantı hatalarını da
bulmanıza yardımcı olacaktır. Ama Markdown dosyalarınızı, bir derleme işlemine
sokuyorsanız kullandığınız araç bu tarz iç bağlantılardaki hataları yakalayabilir,
örneğin [Sphinx](https://www.sphinx-doc.org) bunu yapabiliyor.

**Sizce nasıl?** Görüşlerinizi yorum yaparak iletebilirsiniz…

*İlk yayın: 2023-07-28*
