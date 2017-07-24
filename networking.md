# VPC, virtual private cloud
## AWS 
* VPC http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html
* "When you create a VPC, you must specify a range of IPv4 addresses, e.g. 10.0.0.0/16". 
  **A VPC spans all the Availability Zones in the region.**
* You can add one or more subnets in each AZ. When you create a subnet, you specify the CIDR block for the subnet,
  which is a subset of the VPC CIDR block. **Each subnet must reside entirely within one AZ and cannot span zones.**
