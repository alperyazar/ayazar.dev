---
giscus: 9f5ddc12-67c0-4b75-9da8-4d6748b34cb0
---
# My Zsh Setup

Quick notes on installing and customizing [Zsh](https://www.zsh.org/) on Ubuntu
22.04 (or any Linux machine).

```console
sudo apt install zsh
```

## Oh My Zsh

Let's improve its look and functionality via [Oh My Zsh](https://ohmyz.sh)

Open BASH:

```console
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

```{note}
Please install `git` before the `curl` if it is not installed,
`sudo apt install git`
```

Keep default shell to BASH (my preference for other tools, just in case, like
PetaLinux)

## powerlevel10k

```text
Do you want to change your default shell to zsh? [Y/n] n
```

Now let's install [powerlevel10k](https://github.com/romkatv/powerlevel10k).

```{note}
If you, like me, are not planning to use Unicode in the subsequent steps of
configuring powerlevel10k, you might not need this font. However, I'm not 100%
sure as I haven't conducted a well-controlled experiment.
```

First install the recommended font: `Meslo Nerd Font patched for Powerlevel10k`
[Link](https://github.com/romkatv/powerlevel10k#meslo-nerd-font-patched-for-powerlevel10k)

Download all 4 `.ttf` files.

Install fonts locally:

```console
mkdir -p ~/.fonts
cp *.ttf ~/.fonts/
fc-cache
```

For GNOME terminal, verbatim from
[powerlevel10k documentation](https://github.com/romkatv/powerlevel10k#manual-font-installation):

> GNOME Terminal (the default Ubuntu terminal): Open Terminal → Preferences and
> click on the selected profile under Profiles. Check Custom font under Text
> Appearance and select MesloLGS NF Regular.

If you are not able to see that font in preferences, you might need to close all
GNOME Terminal instances and relaunch a terminal window.

Then download the theme for Oh My Zsh:

```console
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

Set `ZSH_THEME="powerlevel10k/powerlevel10k"` in `~/.zshrc`. The default one
was `ZSH_THEME="robbyrussell"` in my case.

Then open `zsh`.

When we first open `zsh` after installation, we will see `powerlevel10k`
installation wizard like that:

```{figure} assets/zsh-1.png
:align: center

powerlevel10k installation wizard
```

You can modify the shell's appearance to suit your taste, but here are my
choices:

```text
diamond y
lock y
upwards arrow y
fit between the crosses y
-
prompt style: 1 lean
character set: 2 ascii
prompt colors: 1 256 colors
Show current time?: 2 24-hour format.
Prompt Height: 1 one line
Prompt Spacing: 1 compact
Prompt Flow: 1 concise
Enable Transient Prompt?: n no
Instant Prompt Mode: 3 off
Apply changes: y yes
```

Run `p10k configure` anytime to reconfigure it.

Now we can use our new theme. Let's add some plugins!

## plugins

We can use Oh My Zsh plugins to enrich our shell experience:

- [git-prompt](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git-prompt)
- [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh)
- [sudo](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/sudo)
- [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md#oh-my-zsh)
- [zsh-you-should-use](https://github.com/MichaelAquilina/zsh-you-should-use#installation)

My `.zshrc`:

```text
ZSH_THEME="powerlevel10k/powerlevel10k"
plugins=(git git-prompt sudo zsh-autosuggestions you-should-use zsh-syntax-highlighting)
```

## In action

My theme and plugins in action:

<!-- markdownlint-disable-next-line -->
<script async id="asciicast-633779" src="https://asciinema.org/a/633779.js"></script>

Can't see? May be this?:

```{asciinema} /assets/asciinema/zsh.cast
```

Still can't see?? Download
[asciinema record (.cast)](/extra/assets/asciinema/zsh.cast)

*First Published: 2024-01-27*

