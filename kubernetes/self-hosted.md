# Docs
* [Self-Hosted Kubernetes](https://www.youtube.com/watch?v=tXyV3IQ8-0k), 2016-08-05, Aaron Levy
* [KubeCeption! A Story of Self-Hosted Kubernetes by Aaron Levy, CoreOS, Inc.](https://www.youtube.com/watch?v=EbNxGK9MwN4), 2016-11-16, KubeCon 2016, Seattle
  * commands
    * kubectl get deployments
    * kubectl get daemonsets
    * kubectl get
  * why self-host
    * vastly simplify Node bootstrap
    * vastly simplify life cycle management
  * On host requirements
    * install kubelet
    * install container runtime
    * write kubeconfig
    * start kubelet: systemctl start kubelet
