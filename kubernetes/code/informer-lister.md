# Informer
## Deployment informer
* https://github.com/kubernetes/client-go/blob/master/informers/apps/v1/deployment.go, specifies
  * ListFunc: what to list and options
    * client.AppsV1().Deployments(namespace).List(options)
  * WatchFunc: what to watch and options
    * client.AppsV1().Deployments(namespace).Watch(options)
* It also returns the lister
* DeploymentController uses informer to create, but uses the Lister from informer internally.
 * https://github.com/kubernetes/kubernetes/blob/master/pkg/controller/deployment/deployment_controller.go
 
* interface and struct
  * type DeploymentInformer interface {
  * type deploymentInformer struct {

## Lister
# Deployment Lister
* Lister is used by informer
* https://github.com/kubernetes/client-go/blob/master/listers/apps/v1/deployment.go
