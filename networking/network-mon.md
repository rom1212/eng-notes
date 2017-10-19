# Network Monitoring

## What to monitor
### Per-Process Monitoring
* use libcap - e.g. nethogs


## Tools
### Docs
* https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/

### libpcap
* Install
```
# ubuntu
sudo apt-get install libpcap-dev
man pcap
```
* Usage
```
#include <pcap/pcap.h>
```
* Source: https://github.com/the-tcpdump-group/libpcap

### nethogs
* Source: https://github.com/raboof/nethogs/
* Implementation
  * https://github.com/raboof/nethogs/blob/master/src/decpcap.c
    * call pcap_* functions
  * libnethogs.cpp: nethogsmonitor_handle_update
  * Packet.h, Process.h, 
* reference to other tools, e.g. nettop, iftop, 

### cacti
* mostly a graphing tool
* https://github.com/Cacti/cacti

### arp-watch
https://github.com/st3v/arp-watch/tree/master/observer

### net-tools
* source: https://github.com/ecki/net-tools, https://github.com/giftnuss/net-tools
* including
  * arp, hostname, ifconfig, netstat, rarp and route
  * particular network hardware types (plipconfig, slattach, mii-tool)
  * advanced aspects of IP configuration (iptunnel, ipmaddr).
### traceroute
https://packages.ubuntu.com/trusty/inetutils-traceroute
