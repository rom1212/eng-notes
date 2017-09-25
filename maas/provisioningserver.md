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
  * tgt-admin: https://linux.die.net/man/8/tgt-admin
  * tgtadm: https://linux.die.net/man/8/tgtadm
  * tgtd: http://manpages.ubuntu.com/manpages/zesty/man8/tgtd.8.html 
  * tgtimg, tgt-setup-lun
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
  * update_iscsi_targets
  ```
  def update_iscsi_targets(snapshot_path):
    maaslog.info("Updating boot image iSCSI targets.")
    update_targets_conf(snapshot_path)

  def update_targets_conf(snapshot):
    targets_conf = os.path.join(snapshot, 'maas.tgt')
    try: 
            call_and_check(sudo([
            get_path('/usr/sbin/tgt-admin'),
            '--conf', targets_conf,
            '--update', 'ALL',
            ]))
  ```
