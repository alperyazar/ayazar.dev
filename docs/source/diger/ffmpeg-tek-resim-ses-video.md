# FFMmpeg ile Tek Resim ve Ses Dosyası ile Video Oluşturma

Podcast için iyi olabiliyor. Tek kapak fotosu ve ses kaydı ile video oluşturma:

```text
.\ffmpeg.exe -loop 1 -i .\foto.jpg -i .\ses.mp3 -shortest out.mp4
```

Üstteki komut Windows'ta çalışıyor. `.jpg` yerine `.png` verince olmadı.

## Kaynaklar

- <https://superuser.com/questions/1041816/combine-one-image-one-audio-file-to-make-one-video-using-ffmpeg>
