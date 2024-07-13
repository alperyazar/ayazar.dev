# `.` and `..`

Let's create a working directory using `-p` switch of the `mkdir` command to
create all nested directories at once and navigate to `b`:

```shell
$ mkdir -p a/b/c
$ cd b
```

Now let's list the content of `b`:

```shell
alper@brs23-2204:~/a/b$ ls -l

total 4
drwxrwxr-x 2 alper alper 4096 Jul 13 14:20 c
```

We see only `c` as expected. But now, let's use `-a` option of the `ls` command.

```shell
alper@brs23-2204:~/a/b$ ls -la

total 12
drwxrwxr-x 3 alper alper 4096 Jul 13 14:20 .
drwxrwxr-x 3 alper alper 4096 Jul 13 14:20 ..
drwxrwxr-x 2 alper alper 4096 Jul 13 14:20 c
```

Now, we see additional 2 entries: `.` and `..` What are those?

The `-a` stands for *all*. As a convention, directories and files starting with
`.` are considered *hidden* on Linux. Most of the configuration files at home
directories begin with `.`. Hidden files aren't different from our well-known
regular files, it is just a convention among Linux distributions. By default,
many file utilities like `ls` command or GUI based file browsers hide those
directories and files. Here is the explanation from the `ls` manual:

```text
-a, --all
       do not ignore entries starting with .
```

Okay, we know that there are two additional *hidden* entries in `b` and they are
directories (entries with type `d`) too, similar to `c`. But where do they point
to? The best way to understand is to examine their inode numbers. Let's do:

```shell
alper@brs23-2204:~/a/b$ ls -lai

total 12
8520988 drwxrwxr-x 3 alper alper 4096 Jul 13 14:20 .
8520987 drwxrwxr-x 3 alper alper 4096 Jul 13 14:20 ..
8520989 drwxrwxr-x 2 alper alper 4096 Jul 13 14:20 c

alper@brs23-2204:~/a$ ls -lai
total 12

8520987 drwxrwxr-x  3 alper alper 4096 Jul 13 14:20 .
3149103 drwxr-x--- 38 alper alper 4096 Jul 13 14:20 ..
8520988 drwxrwxr-x  3 alper alper 4096 Jul 13 14:20 b

alper@brs23-2204:~$ ls -laid a
8520987 drwxrwxr-x 3 alper alper 4096 Jul 13 14:20 a
```

The numbers on each row are the inode numbers for the corresponding entries. The
inode number of directory the `a` is `8520987` on my system. You might have been
noticed that the inode number of `.` in `a` and `..` in `b` are also the same.
That means that they are hard links to directory `a` and this is what `.` and
`..` are really mean.

---

Each directory on Linux has two directory entries called `.` and `..`. Those are
automatically created when we create a new directory. Similarly, they are
automatically removed when we remove a directory. They are hard links to
existing directories. `.` is a hard link to its own directory and `..` is a hard
link to parent, in other words to top, directory.

```shell
alper@brs23-2204:~$ cd a/b

alper@brs23-2204:~/a/b$ cd ./././././././
alper@brs23-2204:~/a/b$
```

For example, if you `cd` into `.` repeatedly, you will end up in the same
directory.

---

In order to expand the example, I created 3 directories under `c`. Now, let's
examine the meaning of hard links for directories.

```shell
alper@brs23-2204:~$ find a -type d -exec ls -ld {} + | awk '{print $2, $9}'

3 a
3 a/b
5 a/b/c
2 a/b/c/d
2 a/b/c/e
2 a/b/c/f
```

Numbers at each row show number of hard links given to the corresponding
directory. If you remember, we saw that we can't create hard links to
directories. We are only allowed to create soft links or symlinks to directories.
The only possible hard links to directories are `.` and `..` entries which are
automatically created by the kernel. Thus, kernel is allowed to create hard
links to directories but even the root user can't create them with `ln` command.

Let's try to understand the numbers:

```{figure} assets/dot-dot-dot.png
:align: center

Since `a` is not the root directory, `/`, it exists under a not-shown directory.
```

Hard links are essentially the number of links pointing to that directory. Let's
consider `b`. `b` is under `a` and there is an entry like `b-<inode number>` in
`a`, this is 1. Now `.` in `b` points to `b`, link count is 2. Lastly, `..` in
`c` points to `b` and this is why hard link count of `b` is 3. Since each child
directory points to its parent directory, `c` has the highest number of hard
link.

---

You might be wondering that how `..` directory of the root directory `/` is
implemented. Since `/` is the root directory, it doesn't have a parent. Therefore,
`/..` points to `/`. `/..`, `/.` and `/` points to the same directory with
inode number 2.

```shell
alper@brs23-2204:/$ ls -lid . ..

2 drwxr-xr-x 20 root root 4096 Apr 19  2023 .
2 drwxr-xr-x 20 root root 4096 Apr 19  2023 ..
```

## Are they virtual or real?

As you can see that `.` and `..` are kind of virtual entries. However, most of
the file systems store these entries on the disk physically. Directories are
list of `name - inode` pairs. In our example, the only *real* entry in `b` is
directory `c`. We have also `.` and `..`. Those entries are also stored on the
disk along with `c` like that:

```text
content of b:

.  - inode of b
.. - inode of a
c  - inode of c
```

If you try to create `.` and `..`, you will get an error:

```shell
alper@brs23-2204:~/a/b$ mkdir .
mkdir: cannot create directory ‘.’: File exists

alper@brs23-2204:~/a/b$ mkdir ..
mkdir: cannot create directory ‘..’: File exists
```

According to my research (ChatGPT, not completely sure especially for non-ext
file systems), file systems like ext2/3/4, FAT32, Btrfs and ZFS store `.` and
`..` entries on the disk physically while exFAT, NTFS don't. However, if you
mount those file systems on Linux you will see `.` and `..`. How? Because
Virtual File System (VFS) layer creates them *virtually*. NTFS doesn't have
Linux concepts like `rwx` or `user:group` permissions naturally. Those
transformations are created by NTFS driver while VFS is responsible for creating
unified file system view from the user perspective by creating `.` and `..`, if
necessary.

### But why?

At first glance, we can think that storing `.` and `..` entries on the disk
physically is waste of space. As the kernel traverse the file system, it could
potentially create them virtually. Although this seems to be technically
possible, storing them on the disk isn't a bad idea at all.

File systems are tree-like data structures stored on disks. Disks are prone to
errors due to power losses or internal errors. Storing `.` and `..` on the disk
increases success ratio of file recovery tools like `fsck`. Because those
entries are sort of duplicate pointers pointing to current and parent
directories. This duplication creates a backup. Even if some part of the disk is
corrupted with this duplication, `fsck` can recreate the data structure.

If the kernel had to create `.` and `..` virtually all the time, we might
observe a performance penalty. Also storing them on the disk causes a little bit
space inefficiency, they are stored on the disk efficiently as much as possible
by the file systems. Having physically `.` and `..` entries on the disk allow
fast directory traversal since kernel can read those entries from the disk
directly.

## Symlinks, Weird `cd` and `pwd` Behavior on `.` and `..`

We can't create hard links to directories, but we can create symlinks (soft
links). Navigating with symlinks directed to directories can be a little
weird.

This is our structure:

```shell
alper@brs23-2204:~$ tree a

a
└── b
    └── c

2 directories, 0 files
```

Now let's create a symlink to `b` from the outside of the structure:
`ln -s a/b x`.

If we `cd` to `x` we get to `b`:

```shell
alper@brs23-2204:~$ cd x
alper@brs23-2204:~/x$ ls
c
```

and

```shell
alper@brs23-2204:~/x$ ls -lai
total 12
8520988 drwxrwxr-x 3 alper alper 4096 Jul 13 19:53 .
8520987 drwxrwxr-x 3 alper alper 4096 Jul 13 14:20 ..
8520989 drwxrwxr-x 2 alper alper 4096 Jul 13 19:50 c
```

For example, let's `cd` into `..`. The inode number for `..` is `8520987` which
is `b`. But when we `cd` to `..`, we don't reach to `b` instead we are now
at the parent directory of `x`, not at the parent of `c`. **This is due to
default behavior of the `cd` command of the shell, BASH.** According to my
observations, ZSH also behaves the same.

`cd` is a built-in command for shells. Unlike `ls`, `grep` or many other tools,
it isn't a separate executable. When we execute `cd ..`, the shell doesn't have
to `cd` into the listed, the actual `..` which is confusing. The default
behavior of `cd`, for most (?) of the shell, is following **logical** semantics.
Therefore, when we type `cd ..`, we go to the parent of the symlink not parent
of the target. If we want `cd` to follow symlinks *truly* then we should use the
`-P` flag. [^1f] This behavior is defined in the POSIX standards [^2f].

```text
-P

Handle  the  operand dot-dot physically; symbolic link components shall be
resolved before dot-dot components are processed (see step 7. in the
DESCRIPTION).
```

The default behavior is *logical* mode:

```text
-L

Handle the operand dot-dot physically; symbolic link components shall be
resolved before dot-dot components are processed (see step 7. in the
DESCRIPTION).
```

Here is the example:

```shell
alper@brs23-2204:~$ cd -P x
alper@brs23-2204:~/a/b$ cd ..
alper@brs23-2204:~/a$

alper@brs23-2204:~$ cd x
alper@brs23-2204:~/x$ cd -P ..
alper@brs23-2204:~/a$
```

If you want this as default behavior, you can create an alias like
`alias cd="cd -P"`.

A similar situation is true for `pwd` command, for both executable and shell's
built-in (if exists): [^3f]

```text
-L, --logical
      use PWD from environment, even if it contains symlinks

-P, --physical
      avoid all symlinks

If no option is specified, -P is assumed.
```

I highly suggest you to read the manual of *your components (cd, pwd, etc.)* to
understand the correct behavior.

[^1f]: <https://askubuntu.com/questions/817292/cd-to-a-symlink-is-the-same-to-cd-to-original-folder>
[^2f]: <https://man7.org/linux/man-pages/man1/cd.1p.html>
[^3f]: <https://man7.org/linux/man-pages/man1/pwd.1.html>
