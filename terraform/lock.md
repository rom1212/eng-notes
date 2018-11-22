# backend lock
## 

## GCS
* lock: tried to create a lock file (default.lock). The lock operation fails [if the file already exists](https://github.com/hashicorp/terraform/blob/27b720113ed5143a870ec151b3b7c9d955a09bc0/backend/remote-state/gcs/client.go#L93).
  ```go
  w := lockFile.If(storage.Conditions{DoesNotExist: true}).NewWriter(c.storageContext)
  ```
* unlock: check the generation number from lock, and make sure they match.

# general gslock (similar)
* https://github.com/marcacohen/gcslock
* https://cloud.google.com/storage/docs/object-versioning
