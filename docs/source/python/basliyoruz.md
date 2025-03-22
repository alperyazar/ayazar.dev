---
giscus: 21e43778-c171-4a44-8d13-75462c5292f9
---

# Başlıyoruz!

Önceki yazılarda genel programlama dili ilgili kavramlara ve Python diline geniş
bir bakış açısı ile biraz baktık. Artık yavaştan dile geçebiliriz.

## REPL Çalışma

Python implementasyonlarının çoğunda, C derleyicisi gibi ortamlarda bulunmayan
bir özellik bulunmaktadır: interaktif çalışma. Bu özellik aslında Python dilinin
doğrudan bir özelliği olmasa da birçok implementasyonda bulunur. Bir komut
satırı üzerinden Python deyimlerini tek tek çalıştırıp sonuçlarını görebiliriz.
Bu, bir şeyleri öğrenirken ya da hata ayıklarken geliştiriciyi hızlandıran bir
özelliktir. `python` veya `python3` komutunu komut satırı üzerinde
çalıştırdığımızda karşımıza terminal benzeri bir prompt gelmektedir. Burada
Python'da geçerli bir deyim yazdığımız zaman ve `Enter` tuşuna bastığımızda o
deyim çalıştırılır. Örneğin:

```text
Python 3.11.2 (main, Nov 30 2024, 21:22:50) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 4
>>> print(x)
4
>>>
```

Burada `x=4` ifadesini `Enter` ile girdim ve sonrasında `print(x)` ifadesini
çalıştırınca da `x` in değerini ekranda görmüş oldum. Bu tarz interaktif
çalışmalar sadece Python'da değil, Ruby, R, Swift, MATLAB gibi dillerde de
yapılmaktadır. Bu tarz çalışma yöntemine **REPL, Read Evaluate Print Loop** da
denmektedir.

Bu yöntem bir şeyleri denerken ya da hata ayıklama yaparken kullanışlı olabilir.
Ama Python programları tipik olarak uzantısı `.py` olan metin dosyalarında
saklanır. Eğer Python'ı, yani CPython'dan bahsediyorum, `python` veya `python3`
diye argümansız değil de `python script.py` gibi çağırırsak bu sefer REPL
modunda çalışmaz ve doğrudan programımızı çalıştır.

---

Yukarıdaki örnekte CPython'nun shell'ini görmüş olduk. Buradaki shell çok da
yetenekli değildir. [IPython](https://pypi.org/project/ipython/) isminde daha
yetenekli bir shell de mevcuttur. `pip` ve `pipx` ile, örneğin
`pipx install ipython` diyerek, kurabilirsiniz. Kurduktan sonra komut satırından
`ipython` diyerek çalıştırılabilir.

Bu shell, daha detaylı, daha "interaktif" çalışmamızı sağlayabilir. Örnek:

```text
Python 3.11.2 (main, Nov 30 2024, 21:22:50) [GCC 12.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 9.0.2 -- An enhanced Interactive Python. Type '?' for help.
Tip: Use `object?` to see the help on `object`, `object??` to view it's source

In [1]: x = 4

In [2]: x?
Type:        int
String form: 4
Docstring:
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4

In [3]:
```

## IDE

IPython, Interactive Python, her ne kadar basit işlerimiz için yeterli olsa da
Python projemiz büyüdükçe bizler için bu şekilde çalışmak yetersiz gelecektir.
Burada genel olarak bir IDE, Integrated Development Environment, ile çalışmak
işlerimizi kolaylaştıracaktır.

Piyasada ücretli/ücretsiz birçok IDE vardır. CPython içerisinde kurulu gelen
IDLE (Integrated Development and Learning Environment),
[Anaconda](https://www.anaconda.com/) dağıtımı ile gelen fakat ayrıca da
kurulabilen [Spyder IDE](https://www.spyder-ide.org/),
[PyCharm](https://www.jetbrains.com/pycharm/), [Visual Studio
Code](https://code.visualstudio.com/docs/languages/python),
[PyDev](https://marketplace.eclipse.org/content/pydev-python-ide-eclipse)
[Thonny](https://thonny.org/) hatta online çalışan [Online
Python](https://www.online-python.com/),
[Replit](https://replit.com/languages/python3) sayabileceğimiz IDE'ler
arasındadır. Elbette yazılımların yetenekleri birbirlerinden faklıdır.

Eğer ağırlıklı öğrenme amaçlı çalışıyorsak, **Spyder IDE**nin iyi bir tercih
olabileceğini düşünüyorum. Spyder, *IDEcik* denilebilecek bir büyüklüktedir.
Projelerimiz büyüdükçe PyCharm'ı tercih etmeyi düşünebiliriz örneğin. Spyder'ı
Anaconda dağıtımı içerisinden de kurabilirsiniz ya da bağımsız da
kurulabilmektedir. İçerisinde IPython da bulunur.

```{figure} assets/spyder.png
:align: center

Spyder IDE şuna benziyor
```

Siz de istediğiniz IDE'yi kurabilirsiniz. Kurulum dokümanlarına da arama yaparak
ulaşabilirsiniz.
