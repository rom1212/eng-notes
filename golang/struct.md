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
