# network discovery
## arp
```
$ /usr/sbin/arp
```

## arp-scan
https://www.blackmoreops.com/2015/12/31/use-arp-scan-to-find-hidden-devices-in-your-network/
```
$ sudo -E apt-get install arp-scan
$ sudo arp-scan --interface=eth0 --localnet
```
* http://www.nta-monitor.com/wiki/index.php/Arp-scan_User_Guide

## nmap
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

## Net Scan
* Netcat Power Tools - book
  * using ICMP, or TCP SYN
  * using nmap
  
## TCP Ping
* https://serverfault.com/questions/14376/ping-alternative-for-tcp
  * hping
  * exmaple with hping - http://www.slashroot.in/what-tcp-ping-and-how-it-used
* https://elifulkerson.com/projects/tcping.php



## others  
* https://serverfault.com/questions/245136/how-to-find-out-mac-addresses-of-all-machines-on-network
* "linux discovery nearby mac address"
* http://rayslinux.blogspot.com/2015/02/10-handy-tools-for-network-discovery.html
* https://www.linux.com/learn/who-and-what-my-network-probing-your-network-linux
* 

