# input variables
## docs
* https://www.terraform.io/docs/configuration/variables.html

## Variable Precedence
From low to high
* default value during declaration
* TF_VAR_ environment variables
* terraform.tfvars or *.auto.tfvars
* -var-file or -var
  * these two are the same precedence, and the latter ones can override previous ones, except for maps

Code
* command/validate.go
  * https://github.com/hashicorp/terraform/blob/4db963c7429ade49c856ae981b7bea010d09ca37/command/validate.go#L124
  * context
    * https://github.com/hashicorp/terraform/blob/4db963c7429ade49c856ae981b7bea010d09ca37/terraform/context.go#L165
  * meta: 
    * https://github.com/hashicorp/terraform/blob/4db963c7429ade49c856ae981b7bea010d09ca37/command/meta.go#L361
    * https://github.com/hashicorp/terraform/blob/4db963c7429ade49c856ae981b7bea010d09ca37/command/meta.go#L324
