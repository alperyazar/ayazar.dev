---
og:description: "Blog yazmaya Hugo ile devam ediyorum."
giscus: f11aa683-468f-496c-acb2-7c5d5d493acc
---

# Merhaba (go)Hugo!

`alperyazar.com` alan adını 2011 tarihinde almışım. O günden bu zaman bu
sitenin altyapısında birçok değişiklik yaptım. İlk başlarda WordPress'i bir
paylaşımlı hosting üzerinde kullanırken daha sonra WordPress'i aldığım bir
VPS'e taşıdım. O zamanlar hosting panelinde ve VPS'e SSH ile bağlanıp bir
şeyler denemek fazlasıyla öğretici olduğundan altyapı ile uğraşmak hoşuma
gidiyordu. Zamanla WordPress'in çıkarttığı problemlerden (Aslında WordPress'e
çok da özgü problemler değildi. PHP gibi herhangi bir bileşen kullanan birçok
yazılımı idame etmek için bir çaba gerekiyor.) sıkıldığımdan dolayı çareyi
*statik site üreteci* sistemlerde buldum. Bu sistemler arasında da hatırladığım
kadarıyla [Sphinx](https://www.sphinx-doc.org/en/master/)'i
[MkDocs](https://www.mkdocs.org/)'u ve [Jekyll](https://jekyllrb.com/)'i
denedim çeşitli başka sitelerle de. En çok kullandığım Jekyll oldu,
([asynx.dev](https://asynx.dev/)'de kullanıyoruz.) Fakat çoğunda yine statik
HTML çıktılarını kendi sunucum üzerinden internete açtım. Daha sonraları CI/CD
kavramı ile tanışmam ile ilk olarak [Travis CI](https://www.travis-ci.com/) ve
[GitHub Pages](https://pages.github.com/) ile siteyi otomatik derlemeye ve
sundurmaya başladım. Daha sonraları Travis CI'ın yerini [Github
Actions](https://github.com/features/actions) aldı. Bu süre zarfında bir
elektronikçi olarak yazılım dünyasında yer etmiş olan CI/CD gibi kavramları
görmek, kullanmak, YAML diye bir şeyle tanışmak, *container*lardan haberdar
olmak bu sayede oldu. 2011'lerde sunucu konfigüre etme ile aldığım keyifi bu
sefer de [CI/CD](https://www.redhat.com/en/topics/devops/what-is-ci-cd)
kurcalarken aldım.

Statik üreteçlere çeşitli formatlarda girdi üretmek mümkün. Bunlardan en
popüleri herhalde [Markdown](https://www.markdownguide.org/)'dur. Yine Sphinx
tarafından varsayılan olarak kullanılan
[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
ise Markdown'dan daha kapsamlı bir *işaretleme(markup) dili* olsa da onun kadar
popüler olmadığını söyleyebilirim. Bir de denediğim
[AsciiDoc](https://asciidoc-py.github.io/index.html) var. Bu da Markdown'a göre
daha kapsamlı olsa *de facto* Markdown olmuş durumda. Ben de pek Markdown'dan
uzaklaşmak istemediğim için yine bunu destekleyen başka bir araç olan
[Hugo](https://gohugo.io/)'yu tercih ettim.

```{hint}
💡 Sphinx'i başka projelerde kullanıyorum.
[RST](https://en.wikipedia.org/wiki/ReStructuredText) yi özellikle başka
kişilerle beraber yaptığım çalışmalarda tercih etmiyorum. Sphinx,
[MyST-Parser](https://myst-parser.readthedocs.io/en/latest/) ile çok güzel bir
[Markdown desteği](https://www.sphinx-doc.org/en/master/usage/markdown.html)
veriyor. Son dönemlerde Sphinx'i, Markdown ile kullanıyorum.
```

## Neden değiştirdim?

Jekyll ile çalışırken neden Hugo'ya geçtim? Aslında çok bir sebebi yok, temelde
denemek istedim. Duyduğum bir araçtı, bir görmek istedim. Ayrıca Hugo'nun Go dilinde
yazılması sebebiyle kendisini ayrıca merak ettim. Jekyll'i kullanırken Ruby
öğrenmek zorunda kalmamıştım, sanıyorum Hugo'da da böyle olur ama Jekyll ile
en azından *RubyGems* gibi şeyleri biraz kurcalamıştım.

İlk bakışta Hugo, kendi reklamını yaptığı gibi gerçekten çok hızlı. Örneğin
[asynx.dev](https://asynx.dev/) de yaklaşık 15-20 sayfa var desek derleme 4-5
saniye sürüyor. Şu an tam olarak 13 sayfa olan bu blog (nerdeyse hepsi statik
sayfa, blog yazısı değil) 57 **milisaniye** de derleniyor, gerçekten
etkileyici. Ayrıca tema seçeneklerinin de Jekyll'den fazla olduğunu
söyleyebilirim. Şimdilik sadeliği ile hoşuma giden
[Ink](https://github.com/knadh/hugo-ink) isimli temayı kullanıyorum.

## Bundan sonra ne olacak?

Yine yazmamaya devam edeceğim 😂.

Eski yazıları taşımayı düşünüyorum. İşin şakası bir yana belki daha çok içerik
üretirim 🤣.

*İlk yayın: 2022-02-18*
