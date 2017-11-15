# Docs
* [Self-Hosted Kubernetes](https://www.youtube.com/watch?v=tXyV3IQ8-0k), 2016-08-05, Aaron Levy
* [KubeCeption! A Story of Self-Hosted Kubernetes by Aaron Levy, CoreOS, Inc.](https://www.youtube.com/watch?v=EbNxGK9MwN4), 2016-11-16, KubeCon 2016, Seattle
  * commands
    * kubectl get deployments
    ```
                             DESIRED
    kube-controller-manager    2
    kube-scheduler             2 
    ```
    * kubectl get daemonsets
    * kubectl get secrets
  * why self-host
    * vastly simplify Node bootstrap
    * vastly simplify life cycle management
  * On host requirements - all nodes
    * install kubelet
    * install container runtime
    * write kubeconfig
    * start kubelet: systemctl start kubelet
  * master nodes
    * Add a label to nodes you want to run "master" workloads
      * kubectl label node n1 master=true
    * Or have the kubelet start as a master
      * --node-labels=master=true
  * Simplify Node Bootstrap
    * Minimal and universal on-host configuration
    * Use your favorite tools for adding compute
    * Let Kubernetes manage the rest
  * Simplify Kubenetes Lifecycle Management
    * Minimize writing external software that manages Kubernetes
      * invevitably end up with less portable & more fragile solutions
    * Instead our tools should stand on the shoulders of Kubernetes
