# Defer
## close on writable file
https://joeshaw.org/dont-defer-close-on-writable-files/
```
if err = out.Sync(); err != nil {
    return err
}

return out.Close()  // usually this is not a long function, and easier to make sure that it is closed.
```
## 
