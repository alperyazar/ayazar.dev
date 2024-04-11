# Layers of Abstraction, Interfaces and Standard C Library

Computer systems are made by stacking layers of technology on top of each other.
Each layer hides the details of the ones below it through interfaces. This setup
is key for advancing technology and helping developers work more effectively,
even though it might use more CPU time and memory. Despite the potential for
using more resources, these layers of abstraction are valuable because they help
technology develop and improve quickly.

```{figure} assets/five-network-layers.jpg
:align: center

A good example of these layers of abstraction is the internet we use today.
```

Communication and data exchange protocols between computers showcase how
abstraction works well. Consider the internet as an example. It is structured
around 5 basic layers of abstraction. Each layer addresses a specific problem,
and by stacking these solutions, we enable two programs running on different
computers—anywhere on Earth or even in space—to communicate. Every layer builds
upon the one below it without needing to know how that layer functions. For
instance, the HTTP protocol operates regardless of whether the web server and
client are connected via Wi-Fi or cable, or whether they use IPv4 or IPv6.
However, each layer of abstraction does introduce some inefficiency. In terms of
protocols, every layer adds extra data to the packet, reducing the efficiency of
the data transmission (meaning the ratio of useful data bits to the total number
of bits sent). Despite this, such inefficiencies are acceptable, as without
these layers, creating a complex network like the internet would be an
incredibly difficult task.

Abstractions are found everywhere, not just between computers but also within a
single computer, where many layers of abstraction exist. From a programmer's
point of view, these abstractions begin with the processor or CPU. Processor
designers use the **Instruction Set Architecture (ISA)** to hide the complex
details of processors' internal structures. **Assembly programming**, which is
the most basic level of programming, uses the ISA specifications provided by the
CPU manufacturer. ISA serves as a bridge between the worlds of hardware and
software, allowing for easy switching between CPU vendors. For example, because
AMD and Intel use very similar ISAs, programmers don't need to worry about
whether their computer is running an Intel or AMD processor.

```{todo}
Add "Why do we have programming langauges part 1" when ready
```

In general, computers use **Operating Systems (OS)** to manage hardware and
software. Programs that run on these OSes interact with the hardware through the
OS. Whenever they need to perform a task involving hardware, they seek
assistance from the OS. The means by which programs and the OS communicate are
often referred to as **system calls.** For example, consider Linux. Throughout this
series, we will discover that to accomplish tasks on Linux, we don't need to
understand the kernel's internals. Instead, we will use a provided interface to
communicate with the kernel and carry out useful actions.

The Linux kernel offers over 300 different system calls for programs to use. [^2f]
While some system calls are almost universally used by programs, others serve
more specific purposes and are rarely employed. Ultimately, these system calls,
or *syscall*s for short, are the sole means of communication between the
programs and the kernel. The syscall interface operates through the CPU's
registers. Each syscall assigns a different role to each register: one might
carry the syscall's parameters, while another might hold the result. This
arrangement is somewhat similar to the ISA concept, which facilitates an
agreement between the hardware and software worlds. Kernel developers have
established their own interface between themselves and system programmers, often
referred to as the **Calling Convention.** If you're interested, you can explore
[this
page](https://www.chromium.org/chromium-os/developer-library/reference/linux-constants/syscalls/)
to see the actual calling conventions the kernel uses.

The calling convention used by the Linux kernel illustrates a concept known as
the **Application Binary Interface (ABI).** ABI sets the rules for creating
programs that can work together. It's a wide-ranging concept, not just about
syscalls. ABI covers the roles of registers, how functions call each other (not
just syscalls but also how one function, like `foo()`, calls another, like
`bar()`), and how the stack is organized. It's important to understand that ABI
is meant for compiled programs, which is why it's referred to as *binary.* It's
not an interface directly used by programmers.

The first version of the Linux kernel was released in 1991, and the project has
continually evolved since then. Every year, kernel developers work on adding new
features and making the kernel more secure and reliable. A significant challenge
they face is **maintaining the stability of the kernel's interface—such as syscall
conventions and the ABI it implements—over decades.** Stability is vital;
otherwise, a program that runs fine on, for example, Linux kernel version 5
might not work on version 6 if the ABI changes. Such a change would necessitate
recompiling all programs for the new kernel version, a hard task especially
for proprietary or older programs. Moreover, even if recompilation were
possible, it would be an undesirable burden. If an operating system were to
change its ABI with each release, it wouldn't be sustainable, and this holds
true for Linux as well. It's worth noting that while the internal structure of
the Linux kernel has undergone dramatic changes over the years, these changes
are largely invisible to users and programmers. This is because the internal
workings are *abstracted* away; programmers only need to interface with the
kernel. As long as the kernel maintains this interface without breaking it,
users and programmers can continue their work unaffected. **This illustrates the
importance of abstraction layers.**

---

**WE DO NOT BREAK USERSPACE!** [^3f]

Linus Torvalds (the creator and the maintainer of Linux) quote [^1f]:

> We care about user-space interfaces to an insane degree. We go to extreme
> lengths to maintain even badly designed or unintentional interfaces. Breaking
> user programs simply isn't acceptable.

---

Linux system call conventions and ABIs are crucial but often too low-level for
many programmers and their projects. Directly using the ABI provided by the
kernel typically involves programming in assembly language, which can be
challenging. **What if we introduced an additional level of abstraction?** This
is the role of specifications like **POSIX**, or Portable Operating System
Interface. I plan to delve into POSIX in a separate article, but in brief, it
offers a standardized C programming interface—complete with functions,
libraries, and header files. This allows programmers to write C programs that
communicate closely with the kernel. By adding this layer, POSIX not only
abstracts complexities but also establishes its own set of interfaces. Since
these interfaces are intended for use in source code by programmers, they serve
as an excellent example of an **Application Programming Interface (API).**

## Standard C Library and POSIX Functions

Many newcomers often mix up POSIX functions with functions provided by the
standard C library. For instance, `open()` is a POSIX function, whereas
`fopen()` is part of the standard C library. **So, what's the difference?**

Firstly, it's important to note that the C programming language isn't tied
exclusively to Unix-like operating systems such as Linux or macOS; C programs
can also be written for Windows. `fopen()` is an OS-independent function
available in any environment that supports the C standard library. On Linux,
calling `fopen()` eventually leads to the `open()` POSIX function being called
by the standard C library. However, on Windows, which doesn't adhere to POSIX
standards, `fopen()` is implemented using *Windows API* functions like
`CreateFile`, because the `open` function doesn't exist there.

Thus, even a low-level programming language like C introduces another layer of
abstraction over operating systems, making programs as OS-independent as
possible.

## Need for Higher Level Languages

C originated in the 70s and has proven to be a highly capable programming
language. However, as programming projects have grown increasingly complex over
the years, we've developed new methodologies like Agile 🫣 and roles like
software engineering to tackle these challenges methodically, along with new
programming languages. Compared to modern languages such as Python, JavaScript,
and PHP, C is often seen as a *low-level language* today. These newer languages
support advanced programming paradigms like object-oriented programming (OOP),
which allows for modeling real-world problems in a different way. They also
further abstract the programmer from the underlying operating system and
hardware.

Nonetheless, whether we work with higher- or lower-level languages, they all
eventually interact with the kernel via Linux syscalls or POSIX functions. As
languages become higher-level, programmers spend less time thinking about the
kernel, POSIX, and other low-level details. It's important to note that being a
higher-level language doesn't necessarily mean it is more capable or easier to
learn than lower-level languages. *Higher-level* simply means the language is
closer to human languages and further from machine code or assembly language.

## Summary

```{figure} assets/layers-of-programs.jpg
:align: center

A summary of possibilities of programming on Linux
```

In summary, there are many ways to write programs on Linux. Although it's not
practical, one could write programs in assembly language and interact directly
with the kernel using system calls. A second option is to use POSIX functions
without relying on the standard C library. This approach might be necessary in
some situations because the standard C library isn't as *flexible* or *capable*
as POSIX functions, but it makes porting the program to Windows challenging. The
third option is to use only standard C functions, which keeps our program's
source code portable to other operating systems. You should choose the method
that best fits your needs.

## Recommended and Resources

- [](resources.md)
- [System call (Wikipedia)](https://en.wikipedia.org/wiki/System_call)
- [Why is there a Linux kernel policy to never break user
  space?](https://unix.stackexchange.com/questions/235335/why-is-there-a-linux-kernel-policy-to-never-break-user-space)
- <https://yarchive.net/comp/linux/gcc_vs_kernel_stability.html>
- [ABI (Wikipedia)](https://en.wikipedia.org/wiki/Application_binary_interface)
- [Binary-code compatibility (Wikipedia)](https://en.wikipedia.org/wiki/Binary-code_compatibility)
- [API (Wikipedia)](https://en.wikipedia.org/wiki/API)
- [POSIX (Wikipedia)](https://en.wikipedia.org/wiki/POSIX)
- [Windows API (Wikipedia)](https://en.wikipedia.org/wiki/Windows_API)

[^1f]: <https://yarchive.net/comp/linux/gcc_vs_kernel_stability.html>
[^2f]: <https://www.chromium.org/chromium-os/developer-library/reference/linux-constants/syscalls/>
[^3f]: <https://linuxreviews.org/WE_DO_NOT_BREAK_USERSPACE>

```{disqus}
:disqus_identifier: d20c7d25-996f-4e29-8c4b-b36ef1898686
```
