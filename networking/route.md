# routing table
* docs
  * http://linux-ip.net/html/routing-tables.html
  * https://www.cyberciti.biz/faq/howto-linux-configuring-default-route-with-ipcommand/
  * http://www.adminsehow.com/2011/09/iptables-packet-traverse-map/
  * http://www.thegeekstuff.com/2012/04/route-examples/
* server routing tables
  * local, main, default, unspec
* routing type for each table entry
  * local, broadcast, nat: these three types are only used for table "local"
* nat
  * use ip tables: http://linux-ip.net/html/nat-dnat.html#ex-nat-dnat-full
  * use iproute2: http://linux-ip.net/html/nat-stateless.html
  * https://serverfault.com/questions/135053/iproute2-rules-and-iptables-nat-what-is-the-difference

# route command

# ip route command

## ip route (show)
* it doesn't print text for route type 'unicast', but it prints text for other types. e.g.
```
$ sudo ip route add blackhole 172.168.0.0/16
$ ip route
default via 10.0.3.2 dev enp0s8  proto static  metric 100
10.0.3.0/24 dev enp0s8  proto kernel  scope link  src 10.0.3.15  metric 100
blackhole 172.168.0.0/16
```

# routing table and iptables

# Docs
* two default gateway on one system: https://www.thomas-krenn.com/en/wiki/Two_Default_Gateways_on_One_System
