# How it works
## Three Phases
* enlist: https://docs.ubuntu.com/maas/2.1/en/nodes-add
  *  maas/contrib/preseeds_v2/enlist_userdata - cloud-init config, maybe for enlistment
* commision: https://docs.ubuntu.com/maas/2.1/en/nodes-commission 
* deploy: https://docs.ubuntu.com/maas/2.1/en/installconfig-nodes-deploy

Within each stage, the first 4 steps are common:
1. DHCP server is contacted
2. kernel and initrd are received over TFTP
3. machine boots
4. initrd mounts a Squashfs image ephemerally over iSCSI

## Tools
* cloud-init: https://cloudinit.readthedocs.io/en/latest/
* curtin for installation

## API
https://docs.ubuntu.com/maas/2.2/en/api

# src/maasserver
##  node_action.py
