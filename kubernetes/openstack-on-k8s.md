
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
