# Golang Tricky Stuff

## Common Mistakes 
* Using goroutines on loop iterator variables
  * https://github.com/golang/go/wiki/CommonMistakes 
  * t.Parallel, https://gist.github.com/posener/92a55c4cd441fc5e5e85f27bca008721 
  ```go
  	for _, tc := range tests {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			t.Parallel()
  ```

## Basic Data types
### string
```go
	list := strings.Split("", ",")
	fmt.Println("len(list):", len(list))
```
output is, where the content is empty string 
```
len(list): 1
```
### slice 
empty slice works fine with append and range,
```go
package main
import "fmt"
func main() {
    var ls []string
    fmt.Println("ls:", ls, "len(ls):", len(ls))
	
    for k,v := range ls {
	    fmt.Println("key:", k, "value:", v, ">")
    }

    ls = append(ls, "first")
    for k,v := range ls {
	    fmt.Println("key:", k, "value:<", v, ">")
    }
	
    ll := []string{}
    fmt.Println("ll:", ll, "len(ll):", len(ll))
    for k,v := range ll {
	    fmt.Println("key:", k, "value:", v, ">")
    }

    ll = append(ll, "second")
    for k,v := range ll {
	    fmt.Println("key:", k, "value:<", v, ">")
    }
}

// output
ls: [] len(ls): 0
key: 0 value:< first >
ll: [] len(ll): 0
key: 0 value:< second >
```

### map
map is a pointer. it can be nil, e.g. this will cause ```panic: assignment to entry in nil map```
```
var skipDirSet map[string]struct{}
skipDirSet[skipDir] = struct{}{}  // create an empty struct.
```

### empty struct
https://dave.cheney.net/2014/03/25/the-empty-struct
```
skipDirSet := map[string]struct{}
skipDirSet[skipDir] = struct{}{}  // create an empty struct.
```
### Pointer
* cannot get a pointer from a const
* cannot get a pointer from function return value
* https://stackoverflow.com/questions/30716354/how-do-i-do-a-literal-int64-in-go
* use case: we define some const value, and want to use them for pointers in a struct
```go
const (
	defaultEndpoint       string = "http://localhost:8080"
)
func getStringPtr(s string) *string {
	return &s
}

func getIntPtr(i int) *int {
	return &i
}

config.endpoint = getStringPtr(defaultEndpoint)
```

## Defer
### close on writable file
https://joeshaw.org/dont-defer-close-on-writable-files/
```go
// solution #1 - logic is simpler, and the same lines of code as solution #2
        if _, err = io.Copy(f, resp.Body); err != nil {
                f.Close()
                return err
        }
        return f.Close()

// solution #2 - io/ioutil/ioutil.go - WriteFile()
        _, err = io.Copy(f, resp.Body);
        if errclose = f.Close(); err == nil {
                err = errclose
        }
        return err

```

this is wrong because file is not closed when Sync returns err (or io.Copy returns error)
```go
if err = out.Sync(); err != nil {
    return err
}

return out.Close()  // usually this is not a long function, and easier to make sure that it is closed.
```

### gotchas
https://blog.learngoprogramming.com/gotchas-of-defer-in-go-1-8d070894cb01

## Tilde Home Directory
* golang itself can not handle tilde (```~```) as home directory, because it is handled by shell/bash when passing it to go code as command line arguments. However, if we use it directly in the code, it can not interpretate it, even with AbsPath.

## json
* If json content is null, then it means empty, and will be converted as the default value of that time.
* For example, 
```
type Book struct  {
    Name string
    Brorrower string    
}
```
If Borrower is absent in the json, it will be empty string. We cannot distinguish between absence and real empty string. So, we can define a pointer to handle this, which will return nil when it is absent or null, e.g.
```
type Book struct  {
    Name string
    Brorrower *string    
}
```
