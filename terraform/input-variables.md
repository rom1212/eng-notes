# input variables
## docs
* https://www.terraform.io/docs/configuration/variables.html

## Variable Precedence
From low to high
* TF_VAR_ environment variables
* terraform.tfvars or *.auto.tfvars
* -var-file or -var
  * these two are the same precedence, and the latter ones can override previous ones, except for maps
