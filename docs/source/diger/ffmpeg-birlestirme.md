# FFmpeg Video ve Ses Birleştirme

Video platformları ses ve video dosyalarını ayrı ayrı verebiliyorlar, ya da
elinizde senkron fakat ayrı dosyalarda duran ses ve video dosyaları olabilir.
Bunları FFmpeg ile birleştirebiliriz, Windows ya da Linux üzerinde. Ben Windows
üzerinden örnek veriyorum:

```text
.\ffmpeg.exe -i .\ses-veya-video.mp4 -i .\video-veya-ses.mp4 -c:v copy -c:a copy cikti.mp4
```
