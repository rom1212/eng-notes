# Helm
## Docs
* quick start: https://docs.helm.sh/using_helm/#quickstart

## Code
* helm init
  * installs Tiller
    * https://github.com/helm/helm/blob/master/cmd/helm/installer/install.go
      * createDeployment
      * createService
      * createSecret
* helm rollback
  * https://github.com/helm/helm/blob/master/cmd/helm/rollback.go
    * talks to Tiller to do the rollback
  * https://github.com/helm/helm/blob/master/pkg/tiller/release_modules.go
    * Rollback() and Update() here is the same 
      * https://github.com/helm/helm/blob/master/pkg/kube/client.go
        * Update()
