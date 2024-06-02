---
og:description: "PetaLinux can be run an offline machine with proper configuration"
giscus: 39f2bee3-db03-444a-82c0-2214a05100e5
---

# Running PetaLinux on an offline machine

If you are a Xilinx customer and want to compile an embedded Linux with PetaLinux
on an offline machine, you can do it by mirroring Xilinx repos and configuring
your project. Even if you are connected to the Internet, you may want to do this
because:

- You will be make sure that your PetaLinux project can be compiled without any
  issue if you lost your connection to `xilinx.com`, to the Internet or Xilinx
  decides to delete their repos for whatever reason.
- You may want to speed up your compilation step by mirroring remote contents
  on your on-premise proxy server. (This requires slightly different setup,
  visit [this
  page](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/60129817/Xilinx+Yocto+Builds+without+an+Internet+Connection#XilinxYoctoBuildswithoutanInternetConnection-MirrorServer)
  for that setup)

There are several questions on this topic especially on Xilinx forum. I found
that not all answers work for me so I will share my *working* configuration.
There could be other solutions providing the same result. **Please add your
comment if you want to share something with me and with readers.**

The following content is tested with PetaLinux 2018.1 but I am almost
completely sure that the exact or very similar setup will work for other
versions too.

## Prerequisites

- A web server with decent disk space to host local mirror to compilation machine.

You will need some disk space. For example mirroring 2018.1 PetaLinux requires
at least 26 GB space. A standard web server like
Apache or Nginx (or may be simple Python `http.server` server?) is sufficient.

- A compilation machine which will run PetaLinux.

This machine should be connected to the server obviously.

- `sstate cache` downloaded from xilinx.com.

Visit [here](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/embedded-design-tools/archive.html)
to get `sstate cache` for your PetaLinux version. For 2018.1:
<https://www.xilinx.com/member/forms/download/xef.html?filename=sstate-rel-v2018.1.tar.gz>
or in the form of
`https://www.xilinx.com/member/forms/download/xef.html?filename=sstate-rel-VERSION.tar.gz`

After getting the `sstate-rel-VERSION.tar.gz` file, extract it on the server.
The files must be accessible via HTTP. Your server may be accessible via IP address,
like  `192.168.1.2` or with a domain like `mirror.mydomain`. Regardless of this,
you should see files when you visit the server with a web browser like `http://192.168.1.2`
or `http://mirror.mydomain`. For the rest of the post, I will assume that server
is accessible via `http://server`.

If you are planning to mirror repository of more than one PetaLinux version, I
would suggest you to follow [Xilinx's
mirror](http://petalinux.xilinx.com/sswreleases/) convention. With that convention,
server structure will look like:

```text
http://server/
              rel-v2018.1/
                          aarch64
                          ...
                          downloads
              rel-v2020.1/
                          aarch64
                          ...
                          downloads
```

You don't need to put `rel-vVERSION` directories at root of your server, they
can be put in another directory but try to keep these directories at the same level
without touching their inner structure.

## Configuring the PetaLinux project

The second step is configuring PetaLinux to use our self-hosted mirror. To do
this you can either run `petalinux-config` command to bring up UI or directly
edit the configuration file.

### `petalinux-config`

Run `petalinux-config` to bring up settings menu then open `Yocto Settings`.

```{figure} assets/petalinux-offline-1.png
:align: center

petalinux-config
```

In this menu, make sure that `Enable Network sstate feeds` is **checked** and
`Enable BB NO NETWORK` is **NOT checked**. I remember that some Xilinx forum
posts say to check this option but if you do this PetaLinux will assume that
you don't have *any* network connection, even a local connection to the local
server.

```{figure} assets/petalinux-offline-2.png
:align: center

petalinux-config
```

Then open `Network sstate feeds URL` setting. This should point `sstate-cache`
URL. In our example, this would be
`http://server/rel-v${PETALINUX_VER}/arm/sstate-cache`. I took screenshots from
a Zynq project so URL contains `arm`. If you are working on ZynqMP project, this
will be `aarch64`. Notice that the URL contains a placeholder,
`${PETALINUX_VER}`. This will be replaced by version like `2018.1` during build
automagically. You can also write a *hard coded* version number but I suggest to
use the placeholder.

Similarly, change `Add pre-mirror url` option to `http://server/rel-v${PETALINUX_VER}/downloads`.
Notice that the path is architecture independent.

Then, Save & Exit settings and build & package the project as usual.

```{warning}
Even if you follow this GUI*ish* way, I strongly suggest you to verify the final
settings by checking the configuration file mentioned at the next section or by
`git diff`.
```

### Edit the config file

Alternatively you can directly edit  `project-spec/configs/config` file. The
settings related to this problem follow as:

```text
CONFIG_PRE_MIRROR_URL="http://server/rel-v${PETALINUX_VER}/downloads"
CONFIG_YOCTO_NETWORK_SSTATE_FEEDS=y
CONFIG_YOCTO_NETWORK_SSTATE_FEEDS_URL="http://server/rel-v${PETALINUX_VER}/arm/sstate-cache"
# The following line is a comment line (like this one) to remind you NOT to set BB_NO_NETWORK
# CONFIG_YOCTO_BB_NO_NETWORK is not set
```

To make sure that configurations are correct you can use `git diff` if your
project under Git (should be!).

## Problem: Still I can't compile some PetaLinux projects

You may notice that your project may start to give compilation errors once you
start to add new components to rootfs with `petalinux-config -c rootfs`. This
is because not all possible rootfs components are included in file that we
got from Xilinx. If you browse to `downloads` directory of `sstate-cache` folder,
you see lots of file. These are mostly source codes of components that we will
enable with `petalinux-config -c rootfs`. If you enable a component that is not
there, PetaLinux will try to get files from the upstream repo of the component.
Since our build machine is disconnected from the Internet, build step will fail.

One possible solution is to check build logs and find which URL is failing. You
can manually download the failing file from the Internet and put the file in
`downloads` directory on the server. This works because PetaLinux checks
`downloads` directory first and it tries to fetch upstream if the file is absent
there. Another option to find upstream URL is checking `.bbappend` files (can be
found under PetaLinux setup directory) of problematic components but looking
errors in build logs is an easier way for me.

If you have many missing packages and carrying them manually is difficult for
you, you may try `bitbake -c fetchall world` command on an **online** machine
but I haven't tried this yet. Check out [this
page](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/60129817/Xilinx+Yocto+Builds+without+an+Internet+Connection)
for further info.

## Further read

- [Xilinx Wiki](https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/60129817/Xilinx+Yocto+Builds+without+an+Internet+Connection)
