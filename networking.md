# VPC, virtual private cloud
## AWS 
### VPC
* VPC http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html
* "When you create a VPC, you must specify a range of IPv4 addresses, e.g. 10.0.0.0/16". 
  **A VPC spans all the Availability Zones in the region.**
* You can add one or more subnets in each AZ. When you create a subnet, you specify the CIDR block for the subnet,
  which is a subset of the VPC CIDR block. **Each subnet must reside entirely within one AZ and cannot span zones.**

### VPC Peering
* http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/Welcome.html
* limitations
  * http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/invalid-peering-configurations.html
  * http://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/vpc-peering-basics.html#vpc-peering-limitations
  
  
# Switch

## Huawei 
### Docs
* Data Center Switches (http://e.huawei.com/us/products/enterprise-networking/switches/data-center-switches)
  * Cloud Engine [CE5800 Seriers](http://e.huawei.com/us/products/enterprise-networking/switches/data-center-switches/ce5800)
  * Cloud Engine [CE6800 Seriers](http://e.huawei.com/us/products/enterprise-networking/switches/data-center-switches/ce6800)
* Configuration for CloudEngine 7800&6800&5800 V100R003C00: http://support.huawei.com/enterprise/en/doc/DOC1000074869
* ZTP (Zero Touch Provisioning): http://support.huawei.com/enterprise/en/doc/DOC1000086918
### Commands
* more similar to Linux, except ?, dir
* ? - help for available commands
* pwd, dir, cd, more,
### Files
* logfile/
* ztp_xxxx.log(.n)

# network discovery
## arp
```
$ /usr/sbin/arp
```

## arp-scan
https://www.blackmoreops.com/2015/12/31/use-arp-scan-to-find-hidden-devices-in-your-network/
```
$ sudo -E apt-get install arp-scan
$ sudo arp-scan --interface=eth0 --localnet
```
* http://www.nta-monitor.com/wiki/index.php/Arp-scan_User_Guide

## others  
* https://serverfault.com/questions/245136/how-to-find-out-mac-addresses-of-all-machines-on-network
* "linux discovery nearby mac address"
* https://superuser.com/questions/750359/check-if-a-dhcp-server-existing-in-my-network-using-bash
