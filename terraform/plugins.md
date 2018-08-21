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
* terraform init -plugin-dir <plugin dir>
* the same directory of "terraform" binary
* ~/.terraform.d/plugins
