# logs
## log01.kernel-opts - enlist
cloud-config-url=http://xx.xx.xx.xx:5240/MAAS/metadata/latest/enlist-preseed/?op=get_enlist_preseed
* should -> AnonMetaDataHandler.get_enlist_preseed -> preseed.py:render_enlistment_preseed,
  * get_preseed_context: metadata_enlist_url=absolute_reverse('enlist', base_url=base_url)
## log02.kernel-opts - commissioning
cloud-config-url=http://xx.xx.xx.xx:5240/MAAS/metadata/latest/by-id/fycnr3/?op=get_preseed
```
Sep 28 11:37:11 kernel_opts.py-compose_purpose_opts-kernel_params: 
['iscsi_target_name=iqn.2004-05.com.ubuntu:maas:ephemeral-ubuntu-amd64-generic-xenial-daily',
 'iscsi_target_ip=xx.xx.xx.xx',
 'iscsi_target_port=3260',
 'iscsi_initiator=alert-ant',
 'ip=::::alert-ant:BOOTIF',
 'ip6=off',
 'ro root=/dev/disk/by-path/ip-xx.xx.xx.xx:3260-iscsi-iqn.2004-05.com.ubuntu:maas:ephemeral-ubuntu-amd64-generic-xenial-daily-lun-1',
 'overlayroot=tmpfs',
 'overlayroot_cfgdisk=disabled',
 "cc:{'datasource_list': ['MAAS']}end_cc",
 'cloud-config-url=http://xx.xx.xx.xx:5240/MAAS/metadata/latest/by-id/fycnr3/?op=get_preseed',
 'apparmor=0'
```

## log06.kernel-opts - deploy/curtin
same cloud-config-url as commissioning, but different image: iscsi_target_name and "ro root"
```
Sep 28 11:53:23 kernel_opts.py-compose_purpose_opts-kernel_params: 
['iscsi_target_name=iqn.2004-05.com.ubuntu:maas:ephemeral-ubuntu-amd64-ga-16.04-xenial-daily',
 'iscsi_target_ip=xx.xx.xx.xx',
 'iscsi_target_port=3260',
 'iscsi_initiator=alert-ant',
 'ip=::::alert-ant:BOOTIF',
 'ip6=off',
 'ro root=/dev/disk/by-path/ip-xx.xx.xx.xx:3260-iscsi-iqn.2004-05.com.ubuntu:maas:ephemeral-ubuntu-amd64-ga-16.04-xenial-daily-lun-1',
 'overlayroot=tmpfs',
 'overlayroot_cfgdisk=disabled',
 "cc:{'datasource_list': ['MAAS']}end_cc",
 'cloud-config-url=http://xx.xx.xx.xx:5240/MAAS/metadata/latest/by-id/fycnr3/?op=get_preseed',
 'apparmor=0'
```
