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

Use template: contrib/preseeds_v2/enlist
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
* EnlistUserDataHandler:read()

Use template: contrib/preseeds_v2/enlist_userdata, which also include in src/metadataserver/user_data/templates/snippets/, e.g.
```
#cloud-config

rsyslog:
   remotes:
     maas: "172.23.48.5:514"

power_state:
   delay: now
   mode: poweroff
   timeout: 1800
   condition: test ! -e /tmp/block-poweroff

misc_bucket:
 - &maas_enlist |
   # Bring up all interfaces. 
   ...
   add_bin "maas-ipmi-autodetect-tool" <<"END_MAAS_IPMI_AUTODETECT_TOOL"
   ...
```
More details: [enlist_userdata_example](https://github.com/romans1212notes/eng-notes/blob/master/maas/enlist_userdata_example)

## commissioning
* tftp.py->kernel_opts.py:compose_purpose_opts-kernel_params()
```
['iscsi_target_name=iqn.2004-05.com.ubuntu:maas:ephemeral-ubuntu-amd64-generic-xenial-daily', 
 'iscsi_target_ip=xxx.xx.xx.x', 
 'iscsi_target_port=3260', 
 'iscsi_initiator=caring-eagle', 
 'ip=::::caring-eagle:BOOTIF', 
 'ip6=off', 
 'ro root=/dev/disk/by-path/ip-xxx.xx.xx.x:3260-iscsi-iqn.2004-05.com.ubuntu:maas:ephemeral-ubuntu-amd64-generic-xenial-daily-lun-1', 
 'overlayroot=tmpfs', 
 'overlayroot_cfgdisk=disabled', 
 "cc:{'datasource_list': ['MAAS']}end_cc", 
 'cloud-config-url=http://xxx.xx.xx.x:5240/MAAS/metadata/latest/by-id/t76377/?op=get_preseed', 
 'apparmor=0']
```
* AnonMetaDataHandler:get_preseed()

Use template: contrib/preseeds_v2/commissioning, which simply use {{preseed_data}} from code, which is generated by ```compose_preseed.py:_compose_cloud_init_preseed()```
```
#cloud-config
apt:
  preserve_sources_list: false
  primary:
  - arches: [default]
    uri: http://archive.ubuntu.com/ubuntu
  proxy: http://yy.yyy.yy.yyy:3128
  security:
  - arches: [default]
    uri: http://archive.ubuntu.com/ubuntu
apt_proxy: http://yy.yyy.yy.yyy:3128
datasource:
  MAAS: {
    consumer_key: NchejBNxtCFJFvmKaW,
    metadata_url: 'http://xxx.xx.xx.x:5240/MAAS/metadata/',
    token_key: qRTZ3Y8EmqZyENrPPf,
    token_secret: QRwpSAyE2PgHEYERkPX2Usw6gJpfpFPN}
manage_etc_hosts: true
power_state: {
  condition: test ! -e /tmp/block-poweroff,
  delay: now,
  mode: poweroff,
  timeout: 3600}
reporting:
  maas: {
    consumer_key: NchejBNxtCFJFvmKaW,
    endpoint: 'http://xxx.xx.xx.x:5240/MAAS/metadata/status/t76377',
    token_key: qRTZ3Y8EmqZyENrPPf,
    token_secret: QRwpSAyE2PgHEYERkPX2Usw6gJpfpFPN,
    type: webhook}
rsyslog:
  remotes: {maas: 'xxx.xx.xx.x:514'}
system_info:
  package_mirrors:
  - arches: [i386, amd64]
    failsafe: {primary: 'http://archive.ubuntu.com/ubuntu', security: 'http://security.ubuntu.com/ubuntu'}
    search:
      primary: ['http://archive.ubuntu.com/ubuntu']
      security: ['http://archive.ubuntu.com/ubuntu']
  - arches: [default]
    failsafe: {primary: 'http://ports.ubuntu.com/ubuntu-ports', security: 'http://ports.ubuntu.com/ubuntu-ports'}
    search:
      primary: ['http://ports.ubuntu.com/ubuntu-ports']
      security: ['http://ports.ubuntu.com/ubuntu-ports'
```
* UserDataHandler:read()

It reads from  NodeUserData by NodeUserData.objects.get_user_data(node), which is written by 
```
maasserver/models/node.py:start_commissioning()
  commissioning_user_data = generate_user_data_for_status(
            node=self, status=NODE_STATUS.COMMISSIONING)
    metadataserver/user_data/__init__.py:generate_user_data_for_status
      read templates from metadataserver/user_data/templates/
          commissioning.template  disk_erasing.template  poweroff.template  rescue_mode.template testing.template
  _start(commissioning_user_data)
    NodeUserData.objects.set_user_data(self, commissioning_user_data)
```
Basically, user data is from metadataserver/user_data/templates/commissioning.template, which also include in src/metadataserver/user_data/templates/snippets/

* MAASScriptsHandler
```NODE_INFO_SCRIPTS```
