# Terraform Provider

## Docs
* https://www.terraform.io/docs/plugins/provider.html
* https://www.terraform.io/docs/extend/writing-custom-providers.html

## Provider Example from users perspective
* https://www.terraform.io/intro/getting-started/build.html

"The provider block is used to configure the named provider, in our case "aws". A provider is responsible for creating and managing resources. Multiple provider blocks can exist if a Terraform configuration is composed of multiple providers, which is a common situation."

## Helper lib to write provider
* https://godoc.org/github.com/hashicorp/terraform/helper/schema
* How to write a provider
  * create resources, using schema.Resource
  * use those resources in the schema.Provider
  * use the new resource in .tf file.

## Provider from developer perspective
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

## Resource
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
