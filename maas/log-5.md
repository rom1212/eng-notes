# logs

## enlist
* tftp.py->kernel_opts.py:compose_purpose_opts-kernel_params()
```
['iscsi_target_name=iqn.2004-05.com.ubuntu:maas:ephemeral-ubuntu-amd64-generic-xenial-daily', 
 'iscsi_target_ip=xx.xx.xx.xx', 
 'iscsi_target_port=3260', 
 'iscsi_initiator=maas-enlist', 
 'ip=::::maas-enlist:BOOTIF', 
 'ip6=off', 
 'ro root=/dev/disk/by-path/ip-xx.xx.xx.xx::3260-iscsi-iqn.2004-05.com.ubuntu:maas:ephemeral-ubuntu-amd64-generic-xenial-daily-lun-1', 
 'overlayroot=tmpfs', 
 'overlayroot_cfgdisk=disabled', 
 "cc:{'datasource_list': ['MAAS']}end_cc", 
 'cloud-config-url=http://xx.xx.xx.xx:5240/MAAS/metadata/latest/enlist-preseed/?op=get_enlist_preseed', 
 'apparmor=0']
```
* AnonMetaDataHandler:get_enlist_preseed()
```
#cloud-config
datasource:
  MAAS:
    timeout : 50
    max_wait : 120
    # there are no default values for metadata_url or oauth credentials
    # If no credentials are present, non-authed attempts will be made.
    metadata_url: http://xx.xx.xx.xx:5240/MAAS/metadata/enlist

output: {all: '| tee -a /var/log/cloud-init-output.log'
```
