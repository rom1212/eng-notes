# Docs
Read more: /var/share/doc/bind9/README.Debina.gz

https://www.ostechnix.com/install-and-configure-dns-server-ubuntu-16-04-lts/

# start and stop bind on Ubuntu 16.04:
```
systemctl status bind9
systemctl restart bind9
ps aux | grep bind
bind      1849  0.0  0.0 1022484 69268 ?       Ssl  21:15   0:00 /usr/sbin/named -f -u bind

zone file:
  . do we need to have dns "A" record to root.ostechnix.lan?
```

set the general dns-nameservers works,  for a specific interface not working for me yet, i.e. add dns-nameservers as the top level entry in /etc/network/interfaces, e.g.
 
```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback
auto enp129s0f0
iface enp129s0f0 inet static
address 172.23.48.12
netmask 255.255.255.0
gateway 172.23.48.254
auto enp2s0f0
iface enp2s0f0 inet static
address 172.23.49.12
netmask 255.255.255.0
dns-nameservers 172.23.48.2
```

Then, run sudo ifdown -a, sudo ifup -a, and we can see that "nameserver 192.168.1.200" in /etc/resolv.conf, e.g.
nameserver 172.23.48.2

# DNS Server Setup
```
Two changes: /etc/bind/named.conf.local, and /etc/bind/for.xx.com

==========================
/etc/bind/named.conf.local, only zone "xx.com" still works
zone "ostechnix.lan" {
        type master;
        file "/etc/bind/for.ostechnix.lan";
        allow-transfer { 192.168.1.201; };
        also-notify { 192.168.1.201; };
};

zone "1.168.192.in-addr.arpa" {
        type master;
        file "/etc/bind/rev.ostechnix.lan";
        allow-transfer { 192.168.1.201; };
        also-notify { 192.168.1.201; };
};

zone "xx.com" {
        type master;
        file "/etc/bind/for.xx.com";
        allow-transfer { 192.168.1.201; };
        also-notify { 192.168.1.201; };
};

==========================
/etc/bind/for.xx.com
$TTL 86400
@   IN  SOA     pri.xx.com. root.xx.com. (
        2011071001  ;Serial
        3600        ;Refresh
        1800        ;Retry
        604800      ;Expire
        86400       ;Minimum TTL
)
@       IN  NS          pri.xx.com.
@       IN  NS          sec.xx.com.
@       IN  A           192.168.1.200
@       IN  A           192.168.1.201
@       IN  A           192.168.1.202
pri     IN  A           192.168.1.200
sec     IN  A           192.168.1.201
client  IN  A           192.168.1.202
```

# DNS on Windows 
```
Go to: Control Panel -> Network and Internet -> Network and Sharing Center -> Change adapter settings -> Local Area Connection -> Properties -> Internet Protocol Version 4 (TCP/IPv4) Properties -> Advanced -> DNS
Add the new DNS server as the first dns server, e.g. 172.23.48.2
Add other DNS servers (you can find them by ipconfig /all)

Download "dig" from BIND:
https://www.isc.org/downloads/
unzip, and run "dig.exe". seems that nslookup doesn't work well.

For cygwin, copy the unzip directory and put to c:/cygwin64/bin/BIND9.10.5.x64, and then change .bashrc:
export PATH=$PATH:/usr/bin/BIND9.10.5.x64
```

