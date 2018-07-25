# OS
* RemoveAll: rm -r

# json
* https://golang.org/pkg/encoding/json/#MarshalIndent

https://coderwall.com/p/cp5fya/measuring-execution-time-in-go

# github/third-party
* https://github.com/satori/go.uuid 

# packages
## time
```
time.Now()
time.Since()
```

time formatting: https://gobyexample.com/time-formatting-parsing

## regular expression
* docs: 
  * https://golang.org/pkg/regexp/syntax/
  * https://golang.org/pkg/regexp/#Match
* examples
```go
regexp.MatchString("foo.*", "seafood")
regexp.MatchString(`foo[\s]*`, "seafoo d"). // match with white space in between
```
