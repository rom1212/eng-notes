
# Docs

* Building OpenStack on Kubernetes for Zero Downtime Large-scale Production SaaS
  * https://www.youtube.com/watch?v=EwOC8ZH_8-8
  * Approach
    * Build highly available and reliable Openstack - K8s
      * deployment order - Infrastructure services, 3-node gillera cluster, Load Balancer, RabbitMQ. Not trivial
    * Continuous integration and deployment - Kolla and Openstack Helm
    * Upgrade with ZDT (Zero down time) - Helm. k8s A/B upgrade.
    * Scale to meeting growing demand - K8s
    * Reduce time to create adn apply hot patches - Kolla, Helm
  * Deployment choices - Kolla can generate Ansible and K8s images.
    * Ansible
      * limited support for rolling upgrade or scaling. First cluster is easy.
      * require secrets management solution
      * highly opiionated about deployment
    * Kubernetes
      * more flexible to support future growth and changes.
  * Lessons learned - Openstack on K8s
    * Good - K8s
      * build from source - need to fix with few lines of changes, hot patcheds, cherry pick, security reviewed
      * orchestration tool
      * easy to deploy and upgrade - new container image, and upgrade
      * relatively easy to customize - Kolla and Helm
      * secrets management - K8s already has
      * deploying requires minimal experience - even an intern can do that.
    * Bad
      * Fast evolving technologies - version control is very very important.
      * Openstack Helm still under heavy development
      * Persistent volumen support is improving - stateful services, RabbitMQ, Ceph
      * Limited RBAC support with Helm
    * Ugly
      * Underly/Overly networking
        * K8s already has serveral components, what if one of them goes down.
      * Persistent Volume setup
      * Building Highly available K8s Cluster
        * rack failure
* Baremetal to Running Openstack on Kubernetes in 2 Minutes
  * https://www.youtube.com/watch?v=3hcfesHqhgg
  * headaches
    * deploy - hard
    * managing - monitoring & altering, logging, load balancer, billing
    * scaling
    * healing
    * upgrade - nightmare: config, database migration, availability, 
  * demo
    * kubectl get nodes
    * kolla-kubernetes
      * other options: lubeadm, local-up-cluster.sh, bootkube
    * Helm
    * kubectl -n kolla get pod
  * PXE Boot baremental to Openstack on Kubernetes
    * PXE
    * MatchBox: https://github.com/coreos/matchbox
      * matches machines (based on lables like MAC, UUID etc) to profile for PXE booting and provisioning
    * Kubernetes using BootKube
      * https://github.com/kubernetes-incubator/bootkube
      * self-hosted: run kubernetes on kuberntes itself. can use kubectl to scale API
    * Openstack using Kolla
      * https://github.com/openstack/kolla-kubernetes
      * containerized Openstack on Kubernetes
* OpenStack on Kubernetes- One Year After
  * https://www.youtube.com/watch?v=hiepQrynsig
    
