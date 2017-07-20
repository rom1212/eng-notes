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

# Swagger Codegen

## Debutg go-resty
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
