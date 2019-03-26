# Golang debug

## Print sub-directory recursively
```golang
filepath.Walk(".",
    func(path string, info os.FileInfo, err error) error {
    if err != nil {
       log.Infof("filepath.Walk error: %v", err)
       return err
    }
    log.Infof("filepath.Walk: path: %v, size: %v", path, info.Size())
    // fmt.Println(path, info.Size())
    return nil
})
```
