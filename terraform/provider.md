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
  * redis resource 
    * [resource_redis_instance.go](https://github.com/terraform-providers/terraform-provider-google/blob/master/google/resource_redis_instance.go)
    * [resource_redis_instance_test.go](https://github.com/terraform-providers/terraform-provider-google/blob/master/google/resource_redis_instance_test.go)
  * pubsub topic
    * [resource_pubsub_topic.go](https://github.com/terraform-providers/terraform-provider-google/blob/master/google/resource_pubsub_topic.go)
    * [resource_pubsub_topic_test.go](https://github.com/terraform-providers/terraform-provider-google/blob/master/google/resource_pubsub_topic_test.go)
    * [resource_container_cluster.go, and timeout](https://github.com/terraform-providers/terraform-provider-google/blob/1c982355e4405974186f97d1dee75af6a37f3aa9/google/resource_container_cluster.go#L59)
* kubernetes: https://github.com/terraform-providers/terraform-provider-kubernetes/tree/master/kubernetes
  * [resource_kubernetes_service.go](https://github.com/terraform-providers/terraform-provider-kubernetes/blob/master/kubernetes/resource_kubernetes_service.go)

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
* Use: https://godoc.org/github.com/hashicorp/terraform/helper/schema#Resource
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
* when each function is used?
  * terraform plan is according to the resource ID??? not exactly sure.
* when to create a resource? when a resource is added to tf file, e.g.
```
An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  + <resource type>.<resource name>
      id:               <computed>
      <other keys>


Plan: 1 to add, 0 to change, 0 to destroy.

```
* when to delete a resource? when a resource is removed from tf file, e.g. when removing a resource, terraform thinks that "0 to change", and "1 to destroy".
```
An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  - <resource type>.<resource name>

Plan: 0 to add, 0 to change, 1 to destroy.
```
* when to update a resource? when the input parameters change, e.g. one of the input parameter changes, and terraform know that because the input parameters are saved in terraform.tfstate file.
```
An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  ~ <resource type>.<resource name>
      <key>: "old value" => "new value"

Plan: 0 to add, 1 to change, 0 to destroy.
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
* when to initialize providers - before confirming actions, i.e. before "Terraform will perform the following actions:"
```
2018-11-xxTxx:xx:xx.xxx-xxxx [DEBUG] plugin.terraform-provider-google: 2018/11/xx xx:xx:xx [INFO] Requesting Google token...
2018-11-xxTxx:xx:xx.xxx-xxxx [DEBUG] plugin.terraform-provider-google: 2018/11/xx xx:xx:xx [INFO] Instantiating GCE client...

...

Terraform will perform the following actions:

...

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: 
```

## Testing
* docs
  * https://www.terraform.io/docs/extend/best-practices/testing.html
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
* print out the State
  ```
  resource.UnitTest(t, resource.TestCase{
          Providers: testProviders,
          Steps: []resource.TestStep{
                  {
                          Config: tc.resource,  
                          Check: resource.ComposeTestCheckFunc(
                                  func(s *terraform.State) error {
                                          fmt.Println("terraform.State:", s)
                                          return nil            
                                  },                    
                          ),                    
                  },
          },
  })
  ```
* debug - plan was not empty after running "terraform apply"
  * symptom
  ```
  // Step 1 is the second step, step 0 is the first step.
  testing.go:538: Step 1 error: After applying this step, the plan was not empty:
  // https://github.com/hashicorp/terraform/blob/master/helper/resource/testing.go
  ```
  * reasons
    * could be that the mock function for the Read() of the second step is wrong, maybe use the same Read in the first step. In this case, can use PreConfig to set a mock function for each step.
    * be careful that there are multiple Read() during one step. For resource Update(), the first Read() should usually be mocked to read the old resource, and after Update(), Reads should be mocked to read new resource. So, it's tricky to setup the mock Read(). track or print out the running of all functions can find the problem. One way is to setup a variable readCalledTimes to track when Read is called, and return different mock, e.g.
    ```
    readCalledTimes := 0
    readFunc = func (xxx) (xxx) {
      readCalledTimes++
      switch readCalledTimes {
      case 1, 2, xxx:
        return xxx
      case l, m, n:
        return xxx
      default:
        return some err
    }
    ```
  * a non-empty plan after successfully running terraform apply. This is typically due to a valid but otherwise misconfiguration of the resource, and is generally undesirable. However, if we want to intentionally create a test case for it, we can use ```ExpectNonEmptyPlan: true```
  * https://www.terraform.io/docs/extend/best-practices/testing.html#expecting-errors-or-non-empty-plans

## Tricky
* Schema
  * Required: true
    * it doens't mean that we need to specify it in the tf file, as long as it has DefaultFunc.
  * Cannot use "Required: false", must use "Optional: true", not verified.
