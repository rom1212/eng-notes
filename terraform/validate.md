# Run
* requires to run "terraform init" first (for tf 0.12)

# check-variables (option for 0.11, default for 0.12)
* https://github.com/hashicorp/terraform/issues/21408
```
Indeed, the documentation is missing a note to say that -check-variables=false applies only to Terraform v0.11 and earlier.

The option is removed from Terraform v0.12 because terraform validate now always behaves as if this were false:
```
* for tf 0.11 and earlier:
```
terraform validate -check-variables=false
```

# validate doesn't catch all errors
* source_ranges
For tf 0.12
```
data "google_compute_lb_ip_ranges" "ranges" {}

resource "google_compute_firewall" "xxx" {
  source_ranges = ["${data.google_compute_lb_ip_ranges.ranges.network}"]
}
```

This can pass "terraform validate", but when running "terraform apply" or "terraform apply", it fails with error
```
Inappropriate value for attribute "source_ranges": element 0: string required.
```

The fix is
```
  source_ranges = "${data.google_compute_lb_ip_ranges.ranges.network}"
```  
