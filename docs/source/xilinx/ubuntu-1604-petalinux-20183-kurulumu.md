---
og:description: "Ubuntu 16.04'e Petalinux 2018.3'ü kurarken çıkan sorunları çözüyoruz."
---

# Ubuntu 16.04.5 Üzerinde Petalinux 2018.3 Kurulumu

Yeni kurulmuş (sanal makina, VirtualBox üzerinde) petalinux 2018.3 kurarken
kurduğum adımları yazacağım. Öncesinde bu bilgisayara Vivado 2018.3 kurdum, bu
aşamada ek bir paket kurmadım. O yüzden olabildiğince "vanilla" bir durumu
gösterdiğimi düşünüyorum.

```shell
$ ./petalinux-v2018.3-final-installer.run /opt/petalinux20183/
```

Bunu yazınca aşağıdaki hata çıkıyor.

```text
INFO: Checking installation environment requirements...
awk: read error (Bad address)

Please refer to the PetaLinux Tools Installation Guide.

Check the troubleshooting guide at the end of that manual, and if you are
unable to resolve the issue please contact customer support with file:
   /home/alper/petalinux_installation_log

awk: read error (Bad address)
./petalinux-v2018.3-final-installer.run: line 139: /tmp/tmp.u0yj3VrSwg/: Is a directory
ERROR: Failed to extract Petalinux installer...
```

Benzer hatayı Arch'a kurarken de almıştım. Petalinux UG1144 2018.3'te Ubuntu
16.04.3'ten bahsediliyor, ben biraz daha güncel sürümde deniyorum. Burada
sanıyorum ki (bir Xilinx forum'da da görmüştüm) awk'ın çıktısının doğru
değerlendirilememesi var. Fakat Arch'ta gördüğüm hata sonraki aşamalarda
sanıyorum aarch64 Yocto kurulumu sırasında çıkıyordu, forumdakini bilmiyorum.

Daha sonra

```shell
$ sudo apt install gawk
```

dediğim zaman bu hata gitti. Kurduğum paket `gawk (1:4.1.3+dfsg-0.1)` oldu. Daha
sonra aldığım hata:

```text
INFO: Checking installation environment requirements...
INFO: Checking free disk space
INFO: Checking installed tools
ERROR: You are missing the following system tools required by PetaLinux:

 - chrpath
 - socat
 - autoconf
 - libtool
 - git
 - texinfo
 - zlib1g-dev
 - gcc-multilib
 - libsdl1.2-dev
 - libglib2.0-dev
Please check PetaLinux installation guide - required tools and libraries package section for detailed information

INFO: Checking installed development libraries
ERROR: You are missing these development libraries required by PetaLinux:

 - zlib
 - ncurses
 - openssl
 - zlib1g:i386

Please install them with your operating system package manager, and try again
WARNING: Please install required packages.

Please refer to the PetaLinux Tools Installation Guide.

Check the troubleshooting guide at the end of that manual, and if you are
unable to resolve the issue please contact customer support with file:
   /home/alper/petalinux_installation_log
```

Daha sonra aşağıdaki komut ile eksikleri yükledim.

```shell
$ sudo apt install chrpath socat autoconf libtool git texinfo zlib1g-dev gcc-multilib libsdl1.2-dev libglib2.0-dev zlib1g-dev libncurses5-dev openssl zlib1g:i386
```

Aşağıdaki hatayı aldım:

```text
$ ./petalinux-v2018.3-final-installer.run /opt/petalinux20183/
INFO: Checking installation environment requirements...
INFO: Checking free disk space
INFO: Checking installed tools
INFO: Checking installed development libraries
ERROR: You are missing these development libraries required by PetaLinux:

 - openssl

Please install them with your operating system package manager, and try again
WARNING: Please install required packages.

Please refer to the PetaLinux Tools Installation Guide.

Check the troubleshooting guide at the end of that manual, and if you are
unable to resolve the issue please contact customer support with file:
   /home/alper/petalinux_installation_log
```

Daha sonra yükleme yaptım:

```shell
$ sudo apt install libssl-dev
```

Yükleme sonra başarı ile sonlandı.

```shell
$ ./petalinux-v2018.3-final-installer.run /opt/petalinux20183/
INFO: Checking installation environment requirements...
INFO: Checking free disk space
INFO: Checking installed tools
INFO: Checking installed development libraries
INFO: Checking network and other services
WARNING: No tftp server found - please refer to "PetaLinux SDK Installation Guide" for its impact and solution
INFO: Checking installer checksum...
INFO: Extracting PetaLinux installer...

LICENSE AGREEMENTS

PetaLinux SDK contains software from a number of sources.  Please review
the following licenses and indicate your acceptance of each to continue.

You do not have to accept the licenses, however if you do not then you may
not use PetaLinux SDK.

Use PgUp/PgDn to navigate the license viewer, and press 'q' to close

Press Enter to display the license agreements
Do you accept Xilinx End User License Agreement? [y/N] > y
Do you accept Webtalk Terms and Conditions? [y/N] > y
Do you accept Third Party End User License Agreement? [y/N] > y
INFO: Installing PetaLinux...
INFO: Checking PetaLinux installer integrity...
INFO: Installing PetaLinux SDK to "/opt/petalinux20183//."
INFO: Installing aarch64 Yocto SDK to "/opt/petalinux20183//./components/yocto/source/aarch64"...
INFO: Installing arm Yocto SDK to "/opt/petalinux20183//./components/yocto/source/arm"...
INFO: Installing microblaze_full Yocto SDK to "/opt/petalinux20183//./components/yocto/source/microblaze_full"...
INFO: Installing microblaze_lite Yocto SDK to "/opt/petalinux20183//./components/yocto/source/microblaze_lite"...
INFO: PetaLinux SDK has been installed to /opt/petalinux20183//.
```

Daha sonra örnek bir proje yaratıp, başarıyla derleyebildim ve QEMU ile test ettim.

> ⚠️ Örnek proje yaparken `setting.sh` source ettiğim zaman `/bin/sh`in `bash`
> olmadığı konusunda uyarı aldım, Ubuntu'da `dash` geliyormuş. Şimdilik bıraktım
> sorun yok gibi ama sıkıntı olursa bunu değiştirebilirim. Umarım bu notu ve
> değişiklik yaparsam burayı da düzeltmeyi unutmam.

Projeyi ilk derlerken aşağıdaki uyarı çıkıyor.

```text
WARNING: petalinux-user-image-1.0-r0 do_rootfs: [log_check] petalinux-user-image: found 1 warning message in the logfile:
[log_check] warning: %post(sysvinit-inittab-2.88dsf-r10.plnx_zynq7) scriptlet failed, exit status 1
```

Xilinx'e göre bu ihmal edilebilir. Ref:
[Link](https://www.xilinx.com/support/answers/71110.html) (Ref ZynqMP üzerine
ama bence benzer durum)

```{disqus}
:disqus_identifier: 7b37f315-cf1e-468b-bb25-f4a7e177de45
```
