# Controller Manager

## binary/main/cmd
* a separate cmd/binary is created for controller manager
  * https://github.com/kubernetes/kubernetes/tree/master/cmd/kube-controller-manager
  * https://github.com/kubernetes/kubernetes/blob/master/cmd/kube-controller-manager/app/controllermanager.go
* there should be one kube-controller-manager pod
  * is it scalable?

## Deployment Controller
* https://github.com/kubernetes/kubernetes/blob/master/pkg/controller/deployment/deployment_controller.go
* DeploymentController uses informer to create, but uses the Lister from informer internally.
* docs
  * https://blog.csdn.net/yan234280533/article/details/78565797

### Deployment informer
* https://github.com/kubernetes/client-go/blob/master/informers/apps/v1/deployment.go, specifies
  * ListFunc: what to list and options
    * client.AppsV1().Deployments(namespace).List(options)
  * WatchFunc: what to watch and options
    * client.AppsV1().Deployments(namespace).Watch(options)
* It also returns the lister
 
* interface and struct
  * type DeploymentInformer interface {
  * type deploymentInformer struct {

### Deployment Lister
* Lister is used by informer
* https://github.com/kubernetes/client-go/blob/master/listers/apps/v1/deployment.go
