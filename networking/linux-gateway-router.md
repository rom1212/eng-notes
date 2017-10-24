# How To
## Docs
* https://monoinfinito.wordpress.com/series/setting-up-a-linux-gatewayrouter-a-guide-for-non-network-admins/

## 1. Enable IP forwarding
* http://www.ducea.com/2006/08/01/how-to-enable-ip-forwarding-in-linux/
* Enable IP forwarding
```
# check ip-forwarding enabled or not
sysctl net.ipv4.ip_forward
cat /proc/sys/net/ipv4/ip_forward

# Enable on the fly
sysctl -w net.ipv4.ip_forward=1
echo 1 > /proc/sys/net/ipv4/ip_forward

# Permanet
vim /etc/sysctl.conf
```

## 2. iptables
* https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/
* man iptables
  * TABLES: 'filter' (default), nat, etc
  * iptables --table nat --list --verbose (-L -v)
* update
```
```

## Example
* ubuntu-dev-hetmon-04-router
  * 192.168.10.1, enp0s3, intnet, used for incoming traffic
  * 192.168.50.1, enp0s8, intnet2, used for the outgoing destination/outgoing target
  * 10.0.4.15, enp0s9, NAT
  * setup ip forwarding
  ```
  # check the value: sysctl net.ipv4.ip_forward
  # enable ip forward
  sysctl -w net.ipv4.ip_forward=1  or echo 1 > /proc/sys/net/ipv4/ip_forward
  # where to route to, i.e. outgoing traffic, MASQUERADE???
  iptables --table nat --append POSTROUTING --out-interface enp0s8 -j MASQUERADE
  # for each incoming interface
  iptables --append FORWARD --in-interface enp0s3 -j ACCEPT
  ```

* ubuntu-dev-hetmon-01:
  * 192.168.10.10, enp0s3, intnet
  * 10.0.3.15, enp0s8, NAT
  * route info before adding new gateway
  ```
  $ ip route
  default via 10.0.3.2 dev enp0s8  proto static  metric 100
  10.0.3.0/24 dev enp0s8  proto kernel  scope link  src 10.0.3.15  metric 100
  169.254.0.0/16 dev enp0s3  scope link  metric 1000
  192.168.10.0/24 dev enp0s3  proto kernel  scope link  src 192.168.10.10  metric 100

  $ route -n
  Kernel IP routing table
  Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
  0.0.0.0         10.0.3.2        0.0.0.0         UG    100    0        0 enp0s8
  10.0.3.0        0.0.0.0         255.255.255.0   U     100    0        0 enp0s8
  169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 enp0s3
  192.168.10.0    0.0.0.0         255.255.255.0   U     100    0        0 enp0s3
  ```
  * add new gateway
  ```
  sudo route add default gateway 192.168.10.1

  sudo ip route
  ```
  * 

* ubuntu-dev-netmon-05
  * 192.168.50.10, enp0s3, intnet2
