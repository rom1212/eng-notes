# Questions
## Which port does the switch send dhcp request?
According to the ztp log, it seems that switch will try different port, first from management port, and the other ports. The steps are
* get all ports (interfaces)
* isolate ports so that they cannot talk to each other. In this way, one port's DHCP request will not goes to other ports.
* create vlan 1
* send DHCP request from MEth1/0/1
* send DHCP request from GE40 ports
* send DHCP request from GE10 ports
* send DHCP request from GE ports


# File Server
## TFTP on Ubuntu 16.04
```
sudo apt install tftpd-hpa
# make tfpt writable, https://askubuntu.com/questions/443117/how-to-configure-tftpd-hpa-to-allow-upload-of-new-files
sudo chown -R tftp /var/lib/tftpboot
sudo vim /etc/default/tftpd-hpa: TFTP_OPTIONS="--secure -c"
sudo systemctl restsrt tftpd-hpa
```
https://askubuntu.com/questions/443117/how-to-configure-tftpd-hpa-to-allow-upload-of-new-files

## FTP
https://www.digitalocean.com/community/tutorials/how-to-set-up-vsftpd-for-a-user-s-directory-on-ubuntu-16-04
* ufw - optional
* the ftp root can not be writable, e.g.
  * sudo chown nobody:nogroup /home/sammy/ftp, or
  * chmod 555 /home/sammy/ftp
* but the sub-directory can be writable.
