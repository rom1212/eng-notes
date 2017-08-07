# Setup PXE Sever with Ubuntu 16.04 in VirtualBox
* Install dhcpd
* Install apache
  * mount -o loop ubuntu-16.04.2-server-amd64.iso /mnt
  * mkdir /var/www/html/ubuntu-16.04.2
  * cp -rf /mnt/* /var/www/html/ubuntu-16.04.2/
* Install tftfd
  * cp -rf /mnt/install/netboot/* /var/lib/tftpboot/
  * vim /var/lib/tftpboot/pxelinux.cfg/default
