# Terraform Provider

## Docs
* https://www.terraform.io/docs/plugins/provider.html
* https://www.terraform.io/docs/extend/writing-custom-providers.html
* https://www.terraform.io/docs/extend/schemas/
  * Can be used for provider schema and resource schema. 
  * https://www.terraform.io/docs/extend/schemas/schema-behaviors.html
    * Default, and DefaultFunc
## Examples
* https://github.com/terraform-providers/terraform-provider-google/blob/master/google/provider.go

## Provider Example from users perspective
* https://www.terraform.io/intro/getting-started/build.html

"The provider block is used to configure the named provider, in our case "aws". A provider is responsible for creating and managing resources. Multiple provider blocks can exist if a Terraform configuration is composed of multiple providers, which is a common situation."
```go
provider "aws" {
  access_key = "ACCESS_KEY_HERE"
  secret_key = "SECRET_KEY_HERE"
  region     = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-2757f631"
  instance_type = "t2.micro"
}
```

## Helper lib to write provider
* https://godoc.org/github.com/hashicorp/terraform/helper/schema
* How to write a provider
  * create resources, using schema.Resource
  * use those resources in the schema.Provider
  * use the new resource in .tf file.

### Step 1 - Create Resource
* "As a general convention, Terraform providers put each resource in their own file, 
named after the resource, prefixed with resource_. To create an example_server, 
this would be resource_server.go by convention"
* User: https://godoc.org/github.com/hashicorp/terraform/helper/schema#Resource
  ```go
  Schema map[string]*schema.Schema // name might better be Schemas, since it is actually a collection of Schemas
  Create CreateFunc
  Read   ReadFunc
  Update UpdateFunc
  Delete DeleteFunc
  Exists ExistsFunc
  ```
  Example
  ```
  func resourceServer() *schema.Resource {
        return &schema.Resource{
                Create: resourceServerCreate,
                Read:   resourceServerRead,
                Update: resourceServerUpdate,
                Delete: resourceServerDelete,

                Schema: map[string]*schema.Schema{
                        "address": &schema.Schema{
                                Type:     schema.TypeString,
                                Required: true,
                        },
                },
        }
  }
  ```

### Step 2 - Create Provider
Provider contains a collection of resources by ResourcesMap.
```go
func Provider() *schema.Provider {
        return &schema.Provider{
                ResourcesMap: map[string]*schema.Resource{
                        "example_server": resourceServer(),
                },
        }
}
```


### Step 3 - Use New Provider and Resource in tf file
```
// Do I have to have "provider" section???
provider "my-provider" {
}

resource "example_server" "my-server" {}
```

## Logging
### Examples
https://github.com/terraform-providers/terraform-provider-google/blob/master/google/resource_container_cluster.go#L687
```go
log.Println("[DEBUG] updating enable_legacy_abac")
log.Printf("[INFO] GKE cluster %s legacy ABAC has been updated to %v", d.Id(), enabled)
```

However, terraform seems only use DEBUG level to print out providers log, e.g.
```
[DEBUG] plugin.terraform-provider-google: 2018/xx/xx xx:xx:xx [INFO] GKE cluster redis has been created
```

## Debugging
* export TF_LOG=DEBUG

## Testing
* Acceptance test
  * example: TF_ACC=1 go test $(TEST) -v $(TESTARGS) -timeout 120m
  * https://github.com/hashicorp/terraform/blob/master/Makefile
  * https://www.terraform.io/docs/extend/testing/acceptance-tests/index.html
* Unittest with Acceptance test framework
  * Instead of using resource.Test, use resource.Unittest. And then use replace the client code which talks to the network/cloud provider. 
  * Looks that it doesn't compile provider into binary and run the binary in the test. However, it just calls the library to talk to the provider.  
  * test for error: 
    * use ExpectError, https://www.terraform.io/docs/extend/best-practices/testing.html#expecting-errors-or-non-empty-plans
    * this applies to the Acceptance test above

## Tricky
* Schema
  * Required: true
    * it doens't mean that we need to specify it in the tf file, as long as it has DefaultFunc.
  * Cannot use "Required: false", must use "Optional: true", not verified.
