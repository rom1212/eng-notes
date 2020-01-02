# terraform apply
## setup steps
* check providers
* figure out references
* start plugins
* add implicity dependencies
* "terraform: building graph: GraphTypeRefresh"
* initialize providers
## start a plugin
* https://github.com/hashicorp/terraform/blob/master/vendor/github.com/hashicorp/go-plugin/client.go#L506
```go
c.logger.Debug("starting plugin", "path", cmd.Path, "args", cmd.Args)
```
```
xxxx [DEBUG] plugin: starting plugin: path=path/to/terraform-provider-template args=[path/to/terraform-provider-template]
xxxx [DEBUG] plugin: waiting for RPC address: path=path/to/terraform-provider-template
xxxx [DEBUG] plugin.terraform-provider-template: plugin address: timestamp=2018-08-29T10:02:29.580-0700 address=/tmp/plugin987776049 network=unix
```
Since cmd.Args includes the command itself as Args[0]. So, the plugin is started without any argument.

# Code

## Config
* https://github.com/hashicorp/terraform/blob/master/config/config.go
* loader: https://github.com/hashicorp/terraform/blob/master/config/loader.go

## Command/Plan
* https://github.com/hashicorp/terraform/blob/master/command/plan.go

## Command/Apply
* https://github.com/hashicorp/terraform/blob/master/command/apply.go
  * https://github.com/hashicorp/terraform/blob/413e423bbabe2b3aea450572c29b54c39638c82a/command/meta.go#L280
  * https://github.com/hashicorp/terraform/blob/413e423bbabe2b3aea450572c29b54c39638c82a/backend/local/backend.go#L296 
