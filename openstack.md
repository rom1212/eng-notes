# Install
* Ubuntu: https://docs.openstack.org/ocata/install-guide-ubuntu/

# Networking
## Two Options
* Networking Option 1: Provider networks
  * primarily layer-2 (bridging/switching) services and VLAN segmentation of networks.
  * Essentially, it bridges virtual networks to physical networks and relies on physical network infrastructure for layer-3 (routing) services
  * a DHCP service provides IP address information to instances.
  * TBD: create virtual switch (e.g. OVS, Linux bridge) to route the VM traffic from one host to another
* Networking Option 2: Self-service networks
  * layer-3 (routing) services that enable self-service networks using overlay segmentation methods such as [VXLAN](https://en.wikipedia.org/wiki/Virtual_Extensible_LAN).
  * Essentially, it routes virtual networks to physical networks using NAT. 
  * Additionally, this option provides the foundation for advanced services such as LBaaS and FWaaS.
  * TBD: It uses a VLAN-like encapsulation technique to encapsulate MAC-based OSI layer 2 Ethernet frames within layer 4 UDP packets
