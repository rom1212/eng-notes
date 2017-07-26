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

## Deployment Cases
https://docs.openstack.org/liberty/networking-guide/deploy.html
* https://docs.openstack.org/liberty/networking-guide/scenario-classic-ovs.html

# Identity 
## domains, projects (tenants), users, and roles.
* doc: https://www.safaribooksonline.com/library/view/identity-authentication-and/9781491941249/ch01.html
* domain:
  * In the same domain, we couldn't have two projects with the same name, or two users with the same name. So, a domain can be used to represent an enterprise. 
    * "For example, a cloud could have two domains, IBM and Acme Inc. IBM has their own collection of groups, users, and projects and so does Acme Inc." [safaribooksonline](https://www.safaribooksonline.com/library/view/identity-authentication-and/9781491941249/ch01.html)
  * cross-domain access
    * projects and users have an unique UUID, and so by design, cross-domain access is possible and it is the same as intra-domain access.
    * However, problems are
      * users in one domain are not visible on another domain
      * only one domain administrator is involed in the process, and the other doman administrator doesn't have control.
      * centralized control will have more overhead for the centralized administrator.
    * [Extending OpenStack Access Control with Domain Trust](https://pdfs.semanticscholar.org/c091/eefd83b0ec82d74bb11d0c6f4cd1090e3efc.pdf)
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
  * user and groups
    * create "admin" user (user is parallel with project)
    ```
    openstack user create --domain default --password-prompt admin
    ```
    * users and groups can be referred as actors.
  * relationship between project and user
    * Projects were originally referred to as Tenants.
    * It is probably fair to say that the most fundamental purpose of Keystone is to be the **registry of Projects and to be able to articulate who should have access to those Projects**. 
    * users and projects are separate so that one user can be assigned to access more than one projects, and one project can have more than one users and each user can have different role (e.g. owner, writer, reader). e.g. 
      * Google project and google gmail users. 
* role
  * can create a role and add to project and user. role can be separate from domain
  * "Roles are used in Keystone to convey a sense of Authorization. An actor may have numerous roles on a target."
  * "A role assignment is a ternary (or triple): the combination of an actor, a target, and a role". "For example, the role of admin is “assigned to” the user “bob” and it is “assigned on” the project “development.”"
  * actors
    * "We refer to Users and Groups as Actors since, when assigning a role, these are the entities to which the role is “assigned to.”"
  * targets
    * "Projects and Domains are very similar in that both are entities where the role is “assigned on.” In other words, a User or User Group is given access to either a Project or Domain by assigning a particular Role value for that User or User Group for a specific Project or Domain. Because Projects and Domains have such similar characteristics, when we need to refer to both entities collectively we refer to them as Targets."
  
# Ironic

## Architecture
* https://docs.openstack.org/ironic/latest/user/
  * use Nova API, message queue and database
* https://docs.openstack.org/ironic/latest/contributor/architecture.html
