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
