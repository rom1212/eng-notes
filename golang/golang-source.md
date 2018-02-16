# fmt.print
* https://golang.org/src/fmt/print.go
  * func (p *pp) doPrintln(a []interface{})
    * printArg
* combined type switch and reflection - TTT??? why

# os
* https://golang.org/src/os/path_test.go

# io
* https://golang.org/src/io/io.go
  * Copy(dst Writer, src Reader) (written int64, err error): 
    * if written data is not all write (i.e. written is not the same as src), there will be error.
