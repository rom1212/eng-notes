# network manager, ifconfig, ifup, ifdown
* https://askubuntu.com/questions/1786/what-is-the-difference-between-network-manager-and-ifconfig-ifup-etc

# commands
## tcpdump
* Only one protocol
  * ICMP only: tcpdump -i eth0 icmp
  * UDP only: tcpdump -i eth0 udp
* Options
  * -S: Abusolute sequence number for TCP
* Analyze TCP traffic
```
# format
#  IP (ttl, etc)
#     <src ip>.port -> <dst ip>.port    # this line is for TCP, N.B. there is no "TCP" text in this line.

# Example for wget http://xxx
$ sudo tcpdump -i enp0s3 -n -v -S
tcpdump: listening on enp0s3, link-type EN10MB (Ethernet), capture size 262144 bytes


10:55:43.630096 IP (tos 0x0, ttl 64, id 9690, offset 0, flags [DF], proto TCP (6), length 60)
    192.168.10.10.56970 > 192.168.10.1.8000: Flags [S], cksum 0xe0c1 (correct), seq 2671964859, win 29200, options [mss 1460,sackOK,TS val 1116114306 ecr 0,nop,wscale 7], length 0
10:55:43.630193 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    192.168.10.1.8000 > 192.168.10.10.56970: Flags [S.], cksum 0x958a (incorrect -> 0xfde1), seq 3975861341, ack 2671964860, win 28960, options [mss 1460,sackOK,TS val 3189662791 ecr 1116114306,nop,wscale 7], length 0
10:55:43.630595 IP (tos 0x0, ttl 64, id 9691, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.10.10.56970 > 192.168.10.1.8000: Flags [.], cksum 0x9ce9 (correct), ack 3975861342, win 229, options [nop,nop,TS val 1116114306 ecr 3189662791], length 0
10:55:43.630629 IP (tos 0x0, ttl 64, id 9692, offset 0, flags [DF], proto TCP (6), length 196)
    192.168.10.10.56970 > 192.168.10.1.8000: Flags [P.], cksum 0x5871 (correct), seq 2671964860:2671965004, ack 3975861342, win 229, options [nop,nop,TS val 1116114306 ecr 3189662791], length 144
10:55:43.630642 IP (tos 0x0, ttl 64, id 64411, offset 0, flags [DF], proto TCP (6), length 52)
    192.168.10.1.8000 > 192.168.10.10.56970: Flags [.], cksum 0x9582 (incorrect -> 0x9c53), ack 2671965004, win 235, options [nop,nop,TS val 3189662791 ecr 1116114306], length 0
10:55:43.631611 IP (tos 0x0, ttl 64, id 64412, offset 0, flags [DF], proto TCP (6), length 69)
    192.168.10.1.8000 > 192.168.10.10.56970: Flags [P.], cksum 0x9593 (incorrect -> 0xdc75), seq 3975861342:3975861359, ack 2671965004, win 235, options [nop,nop,TS val 3189662791 ecr 1116114306], length 17
10:55:43.631784 IP (tos 0x0, ttl 64, id 9693, offset 0, flags [DF], proto TCP (6), length 52)
```
* 

## wireshark
* sudo apt install wireshark
* sudo wireshark - privilige
* absolute sequence number
  * Edit->Preferences->Protocols->TCP->Relative Sequence Numbers

## restart network
* ip addr flush interface-name
* systemctl restart networking.service

## iptables
* beginner guilde to iptables: https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/
