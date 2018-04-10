# fmt.Print
* https://golang.org/src/fmt/print.go
  * func (p *pp) doPrintln(a []interface{})
    * printArg
* combined type switch and reflection - TTT??? why
* fmt.Print(err) is ok. Not sure why??? TTT (where err is an instance of error)
  * glog.Error(err) is also ok.
  * examples
  ```go
        err := os.MkdirAll("/root/tmp", os.ModePerm)
        if err != nil {
                glog.Error("glog err:", err)
                fmt.Println("println err:", err)
                glog.Error("glog nil:", nil)
                fmt.Println("println nil:", nil)
        }
   // output
   E0410 10:35:55.466267   11838 xxx.go:57] glog err:mkdir /root/tmp: permission denied
   println err: mkdir /root/tmp: permission denied
   E0410 10:35:55.466600   11838 xxx.go:59] glog nil:<nil>
   println nil: <nil>
   ```
   


# os
* https://golang.org/src/os/path_test.go

# io
* https://golang.org/src/io/io.go
  * Copy(dst Writer, src Reader) (written int64, err error): 
    * if written data is not all write (i.e. written is not the same as src), there will be error.
