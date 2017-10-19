# Network Monitoring

## What to monitor
### Per-Process Monitoring
* use libcap - e.g. nethogs


## libpcap
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

## nethogs
* Source: https://github.com/raboof/nethogs/
* Implementation
  * https://github.com/raboof/nethogs/blob/master/src/decpcap.c
    * call pcap_* functions
  * libnethogs.cpp: nethogsmonitor_handle_update
  * Packet.h, Process.h, 
* reference to other tools, e.g. nettop, iftop, 
