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

# example from GKE
gcloud container clusters get-credentials <cluster name> --zone us-east4-b --project <proejct name>
kubectl get pods --context gke_<project name>_us-east4-b_<cluster name> --all-namespaces

NAMESPACE     NAME                                              READY     STATUS    RESTARTS   AGE
default       <cluster name>-0                                           1/1       Running   0          12m
default       <cluster name>-1                                           1/1       Running   0          12m
default       <cluster name>-2                                           1/1       Running   0          12m
kube-system   event-exporter-v0.1.9-5c8fb98cdb-qfnsx            2/2       Running   0          15m
kube-system   fluentd-gcp-v2.0.17-7gk6p                         2/2       Running   0          14m
kube-system   fluentd-gcp-v2.0.17-j2pjx                         2/2       Running   0          14m
kube-system   fluentd-gcp-v2.0.17-kqk2k                         2/2       Running   0          14m
kube-system   heapster-v1.5.2-7567ff878d-4t8w6                  3/3       Running   0          14m
kube-system   kube-dns-5dcfcbf5fb-4nzhl                         4/4       Running   0          15m
kube-system   kube-dns-5dcfcbf5fb-kttch                         4/4       Running   0          14m
kube-system   kube-dns-autoscaler-69c5cbdcdd-xhxgp              1/1       Running   0          15m
kube-system   kube-proxy-gke-redis-default-pool-99ec7817-32rs   1/1       Running   0          14m
kube-system   kube-proxy-gke-redis-default-pool-99ec7817-b3fl   1/1       Running   0          14m
kube-system   kube-proxy-gke-redis-default-pool-99ec7817-g0qw   1/1       Running   0          14m
kube-system   kubernetes-dashboard-6c475c4864-rjmd6             1/1       Running   0          15m
kube-system   l7-default-backend-57856c5f55-zcpq7               1/1       Running   0          15m
kube-system   metrics-server-v0.2.1-7f8dd98c8f-9h4gd            2/2       Running   0          14m
```

# kubectl code
## Apply
* https://github.com/kubernetes/kubernetes/blob/master/pkg/kubectl/cmd/apply.go
