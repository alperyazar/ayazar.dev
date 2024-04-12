---
og:description: "How to install WSL on a Windows machine not connected to the Internet"
og:image: assets/social/blog/21/wsl.jpg
---

# Using WSL on an offline Windows machine

```{figure} /extra/assets/social/blog/21/wsl.jpg
:align: center
:figclass: thmbnl
```

---

In this post, we will install Ubuntu 20.04 WSL package on an **offline**
Windows 10 machine. Although this post is prepared with Ubuntu 20.04, the steps
should be valid for other WSL packages too.

## Getting files

If your Windows machine is connected to the Internet and you can easily install
WSL packages via Microsoft Store like by clicking *Download from the Microsoft
Store* [here](https://ubuntu.com/wsl). To install it on an offline machine,
first we get `.appx` package for a corresponding guest OS from Microsoft. All
available Packages are listed
[here](https://docs.microsoft.com/en-us/windows/wsl/install-manual#downloading-distributions).
Transfer the downloaded package to the target offline machine. For example, when
I am writing this post, to install Ubuntu 20.04 I get
`Ubuntu_2004.2020.424.0_x64.appx`.

## Enabling WSL on Windows

Open a PowerShell terminal and type `wsl`. If you get an error about not recognized
command, first you should enable WSL. The official instructions are given
[here](https://docs.microsoft.com/en-us/windows/wsl/install-win10#set-your-distribution-version-to-wsl-1-or-wsl-2).
Alternatively you can do it with GUI. Find `Programs and Features` on `Control Panel`,
then click `Turn Windows features on or off` as shown below.

```{todo}
`2-wsl-enable.png` is missing
```

After rebooting Windows, `wsl` command should be available to use and should be
working on PowerShell. Since we don't have any installed WSL guest OS on the PC,
it will say  `... no installed distributions.`

```{note}
ℹ️ If your machine
[satisfies](https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-2---check-requirements-for-running-wsl-2)
requirements for WSL 2 and you don't have any [specific
reason](https://docs.microsoft.com/en-us/windows/wsl/compare-versions) to stick
with WSL (1), I recommended to switch to WSL 2 now but you can stick with WSL
(1) either. I am not using WSL 2 but I think the following steps should be fine
for WSL 2 too.
```

## Installing WSL package

In theory, the following command given in the [official
page](https://docs.microsoft.com/en-us/windows/wsl/install-manual#installing-your-distro)
should do the work.

```powershell
Add-AppxPackage .\Ubuntu_2004.2020.424.0_x64.appx
```

## Error: "The service has not been started"

After installing the package, you can find the installed software by typing
`Ubuntu` in Windows Start menu search. **However** in my case, I couldn't
start the Ubuntu WSL and got the `The service has not been started.` error as
shown below. This is probably related to version of Windows 10.

```{todo}
`2-wsl-error.png` is missing
```

### Solution

You can remove `Ubuntu` found in Windows Start menu by right clicking and selecting
`Uninstall` since we won't use it.

One solution recommended by Microsoft is extracting `.appx` file with an file
archiver program, like 7-Zip by right clicking on file and selecting `Extract`
option, and then running `ubuntu2004.exe`.

```{attention}
⚠️ After extraction please make sure that your folder is at right place.
Although it is possible to move folders to another location, in my case moving
folders **after** installation gives me `Cannot find the specified path` error.
So before installation make sure that this is the correct location. After
installation, `rootfs` folder is created next to `ubuntu2004.exe` and file
system of the Linux will live here. So make sure that you have enough space for
your future needs. The WSL is somehow *fragile* [^1f]. Although it is possible
to move files as moving ordinary files in Windows after installation, be ready
for side effects.
```

With first run the installation process begins
and you are prompted to select an username and associated password. After
completing installation, you can use your Linux distro. Notice that file system
for the Linux is created under `rootfs` folder. After installation, Ubuntu 20.04
creates ~40K items in its folder.

## Pitfall: Moving Ubuntu 20.04 After Installation

I got `Cannot find the specified path` error when I moved to another folder
after installation. Other people report the same problem too [^1f]. In my case,
since I was using fresh Ubuntu installation, I reinstalled it but I don't know the
proper solution if you don't want to loose your distro. Some people also
reported that a Windows update also breaks the WSL [^1f], so... yeah, classical
Windows...

### Solution

Even if you decide to reinstall the Ubuntu at the new location, when you run
`ubuntu2004.exe` you get `The system cannot find the path specified` error.
Even if you run `wsl` on PowerShell you get the same error. The reason is
the previous machine is still registered. If you run `wslconfig /l`, you will
see the previous machine. So first *unregister* the previous distro, example:

```powershell
wslconfig /u Ubuntu-20.04
```

After that, `wsl` command should run, then you can install the Ubuntu to a
new location.

```{note}
ℹ️ If you know how to move installed distro without reinstalling again, **please
comment.** Maybe [this](https://stackoverflow.com/a/51767786)?
```

## Error: "WslRegisterDistribution failed with error: 0x80070005"

When I tried to install the distro runnig `ubuntu2004.exe` on `D:` drive, I
got this error but if I run it on `C:` drive everything works. This is probably
due to security settings of my Windows machine.

### Solution

Since I don't want to bother with these settings, I chose to **Run as
administrator** on `D:` drive. After installation, user is able to run the
distro and no privilege is required. Similar problems and proper solutions also
exist [^2f], [^3f], [^4f].

## Conclusion

Although using a Linux distro on Windows in a *native* way is a very good
experience, WSL doesn't look so solid and may become broken after an Windows
update. So if you are planning to use be ready for possible future problems.

[^1f]: <https://github.com/microsoft/WSL/issues/3976#issuecomment-581617473>
[^2f]: <https://scriptech.io/windows-10-1903-wsl-access-is-denied-error-0x80070005/>
[^3f]: <https://scriptech.io/group-policy-use-a-custom-security-template-in-a-group-policy-to-globally-manage-the-lxssmanager-service/>
[^4f]: <https://github.com/Microsoft/WSL/issues/3054>

*Published on: 2021-03-16*

```{disqus}
:disqus_identifier: cacb191f-bed5-4927-80ba-8a1e3c8a436f
```
