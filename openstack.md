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

# Identity 
## domains, projects (tenants), users, and roles.
* domain:
  * create default domain
  ```
  openstack domain create --description "Default Domain" default
  ```
  * project:
    * Projects represent the base unit of “ownership” in OpenStack, in that all resources in OpenStack should be owned by a specific project. In OpenStack Identity, a project must be owned by a specific domain.
    * create "admin" project
    ```
    openstack project create --domain default --description "Admin Project" admin
    ```
  * user
    * create "admin" user (user is parallel with project)
    ```
    openstack user create --domain default --password-prompt admin
    ```
* role
  * can create a role and add to project and user. role can be separate from domain
