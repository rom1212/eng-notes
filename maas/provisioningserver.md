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

## rackdservices/tftp.py
* TFTPBackend
```
    Static files such as kernels and initrds, as well as any non-MAAS files
    that the system may already be set up to serve, are served up normally.
    But PXE configurations are generated on the fly.
```

* get_boot_method_reader

## How it get started
* Create a plugin for Twisted - provisioningserver/plugin.py
  * @implementer(IServiceMaker, IPlugin)
  * class ProvisioningServiceMaker
    * makeService -> _makeServices
      * _makeTFTPService
        * rackdservices/tftp.py: TFTPService -> TFTPBackend
      * _makeImageDownloadService
        * class ImageDownloadService(TimerService, object)
          * super(ImageDownloadService, self).__init__(self.check_interval, self.try_download)
            * maybe_start_download -> _start_download 
              * boot_images.py: import_boot_images() -> _run_import() -> boot_resources.import_images()

# Files
## /var/lib/maas/boot-resources/
```
* cache  current  snapshot-20170923-141239
* current -> snapshot-20170923-141239
* snapshot-20170923-141239
  * bootppc64.bin->bootloader/open-firmware/ppc64el/bootppc64.bin
  * bootx64.efi->bootloader/uefi/amd64/bootx64.efi
  * chain.c32->bootloader/pxe/i386/chain.c32
  * grub
  * grubaa64.efi->bootloader/uefi/arm64/grubaa64.efi
  * grubx64.efi->bootloader/uefi/amd64/grubx64.efi
  * ifcpu64.c32->bootloader/pxe/i386/ifcpu64.c32
  * ldlinux.c32->bootloader/pxe/i386/ldlinux.c32
  * libcom32.c32->bootloader/pxe/i386/libcom32.c32
  * libutil.c32->bootloader/pxe/i386/libutil.c32
  * maas.meta
  * maas.tgt
  * pxelinux.0->bootloader/pxe/i386/pxelinux.0
  * syslinux->bootloader/pxe/i386
  * ubuntu
    * amd64/generic/xenial/daily/
      * boot-initrd  boot-kernel  squashfs
```
