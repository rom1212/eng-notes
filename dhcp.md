# DHCP Servers

## ISC-DHCP
* Install & Start
```
sudo apt install isc-dhcp-server
sudo vim /etc/dhcp/dhcpd.conf
sudo systemctl restart isc-dhcp-server
sudo systemctl status isc-dhcp-server
ls /var/lib/dhcp/
```
* Example
  * dhcp server ip: 192.168.1.105/24
  * (dhcp.conf example)[https://github.com/romans1212notes/eng-notes/blob/master/pxe-boot/etc/dhcp/dhcpd.conf]
  * more details: https://github.com/romans1212notes/eng-notes/tree/master/pxe-boot


## ISC-KEA
* http://www.isc.org/kea/
* dev: http://kea.isc.org/wiki
* source: https://github.com/isc-projects/kea
* docs:
  * https://www.isc.org/wp-content/uploads/2017/05/131-kea-ripe74-final.pdf
  * https://code.facebook.com/posts/845909058837784/using-isc-kea-dhcp-in-our-data-centers/
* HA with MySQL Cluster
  * https://www.isc.org/blogs/kea-with-mysql-cluster-backend-test-report/
  * https://kb.isc.org/article/AA-01406/210/MySQL-Cluster-set-up-for-Kea-1.0.html
  
  
# Test DHCP Server: dhcptest
* https://github.com/CyberShadow/dhcptest
* Download DMD (package) from http://dlang.org/download.html#dmd
  * ```sudo dpkg -i dmd_2.075.1-0_amd64.deb```

## Test a specific DHCP server with a specific client MAC Address
```
sudo ./dhcptest --bind xxx.xx.49.11 --mac xx:xx:xx:08:98:85
```

## Test DHCP server with specific options
```
# On the DHCP client, or even on the same host as the DHCP server (i.e. xxx.xx.49.11)
~/dhcptest$ sudo ./dhcptest --bind xxx.xx.49.11 --mac xx:xx:xx:08:98:85 --query --request 66 --request 67
dhcptest v0.7 - Created by Vladimir Panteleev
https://github.com/CyberShadow/dhcptest
Run with --help for a list of command-line options.

Listening for DHCP replies on port 68.
Sending packet:
  op=BOOTREQUEST chaddr=xx:xx:xx:08:98:85 hops=0 xid=C7080B53 secs=0 flags=8000
  ciaddr=0.0.0.0 yiaddr=0.0.0.0 siaddr=0.0.0.0 giaddr=0.0.0.0 sname= file=
  2 options:
     53 (DHCP Message Type): discover
     55 (Parameter Request List):  66 (TFTP server name),  67 (Bootfile name)
```

```
# On the DHCP Server
~$ sudo dhcpdump -i <interface that dhcp server is listening to for xx.xx.49.11, e.g. enp2s0f0>
  TIME: 2017-08-15 21:05:55.480
    IP: xx.xx.49.11 (xx:xx:xx:34:cd:24) > 255.255.255.255 (ff:ff:ff:ff:ff:ff)
    OP: 1 (BOOTPREQUEST)
 HTYPE: 1 (Ethernet)
  HLEN: 6
  HOPS: 0
   XID: c7080b53
  SECS: 0
 FLAGS: 7f80
CIADDR: 0.0.0.0
YIADDR: 0.0.0.0
SIADDR: 0.0.0.0
GIADDR: 0.0.0.0
CHADDR: xx:xx:xx:08:98:85:00:00:00:00:00:00:00:00:00:00
 SNAME: .
 FNAME: .
OPTION:  53 (  1) DHCP message type         1 (DHCPDISCOVER)
OPTION:  55 (  2) Parameter Request List     66 (TFTP server name)
                                             67 (Bootfile name)

---------------------------------------------------------------------------

  TIME: 2017-08-15 21:05:55.480
    IP: xx.xx.49.11 (xx:xx:xx:34:cd:24) > 255.255.255.255 (ff:ff:ff:ff:ff:ff)
    OP: 2 (BOOTPREPLY)
 HTYPE: 1 (Ethernet)
  HLEN: 6
  HOPS: 0
   XID: c7080b53
  SECS: 0
 FLAGS: 7f80
CIADDR: 0.0.0.0
YIADDR: xxx.xx.49.40
SIADDR: xxx.xx.49.11
GIADDR: 0.0.0.0
CHADDR: xx:xx:xx:08:98:85:00:00:00:00:00:00:00:00:00:00
 SNAME: .
 FNAME: ztp_config.ini.
OPTION:  53 (  1) DHCP message type         2 (DHCPOFFER)
OPTION:  54 (  4) Server identifier         xxx.xx.49.11
OPTION:  51 (  4) IP address leasetime      4600 (1h16m40s)
OPTION:  66 ( 12) TFTP server name          xxx.xx.49.11
OPTION:  67 ( 14) Bootfile name             ztp_config.ini
OPTION:   1 (  4) Subnet mask               255.255.255.0
---------------------------------------------------------------------------
```

```
# on DHCP server, dhcpd.conf
host a4 {
  hardware ethernet xx:xx:xx:08:98:85;
  fixed-address xx.xx.49.40;
  option domain-name-servers xxx.xx.49.11;
  option routers xxx.xxx.49.254;
  option broadcast-address xxx.xxx.49.255;
  default-lease-time 4600;
  max-lease-time 7200;
  next-server xxx.xx.49.11;
  filename "ztp_config.ini";
  option tftp-server-name "xxx.xx.49.11";
  option bootfile-name "ztp_config.ini";
}
```

# Debug DHCP
https://github.com/romans1212notes/eng-notes/blob/master/pxe-boot/dhcp-debug.md

# Find DHCP Server using nmap
https://en.wikipedia.org/wiki/Nmap

Find DHCP Server
* https://superuser.com/questions/750359/check-if-a-dhcp-server-existing-in-my-network-using-bash
* https://nmap.org/nsedoc/scripts/broadcast-dhcp-discover.html
```
$ sudo nmap --script broadcast-dhcp-discover
Starting Nmap 7.01 ( https://nmap.org ) at 2017-08-14 22:43 EDT
Pre-scan script results:
| broadcast-dhcp-discover:
|   Response 1 of 1:
|     IP Offered: 192.168.1.114
|     DHCP Message Type: DHCPOFFER
|     Server Identifier: 192.168.1.1
|     IP Address Lease Time: 1 day, 0:00:00
|     Subnet Mask: 255.255.255.0
|     Router: 192.168.1.1
|     Domain Name Server: 192.168.1.1
|     Domain Name: localdomain
|     Broadcast Address: 192.168.1.255
|_    NTP Servers: 192.168.1.1
WARNING: No targets were specified, so 0 hosts scanned.
Nmap done: 0 IP addresses (0 hosts up) scanned in 2.08 seconds
```

??? You can also include a list of hosts that have anything to do with port 67:
```
nmap --script broadcast-dhcp-discover -p67 [your network CIDR]
```
Others:
* https://nmap.org/nsedoc/scripts/dhcp-discover.html
* http://www.unix.com/ip-networking/171195-dhcp-server-discover.html
* https://www.puryear-it.com/find-rogue-dhcp-server-using-linux

# DHCP docs
* a list of options (names, but not config field name in dhcpd.conf):  http://www.networksorcery.com/enp/protocol/bootp/options.htm
* config field name in dhcpd.conf (but no option number/code): https://linux.die.net/man/5/dhcp-options
