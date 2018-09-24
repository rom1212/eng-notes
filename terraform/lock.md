# backend lock
## 

## GCS
* tried to create a lock file (default.lock). The operation fails [if the file already exists](https://github.com/hashicorp/terraform/blob/27b720113ed5143a870ec151b3b7c9d955a09bc0/backend/remote-state/gcs/client.go#L93).
  ```go
  w := lockFile.If(storage.Conditions{DoesNotExist: true}).NewWriter(c.storageContext)
  ```
