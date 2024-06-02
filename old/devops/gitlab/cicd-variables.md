---
giscus: 073b5bbc-ef52-481d-a4a6-4adb00cc9a2a
---

# CI/CD Variables

CI'da kullanılmak üzere kendimiz de değişkenler üretebiliyoruz. Özellikle
belirli bir grup altında olan projelerde grup tabanlı variable yaratmak
kullanışlı oluyor. YML içerisinde *hard coded* bir şeyler koymak yerine
bunları variable olarak tanımlayabiliyoruz.

UI üzerinden yapılan işlemler `Settings -> CI/CD` altında yapılıyor. Diyelim ki
container registry adresini variable olarak tanımladık, adı `$CUSTOM_REGISTERY`
olsun. Bunu `.gitlab-ci.yml` içerisinde kullanabiliyoruz:

```yaml
build:
  image: $CUSTOM_REGISTERY/ubuntu:22.04
```

gibi

Değişken tanımlarken çeşitli ayarlar mevcut, değişkenin görünürlüğü ile ilgili.
Kritik bilgi içerip içermemesi ve senaryoya göre bir ayarlama yapabilirsiniz.

## Kaynaklar

- <https://docs.gitlab.com/ee/ci/variables/#define-a-cicd-variable-in-the-ui>
