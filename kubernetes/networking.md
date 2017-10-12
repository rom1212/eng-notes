# Flannel
## Flannel Diagram
http://chuckbutler.github.io/flannel-docker-charm/user/getting-started.html
[Flannel Diagram](http://chuckbutler.github.io/flannel-docker-charm/images/flannel-topology.png)

## How it works
* flanneld
  * check existing registered subnets in etcd
  * register one subnet for each host in etcd
    * it's a mapping between subnet to host, key is subnet, and value is host
  * when routing
    * look up from etcd (mostly in cached since it is using watch for subnets changes) to find out which host to pass the packet to
    * use UDP to send out the packets to the dst host
    * on that host, flanneld decode the packet, and pass it to a given container interface.
* docs
  * https://coreos.com/blog/introducing-rudder.html

# Docs
https://kubernetes.io/docs/concepts/cluster-administration/networking/

## Hack
https://thenewstack.io/hackers-guide-kubernetes-networking/

http://man7.org/linux/man-pages/man1/nsenter.1.html
