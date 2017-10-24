# routing table
* docs
  * http://linux-ip.net/html/routing-tables.html
* server routing tables
  * local, main, default, unspec
* routing type for each table entry
  * local, broadcast, nat: these three types are only used for table "local"

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
