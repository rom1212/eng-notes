# Golang debug

## Print sub-directory recursively
```golang
func walkDir(dir string) {
	err := filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			log.Infof("filepath.Walk error: %v", err)
			return err
		}
		log.Infof("filepath.Walk: path: %v, size: %v", path, info.Size())
		// fmt.Println(path, info.Size())
		return nil
	})
	if err != nil {
		log.Infof("walkDir error: %v", err)
	}
}
```

## Print stack trace
```go
import (
	"runtime/debug"
)
debug.Stack() // Print out to stderr
fmt.Printf("Stack Trace: %v\n", string(debug.Stack()))  / Print to stdout
```
