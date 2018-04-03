# Basic Data types
## string
```go
	list := strings.Split("", ",")
	fmt.Println("len(list):", len(list))
```
output is 
```
len(list): 1
```

# Defer
## close on writable file
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
## 
