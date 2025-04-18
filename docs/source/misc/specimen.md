---
og:description: This is a sample page and this is a meta description.
giscus: 7b1852ac-ee33-474e-87ac-a4e75b9c35e1
---

# Specimen

Test page. Also see [theme documentation](https://pradyunsg.me/furo/reference/)

## Admonition

```{attention}
attention
```

```{caution}
caution
```

```{danger}
danger
```

```{error}
error
```

```{hint}
hint
```

```{important}
important
```

```{note}
note
```

```{tip}
tip
```

```{warning}
warning
```

## Todo

```{todo}
An example todo item.
```

## Visual

```{figure} https://upload.wikimedia.org/wikipedia/commons/6/6f/SpongeBob_eyes.png
:align: center

I'm ready! I'm ready! I'm ready!
```

## YouTube

```{youtube} T6v8A8Ji3Bc
:align: center
:width: 100%
```

## giphy

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD013 MD033 -->
<center>
<iframe src="https://giphy.com/embed/ule4vhcY1xEKQ" width="360" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/reactionseditor-cat-typing-ule4vhcY1xEKQ">via GIPHY</a></p>

<mark>Type derken bunu kastetmiyoruz…</mark> catly typed languages 🐈
</center>
<!-- markdownlint-restore -->

## giscus

See the bottom.

## reST Specific

[Ref](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html)

### Code Block

```{code-block} c
:lineno-start: 33
:emphasize-lines: 8
:caption: kernel/console.c

void
consputc(int c)
{
  if(c == BACKSPACE){
    // if the user typed backspace, overwrite with a space.
    uartputc_sync('\b'); uartputc_sync(' '); uartputc_sync('\b');
  } else {
    uartputc_sync(c);
  }
}
```

## Asciinema

[The Plugin](https://github.com/divi255/sphinxcontrib.asciinema)

Online (`asciinema.org`):

```{asciinema} 633779
:cols: 80
```

and self hosted:

```{asciinema} assets/zsh.cast
:cols: 80
```

Not working? direct embed:

<!-- markdownlint-disable-next-line -->
<script async id="asciicast-633779" src="https://asciinema.org/a/633779.js"></script>
