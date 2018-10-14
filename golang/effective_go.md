# Effective Go
## names/naming
### interface and struct names
* plus an -er suffix
* example
  * kubernetes cache
    * type ListerWatcher interface, type ListWatch struct 
    * https://github.com/kubernetes/client-go/blob/master/tools/cache/listwatch.go
 * kubernetes informer
   * https://github.com/kubernetes/client-go/blob/master/informers/apps/v1/deployment.go
   * interface and struct has the same name, but export inteface only
     * type DeploymentInformer interface {
     * type deploymentInformer struct {
