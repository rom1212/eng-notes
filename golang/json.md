# golang json
## Read Json to Struct
https://www.chazzuka.com/2015/03/load-parse-json-file-golang/

## Cases
* new fields
* missing fields
* bad fields

## pointer
* https://dhdersch.github.io/golang/2016/01/23/golang-when-to-use-string-pointers.html
* https://stackoverflow.com/questions/19633763/unmarshaling-json-in-golang-required-field
* https://stackoverflow.com/questions/47256201/golang-ignore-json-fields-when-marshalling-not-unmarshalling

## Json parsing error
```invalid character 'p' after top-level value```

## Decoding arbitrary data
* https://blog.golang.org/json-and-go
* Only decode the top level string, and make lower level as json string
```golang
b := []byte(`{"Name":"Wednesday","Age":6,"Parents":["Gomez","Morticia"]}`)

var f interface{}
if err := json.Unmarshal(b, &f); err != nil {
    fmt.Print(err)
    return
}

for k, v := range f {
    bytes, err := json.Marshal(v)
    if err != nil {
        fmt.Println(err)
    }
    fmt.Println(k, string(bytes))
}
```
