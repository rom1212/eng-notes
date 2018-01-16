# Swagger Example
* https://github.com/romans1212notes/swagger-guide

# Swagger Codegen
## Usage
```
package main

import "fmt"
import mapi "marathon-api"

func main() {
	fmt.Printf("hello, world\n")
	api := mapi.NewDefaultApiWithBasePath("http://localhost:8080")
	fmt.Println("api.Configuration", api.Configuration)
	applist, response, error := api.V2AppsGet("", "", "", "");

	if error != nil {
		fmt.Println("error:", error)
	} else {
		fmt.Println("error:", error)
		fmt.Println("applist:", applist)
		fmt.Println("applist len:", len(applist.Apps))
		//var app mapi.AppApp
		for _, app := range applist.Apps {
			fmt.Println("app.Id:", app.Id)
			fmt.Println("app.Cmd:", app.Cmd)
		}
		fmt.Println("response:", response)
		fmt.Println("response.Message:", response.Message)
		fmt.Println("response.Payload:", response.Payload)
		fmt.Println("response.len(Payload):", len(response.Payload))
	}

}
```

## Debug go-resty
https://github.com/go-resty/resty
```
// api_client.go
func (c *APIClient) prepareClient() *resty.Client {

	rClient := resty.New()

	rClient.SetDebug(true)
	if c.config.Transport != nil {
		rClient.SetTransport(c.config.Transport)
	}

	if c.config.Timeout != nil {
		rClient.SetTimeout(*c.config.Timeout)
	}
	rClient.SetLogger(os.Stdout)
	return rClient
}
```

# Go swagger
https://github.com/go-swagger/go-swagger

## Install
```
sudo apt-get install jq
latestv=$(curl -s https://api.github.com/repos/go-swagger/go-swagger/releases/latest | jq -r .tag_name)
curl -o ./swagger -L'#' https://github.com/go-swagger/go-swagger/releases/download/$latestv/swagger_$(echo `uname`|tr '[:upper:]' '[:lower:]')_amd64
chmod +x ./swagger
```

## Generate Client
```
./swagger generate client --spec api.swagger.json --name marathon-api --target go-swagger-client
```

## Find Problems
* Cannot be "nil"
```
- must validate at least one schema (anyOf)
- must validate at least one schema (anyOf)
- definitions.app.health.command.ShellCommand.additionalProperties.type in body must be of type array: "string"
```
* Path cannot use ::
```
- path param "id" is not present in path "/v2/pods/{id}::versions/{version}"
```
* Cannot have "default" key and value
```
- definitions.app.appContainer.Container.type in body must be of type string: "null"
- definitions.app.appContainer.Container.type in body should be one of [MESOS DOCKER]
```
