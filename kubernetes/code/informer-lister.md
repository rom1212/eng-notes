# Informer
## deployment informer
* https://github.com/kubernetes/client-go/blob/master/informers/apps/v1/deployment.go, specifies
  * ListFunc: what to list and options
    * client.AppsV1().Deployments(namespace).List(options)
  * WatchFunc: what to watch and options
    * client.AppsV1().Deployments(namespace).Watch(options)

# Lister
Lister is used by informer
