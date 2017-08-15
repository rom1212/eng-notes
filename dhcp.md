# Test DHCP Server: dhcptest
* https://github.com/CyberShadow/dhcptest
* Download DMD (package) from http://dlang.org/download.html#dmd
  * ```sudo dpkg -i dmd_2.075.1-0_amd64.deb```
## Test a specific DHCP server with a specific client MAC Address
```
sudo ./dhcptest --bind xxx.xx.49.11 --mac xx:xx:xx:08:98:85
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
