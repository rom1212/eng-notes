# kubctl command
## Normal Usage

```
kubectl config view
kubectl cluster-info
kubectl get pods --all-namespaces
kubectl get pods -o json
# get credential from GKE
gcloud container clusters get-credentials --zone <zone, might use --region> --project <project name> <cluster name>

kubectl get ns --show-labels
```

## kubectl get
* output formats: https://gist.github.com/so0k/42313dbb3b547a0f51a547bb968696ba
* jsonpath
* go-template
  * basic: https://blog.gopheracademy.com/advent-2017/using-go-templates/
  * newline: https://medium.com/@hank.jacobs/kubectl-printing-newlines-when-using-go-template-output-cce67a0cfe46

## kubectl config
```
kubectl config set clusters.<cluster name>.certificate-authority-data <certificate string>

kubectl config set users.<user name>.client-certificate-data <certificate string>
kubectl config set users.<user name>.client-key-data <certificate string>
```

## kubectl apply
```
kubectl --cluster <> --username <e.g. admin> --password <> get pods --all-namespaces

# can use to skip https check: --insecure-skip-tls-verify=true
kubectl --insecure-skip-tls-verify=true --server https:// --username --password  get pods --all-namespaces

# example from GKE
gcloud container clusters get-credentials <cluster name> --zone us-east4-b --project <proejct name>
kubectl get pods --context gke_<project name>_us-east4-b_<cluster name> --all-namespaces

NAMESPACE     NAME                                              READY     STATUS    RESTARTS   AGE
default       <cluster name>-0                                  1/1       Running   0          12m
default       <cluster name>-1                                  1/1       Running   0          12m
default       <cluster name>-2                                  1/1       Running   0          12m
kube-system   event-exporter-v0.1.9-5c8fb98cdb-qfnsx            2/2       Running   0          15m
kube-system   fluentd-gcp-v2.0.17-7gk6p                         2/2       Running   0          14m
kube-system   fluentd-gcp-v2.0.17-j2pjx                         2/2       Running   0          14m
kube-system   fluentd-gcp-v2.0.17-kqk2k                         2/2       Running   0          14m
kube-system   heapster-v1.5.2-7567ff878d-4t8w6                  3/3       Running   0          14m
kube-system   kube-dns-5dcfcbf5fb-4nzhl                         4/4       Running   0          15m
kube-system   kube-dns-5dcfcbf5fb-kttch                         4/4       Running   0          14m
kube-system   kube-dns-autoscaler-69c5cbdcdd-xhxgp              1/1       Running   0          15m
kube-system   kube-proxy-gke-<cnm>-default-pool-99ec7817-32rs   1/1       Running   0          14m
kube-system   kube-proxy-gke-<cnm>-default-pool-99ec7817-b3fl   1/1       Running   0          14m
kube-system   kube-proxy-gke-<cnm>-default-pool-99ec7817-g0qw   1/1       Running   0          14m
kube-system   kubernetes-dashboard-6c475c4864-rjmd6             1/1       Running   0          15m
kube-system   l7-default-backend-57856c5f55-zcpq7               1/1       Running   0          15m
kube-system   metrics-server-v0.2.1-7f8dd98c8f-9h4gd            2/2       Running   0          14m
# cnm = cluster name
```

```
kubectl apply -f <file name, or - which mean stdin>

https://stackoverflow.com/questions/46238571/explain-the-last-dash-in-a-bash-pipe-expression
```
## kubectl apply --prune
* https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply
* https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/#in-place-updates-of-resources
* ```kubectl apply attaches an annotation to the resource in order to determine the changes to the configuration since the previous invocation```

## kubectl apply vs create
* https://kubernetes.io/docs/concepts/overview/object-management-kubectl/overview/
* https://stackoverflow.com/questions/47369351/kubectl-apply-vs-kubectl-create
* How to delete what's created by kubectl apply
* manage deployment
  * https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
  * https://kubernetes.io/docs/concepts/configuration/overview/

## kubectl explain
```shell
kubectl explain deployment --recursive
```

# kubectl code
## Apply
* https://github.com/kubernetes/kubernetes/blob/master/pkg/kubectl/cmd/apply.go

## kubectl cmd examples
From https://github.com/coreos/tectonic-installer/issues/2945
```
$ kubectl --namespace kube-system get pod

NAME                                                                    READY     STATUS    RESTARTS   AGE
kube-apiserver-9kwj9                                                    1/1       Running   0          7d
kube-controller-manager-5b65d64c97-hkkxk                                0/1       Pending   0          14h
kube-dns-64cd9cc494-d9hdp                                               0/3       Pending   0          14h
kube-flannel-2mhqh                                                      2/2       Running   0          7d
kube-flannel-4d6s6                                                      2/2       Running   1          7d
kube-flannel-gb4ph                                                      2/2       Running   0          7d
kube-flannel-w5xfq                                                      2/2       Running   1          7d
kube-proxy-hsx5w                                                        1/1       Running   0          7d
kube-proxy-pq6mz                                                        1/1       Running   0          7d
kube-proxy-s9x2p                                                        1/1       Running   0          7d
kube-proxy-vkwv7                                                        1/1       Running   0          7d
kube-scheduler-7b675dc9f7-9s7hb                                         0/1       Pending   0          14h
pod-checkpointer-mjpz9                                                  1/1       Running   0          7d
pod-checkpointer-mjpz9-ip-10-17-1-125.ap-northeast-1.compute.internal   1/1       Running   0          7d
tiller-deploy-7dcdcd5f64-5pt8z                                          1/1       Running   0          14h

$ kubectl --namespace kube-system get deployment              
NAME                      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
kube-controller-manager   1         1         1            0           8d
kube-dns                  1         1         1            0           8d
kube-scheduler            1         1         1            0           8d
```
