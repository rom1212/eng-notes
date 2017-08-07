# Setup PXE Sever with Ubuntu 16.04 in VirtualBox
* Install dhcpd
* Install apache
  * mount -o loop ubuntu-16.04.2-server-amd64.iso /mnt
  * mkdir /var/www/html/ubuntu-16.04.2
  * cp -rf /mnt/* /var/www/html/ubuntu-16.04.2/
* Install tftfd
  * cp -rf /mnt/install/netboot/* /var/lib/tftpboot/
  * vim /var/lib/tftpboot/pxelinux.cfg/default
* Double check that system is setup correctly:
```
# check tftpd
systemctl restart tftpd-hpa
systemctl status tftpd-hpa
curl tftp://localhost/pxelinux.cfg/default  # make sure the content is correct.
# check dhcp
systemctl restart isc-dhcp-server
systemctl status isc-dhcp-server
# check apache http and kickstart file
curl http://localhost/ks-ubuntu-16.04.2.cfg  # make sure the content is correct.
# live monitor DHCP and http log.
tail -f /var/log/syslog  # for DHCP log
tail -f /var/log/apache2/access.log
```
