# Custom Resources

## What
* https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/

On their own, custom resources simply let you store and retrieve structured data. When you combine a custom resource with a custom controller, custom resources provide a true declarative API.

A declarative API allows you to declare or specify the desired state of your resource and tries keep the current state of Kubernetes objects in sync with the desired state. The controller interprets the structured data as a record of the user’s desired state, and continually maintains this state.

You can deploy and update a custom controller on a running cluster, independently of the cluster’s own lifecycle. Custom controllers can work with any kind of resource, but they are especially effective when combined with custom resources. The Operator pattern combines custom resources and custom controllers. You can use custom controllers to encode domain knowledge for specific applications into an extension of the Kubernetes API.

## CRD - CustomResourceDefinitions
* https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/

```bash
# both plural or singular works on kubectl
kubectl --insecure-skip-tls-verify=true --server https://<> --username admin --password <>  get crontabs --all-namespaces
kubectl --insecure-skip-tls-verify=true --server https://<> --username admin --password <>  get crontab --all-namespaces
No resources found.

# for wrong resource type
kubectl --insecure-skip-tls-verify=true --server https://<> --username admin --password <>  get crontabsss --all-namespaces
the server doesn't have a resource type "crontabsss"

```

## AA - Agregated API
