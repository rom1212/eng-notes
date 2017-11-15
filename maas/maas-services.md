# Find maas Services
```
$ systemctl list-unit-files | grep enabled
...
maas-dhcpd.service                         enabled
maas-dhcpd6.service                        enabled
maas-proxy.service                         enabled
maas-rackd.service                         enabled
maas-regiond.service                       enabled
...
```
The DHCP server is started by maas-dhcpd.service.

# DHCP
```
 dhcpd -user dhcpd -group dhcpd -f -q -4 -pf /run/maas/dhcp/dhcpd.pid -cf /var/lib/maas/dhcpd.conf -lf /var/lib/maas/dhcp/dhcpd.leases eth0
```

