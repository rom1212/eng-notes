# Dev
* go get ./...
* go build
* go get -t ./...
* go test -v ./...
* checks
  * gofmt -l -w .
  * go vet ./...
* guide???TTT
* [errcheck](https://github.com/kisielk/errcheck): ```errcheck ./...```

# Docs
* Effective Go: https://golang.org/doc/effective_go.html
* Cmd/Tools: https://golang.org/cmd/
* Code Review: https://github.com/golang/go/wiki/CodeReviewComments
* How to write Go code: https://golang.org/doc/code.html

# Questions (TTT???):
* GOPATH - a list of directories?
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
