# Persistent Disk/Block Storage

## What's the max number limit? 
* Amazon
  * "how many ebs volumes per instance", [volume limits](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html)
  * Linux - 40
  * Bandwidth vs Capacity: "For consistent and predictable bandwidth use cases, use EBS-optimized or 10 Gigabit network connectivity instances and General Purpose SSD or Provisioned IOPS SSD volumes. "
* Google
  * "compute engine max number of persistent disks"
  * [pdlimits](https://cloud.google.com/compute/docs/disks/#pdlimits): "Attaching more than 16 persistent disks is available as a Beta feature. You can attach up to 128 persistent disks to instances with predefined machine types depending on the number of vCPUs in that instance."
# Azure
  * http://windowsitpro.com/windows-azure/maximum-number-data-disks-azure-iaas-vm
    * 16
