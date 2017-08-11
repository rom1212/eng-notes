# Questions
## Which port does the switch send dhcp request?
According to the ztp log, it seems that switch will try different port, first from management port, and the other ports. The steps are
* get all ports (interfaces)
* isolate ports so that they cannot talk to each other. In this way, one port's DHCP request will not goes to other ports.
* create vlan 1
* send DHCP request from MEth1/0/1
* send DHCP request from GE40 ports
* send DHCP request from GE10 ports
* send DHCP request from GE ports
