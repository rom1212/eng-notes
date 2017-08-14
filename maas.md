# DHCP
```
 dhcpd -user dhcpd -group dhcpd -f -q -4 -pf /run/maas/dhcp/dhcpd.pid -cf /var/lib/maas/dhcpd.conf -lf /var/lib/maas/dhcp/dhcpd.leases eth0
```
