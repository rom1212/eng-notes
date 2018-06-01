# Dev
* go get ./...
* go build
* go get -t ./...
* go test -v ./...
* checks
  * gofmt -l -w .
  * go vet ./...
  * golint ./... (go get -u golang.org/x/lint/golint)
    * only for some directories, e.g.: golint . utils/ tools/
  * gometalint
  * goreporter: https://github.com/360EntSecGroup-Skylar/goreporter/
  * awesome static analysis: https://github.com/360EntSecGroup-Skylar/goreporter/commits/master
* guide???TTT
* [errcheck](https://github.com/kisielk/errcheck): ```errcheck ./...```
* editors
  * Eclipse
    * https://goclipse.github.io/

# Docs
* Effective Go: https://golang.org/doc/effective_go.html
* Cmd/Tools: https://golang.org/cmd/
* Code Review: https://github.com/golang/go/wiki/CodeReviewComments
* How to write Go code: https://golang.org/doc/code.html

# Questions (TTT???):
## Major Questions
### what are the cases for runtime crash? 
* nil pointer deferencence
  * interface is not set to a real object.
* panic: assignment to entry in nil map
```
var skipDirSet map[string]struct{}
skipDirSet[skipDir] = struct{}{}  // create an empty struct.
```

## Other Questions
* GOPATH - a list of directories?
  * ```go get``` put code in the first path
  * ```go install``` put package in the one of the code.
* import local package "./xxxx" or must "myproject/xxx"
* pipe: 
  * https://golang.org/pkg/os/exec/#example_Cmd_StdinPipe
  * http://blog.ralch.com/tutorial/golang-command-line-pipes/
  * "golang command redirection"
* https://golang.org/ref/spec#Slice_expressions
  * For arrays or strings, the indices are in range if 0 <= low <= high <= len(a)
  * append nil
  * nil slice
* https://golang.org/ref/spec#Run_time_panics
* dependencies
  * https://stackoverflow.com/questions/17539407/golang-how-to-import-local-packages-without-gopath
  * https://dave.cheney.net/2014/12/01/five-suggestions-for-setting-up-a-go-project  
