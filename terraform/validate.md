# check-variables or not
* https://github.com/hashicorp/terraform/issues/21408
```
Indeed, the documentation is missing a note to say that -check-variables=false applies only to Terraform v0.11 and earlier.

The option is removed from Terraform v0.12 because terraform validate now always behaves as if this were false:
```
* for tf 0.11 and earlier:
```
terraform validate -check-variables=false
```

