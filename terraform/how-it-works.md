# terraform apply
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
