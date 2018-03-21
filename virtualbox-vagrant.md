# Virtualbox
## Fedoral
* Workstation for desktop (vs. server, atomic-docker)
  * https://getfedora.org/en/workstation/download/
    * Netinstall Images: 64-bit 482MB image
  * After installation, and Reboot - need to remove iso from Virtualbox Settings->Storage->Controller IDE.
  * After reboot - click on "Activities" on upper left corner, or right click on desktop, or click ```_^_``` network icon

# Install on Ubuntu 16.04
## Install vagrant
```
sudo apt-get update (optional)
apt-cache show vagrant (see Version: 1.8.1+dfsg-1)
sudo apt-get install vagrant
vagrant --version
# Vagrant 1.8.1
```
## Install VirtualBox
```
# https://www.virtualbox.org/wiki/Linux_Downloads
# Download AMD64 from Ubuntu 16.04 ("Xenial")  i386 |  AMD64
sudo apt install libqt5x11extras5
sudo dpkg -i virtualbox-5.1_5.1.26-117224~Ubuntu~xenial_amd64.deb
```
## Fix Problem that vagrant cannot find virtualbox
https://github.com/romans1212notes/vagrant-virtualbox-fix