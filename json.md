# Command Line jq
## Install
```
sudo apt install jq
```
## Get a value of a key
```
cat <json file> | jq .key, where .key is called a filter
e.g. Get the value of "tag_name" from the release file.
curl -s https://api.github.com/repos/go-swagger/go-swagger/releases/latest | jq -r .tag_name
```
