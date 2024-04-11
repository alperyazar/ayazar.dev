# Finding and Reading MAN Pages

As [mentioned earlier](posix.md), Linux—both the kernel and distributions—are
not completely but mostly POSIX compliant. There are instances where POSIX
functions may not be fully supported by Linux, and there are also times when
Linux extends or enhances some POSIX functions. If you, like me, aim to write
programs that will run solely on Linux without considering their operation on
other Unix-like systems, then it's possible to set aside POSIX standards and
concentrate exclusively on the Linux programming environment. This doesn't mean
to "forget POSIX" entirely—POSIX documentation should still be accessible to
you, but you might consider Linux-specific resources as your primary reference.

## man-pages

Linux man-pages project aims to document the kernel and userspace C API [^1f]:

> The Linux man-pages project documents the Linux kernel and C library
> interfaces that are employed by user-space programs. With respect to the C
> library, the primary focus is the GNU C library (glibc), although, where
> known, documentation of variations in other C libraries available for Linux is
> also included.

If we aim to interact with the kernel through C programs, then we should consult
the man pages. The current maintainer of the Linux man-pages project (since
2004) is [Michael Kerrisk](https://man7.org/mtk/), who is also the author of the
renowned book *The Linux Programming Interface.* The concept of man pages, or
manual pages, has a long history, tracing back to the early days of Unix [^2f].
These pages provide documentation for both programmers and users. Next, let's
explore how to locate and navigate these pages effectively.

## Local man-pages

Most Linux distributions come with man-pages installed locally. To check, type
`man` in your shell. If the command doesn't work, you'll need to look up how to
install man pages for your specific distribution. For a quick start, try `man ls`
to view the manual page for the `ls` command. Once there, press `h` to see
navigation help and learn shortcuts. Use `/` to search within the page. Curious
about the `man` command itself? Just type `man man` to read its manual page.

## Sections

Man pages are organized into sections because a single keyword might appear in
more than one section. If a keyword exists in multiple sections, the `man`
command displays the first entry it finds, searching through the sections in a
predefined order. The order is defined in `/etc/manpath.config` (at least in
Ubuntu).

Here are the section numbers and their corresponding meanings:

```text
1   Executable programs or shell commands
2   System calls (functions provided by the kernel)
3   Library calls (functions within program libraries)
4   Special files (usually found in /dev)
5   File formats and conventions, e.g. /etc/passwd
6   Games
7   Miscellaneous (including  macro  packages  and  conventions),  e.g.
    man(7), groff(7), man-pages(7)
8   System administration commands (usually only for root)
9   Kernel routines [Non standard]
```

```{note}
Note that the main sections are numbered, and there might be additional sections
like `3perl`, but these are generally not our primary focus. For system
programming, we'll mainly use sections 1 to 3.
```

For example, `man 1 chmod` shows the manual page for `chmod` command whereas
`man 2 chmod` gives the documentation about `chmod()` C function. To list
sections for a word, we may use:

```text
$ man -f chmod
chmod (2)            - change permissions of a file
chmod (1)            - change file mode bits

$ whatis chmod
chmod (2)            - change permissions of a file
chmod (1)            - change file mode bits

$ apropos chmod
chmod (1)            - change file mode bits
chmod (2)            - change permissions of a file
fchmod (2)           - change permissions of a file
fchmodat (2)         - change permissions of a file
```

`man -f` is equivalent to `whatis` and `man -k` is equivalent to `apropos`.
Use `man -a chmod` to see all documentation on `chmod` sequentially.

## The GNU Info System

The GNU Info System, while not as widely used as man pages (based on my
observations), does offer some advantages over them [^3f]. Created in 1986,
before the advent of HTML, info pages are interconnected with links. To see what
GNU Info looks like, type `info ls` in your shell. It can be particularly useful
for getting help with GNU tools, such as `make`. For example, try `info make`.

## GUI Tools

If you are on GNOME, try `yelp man:chmod.2` or `yelp info:cpio` (for GNU Info).
If you are on Plasma (KDE), try `khelpcenter`. But personally, I don't use these
GUI tools.

## Online

There are many online man pages available on the internet.
[man7.org](https://man7.org/linux/man-pages/index.html) serves as an *official*
online man page resource for Linux. Personally, I prefer using
[mankier.com](https://www.mankier.com/), [tldr](https://tldr.inbrowser.app/),
and [the Arch Linux online man pages](https://man.archlinux.org/). You can find
a list of additional online man pages on the [](resources.md) page.

## Resources

- [](resources.md)
- [List available man page sections for an application
  (SO)](https://unix.stackexchange.com/questions/256205/list-available-man-page-sections-for-an-application)
- [STOP Using 'man' Pages Incorrectly!
  (YT)](https://www.youtube.com/watch?v=cnmtKv2kUXs)
- [Introduction to Linux
  (LFS101x)](https://training.linuxfoundation.org/training/introduction-to-linux/)

[^1f]: <https://www.kernel.org/doc/man-pages/>
[^2f]: <https://en.wikipedia.org/wiki/Man_page>
[^3f]: <https://unix.stackexchange.com/a/77561>

```{disqus}
:disqus_identifier: 05503364-0731-4523-928d-c62906c29e86
```
