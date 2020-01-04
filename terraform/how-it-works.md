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
  * [command/meta.go:RunOperation](https://github.com/hashicorp/terraform/blob/413e423bbabe2b3aea450572c29b54c39638c82a/command/meta.go#L280)
  * [backend/local/backend.go:Operation](https://github.com/hashicorp/terraform/blob/413e423bbabe2b3aea450572c29b54c39638c82a/backend/local/backend.go#L296)
    * [backend/backend.go:RunningOperation](https://github.com/hashicorp/terraform/blob/413e423bbabe2b3aea450572c29b54c39638c82a/backend/backend.go#L246)    
    * opRefresh, opPlan, opApply
      * [terraform/context.go:Refresh()](https://github.com/hashicorp/terraform/blob/413e423bbabe2b3aea450572c29b54c39638c82a/terraform/context.go#L583): This will update the state that this context works with, along with returning it.
        * Build the graph: [terraform/context.go:Graph(): "[INFO] terraform: building graph: GraphTypeRefresh"](https://github.com/hashicorp/terraform/blob/413e423bbabe2b3aea450572c29b54c39638c82a/terraform/context.go#L257)
        * Do the walk: terraform/context.go:walk(): "[DEBUG] Starting graph walk: walkRefresh"
    * [opRefresh](https://github.com/hashicorp/terraform/blob/413e423bbabe2b3aea450572c29b54c39638c82a/backend/local/backend_refresh.go#L17): get new state, and save it
      * ```newState, refreshDiags = tfCtx.Refresh()```
      * ```err := statemgr.WriteAndPersist(opState, newState)```
    * [opPlan](https://github.com/hashicorp/terraform/blob/413e423bbabe2b3aea450572c29b54c39638c82a/backend/local/backend_plan.go#L25)
      * ```refreshedState, refreshDiags := tfCtx.Refresh()```
      * ```baseState = refreshedState // plan will be relative to our refreshed state```
      * ```plan, planDiags = tfCtx.Plan() // Plan only depends on tfCtx, not depends on baseState. baseState is only used for renderPlan(), and this is why opApply ignores refreshedState from tfCtx.Refresh``` 
      * ```b.renderPlan(plan, baseState, schemas)```
      
