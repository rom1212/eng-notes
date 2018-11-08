# struct
## Empty struct
```go
func ListFiles(dir string, skipDirs []string) ([]string, error) {
	skipDirSet := map[string]struct{}{}
	for _, skipDir := range skipDirs {
		skipDirSet[skipDir] = struct{}{}
	}
	return ListFilesWithSkipDirSet(dir, skipDirSet)
}
```

## Simple Deep Copy
```go
type Books []Book
func (books Books) clone() Books {
        clone := make([]Book, 0)
        for _, book := range books {
                clone = append(clone, book)
        }
        return clone
}
```
It seems that slice doesn't work, e.g. 
```go
clone := books[:]
```
I guess it is because each element is still a pointer internally.

## exported field
* Only fields whose first letter is capital are exported.
* https://golang.org/ref/spec#Exported_identifiers

## Prompted fields
* composite fields
  * cannot be used as field names in composite literals of the struct, i.e. cannot used in initialization
* https://stackoverflow.com/questions/41686692/embedding-structs-in-golang-gives-error-unknown-field

