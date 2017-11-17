# Setup
## Doc
https://docs.openstack.org/kolla-kubernetes/latest/deployment-guide.html

## Steps
* kubelet is not starting
  * file /etc/systemd/system/kubelet.service.d/10-kubeadm.conf:
    * ExecStart=/usr/bin/kubelet --fail-swap-on=false 
