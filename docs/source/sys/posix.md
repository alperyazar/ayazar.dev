# POSIX, SUS and LSB

System programming on Linux often involves many POSIX functions. So, what is
POSIX? As you explore POSIX, you'll encounter two more terms: SUS and LSB.
There's a history behind these terms, but I'm not particularly focused on their
detailed history at this moment, so I'll stick to some key points. If you're
interested in diving deeper, you might want to check out the first chapters of
[The Linux Programming Interface](https://man7.org/tlpi/) by Michael Kerrisk.

The late 70s and early 80s were a golden era for Unix and Unix-like operating
systems [^1f]. However, each Unix-like system had its own interface for
programmers, such as APIs, and command-line utilities for users. Writing a
single program that worked on all Unix-like systems without issues was
challenging. One of the earliest efforts to create a standard programming
interface was **POSIX**, or **Portable Operating System Interface**, by IEEE.
The first POSIX standard, POSIX.1, initially drew from an unofficial standard
from 1984, produced by a consortium of UNIX vendors known as `/usr/group`.
POSIX.1 was officially recognized as an IEEE standard in 1988 under the
designation **IEEE 1003** and as an ISO standard in 1990 as **ISO/IEC
9945-1:1990.** The name POSIX was suggested by Richard Stallman.

Today, POSIX sets standards not just for C programming APIs but also for shell
utilities like `cat`, `chmod`, `cp`, `tee`, and others. An operating system must
pass automated conformance tests to earn the official *POSIX compliant* badge.
**While most of the Linux distros aren't officially recognized as POSIX
compliant, they practically adhere closely to POSIX standards.** It's important
to note that the `UNIX` trademark isn't owned by IEEE but by [The Open
Group](https://unix.org/trademark.html). As a result, IEEE doesn't have the
authority to officially declare any operating system as UNIX compliant.

**SUS**, or **Single Unix Specification**, is a standard similar to POSIX. For
operating system developers wishing to earn the UNIX trademark for their OS,
adherence to SUS is required, along with paying a significant licensing fee to
obtain the UNIX certification.

**LSB**, or **Linux Standard Base**, represents a similar endeavor to POSIX and
SUS but focuses on standardizing Linux distributions. By building on the
foundations of POSIX and SUS, LSB seeks to standardize various aspects,
including libraries and filesystem hierarchy [^2f].

**Ultimately, the goal of all these standardization efforts is to create an
interoperable environment that benefits both users and programmers.**

---

With this series, my personal goal is to provide a resource specifically for
system programming on Linux, rather than focusing on other Unix-like systems
like macOS. I'm not concerned with interoperability between different operating
systems. My interest lies solely in Linux system programming. I've mentioned
standards only for the sake of completeness.

As of now, the latest POSIX and SUS standards essentially refer to the same
document, which can be accessed
[here](https://pubs.opengroup.org/onlinepubs/9699919799/). Moving forward in
this series, I will primarily refer to the [MAN pages.](man.md)

## Resources

- [](resources.md)
- [What is Linux? Unix? POSIX? (YouTube)](https://www.youtube.com/watch?v=hy4OeVCLGZ4)
- [What is the meaning of "POSIX"? (SO)](https://stackoverflow.com/questions/1780599/what-is-the-meaning-of-posix)
- [What exactly is POSIX? (SO)](https://unix.stackexchange.com/q/11983)
- [Officially recognized UNIX systems](https://www.opengroup.org/openbrand/register/)
- [SUS, POSIX, and Other Standards](https://dcjtech.info/topic/sus-posix-and-other-standards/)
- [POSIX Compliance Explained: Does It Even Matter In 2020 (YT)](https://www.youtube.com/watch?v=728Eu5RFoTs)

[^1f]: <https://en.wikipedia.org/wiki/List_of_Unix_systems>
[^2f]: <https://en.wikipedia.org/wiki/Linux_Standard_Base>

```{disqus}
:disqus_identifier: df2203f1-d317-47df-b174-913d50457ccc
```
