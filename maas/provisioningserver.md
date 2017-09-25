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
  * link_bootloaders(snapshot_path)
    * link_bootloader(destination=snapshot_path)
      * ```boot/__init__.py```
        * stream_path = os.path.join(destination, 'bootloader', self.bios_boot_method, arch)
          * /var/lib/maas/boot-resources/snapshot-20170923-141239/bootloader/pxe/i386/
        * self._link_simplestream_bootloaders(stream_path, destination)
          * put bootloader files in the root of the snapshot_path, i.e. directly under snapshot_path/
          * _link_simplestream_bootloaders()
            * /boot/pxe.py also has this method, and also add syslinux
            * TTT??? where are the other files? _find_and_copy_bootloaders???
    * ??? /var/lib/maas/boot-resources/snapshot-20170923-141239/ubuntu/amd64/generic/xenial/daily/
  * update_iscsi_targets(snapshot_path)
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
