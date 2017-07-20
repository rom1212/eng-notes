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
