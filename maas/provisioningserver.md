# src/provisioningserver/
## service_monitor.py
```
service_monitor = ServiceMonitor(
    DHCPv4Service(),
    DHCPv6Service(),
    NTPServiceOnRack(),
    TGTService(),
)
```
* tgt
  * https://linux.die.net/man/8/tgt-admin
  * https://linux.die.net/man/8/tgtadm
  * tgtd, tgtimg, tgt-setup-lun
  * /etc/tgt/conf.d/maas.conf
```
<target iqn.2004-05.com.ubuntu:maas:ephemeral-ubuntu-arm64-xgene-uboot-xenial-daily>
    readonly 1
    allow-in-use yes
    backing-store "/var/lib/maas/boot-resources/snapshot-20170923-141239/ubuntu/arm64/xgene-uboot/xenial/daily/squashfs"
    driver iscsi
</target>
<target iqn.2004-05.com.ubuntu:maas:ephemeral-ubuntu-arm64-xgene-uboot-mustang-xenial-daily>
    readonly 1
    allow-in-use yes
    backing-store "/var/lib/maas/boot-resources/snapshot-20170923-141239/ubuntu/arm64/xgene-uboot-mustang/xenial/daily/squashfs"
    driver iscsi
</target>
```
  
## import_images/
* boot_resources.py
