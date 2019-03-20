# Custom Resources

## What
* https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/

On their own, custom resources simply let you store and retrieve structured data. When you combine a custom resource with a custom controller, custom resources provide a true declarative API.

A declarative API allows you to declare or specify the desired state of your resource and tries keep the current state of Kubernetes objects in sync with the desired state. The controller interprets the structured data as a record of the user’s desired state, and continually maintains this state.

You can deploy and update a custom controller on a running cluster, independently of the cluster’s own lifecycle. Custom controllers can work with any kind of resource, but they are especially effective when combined with custom resources. The Operator pattern combines custom resources and custom controllers. You can use custom controllers to encode domain knowledge for specific applications into an extension of the Kubernetes API.

## CRD - CustomResourceDefinitions
* https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/

```bash
# create CRD - "kind: Crontab" is defined under "names"
$ kubectl create -f resourcedefinition.yaml
$ kubectl get crd
```

```
# create crontab - what matters here is "kind: Crontab"
$ kubectl create -f my-crontab.yaml

# plural, singular or shortNames work on kubectl
$ kubectl --insecure-skip-tls-verify=true --server https://<> --username admin --password <>  get crontabs --all-namespaces
$ kubectl --insecure-skip-tls-verify=true --server https://<> --username admin --password <>  get crontab --all-namespaces
$ kubectl --insecure-skip-tls-verify=true --server https://<> --username admin --password <>  get ct --all-namespacesNo resources found.

# for wrong resource type, partial resource names doesn't work, e.g. "get cronta"
$ kubectl --insecure-skip-tls-verify=true --server https://<> --username admin --password <>  get crontabsss --all-namespaces
the server doesn't have a resource type "crontabsss"


$ kubectl --insecure-skip-tls-verify=true --server https://<> --username admin --password <>  get ct --all-namespaces -o yaml
$ kubectl --insecure-skip-tls-verify=true --server https://<> --username admin --password <>  get ct --all-namespaces -o json
```
metadata.generation can be automatically increased by using [status subresource](
https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/#status-subresource)

## CRD and Controller
* Kubernetes controllers
  * https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
  * controller status, e.g. kubectl rollout status
    * https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#deployment-status
    * [Deployment status]( https://github.com/kubernetes/kubernetes/blob/ac16ac7cbe11585a53f70057d05a6212952b5051/pkg/kubectl/rollout_status.go#L60)
    * [DaemonSet status](https://github.com/kubernetes/kubernetes/blob/ac16ac7cbe11585a53f70057d05a6212952b5051/pkg/kubectl/rollout_status.go#L96)
    * [StatefulSet status](https://github.com/kubernetes/kubernetes/blob/ac16ac7cbe11585a53f70057d05a6212952b5051/pkg/kubectl/rollout_status.go#L121)
* Conventions:
  * API conventions
    * https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md
    * API references
      * https://kubernetes.io/docs/reference/kubernetes-api/
      * https://kubernetes.io/docs/reference/
  * Writing Controllers
    * https://github.com/kubernetes/community/blob/master/contributors/devel/sig-api-machinery/controllers.md
* Concepts
  * https://kubernetes.io/docs/concepts/
  * API Resource
    * StatefulSet was a beta resource.
    * A resource has many objects created under it.
    * resource can also refers to the compute resources.
    * ```kubectl api-resources```: a complete list of supported resources.
  * Object
    * https://kubernetes.io/docs/concepts/#kubernetes-objects
    * An object is under an API resource.
  * kubectl use a different naming - resource is the same as object, resource type is the same as API resource.
    * kubectl apply -h: 
      * Apply a configuration to a resource by filename or stdin. The resource name must be specified.
      * Here it is using "resource" as "object"
      * However, the comment is right for this: 
        * "save-config: If true, the configuration of current object will be saved in its annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future."

## AA - Agregated API
