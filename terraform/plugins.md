# Plugins

## Kinds
* provider
* provisioner

## Code
* https://github.com/hashicorp/terraform/blob/master/command/plugins.go: 
  * pluginDirs()
* https://github.com/hashicorp/terraform/blob/master/command/meta.go
  * GlobalPluginDirs
  * pluginPath

## How to Setup Plugin Directory
* the same directory of "terraform" binary
* terraform init -plugin-dir <plugin dir>
* ~/.terraform.d/plugins
 
## Communication with Terraform
* https://www.terraform.io/docs/internals/internal-plugins.html
  * "Plugins are executed as a separate process and communicate with the main Terraform binary over an RPC interface."
  * "the main process communicates with the plugin process over HTTP"
