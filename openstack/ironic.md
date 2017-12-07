# Repos

## ironic
* https://github.com/openstack/ironic
* deploy_utils.py
  * search "ironic use dd command"
  * https://bugs.launchpad.net/ironic/+bug/1417928
  * https://review.openstack.org/#/c/152734/4/ironic/drivers/modules/deploy_utils.py
  * find 
    * deploy_partition_image
      * https://github.com/openstack/ironic/blob/bbb58672ab95c840b2a0f03853bd596f8d7143dc/ironic/drivers/modules/deploy_utils.py#L337
      * called work_on_disk
    * deploy_disk_image - maybe
      * https://github.com/openstack/ironic/blob/bbb58672ab95c840b2a0f03853bd596f8d7143dc/ironic/drivers/modules/deploy_utils.py#L393
      * called populate_image

## ironic-lib
* https://github.com/openstack/ironic-lib/blob/master/ironic_lib/disk_utils.py, 
  * dd
  * work_on_disk: https://github.com/openstack/ironic-lib/blob/master/ironic_lib/disk_utils.py#L445
  * populate_image: dd(src, dst)

## ironic-python-agent
* https://github.com/openstack/ironic-python-agent
