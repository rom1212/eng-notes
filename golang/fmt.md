# error
```go
  err := errors.New("this error")
  fmt.Printf("error: %s", err) // error: this error
  fmt.Printf("error: %v", err) // error: this error

  fmt.Printf("error:%q", err) // error: "this error"
```
