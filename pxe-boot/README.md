# Setup PXE Sever with Ubuntu 16.04 in VirtualBox
* Docs:
  * https://www.ostechnix.com/how-to-install-pxe-server-on-ubuntu-16-04/
* Install dhcpd
  * https://www.ostechnix.com/install-dhcp-server-in-ubuntu-16-04/
  * sudo -E apt-get install isc-dhcp-server
  * Add interface in /etc/default/isc-dhcp-server
  * Add subnet in /etc/dhcp/dhcpd.conf. All interfaces must have subnet declared here for dhcpd to start properly.
* Install apache
  * mount -o loop ubuntu-16.04.2-server-amd64.iso /mnt
  * mkdir /var/www/html/ubuntu-16.04.2
  * cp -rf /mnt/* /var/www/html/ubuntu-16.04.2/
* Install tftfd
  * sudo apt install tftpd-hpa
  * cp -rf /mnt/install/netboot/* /var/lib/tftpboot/
  * vim /var/lib/tftpboot/pxelinux.cfg/default
  * optional - to make tfpt writable
    * https://askubuntu.com/questions/443117/how-to-configure-tftpd-hpa-to-allow-upload-of-new-files
    * sudo chown -R tftp /var/lib/tftpboot
    * sudo vim /etc/default/tftpd-hpa: TFTP_OPTIONS="--secure -c"
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
