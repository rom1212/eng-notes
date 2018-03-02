# Profiling
## Setup with net/http/pprof
* https://golang.org/pkg/net/http/pprof/
  * import _ "net/http/pprof"
  * http.ListenAndServe("localhost:6060", nil)
```go
import (
	_ "net/http/pprof"
	"net/http"
  "log"
}
func main() {
    // we need a webserver to get the pprof webserver
    go func() {
        log.Println(http.ListenAndServe("localhost:6060", nil))
    }()
    // this works for a long running process, e.g. backend server
}
```


## Memory
go tool pprof http://localhost:6060/debug/pprof/heap
