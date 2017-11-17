# Setup
## Doc
https://docs.openstack.org/kolla-kubernetes/latest/deployment-guide.html

## Steps
* kubelet is not starting
  * file /etc/systemd/system/kubelet.service.d/10-kubeadm.conf:
    * ExecStart=/usr/bin/kubelet --fail-swap-on=false
* kubeadm init --pod-network-cidr=10.1.0.0/16 --service-cidr=10.3.3.0/24
