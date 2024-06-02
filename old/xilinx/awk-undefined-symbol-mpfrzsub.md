---
og:description: "A problem running Vivado 2016.4 on Ubuntu 16.04"
giscus: 5631761e-a5b4-4e6d-a6e9-d38d99bfb3d4
---

# awk: symbol lookup error: awk: undefined symbol: mpfr_z_sub

## Symptoms

Running TCL script of a **Vivado 2016.4** project on **Ubuntu 16.04 (.6) LTS**
emits this error. It looks like a bug in Vivado 2016.4 which is triggered while
running on Ubuntu. There are possible solutions. My solution doesn’t look like
the best one but it works.

## Solution

Open `bin/loader` file located at Vivado installation directory, for example
`... Vivado/2016.4/bin/loader`. Find the following code around **line 420**.

```bash
OS=$(awk '/DISTRIB_ID=/' /etc/*-release | sed 's/DISTRIB_ID=//' | tr '[:upper:]' '[:lower:]')
```

Comment the line and add a one line command as follows.

```bash
#OS=$(awk '/DISTRIB_ID=/' /etc/*-release | sed 's/DISTRIB_ID=//' | tr '[:upper:]' '[:lower:]')
OS="ubuntu"
```

By doing this we are assigning variable OS directly. If you execute the
problematic line at shell, you will get `ubuntu` as expected. However AFAIK
`awk` command executed at `bin/loader` script is different than the command
executed at command line due to include order of the script.

This solution works but the solution given
[there](https://forums.xilinx.com/t5/Installation-and-Licensing/Vivado-2016-4-on-Ubuntu-16-04-LTS-quot-awk-symbol-lookup-error/m-p/756779/highlight/true#M17778)
may be a better solution.

## Ref

- [1](https://forums.xilinx.com/t5/Installation-and-Licensing/Vivado-2016-4-on-Ubuntu-16-04-LTS-quot-awk-symbol-lookup-error/m-p/756779/highlight/true#M17778)
- [2](https://forums.xilinx.com/t5/Installation-and-Licensing/XSCT-symbol-lookup-error-awk-undefined-symbol-mpfr-z-sub/td-p/741141)
