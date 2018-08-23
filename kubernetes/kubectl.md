# kubctl command
## Normal Usage

```
kubectl config view
kubectl cluster-info
kubectl get pods --all-namespaces
```

## kubectl config
```
```

## kubectl
```
kubectl --cluster <> --username <e.g. admin> --password <> get pods --all-namespaces

# can use to skip https check: --insecure-skip-tls-verify=true
```

# kubectl code
## Apply
* https://github.com/kubernetes/kubernetes/blob/master/pkg/kubectl/cmd/apply.go
