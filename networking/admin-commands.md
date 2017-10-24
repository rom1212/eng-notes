# network manager, ifconfig, ifup, ifdown
* https://askubuntu.com/questions/1786/what-is-the-difference-between-network-manager-and-ifconfig-ifup-etc

# commands
## tcpdump
* ICMP only: tcpdump -i eth0 icmp

## restart network
* ip addr flush interface-name
* systemctl restart networking.service

## iptables
* beginner guilde to iptables: https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/
